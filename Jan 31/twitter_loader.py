"""
filename: twitter_loader.py

This file uses the UserAPI to post 1 Million Tweets
to the TwitterDB database

Homework 1: TwitterDB
Avril Mauro & Katelyn Donn
"""
from twitter_objects import Tweet
from twitter_redis import UserAPI
import pandas as pd
from datetime import datetime


tweet_file = 'tweets_sample.csv'


def main():
    # POSTING TWEETS: Write one program that reads pre-generated tweets from the file tweets.csv.
    # Your code (or the database) should auto-assign tweet_ids and timestamps as the tweet is loaded

    api = UserAPI(port=6379, host="localhost")
    api.clear()

    # POST 1 MILLION TWEETS
    df_tweet = pd.read_csv(tweet_file)
    start_time = datetime.now()

    for uid, text in zip(df_tweet.USER_ID.values, df_tweet.TWEET_TEXT.values):
        tw = Tweet(user_id=uid, tweet_text=text)
        api.post_tweet(tw, store_ref='tweet_store')
        print(tw)

    end_time = datetime.now()

    elapsed_time = (end_time - start_time).total_seconds()
    tps = 1000000/elapsed_time
    print(f"Tweets per second: {tps:.2f}")


if __name__ == '__main__':
    main()
