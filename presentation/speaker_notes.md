

## speaker notes:

---
## 1) Cover silde

Hiii, I am Lara.

My Background is in geography. Looking at maps has always been one of greatest interest. 
I love exploring thematic information in a spatial context.

My final project is about trying to answer the question: 'How gloablized are out tweets?' visually on a map. 

---

## 2) Motivation for my project

firstly, out of my personal environment: 
- my boyfriend comes from Australia.
Talking to him made me realize how little I knew about his home country -except from being the country of kangaroos, sharks and poisonous spiders. And it made me realize how little is reported about Australia in the german news.
 And if so, then it's only because of a shark attack at Bondy Beach. Or sadly, about  the large bushfires at the start of 2020. 
The second driver for my project idea was the, at least in my opinion, one-sided reporting in german news about the pandemic.
* why do I know about the pandemic sitation in  sweden, the UK, France and Italy, but not really about Poland even though it is so close to Berlin? 

That's why my I wanted to find out how globalized our news actually are in our economically globalized world. 

- In which countries do  citizens get global news in their national newschannels? 
- Are you stuck in your local or national news bubble If you do not pro-actively search for global news?
- Which news channels should I use considering myself as a global citizen? 

---


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

* put a tweet in here
* put a user profile here from a newspaper
* problem: USER location, show example where something random is in there 



---

notes
* getting ready and write load to DB function
    * which attributes are available in the tweet jsons?
    * which filters make sense to apply?
    * which csv lookup files do I have to connect to which variable
    * write helper functions to get coordinates
    * explore location attributes
    * come up with a strategy to get some location



Future plans
- rewrite my giant filtering and insert into database function that probably only I can understand (use classes) 
- dockerize my pipeline
- connect it to the twitter API to see recent globalized tweets (so far i only used a tweet dump for june 2020)

---

thanks to all the teachers, it was fabulous to learn from you!
And thanks spearmints for sharing knowledge, ideas, discussions and of course, cake :)