"""
filename: dbutils.py
Requires the driver:  conda install mysql-connector-python

description: A collection of database utilities to make it easier
to implement a database application
"""


import redis


class DBUtils:

    def __init__(self, port, host="localhost"):
        """ Future work: Implement connection pooling """
        self.con = redis.Redis(host=host,
                               port=port,
                               decode_responses=True)

    def close(self):
        """ Close or release a connection back to the connection pool """
        self.con.close()
        self.con = None

    def hset(self, key, field, value):
        self.con.hset(key, field, value)

    def get(self, key):
        return self.con.get(key)

    def hget(self, key, field):
        return self.con.hget(key, field)

    def lpush(self, key, value):
        self.con.lpush(key, value)

    def lrange(self, key, start, end):
        return self.con.lrange(key, start, end)

    def sadd(self, key, value):
        self.con.lpush(key, value)

    def smembers(self, key):
        return self.con.smembers(key)

    def sismember(self, key, member):
        return self.con.sismember(key, member)


