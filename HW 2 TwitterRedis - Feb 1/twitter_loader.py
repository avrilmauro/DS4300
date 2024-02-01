"""
filename: twitter_loader.py
Homework 2: TwitterRedis
Avril Mauro & Katelyn Donn

required libraries: datetime, redis, random, pandas
dependent files: twitter_redis.py, twitter_tools.py, twitter_objects.py, tweet.csv

This file uses the UserAPI to post 1 Million Tweets
to the TwitterDB database
"""

from twitter_redis import UserAPI
from twitter_tools import load_tweets, get_speed
from datetime import datetime

tweet_file = 'tweet.csv'
num_tweets = 1000000


def main():

    # Log into the database
    api = UserAPI(port=6379, host="localhost")
    api.clear()

    # Load tweets, track speed of load
    start_time = datetime.now()
    load_tweets(api, tweet_file, "USER_ID", "TWEET_TEXT")
    end_time = datetime.now()
    print(get_speed(end_time, start_time, num_tweets, label="Tweets"))

    # Close redis connection
    api.close()


if __name__ == '__main__':
    main()
