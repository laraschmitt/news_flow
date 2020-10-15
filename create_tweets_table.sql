-- script to create a table for storing twitter tweets 
CREATE TABLE tweets_test(
    id INT NOT NULL PRIMARY KEY,
    timestamp_ms TIMESTAMP NOT NULL,
    tweet VARCHAR NOT NULL,
    url_in_tweet VARCHAR,
    user_url VARCHAR,
    user_location VARCHAR, 
    user_followers_count INT NOT NULl,
    user_verified VARCHAR NOT NULL,
    user_statuses_count INT NOT NULL,
    lang VARCHAR(10),
    geo VARCHAR,
    coordinates VARCHAR,
    place VARCHAR,
    user_id INT NOT NULL,
    user_created_at TIMESTAMP NOT NULL
);


-- create a column only for the data, how to insert?
SELECT to_timestamp(1195374767);