"""
filename: twitter_mysql.py

This file define the class UserAPI which will be used to
(1) post tweets into the TwitterDB database and (2) return user data

Homework 1: TwitterDB
Avril Mauro & Katelyn Donn
"""

from dbutils import DBUtils


class UserAPI:

    def __init__(self, port, host="localhost"):
        self.dbu = DBUtils(port, host)

    def post_tweet(self, tweet, store_ref):
        self.dbu.hset(f'Tweet:{tweet.tweet_id}', 'user', tweet.user_id)
        self.dbu.hset(f'Tweet:{tweet.tweet_id}', 'text', tweet.tweet_text)
        self.dbu.hset(f'Tweet:{tweet.tweet_id}', 'time', tweet.tweet_ts)

        # build a list of tweet id's posted by each user
        user_key = 'Tweets:' + str(tweet.user_id)
        self.dbu.lpush(user_key, tweet.tweet_id)

        # build a set of tweet id's to search later
        self.dbu.sadd(store_ref, tweet.tweet_id)

    def load_users(self, users, followers):
        for u, f in zip(users, followers):
            following_key = 'Following:' + str(u)
            followers_key = 'Followers:' + str(f)
            self.dbu.sadd(following_key, f)
            self.dbu.sadd(followers_key, u)

    def get_followers(self, selected_user):
        followers_key = 'Followers:' + str(selected_user)
        return self.dbu.smembers(followers_key)

    def get_following(self, selected_user):
        following_key = 'Following:' + str(selected_user)
        return self.dbu.smembers(following_key)

    def get_tweets(self, selected_user):
        user_key = 'Tweets:' + str(selected_user)
        print(self.dbu.lrange(user_key, 0, -1))
        return self.dbu.lrange(user_key, 0, -1)

    def get_post(self, tweetid, field):
        return self.dbu.hget(tweetid, field)

    def clear(self):
        self.dbu.flushall()

    # EXTRA CREDIT -- build timeline through searches
    def get_timeline(self, selected_user, store_ref):
        # following is a set
        following = self.get_following(selected_user)
        ''' METHOD 2: search through all tweets for users you follow, append to a list, sort top 10 time '''''

        # t = tweet id
        for t in self.dbu.smembers(store_ref):
            u = self.dbu.hget(f'Tweet:{t}', 'user')

            if self.dbu.sismember(following, u) is True:
                print("TRUE")
                tw = self.dbu.hget(f'Tweet:{t}', 'text')
                self.dbu.lpush(f'Timeline{selected_user}', tw)

        timeline = self.dbu.lrange(f'Timeline{selected_user}', 0, -1)
        return timeline[0:10]

        ''' METHOD 1: get all tweetids from all following, then find their timestamps to sort top 10
        full_timeline = []
        for uid in following:
            # returns a list of tweet ids
            tweets = self.get_tweets(uid)

            for t in tweets:
                full_timeline.append(t)

        for tweetid in full_timeline:
        '''
