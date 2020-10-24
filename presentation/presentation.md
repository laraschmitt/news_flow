---
marp: true
theme: gaia
_class: invert

---
# 🌍 How globalized are our news?
### (on twitter)
<br>
<br>
<br>
<br>


##### Lara Schmitt
Spiced Academy Data Science Course - Final Project
Spearmint Vector Machine Cohorte 
2 November, 2020

---
speaker notes:
i am Lara and I studied global change geography. I love looking at mags and I love creating maps. 





---
## Motivation

German news seems so one-sided
* At the beginning of the year: fires in Australia
* during the pandemic - "Querdenker" haven't read about how serious the situation is elsewhere?
* why do I know about the corona cases in the western europe but not really about Poland even though it is so close to Berlin? 
* which news to I have to consume as a global citizen? 
* (is twitter a good source for getting informed?)

---
speaker notes:
^ During the lockdown: in Germany corona cases from Western Europe and China and US but not Eastern Europe
^ The news seem to be really biased
^ And if you do not actively try to be a "global citizen" and search for international news, you get stuck in your local/national bubble
^ This is dangerous, especially in the face of climate change (we need to care about all humans/ all creatures on earth and not only about our immediate surroundings?
Maybe then people would not go on the street in Berlin to demonstrate against wearing a mask in the supermarket if they understood how severe the situation is elsewhere?

---

## Data source

Using the API from different news ...?

Problem: not all countries are represented (especially Africa and Asia are missing)
But good for a start to test my pipeline

# at the end:
Get data from twitter tweets:
Is it used everywhere around the globe?
Not sure
But at least everyone can use it and probably the big newspapers of many countries use it

I am geographer and love to make maps! 
That is why my visualisation goal was to make a flow map 

---
# [fit] ⌘+C ⌘+V = :v:
---

# Tweet structure
* put a tweet in here
* put a user profile here from a newspaper
* problem: USER location, show example where something random is in there 
---
notes;
- only very few tweets are georeferenced
- and also only available if you pay for the Twitter API
- BUT: i was only interested in tweets sent from newspapers and thought about a way to identify them
criteria: certain follower count or user profile verified, URL given in profile (links to their website), URL given in tweet (link to the newspaper article)

problem: user_location is a free text field, so it can be anything 
filtered for citynames or countrynames appearing in the user_location field

GNERAL IDEA: check if a countryname (in any language) is mentioned in the tweet/header of the article and see this as a proxy 
FIST IDEA: create a live dashboard, that updates all the time counting the number of tweets in which another country is mentioned and show per country of the world for today, for the last seven days, and show which countries are mentioned the most (US, china?)
create a flowmap that shows the relationships

luckely I found some freely available lookup tables for
- countryname multilingual
- countryname - coordinates (in the middle)
- world cities (in english) - coordinates
- world cities multilingual...

so: spend a lot of time with data extraction/wrangling before i was able to put it into a database

sure not perfect method, since i also got some indiviudals that are very popular on twitter (showe example)

---

# 💻 Tech stack
* 🐍 **python**: data exploration and scraping
    * 🜁 sql alchemy
    * 🐼 pandas
    * 🔢 numpy 
* 🐘 **postgres** database
* 🍼 **flask**
* 🎨 **D3** for creating plots
* ☁️ heroku
* 🐳 docker 


---
# ⏰ Time spend 
* find data: `2 hours`

* getting ready and write load to DB function `3 days`
  
* write scraping script `1 afternoon`

* create flow map 

* set up dashboard and write SQL queries `loooong`

* set up flask `lllong`

* deploy on .... `shorter`

---

notes
* getting ready and write load to DB function
    * which attributes are available in the tweet jsons?
    * which filters make sense to apply?
    * which csv lookup files do I have to connect to which variable
    * write helper functions to get coordinates
    * explore location attributes
    * come up with a strategy to get some location

---

# ⏩ Data pipeline

for the tweet dump of June 2020:
json files → filter & get coordinates script → postgres db → dashboard

for the live dashboard:
twitter API scraping → filtering  ...

---

# 💡 What was exciting to learn?

* setting up a whole pipeline on my own
* learning how to use DJ3
* creating flow maps 😍
* the content [result](www.google.de) of the project 


---



# Future plans
* set up ... 
