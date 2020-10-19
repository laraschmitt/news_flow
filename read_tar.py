import pandas as pd
import json
from sqlalchemy import create_engine
import zipfile
import tarfile
import bz2
import sys
import os
import pprint

# tar file for the first day 
tar = tarfile.open("/Users/lara/Downloads/archiveteam-twitter-stream-2020-06/twitter_stream_2020_06_01.tar", "r")


for member in tar.getmembers():
    f = tar.extractfile(member)
    if f != None:
        content = f.read()
        print(content)
