"""
filename: twitter_redis.py
Homework 2: TwitterRedis
Avril Mauro & Katelyn Donn

dependent files: dbutils.py

This file define the class UserAPI which will be used to
(1) post tweets into the TwitterDB database and (2) return user data
"""

from dbutils import DBUtils


class UserAPI:

    def __init__(self, port, host="localhost"):
        """ Open connection """
        self.dbu = DBUtils(port, host)

    def close(self):
        """ Close connection """
        self.dbu.close()

    def post_tweet(self, tweet, store_ref):
        """ Create hash key using tweet_id, assigning fields for user, text, and time """
        self.dbu.hset(f'Tweet:{tweet.tweet_id}', 'user', tweet.user_id)
        self.dbu.hset(f'Tweet:{tweet.tweet_id}', 'text', tweet.tweet_text)
        self.dbu.hset(f'Tweet:{tweet.tweet_id}', 'time', tweet.tweet_ts)

        # build a list of tweet id's posted by each user
        user_key = 'Tweets:' + str(tweet.user_id)
        #self.dbu.lpush(user_key, tweet.tweet_text)
        self.dbu.lpush(user_key, tweet.tweet_id)

        # build a set of tweet id's to search later
        # self.dbu.lpush(store_ref, tweet.tweet_id)
        self.dbu.zadd(store_ref, tweet.tweet_ts, tweet.tweet_id)


    def load_users(self, users, followers):
        """ Takes a list of user ids and follow ids and
        creates sets of followers and following for each user """
        for u, f in zip(users, followers):
            following_key = 'Following:' + str(u)
            followers_key = 'Followers:' + str(f)
            self.dbu.sadd(following_key, f)
            self.dbu.sadd(followers_key, u)

    def get_followers(self, selected_user):
        """ Retrieve the set of user ids that are following a given user """
        followers_key = 'Followers:' + str(selected_user)
        return self.dbu.smembers(followers_key)

    def get_following(self, selected_user):
        """ Retrieve the set of user ids that a given user is following """
        following_key = 'Following:' + str(selected_user)
        return self.dbu.smembers(following_key)

    def get_tweets(self, selected_user):
        """ Retrieve a list of tweets (ids) posted by a given user """
        user_key = 'Tweets:' + str(selected_user)
        return self.dbu.lrange(user_key, 0, -1)

    def clear(self):
        """ Clear the database of all tweets and users """
        self.dbu.flushall()

    def get_timeline(self, selected_user, store_ref):
        """ Retrieve the 10 most recent tweets from a user's following list """
        following_key = 'Following:' + str(selected_user)

        f_tweets = []
        for f in self.dbu.smembers(following_key):
            f_tweets += self.dbu.lrange(f'Tweets:{f}', 0, -1)

        for t in f_tweets:
            ts = self.dbu.hget(f'Tweet:{t}', 'time')
            tw = self.dbu.hget(f'Tweet:{t}', 'text')
            self.dbu.zadd(f'Timeline:{selected_user}', ts, tw)

        # return the most recent 10 tweets
        timeline = self.dbu.zrange(f'Timeline:{selected_user}', 0, 10, desc=True)
        return timeline
    '''
    def get_timeline(self, selected_user, store_ref):
        """ Retrieve the 10 most recent tweets from a user's following list """
        following_key = 'Following:' + str(selected_user)

        # search through all tweet ids
        for t in self.dbu.zrange(store_ref, 0, -1, desc=True):
            # retrieve the user id of each tweet
            u = self.dbu.hget(f'Tweet:{t}', 'user')

            # add the tweet to the timeline if the user is in the following set
            if self.dbu.sismember(following_key, u) is True:
                ts = self.dbu.hget(f'Tweet:{t}', 'time')
                tw = self.dbu.hget(f'Tweet:{t}', 'text')
                self.dbu.zadd(f'Timeline:{selected_user}', int(round(float(ts), 0)), tw)

        # return the most recent 10 tweets
        timeline = self.dbu.zrange(f'Timeline:{selected_user}', 0, 10, desc=True)
        return timeline
    '''