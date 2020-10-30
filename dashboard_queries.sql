-- DASHBOARD QUERIES --

-- countries where most tweets came from 
-- (mentioned a foreign location (country or city)
SELECT from_country_name, COUNT(tweet_id)
FROM tweets_test
GROUP BY from_country_name
ORDER BY COUNT DESC;

-- countries most tweets are about
-- (places (countries/cities) that were mentioned the most 
SELECT to_country_name, COUNT(tweet_id)
FROM tweets_test
GROUP BY to_country_name
ORDER BY COUNT DESC;


-- user_url of users who tweeted the most about foreign places
-- these newspaper accounts should we follow on twitter
-- if we want to be informed about what's happening elswhere
SELECT user_url, user_followers_count, COUNT(tweet_id)
FROM tweets_test
GROUP BY  user_followers_count, user_url
ORDER BY COUNT DESC;

-- users with the biggest reach (highest follower count)
DROP VIEW highest_reach;

CREATE VIEW highest_reach AS
SELECT DISTINCT user_url, user_followers_count
FROM tweets_test
ORDER BY user_followers_count DESC;

-- the follower count changed over time,
-- keep only the rows with the highest follower count per user
SELECT user_url, max(user_followers_count) as followers
FROM highest_reach 
GROUP BY user_url
ORDER BY followers DESC;


-- most frequent languages:
SELECT COUNT(tweet_id), lang
FROM tweets_test
GROUP BY lang
ORDER BY COUNT DESC;


-- need: hashtags, city names, retweeted / upvotes




--tweets with lots of engagement
SELECT *
FROM tweets_test;



-- cities most tweets are about
-- cities that were mentioned the most 
SELECT XXX, COUNT(tweet_id)
FROM tweets_test
GROUP BY XXX
ORDER BY COUNT DESC;
