# first python script that reads the csv and queries one source - print to commandline

import json
import os
import time
from newsapi import NewsApiClient
from datetime import date, timedelta
# keys: name and alpha2

# init

newsapi = NewsApiClient(api_key='98b9ddb4d2eb4ecfb42a33c38daaeb74')
print(os.getcwd())
data_dir = '/data/'
for filename in os.listdir(os.getcwd() + data_dir):
    print('→ Querying news for', filename)
    with open(os.getcwd() + data_dir + filename, 'r') as json_file:
        today = date.today()
        month_ago = today - timedelta(days=30)
        format = '%Y-%m-%d'

        data = json.load(json_file)
        response = newsapi.get_sources(
            country=filename.replace('.json', ''))  # response is a dict
        source_ids = ','.join(
            list(map(lambda s: s['id'], response['sources'])))

        for p in data:
            # /v2/everything
            all_articles = newsapi.get_everything(
                q=p['name'],
                sources=source_ids,
                from_param=month_ago.strftime(format),
                to=today.strftime(format)
            )
            time.sleep(3)
            print('📚 Total articles for',
                  p['name'], all_articles['totalResults'])

            for article in all_articles:
                score = 1
                if article['title'].contains(p['name']):
                    score += 1
                result = {
                    'id': article['url'],
                    'score': score,
                    'from_country': filename.replace('.json', ''),
                    'to_country': p['alpha2'],
                    'published_date': article['publishedAt'],
                    'title': article['title'],
                    'url_to_image': article['urlToImage']
                    'source': article['source']
                }
                print('🧮 Writing to Mongo', result['id'])


# germany often uses USA instead of "Vereinigte Staaten"
# and "Grossbritannien" for the UK (Vereinigtes Koenigreich)


# for mongo
# {
#   id: "https://somearticle.com/foo/bar",
#   score: 2,
#   from_country: "de",
#   to_country: "au",
#   published_date: "XXXXXX"
#   query: "australien"
# }
