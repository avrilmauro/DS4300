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


def load_tweets(api, csv, user_col, text_col):
    df = pd.read_csv(csv)
    for uid, text in zip(df[user_col].values, df[text_col].values):
        tw = Tweet(user_id=uid, tweet_text=text)
        api.post_tweet(tw, store_ref='tweet_store')
        print(tw)


def get_speed(end_time, start_time, tweet_amount):
    elapsed_time = (end_time - start_time).total_seconds()
    tps = tweet_amount/elapsed_time
    return f'Tweets per second: {tps:.2f}'


tweet_file = 'tweet.csv'


def main():

    api = UserAPI(port=6379, host="localhost")
    api.clear()

    start_time = datetime.now()
    load_tweets(api, tweet_file, "USER_ID", "TWEET_TEXT")
    end_time = datetime.now()

    print(get_speed(end_time, start_time, 1000000))


if __name__ == '__main__':
    main()
