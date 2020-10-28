import pandas as pd
import json
from sqlalchemy import create_engine
import bz2
import os

# load lookup tables
df_city = pd.read_csv(
    './data/location_ref/city_multilingu_citycoord_countrycode_countrycoord.csv',
    index_col=0)
df_country = pd.read_csv(
    './data/location_ref/country_multilingu_countrycode_countrycoord.csv',
    index_col=0)
df_councode_counname = pd.read_csv(
    './data/location_ref/IP2LOCATION-COUNTRY-MULTILINGUAL.csv')
df_councode_counname_en = df_councode_counname[df_councode_counname['LANG_NAME'] == 'ENGLISH']


# extract URL function
def extract_url(urls) -> str:
    """ Function to extract the url from the entities dict of the tweet json"""

    found_url = ''
    url_given = urls

    if url_given is not None:
        for url in url_given:
            found_url = url.get('url')

    return found_url


# Declare postgres config
HOST = 'localhost'
USERNAME = 'postgres'
PORT = '5432'
DB = 'tweets_multilingu'
PASSWORD = 'postgres'

# Create a postgres connection and assign it to 'engine' variable
engine = create_engine(f'postgres://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB}')


# function to load data into postgres
def load(j):
    """ Loads transformed tweeets into the Postgres database
    Parameters:
    ------------
    tweets: List of tweet dictionaries that
    were retrieved from the Twitter API """

    insert_query = """INSERT INTO tweets_test (
        tweet_id,
        timestamp_ms,
        tweet,
        url_in_tweet,
        user_url,
        user_location,
        user_followers_count,
        user_verified,
        user_statuses_count,
        user_id,
        user_created_at,
        lang,
        user_loc_city_coords,
        user_loc_country_coords,
        from_country_coords,
        from_country_name,
        to_country_coords,
        to_country_name
        )
        VALUES (%s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s,
                %s, %s, %s);"""

    # check for valid entries and if tweet json contains
    # any location information
    # get user dict
    user = j.get('user')
    user_location = j.get('user', {}).get('location')
    valid_entry = j.get('created_at')
    place_attr = j.get('place')
    user_url = j.get('user', {}).get('url')
    urls = j.get('entities', {}).get('urls')
    lang_code = j.get('lang')

    # conditions to still be included !
    follower_c = j.get('user', {}).get('followers_count')
    ver = j.get('user', {}).get('verified')

    if (valid_entry and len(urls) and user_url) and user_location and ver and (follower_c > 10000):

        user_loc_city_coords = ''
        user_loc_country_coords = ''
        to_country_coords = ''
        to_country_name = ''
        from_country_coords = ''
        from_country_name = ''

        # loop through multilingual city list
        for c_name_multi in df_city['CITY_NAME']:
            # check if the found cityname in the tweet is a cityname in the language the tweet was written in (detected from twitter)
            if c_name_multi in j['text'] and df_city.loc[df_city['CITY_NAME'] == c_name_multi]['language'].values[0] == lang_code:

                print('-------Cityname found in local language tweet---------', c_name_multi)

                # map the cityname to its countries coordinates
                to_country_coords = df_city.loc[df_city['CITY_NAME']
                                                == c_name_multi]['country_lat_long_3857'].values[0]
                # get countrycode and then countryname
                to_country_code = df_country.loc[df_country['country_lat_long_3857']
                                                 == to_country_coords]['COUNTRY_ALPHA2_CODE'].values[0]
                to_country_name = df_councode_counname_en.loc[df_councode_counname_en[
                    'COUNTRY_ALPHA2_CODE'] == to_country_code]['COUNTRY_NAME'].values[0]

                # print('Cityname found in tweet: ',
                #       c_name_multi, 'in language: ', lang_code)

                # find user loc coordinates and country coords
                for _c_name_multi in df_city['CITY_NAME']:

                    if _c_name_multi in user_location.lower():
                        user_loc_city_coords = df_city.loc[df_city['CITY_NAME'] == _c_name_multi]['city_lat_long_3857'].values[0]
                        from_country_coords = df_city.loc[df_city['CITY_NAME'] == _c_name_multi]['country_lat_long_3857'].values[0]
                        from_country_code = df_country.loc[df_country['country_lat_long_3857']
                                                           == from_country_coords]['COUNTRY_ALPHA2_CODE'].values[0]
                        from_country_name = df_councode_counname_en.loc[df_councode_counname_en[
                            'COUNTRY_ALPHA2_CODE'] == from_country_code]['COUNTRY_NAME'].values[0]

                for _c_name_multi in df_country['COUNTRY_NAME']:

                    if _c_name_multi in user_location.lower():

                        user_loc_country_coords = df_country.loc[df_country['COUNTRY_NAME']
                                                                 == _c_name_multi]['country_lat_long_3857'].values[0]
                        from_country_coords = df_country.loc[df_country['COUNTRY_NAME']
                                                             == _c_name_multi]['country_lat_long_3857'].values[0]
                        from_country_code = df_country.loc[df_country['country_lat_long_3857']
                                                           == from_country_coords]['COUNTRY_ALPHA2_CODE'].values[0]
                        from_country_name = df_councode_counname_en.loc[df_councode_counname_en[
                            'COUNTRY_ALPHA2_CODE'] == from_country_code]['COUNTRY_NAME'].values[0]

                        # print('user location COUNTRY found', user_location, user_loc_country_coords,
                        #       'english name: ', from_country_name)

                print('City Loop', j['id'])
                print('Setting user_location', user_location)
                print('user_loc_city_coords', user_loc_city_coords)
                print('from_country_coords', from_country_coords)
                print('from_country_name', from_country_name)

        # loop through multilingual country list
        for c_name_multi in df_country['COUNTRY_NAME']:

            # check if the found country in the tweet is a country in the language the tweet was written in (detected from twitter)
            if c_name_multi in j['text'] and df_country.loc[df_country['COUNTRY_NAME'] == c_name_multi]['LANG'].values[0] == lang_code:

                print('-------Country found in local lang in tweet---------', c_name_multi)

                # get country coords
                if not to_country_coords:
                    to_country_coords = df_country.loc[df_country['COUNTRY_NAME'] == c_name_multi]['country_lat_long_3857'].values[0]
                # get countrycode and then countryname
                to_country_code = df_country.loc[df_country['country_lat_long_3857'] == to_country_coords]['COUNTRY_ALPHA2_CODE'].values[0]
                if not to_country_name:
                    to_country_name = df_councode_counname_en.loc[df_councode_counname_en['COUNTRY_ALPHA2_CODE'] == to_country_code]['COUNTRY_NAME'].values[0]

                # print('Country found in tweet: ', c_name_multi,
                #       'in language: ', lang_code, 'english_name', to_country_name)

                # find user loc coordinates and country coords
                for _c_name_multi in df_country['COUNTRY_NAME']:

                    if _c_name_multi in user_location.lower():

                        if not user_loc_country_coords:
                            user_loc_country_coords = df_country.loc[df_country['COUNTRY_NAME'] == _c_name_multi]['country_lat_long_3857'].values[0]

                        if not from_country_coords:
                            from_country_coords = df_country.loc[df_country['COUNTRY_NAME'] == _c_name_multi]['country_lat_long_3857'].values[0]

                        from_country_code = df_country.loc[df_country['country_lat_long_3857'] == from_country_coords]['COUNTRY_ALPHA2_CODE'].values[0]

                        if not from_country_name:
                            from_country_name = df_councode_counname_en.loc[df_councode_counname_en['COUNTRY_ALPHA2_CODE'] == from_country_code]['COUNTRY_NAME'].values[0]

                for _c_name_multi in df_city['CITY_NAME']:

                    if _c_name_multi in user_location.lower():

                        if not user_loc_city_coords:
                            user_loc_city_coords = df_city.loc[df_city['CITY_NAME'] == _c_name_multi]['city_lat_long_3857'].values[0]

                        if not from_country_coords:
                            from_country_coords = df_city.loc[df_city['CITY_NAME'] == _c_name_multi]['country_lat_long_3857'].values[0]

                        from_country_code = df_country.loc[df_country['country_lat_long_3857']
                                                           == from_country_coords]['COUNTRY_ALPHA2_CODE'].values[0]
                        if not from_country_name:
                            from_country_name = df_councode_counname_en.loc[df_councode_counname_en['COUNTRY_ALPHA2_CODE'] == from_country_code]['COUNTRY_NAME'].values[0]

                        print('user location CITY found', user_location,
                              user_loc_city_coords, 'from_country', from_country_name)

                # get url mentionend in tweet from entities dict
                found_url = extract_url(j.get('entities').get('urls'))

                print('Country Loop', j['id'])
                print('Setting user_location', user_location)
                print('user_loc_country_coords', user_loc_country_coords)
                print('from_country_coords', from_country_coords)
                print('from_country_name', from_country_name)

                if (from_country_coords and to_country_coords) and (from_country_name != to_country_name):
                    # insert values into postgres DB
                    engine.execute(insert_query, (
                        j['id'],  # id
                        j['timestamp_ms'],  # timestamp_ms
                        j['text'],  # tweet
                        found_url,  # url_in_tweet
                        user['url'],  # user_url
                        user_location,  # user_location
                        user['followers_count'],  # user_followers_count
                        user['verified'],  # user_verified
                        user['statuses_count'],  # user_statuses_count
                        user['id'],  # user_id
                        user['created_at'],  # user_created_at

                        j['lang'],  # lang
                        user_loc_city_coords,
                        user_loc_country_coords,
                        from_country_coords,
                        from_country_name,
                        to_country_coords,
                        to_country_name
                    ))

                    print('-------TWEET INGESTED IN DATABASE---------')

# import from one day
# next folder: stream-2020-06/06 2/02/


path = "./data/archiveteam-twitter-stream-2020-06/06/01/"
for folder in sorted(os.listdir(path)):
    # print('load folder', folder)
    if not folder.startswith('.'):

        t = 0
        for file in sorted(os.listdir(path + folder)):

            t += 1
            if file.endswith('.bz2'):

                # print(t)
                # print('load file', file)

                with bz2.open(path + folder + "/" + file, "rt") as bzinput:

                    for i, line in enumerate(bzinput):
                        tweet = json.loads(line)
                        load(tweet)

                if t == 3:
                    break
