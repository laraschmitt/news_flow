from flask import Flask, escape, request, render_template, jsonify
import psycopg2
import os
from urllib.parse import urlparse

database_url = os.getenv('DATABASE_URL')
result = urlparse(database_url)

username = result.username
password = result.password
database = result.path[1:]
hostname = result.hostname


try:
    conn = psycopg2.connect(
        database=database,
        user=username,
        password=password,
        host=hostname
    )
except:
    print("I am unable to connect to the database")

cur = conn.cursor()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/places')
def places():
    cur.execute("""SELECT from_country_coords, to_country_coords, from_country_name, to_country_name from tweets_test""")
    rows = cur.fetchall()

    features = []

    for row in rows:
        features.append({
            'type': 'Feature',
            'properties': {
                'from_country': row[2],
                'to_country': row[3],
            },
            'geometry': {
                'type': 'LineString',
                'coordinates': [
                        row[0].split(',')[::-1],
                        row[1].split(',')[::-1]
                ]
            }
        })
    return jsonify({
        'type': 'FeatureCollection',
        'features': features
    })


if __name__ == "__main__":
    app.run(host='0.0.0.0')
