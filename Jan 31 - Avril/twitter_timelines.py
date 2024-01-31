"""
filename: twitter_timelines.py

This file uses the UserAPI to display user data such as
(1) follower list, (2) following list, (3) tweets posted, and (4) home timeline

Homework 1: TwitterDB
Avril Mauro & Katelyn Donn
"""

from twitter_redis import UserAPI
import random
import pandas as pd
from twitter_objects import Tweet
import time


def get_random_user(users_list):
    unique_users = list(set(users_list))
    random.shuffle(unique_users)
    return unique_users.pop()


def get_user_data(api, userid):
    print("User: ", userid)
    print("Followers: ", api.get_followers(userid))
    print("Following: ", api.get_following(userid))
    print("Tweets: ", api.get_tweets(userid))
    print("Timeline: ", api.get_timeline(userid, store_ref='tweet_store'))


def load_follows(api, csv, user_col, follow_col):
    df = pd.read_csv(csv)
    api.load_users(df[user_col].values.astype(str), df[follow_col].values.astype(str))
    return df


def load_tweets(api, csv, user_col, text_col):
    df = pd.read_csv(csv)
    for uid, text in zip(df[user_col].values, df[text_col].values):
        tw = Tweet(user_id=uid, tweet_text=text)
        api.post_tweet(tw, store_ref='tweet_store')


follow_file = 'follows_sample.csv'
tweet_file = 'tweets_sample.csv'


def main():

    # log into the database
    api = UserAPI(port=6379, host="localhost")

    # load followers and users
    df = load_follows(api, follow_file, "USER_ID", "FOLLOWS_ID")

    start_time = time.time()
    count = 0
    while time.time() - start_time < 60:

        random_user = get_random_user(df.USER_ID)
        get_user_data(api, random_user)

        count += 1

    timeline_count = count/60
    print(f"Timelines per second: {timeline_count:.2f}")


if __name__ == '__main__':
    main()
