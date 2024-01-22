"""
filename: twitter_mysql.py

This file define the class UserAPI which will be used to
(1) post tweets into the TwitterDB database and (2) return user data

Homework 1: TwitterDB
Avril Mauro & Katelyn Donn
"""

from dbutils import DBUtils


class UserAPI:

    def __init__(self, user, password, database, host="localhost"):
        self.dbu = DBUtils(user, password, database, host)

    def post_tweet(self, tweeter):
        sql = 'INSERT INTO Tweet (tweet_id, user_id, tweet_ts, tweet_text) VALUES (%s, %s, %s, %s)'

        val = (tweeter.tweet_id, tweeter.user_id, tweeter.tweet_ts, tweeter.tweet_text)

        self.dbu.insert_one(sql, val)

    def get_followers(self, selected_user):
        sql = f"""  SELECT user_id FROM TwitterDB.Follows
                    WHERE follows_id = {selected_user};
               """
        df = self.dbu.execute(sql)
        df.columns = ['Followers']

        if len(df) == 0:
            return f'This user ({selected_user}) has no followers.'
        else:
            return df

    def get_following(self, selected_user):
        sql = f"""  SELECT follows_id FROM TwitterDB.Follows
                    WHERE user_id = {selected_user};
               """
        df = self.dbu.execute(sql)
        df.columns = ['Following']
        if len(df) == 0:
            return f'This user ({selected_user}) is not following anyone.'
        else:
            return df

    def get_tweets(self, selected_user):
        sql = f"""  SELECT * FROM TwitterDB.Tweet
                    WHERE user_id = {selected_user};
               """
        df = self.dbu.execute(sql)

        print('-'*45 + f'\n\tdisplaying tweets made by user: {selected_user}\n' + '-'*45)

        return df

    def get_timeline(self, selected_user):
        sql = f"""  SELECT t.user_id, t.tweet_text FROM TwitterDB.Tweet t
                    JOIN TwitterDB.Follows f ON t.user_id = f.follows_id
                    WHERE f.user_id = {selected_user}
                    ORDER BY t.tweet_ts DESC
                    LIMIT 10; 
              """

        df = self.dbu.execute(sql)

        print('-'*45 + f'\n\tgenerating timeline for user: {selected_user}\n' + '-'*45)

        return df





