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


---

## Motivation 

* Australia: the country of bushfires, sharks and kangaroos - that's all?

* Why do I know about the pandemic situation in France but not about it in Poland?

---
## Idea and Data

* create an interactive globe displaying country connections within a tweet 


<style>
img[alt~="center"] {
  display: block;
  margin: 0 auto
}
</style>

![w:200 center](flowmap_to_globe.png)
 

* first idea: use API from news collection websites → rate limits
* second idea: **twitter data**: news provider have twitter accounts 
* [**https://archive.org/**](https://archive.org/details/archiveteam-twitter-stream-2020-06)

---

###### 🐦 Tweet json

<style>
img[alt~="center"] {
  display: block;
  margin: 1
}
</style>

![w:700 center](tweet_json.png)


---

# ⏩ Data pipeline
 
R
<style>
img[alt~="center"] {
  display: block;
  margin: 0 auto
}
</style>

![w:1100 center](flowchart_tweet_globe.png)




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

