"""
filename: twitter_timelines.py

This file uses the UserAPI to display user data such as
(1) follower list, (2) following list, (3) tweets posted, and (4) home timeline

Homework 1: TwitterDB
Avril Mauro & Katelyn Donn
"""

from twitter_mysql import UserAPI
import random
import pandas as pd


follow_file = 'follows.csv'


def get_random_user(users_list):
    unique_users = list(set(users_list))
    random.shuffle(unique_users)
    return unique_users.pop()


def main():

    # log into the database
    api = UserAPI("T_USER", "T_PASS", "TwitterDB", host="localhost")

    # select a random user
    df_follows = pd.read_csv('follows.csv')
    random_user = get_random_user(df_follows.USER_ID)

    # display user data
    print(api.get_followers(random_user))
    print(api.get_following(random_user))
    print(api.get_tweets(random_user))

    # display home timeline
    print(api.get_timeline(random_user))


if __name__ == '__main__':
    main()
