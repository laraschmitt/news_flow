from flask import Flask, escape, request, render_template, jsonify
import psycopg2

try:
    conn = psycopg2.connect(
        "dbname='tweets_multilingu' user='postgres' host='localhost' password='postgres'")
except:
    print("I am unable to connect to the database")

cur = conn.cursor()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/places')
def places():
    cur.execute("""SELECT from_coords from tweets_test""")
    rows = cur.fetchall()

    features = []

    for row in rows:
        features.append({
            'type': 'Feature',
            'geometry': {
                    'type': 'LineString',
                    'coordinates': [
                        row[0].split(','),
                        row[0].split(',')
                    ]
            }
        })
    return jsonify({
        'type': 'FeatureCollection',
        'features': [
            {
                'type': 'Feature',
                'properties': {
                    'count_tweets': 5,
                    'from_country': 'USA',
                    'to_country': 'random'
                },
                'geometry': {
                    'type': 'LineString',
                    'coordinates': [
                        [
                            -85.605166,
                            30.355644
                        ],
                        [
                            -99.1329340602939,
                            19.444388301415472
                        ]
                    ]
                }
            }
        ]
    })
