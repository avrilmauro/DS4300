"""
filename: twitter_timelines.py
Homework 2: TwitterRedis
Avril Mauro & Katelyn Donn

required libraries: datetime, redis, random, pandas
dependent files: twitter_redis.py, twitter_tools.py, follows.csv

This file uses the UserAPI to display user data such as
(1) follower list, (2) following list, (3) tweets posted, and (4) home timeline
"""

from twitter_redis import UserAPI
from twitter_tools import get_random_user, get_user_data, load_follows, get_speed
from datetime import datetime

follow_file = 'follows.csv'
num_runs = 2000


def main():

    # Log into the database
    api = UserAPI(port=6379, host="localhost")

    # Load followers and users
    df = load_follows(api, follow_file, "USER_ID", "FOLLOWS_ID")

    # Load an example
    example_user = get_random_user(df.USER_ID)
    get_user_data(api, example_user, tweets=True)

    # Get timelines for random user, track speed of timeline pull
    start_time = datetime.now()
    for i in range(num_runs):
        random_user = get_random_user(df.USER_ID)
        get_user_data(api, random_user, tweets=False)
    end_time = datetime.now()
    print(get_speed(end_time, start_time, num_runs, label='Timelines'))

    # Close redis connection
    api.close()


if __name__ == '__main__':
    main()
