def load(j):
    """ Loads transformed tweeets into the Postgres database
    Parameters:
    ------------
    tweets: List of tweet dictionaries that were retrieved from the Twitter API """

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
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""

    # check for valid entries and if tweet json contains any location information
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

    if (valid_entry and len(urls) != 0 and user_url) and (user_location or place_attr) and (ver == True) and (follower_c > 10000):

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

                #print('city_name: ', c_name_multi, 'in language: ', lang_code)

                # map the cityname to its countries coordinates
                to_country_coords = df_city.loc[df_city['CITY_NAME']
                                                == c_name_multi]['country_lat_long_3857'].values[0]
                # get countrycode and then countryname
                to_country_code = df_country.loc[df_country['country_lat_long_3857']
                                                 == to_country_coords]['COUNTRY_ALPHA2_CODE'].values[0]
                to_country_name = df_councode_counname_en.loc[df_councode_counname_en[
                    'COUNTRY_ALPHA2_CODE'] == to_country_code]['COUNTRY_NAME'].values[0]

                # predefine from attributes

                # find user loc coordinates and country coords
                for _c_name_multi in df_city['CITY_NAME']:
                    # and df_city.loc[df_city['CITY_NAME'] == c_name_multi]['language'].values[0] == lang_code:
                    if _c_name_multi in user_location.lower():
                        user_loc_city_coords = df_city.loc[df_city['CITY_NAME']
                                                           == _c_name_multi]['city_lat_long_3857'].values[0]
                        from_country_coords = df_city.loc[df_city['CITY_NAME']
                                                          == _c_name_multi]['country_lat_long_3857'].values[0]
                        from_country_code = df_country.loc[df_country['country_lat_long_3857']
                                                           == from_country_coords]['COUNTRY_ALPHA2_CODE'].values[0]
                        from_country_name = df_councode_counname_en.loc[df_councode_counname_en[
                            'COUNTRY_ALPHA2_CODE'] == from_country_code]['COUNTRY_NAME'].values[0]
                        #print(user_location, user_loc_city_coords)

                for _c_name_multi in df_country['COUNTRY_NAME']:
                    # and df_city.loc[df_city['CITY_NAME'] == c_name_multi]['language'].values[0] == lang_code:
                    if _c_name_multi in user_location.lower():

                        user_loc_country_coords = df_country.loc[df_country['COUNTRY_NAME']
                                                                 == _c_name_multi]['country_lat_long_3857'].values[0]
                        from_country_coords = df_country.loc[df_country['COUNTRY_NAME']
                                                             == _c_name_multi]['country_lat_long_3857'].values[0]
                        from_country_code = df_country.loc[df_country['country_lat_long_3857']
                                                           == from_country_coords]['COUNTRY_ALPHA2_CODE'].values[0]
                        from_country_name = df_councode_counname_en.loc[df_councode_counname_en[
                            'COUNTRY_ALPHA2_CODE'] == from_country_code]['COUNTRY_NAME'].values[0]

        # loop through multilingual country list
        for c_name_multi in df_country['COUNTRY_NAME']:
            # check if the found country in the tweet is a country in the language the tweet was written in (detected from twitter)

            if c_name_multi in j['text'] and df_country.loc[df_country['COUNTRY_NAME'] == c_name_multi]['LANG'].values == lang_code:

                #print('country_name: ', c_name_multi, 'in language: ', lang_code)
                if user_location and '東京' in user_location.lower():
                    print('setting 東京 country values')

                # get country coords
                to_country_coords = df_country.loc[df_country['COUNTRY_NAME']
                                                   == c_name_multi]['country_lat_long_3857'].values[0]
                # get countrycode and then countryname
                to_country_code = df_country.loc[df_country['country_lat_long_3857']
                                                 == to_country_coords]['COUNTRY_ALPHA2_CODE'].values[0]
                to_country_name = df_councode_counname_en.loc[df_councode_counname_en[
                    'COUNTRY_ALPHA2_CODE'] == to_country_code]['COUNTRY_NAME'].values[0]

                # find user loc coordinates and country coords
                for _c_name_multi in df_country['COUNTRY_NAME']:
                    # and df_city.loc[df_city['CITY_NAME'] == c_name_multi]['language'].values[0] == lang_code:
                    if _c_name_multi in user_location.lower():

                        user_loc_country_coords = df_country.loc[df_country['COUNTRY_NAME']
                                                                 == _c_name_multi]['country_lat_long_3857'].values[0]
                        from_country_coords = df_country.loc[df_country['COUNTRY_NAME']
                                                             == _c_name_multi]['country_lat_long_3857'].values[0]
                        from_country_code = df_country.loc[df_country['country_lat_long_3857']
                                                           == from_country_coords]['COUNTRY_ALPHA2_CODE'].values[0]
                        from_country_name = df_councode_counname_en.loc[df_councode_counname_en[
                            'COUNTRY_ALPHA2_CODE'] == from_country_code]['COUNTRY_NAME'].values[0]
                        print(from_country_name)
                        #print(user_location, user_loc_country_coords)

                for _c_name_multi in df_city['CITY_NAME']:
                    # and df_city.loc[df_city['CITY_NAME'] == c_name_multi]['language'].values[0] == lang_code:
                    if _c_name_multi in user_location.lower():
                        user_loc_city_coords = df_city.loc[df_city['CITY_NAME']
                                                           == _c_name_multi]['city_lat_long_3857'].values[0]
                        from_country_coords = df_city.loc[df_city['CITY_NAME']
                                                          == _c_name_multi]['country_lat_long_3857'].values[0]
                        from_country_code = df_country.loc[df_country['country_lat_long_3857']
                                                           == from_country_coords]['COUNTRY_ALPHA2_CODE'].values[0]
                        from_country_name = df_councode_counname_en.loc[df_councode_counname_en[
                            'COUNTRY_ALPHA2_CODE'] == from_country_code]['COUNTRY_NAME'].values[0]

                # get url mentionend in tweet from entities dict
                found_url = extract_url(j.get('entities').get('urls'))

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
                    )
                    )


tweet = {'created_at': 'Mon Jun 01 06:29:00 +0000 2020',
         'id': 1267342365443780608,
         'id_str': '1267342365443780608',
         'text': '@jennirurbyjane @xsinbgf Hadeeh netijen netijen.. Kagak!! Adek lo galau https://t.co/q9dNOABbDr',
         'display_text_range': [25, 71],
         'source': '<a href="http://twitter.com/download/android" rel="nofollow">Twitter for Android</a>',
         'truncated': False,
         'in_reply_to_status_id': 1267341794687070209,
         'in_reply_to_status_id_str': '1267341794687070209',
         'in_reply_to_user_id': 1242524414006013952,
         'in_reply_to_user_id_str': '1242524414006013952',
         'in_reply_to_screen_name': 'jennirurbyjane',
         'user': {'id': 1115637256365068288,
                  'id_str': '1115637256365068288',
                  'name': 'Rene🕊',
                  'screen_name': 'renebaebaei',
                  'location': '↻  A womαn born in 1991 ↷ who hαs α fαce like α Greek goddess ﾐ 남자가 그녀를 좋아하게 할 아름다움으로. ៚ 𝐉𝐨𝐨𝐡𝐲𝐮𝐧 𝐝é 𝐁𝐚𝐞 ❀ #SMOFC ◆ Selective ◆ NOTWIN',
                  'url': 'http://mingyu.xn--c6h',
                  'description': "My Infinity 8 @SVT_KMG1997' 🎎 & My 👼 @KimMinjo06 💜 #TRAVMO  🔞",
                  'translator_type': 'none',
                  'protected': False,
                  'verified': False,
                  'followers_count': 381,
                  'friends_count': 365,
                  'listed_count': 14,
                  'favourites_count': 952,
                  'statuses_count': 41212,
                  'created_at': 'Tue Apr 09 15:27:04 +0000 2019',
                  'utc_offset': None,
                  'time_zone': None,
                  'geo_enabled': False,
                  'lang': None,
                  'contributors_enabled': False,
                  'is_translator': False,
                  'profile_background_color': 'F5F8FA',
                  'profile_background_image_url': '',
                  'profile_background_image_url_https': '',
                  'profile_background_tile': False,
                  'profile_link_color': '1DA1F2',
                  'profile_sidebar_border_color': 'C0DEED',
                  'profile_sidebar_fill_color': 'DDEEF6',
                  'profile_text_color': '333333',
                  'profile_use_background_image': True,
                  'profile_image_url': 'http://pbs.twimg.com/profile_images/1265268090582872067/f-af8Z9m_normal.jpg',
                  'profile_image_url_https': 'https://pbs.twimg.com/profile_images/1265268090582872067/f-af8Z9m_normal.jpg',
                  'profile_banner_url': 'https://pbs.twimg.com/profile_banners/1115637256365068288/1590163926',
                  'default_profile': True,
                  'default_profile_image': False,
                  'following': None,
                  'follow_request_sent': None,
                  'notifications': None},
         'geo': None,
         'coordinates': None,
         'place': None,
         'contributors': None,
         'is_quote_status': False,
         'quote_count': 0,
         'reply_count': 0,
         'retweet_count': 0,
         'favorite_count': 0,
         'entities': {'hashtags': [],
                      'urls': [],
                      'user_mentions': [{'screen_name': 'jennirurbyjane',
                                         'name': '🕊 Jennie.',
                                         'id': 1242524414006013952,
                                         'id_str': '1242524414006013952',
                                         'indices': [0, 15]},
                                        {'screen_name': 'xsinbgf',
                                         'name': '🕊 ʙɪɪ ᴍᴀᴜ ʜᴀʙᴇᴅᴇ',
                                         'id': 1108652797489111040,
                                         'id_str': '1108652797489111040',
                                         'indices': [16, 24]}],
                      'symbols': [],
                      'media': [{'id': 1267342352156250112,
                                 'id_str': '1267342352156250112',
                                 'indices': [72, 95],
                                 'media_url': 'http://pbs.twimg.com/media/EZaBJ5UU0AAtgZm.jpg',
                                 'media_url_https': 'https://pbs.twimg.com/media/EZaBJ5UU0AAtgZm.jpg',
                                 'url': 'https://t.co/q9dNOABbDr',
                                 'display_url': 'pic.twitter.com/q9dNOABbDr',
                                 'expanded_url': 'https://twitter.com/renebaebaei/status/1267342365443780608/photo/1',
                                 'type': 'photo',
                                 'sizes': {'medium': {'w': 1080, 'h': 810, 'resize': 'fit'},
                                           'thumb': {'w': 150, 'h': 150, 'resize': 'crop'},
                                           'large': {'w': 1080, 'h': 810, 'resize': 'fit'},
                                           'small': {'w': 680, 'h': 510, 'resize': 'fit'}}}]},
         'extended_entities': {'media': [{'id': 1267342352156250112,
                                          'id_str': '1267342352156250112',
                                          'indices': [72, 95],
                                          'media_url': 'http://pbs.twimg.com/media/EZaBJ5UU0AAtgZm.jpg',
                                          'media_url_https': 'https://pbs.twimg.com/media/EZaBJ5UU0AAtgZm.jpg',
                                          'url': 'https://t.co/q9dNOABbDr',
                                          'display_url': 'pic.twitter.com/q9dNOABbDr',
                                          'expanded_url': 'https://twitter.com/renebaebaei/status/1267342365443780608/photo/1',
                                          'type': 'photo',
                                          'sizes': {'medium': {'w': 1080, 'h': 810, 'resize': 'fit'},
                                                    'thumb': {'w': 150, 'h': 150, 'resize': 'crop'},
                                                    'large': {'w': 1080, 'h': 810, 'resize': 'fit'},
                                                    'small': {'w': 680, 'h': 510, 'resize': 'fit'}}}]},
         'favorited': False,
         'retweeted': False,
         'possibly_sensitive': False,
         'filter_level': 'low',
         'lang': 'hi',
         'timestamp_ms': '1590992940661'}


test = load(tweet)
