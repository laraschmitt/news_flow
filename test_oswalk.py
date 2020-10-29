import os

coll = []
path = "./data/archiveteam-twitter-stream-2020-06/"

for dirpath, dirs, files in os.walk(path):
    for f in files:
        os.path.join(dirpath, f)
