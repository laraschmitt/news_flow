from sqlalchemy import create_engine

# Declare postgres config
HOST = 'localhost'
USERNAME = 'postgres'
PORT = '5432'
DB = 'tweets_multilingu'
PASSWORD = 'postgres'


# Create a postgres connection and assign it to 'engine' variable
engine = create_engine(f'postgres://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB}')


def load(tweets):
    """ Loads transformed tweeets into the Postgres database
    Parameters:
    ------------
    tweets: List of tweets that were extracted from the MongoDB database and transformed """

    insert_query = ''''INSERT INTO tweets_test (
        id, timestamp_ms, tweet, url_in_tweet, user_url, user_location,
        user_follower_count, user_verified, user_statuses_count, lang, geo, 
        coordinates, place, user_id, user_created_at) 
        VALUES (%s, %s, %s);'''
    for i in tweets:
        engine.execute(
            insert_query, (tweet['username'], tweet['text'], tweet['sentiment_score']))
