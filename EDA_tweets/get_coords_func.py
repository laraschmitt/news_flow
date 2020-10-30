import pandas as pd
import json
import bz2
import os

# load lookup tables
df_city = pd.read_csv('../data/location_ref/city_multilingu_citycoord_countrycode_countrycoord.csv', index_col=0)
df_country = pd.read_csv('../data/location_ref/country_multilingu_countrycode_countrycoord.csv', index_col=0)
print(df_city.head(), df_country.head())
# As test data:
# load only two files from every hour folder from the first day of the month into a list

tweet_data = []

for folder in sorted(os.listdir("../data/archiveteam-twitter-stream-2020-06/06/01/")):
    if not folder.startswith('.'):
        print('load folder', folder)

        t = 0
        for file in sorted(os.listdir("../data/archiveteam-twitter-stream-2020-06/06/01/" + folder)):

            t += 1
            if file.endswith('.bz2'):

                print(t)
                print('load file', file)

                with bz2.open("./data/archiveteam-twitter-stream-2020-06/06/01/" + folder + "/" + file, "rt") as bzinput:

                    for i, line in enumerate(bzinput):
                        tweet = json.loads(line)
                        tweet_data.append(tweet)

            # include break statement to test
            # load only 2 files from each hour folder
                if t == 2:
                    break

print(len(tweet_data))

# Function from countryname or cityname in tweet to TO_countrycoords


def get_country_coords(country_or_city_name_multilingu):
    """Function to retrieve the coordinates of the geographical center of a country 
    from the country name or a cityname that is contained in a string (usecase: tweet). 
    Based on the lookup in two pandas dataframes.

    Parameters:
    ----------------------------
    country_or_city_name_multilingu: string

    CSV files needed for the coordinates lookup:
    ----------------------------
    df_city = './data/location_ref/city_multilingu_citycoord_countrycode_countrycoord.csv'
    df_country = './data/location_ref/country_multilingu_countrycode_countrycoord.csv'

    """

    # make input string lowercase
    search_string = country_or_city_name_multilingu.lower()

    # account for special cases UK, US and USA
    if country_or_city_name_multilingu == 'UK':
        print('UK found')
        return df_country.loc[df_country['COUNTRY_NAME'] == 'united kingdom']['country_lat_long_3857'].values

    if country_or_city_name_multilingu == 'US' or search_string == 'USA':
        return df_country.loc[df_country['COUNTRY_NAME'] == 'united states']['country_lat_long_3857'].values

    # check for country name
    if not (df_country[df_country['COUNTRY_NAME'].isin([search_string])]).empty:
        print('country found')
        return df_country.loc[df_country['COUNTRY_NAME'] == search_string]['country_lat_long_3857'].values[0]

    # if country name not found, check for city name
    elif not (df_city[df_city['CITY_NAME'].str.contains(search_string)]).empty:
        print('cityname found')
        idx = df_city[df_city['CITY_NAME'].str.contains(search_string)]['population'].idxmax()
        return df_city.iloc[idx]['country_lat_long_3857']

    print('No coords found')
    return None


# test
str = 'france'
get_country_coords(str)
