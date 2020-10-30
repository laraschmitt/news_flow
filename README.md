# Tweet globe 


Analysis of foreign country and citynames mentionend in Tweets of users with a certain followercount and given user location. 

hosted on heroku: https://twitter-globe.herokuapp.com/

### Data obtained from:
- [archiveteam-twitter-stream-2020-06](https://archive.org/details/archiveteam-twitter-stream-2020-06)
- [IP2Location™ City Multilingual Database](https://www.ip2location.com/free/city-multilingual)
- [IP2Location™ Country Multilingual Database](https://www.ip2location.com/free/country-multilingual)
- [wikidata](https://query.wikidata.org/)

#### Globe basemap obtained from:
- [Faux-3d Shaded Globe](http://bl.ocks.org/dwtkns/4686432)

## Requirements

- free heroku account (webapp and postgres db)
- heroku cli installed and set up locally 

## Instructions

0. load dataset
* archiveteam

1. clone the repository

```bash
git clone https://github.com/bonartm/heroku-flask.git
cd heroku-flask
```

2. create a new heroku app

```bash
heroku create twitter-globe`
```

3. test the app locally

```bash
heroku local web
```

4. push code to heroku

```bash
git push heroku master
```

5. open website in browser

```bash
heroku open
```

