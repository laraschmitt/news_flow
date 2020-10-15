-- script to create a table for storing twitter tweets 

DROP TABLE tweets_test;

CREATE TABLE tweets_test(
    id BIGINT NOT NULL,
    timestamp_ms VARCHAR NOT NULL,
    tweet VARCHAR NOT NULL,
    url_in_tweet VARCHAR,

    user_url VARCHAR,
    user_location VARCHAR, 
    user_followers_count BIGINT,
    user_verified BOOLEAN,
    user_statuses_count BIGINT,
    user_id BIGINT,
    user_created_at TIMESTAMP,

    lang VARCHAR(10),
    from_coords VARCHAR,
    from_country_coords VARCHAR,
    to_country_coords VARCHAR,
    tweet_country_code VARCHAR    
);