"""
filename: twitter_objects.py

This file contains the Tweet class which is used to
initialize a tweet object to be loaded into the database

Homework 1: TwitterDB
Avril Mauro & Katelyn Donn
"""

import random
from datetime import datetime


all_ids = list(range(1, 1000001))
random.shuffle(all_ids)


class Tweet:

    def __init__(self, user_id, tweet_text):
        self.tweet_id = int(all_ids.pop())
        self.user_id = int(user_id)
        self.tweet_ts = datetime.now()
        self.tweet_text = str(tweet_text)

    def __str__(self):
        return f"user_id: {self.user_id}\n" \
               f"tweet: {self.tweet_text}\n" \
               f"tweet_id: {self.tweet_id}\n" \
               f"timestamp: {self.tweet_ts}\n"

