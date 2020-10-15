import time
import logging
from sqlalchemy import create_engine


# Create a postgres connection and assign it to 'engine' variable
engine = create_engine(f'postgres://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB}')

# create table 'tweets' in the postgres database
# CREATE_QUERY = '''CREATE TABLE IF NOT EXISTS tweets
#                  ;'''

# engine.execute(CREATE_QUERY)

# perform sentiment analysis?!


def load(tweets):
    """ Loads transformed tweeets into the Postgres database
    Parameters:
    ------------
    tweets: List of tweets that were extracted from the MongoDB database and transformed """

    insert_query = 'INSERT INTO tweets (name, text, sentiment_score) VALUES (%s, %s, %s);'
    for tweet in tweets:
        engine.execute(
            insert_query, (tweet['username'], tweet['text'], tweet['sentiment_score']))

    tweet_collection.remove({})


while True:
    time.sleep(10)
    extracted_tweets = extract()
    transformed_tweets = transform(extracted_tweets)
    load(transformed_tweets)
    logging.warning(
        '----- New list of tweets has been written into the Postgres database-----')
