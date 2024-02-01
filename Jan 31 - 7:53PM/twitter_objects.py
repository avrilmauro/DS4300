"""
filename: twitter_objects.py
Homework 2: TwitterRedis
Avril Mauro & Katelyn Donn

required libraries: random, datetime

description: this file contains the Tweet class which is used to
initialize a tweet object to be loaded into the database
"""

import random
from datetime import datetime

# Random id for tweet
all_ids = list(range(1, 1000001))
random.shuffle(all_ids)


class Tweet:

    def __init__(self, user_id, tweet_text):
        self.tweet_id = int(all_ids.pop())
        self.user_id = int(user_id)
        # self.tweet_ts = int(datetime.now().strftime('%Y%m%d%H%M%S%f'))
        self.tweet_ts = datetime.timestamp(datetime.now())*1000
        self.tweet_text = str(tweet_text)


    def __str__(self):
        return f"user_id: {self.user_id}\n" \
               f"tweet: {self.tweet_text}\n" \
               f"tweet_id: {self.tweet_id}\n" \
               f"timestamp: {self.tweet_ts}\n"

