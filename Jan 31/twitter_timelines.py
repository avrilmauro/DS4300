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
import time

def get_random_user(users_list):
    unique_users = list(set(users_list))
    random.shuffle(unique_users)
    return unique_users.pop()


def main():

    # log into the database
    api = UserAPI(port=6379, host="localhost")
    api.clear()

    df_follows = pd.read_csv('follows_sample.csv')

    # NEW
    api.load_users(df_follows.USER_ID.values.astype(str), df_follows.FOLLOWS_ID.values.astype(str))

    # start_time = time.time()
    # count = 0
    # while time.time() - start_time < 60:

        # select a random user
    random_user = get_random_user(df_follows.USER_ID)

        # display user data
    random_user = 1
    print(random_user)
    print('1',api.get_followers(random_user))
    print('2',api.get_following(random_user))
    print('3',api.get_tweets(random_user))

        # display home timeline
    print(api.get_timeline(random_user, store_ref='tweet_store'))

        # count += 1

    # timeline_count = count/60
    # print(f"Timelines per second: {timeline_count:.2f}")

if __name__ == '__main__':
    main()
