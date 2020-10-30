---
marp: true
theme: gaia
_class: invert

---
# 🌍 How globalized are our tweets?

<br>
<br>
<br>
<br>


##### Lara Schmitt
Spiced Academy Data Science Course - Final Project
Spearmint Vector Machine Cohorte 
2 November, 2020

---

## Motivation 

* Australia: the country of bushfires, sharks and kangaroos - that's all?

* Why do I know about the pandemic situation in France but not about it in Poland?

---
## Goal

* flowmap mapped to a globe to show about which countries a country reports 


<style>
img[alt~="center"] {
  display: block;
  margin: 0 auto
}
</style>

![w:200 center](flowmap_to_globe.png)


---

## Data sources

* first idea: use API from news collection websites → rate limits
* twitter: news provider have twitter accounts 

---

# Tweet structure


---



# ⏩ Data pipeline


FLOWCHART 
for the tweet dump of June 2020:
json files → filter & get coordinates script → postgres db → dashboard

for the live dashboard:
twitter API scraping → filtering  ...

adjust code of ([globe basemap](http://bl.ocks.org/dwtkns/4686432))



---

# 💻 Tech stack
* 🐍 **python**: data exploration, wrangling and db insert
     * 🐼 pandas
     * 🧙🏻‍♀️ sql alchemy
* 🐘 **postgres**: database
* ❓ **SQL**: query the DB
* 🧪 **flask**: python web framework
* 🎨 **D3.js**: visualization
* ☁️ **heroku**: hosting 



---
# ⏰ Time spend 

* find/ explore datasets: `1 day`

* write SPARQL queries `1 afternoon`

* **data wrangling**: explore/ combine/ alter lookup tables `3 days`

* **write function** to filter tweets and load to DB: `3-4 days`
  
* create globe visualization (with major help!) `1 morning`

* set up flask server `1 afternoon`

* deploy on heroku `1 afternoon`

---

# 💡 What was exciting to learn?

* exploring tweets from around the world 
* setting up a whole pipeline on my own
* first insights in how to visualize with D3.js 
* creating a [data-driven map](https://twitter-globe.herokuapp.com/)


---

# Future plans
* 📝 rewrite my giant "filter_and_insert_data" function 
* 🐳 dockerize 
* 🐦 connect to twitter API 
* ...

---
<br>

# Thanks, spiced & spearmints! 