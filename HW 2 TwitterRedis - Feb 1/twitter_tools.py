"""
filename: twitter_tools.py
Homework 2: TwitterRedis
Avril Mauro & Katelyn Donn

required libraries: pandas, random
dependent files: twitter_objects.py

description: A collection of functions to
aid the implementation a Twitter API (see twitter_redis.py)
"""

from twitter_objects import Tweet
import pprint as pp
import pandas as pd
import random


def load_tweets(api, csv, user_col, text_col):
    """ Load tweets & post to redis """
    df = pd.read_csv(csv)
    for uid, text in zip(df[user_col].values, df[text_col].values):
        tw = Tweet(user_id=uid, tweet_text=text)
        api.post_tweet(tw, store_ref='tweet_store')
        print(tw)


def get_speed(end_time, start_time, tweet_amount, label):
    """ Get speed of tweet post and retrieval """
    elapsed_time = (end_time - start_time).total_seconds()
    tps = tweet_amount / elapsed_time
    return f'\n{label} per second: {tps:.2f}'


def get_random_user(users_list):
    """ Generates random user out of unique user list """
    unique_users = list(set(users_list))
    random.shuffle(unique_users)
    return unique_users.pop()


def refresh_timeline(api, userid):
    """ Generates timeline for a user """
    print('Timeline:')
    pp.pprint(api.get_timeline(userid), indent=4, width=500)


def get_user_data(api, userid, tweets=True):
    """ Generates and prints user data based on userid """
    print("\nUser: ", userid)
    print("Followers: ", api.get_followers(userid))
    print("Following: ", api.get_following(userid))

    if tweets is True:
        print("Tweets:")
        pp.pprint(api.get_tweets(userid), indent=4)

    # displays timeline
    refresh_timeline(api, userid)


def load_follows(api, csv, user_col, follow_col):
    """ Loads users and corresponding follows into a df """
    df = pd.read_csv(csv)
    api.load_users(df[user_col].values.astype(str), df[follow_col].values.astype(str))
    return df
