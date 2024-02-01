"""
filename: dbutils.py
Homework 2: TwitterRedis
Avril Mauro & Katelyn Donn

Requires the driver:  conda install redis-py

description: A collection of database utilities to make it easier
to implement a database application
"""

import redis


class DBUtils:

    def __init__(self, port, host="localhost"):
        """ Open a connection """
        self.con = redis.Redis(host=host,
                               port=port,
                               decode_responses=True)

    def close(self):
        """ Close or release a connection back to the connection pool """
        self.con.close()
        self.con = None

    def hset(self, key, field, value):
        """ Create a hash key category """
        self.con.hset(key, field, value)

    def get(self, key):
        """ Retrieve value from a key """
        return self.con.get(key)

    def hget(self, key, field):
        """ Retrieve value from a hash key """
        return self.con.hget(key, field)

    def lpush(self, key, value):
        """ Create a list key category """
        self.con.lpush(key, value)

    def lrange(self, key, start, end):
        """ Retrieve list of values from a list key """
        return self.con.lrange(key, start, end)

    def sadd(self, key, value):
        """ Create a set key category """
        self.con.sadd(key, value)

    def smembers(self, key):
        """ Retrieve members of a set key """
        return self.con.smembers(key)

    def sismember(self, key, member):
        """ Return True or False, checking if a value is a member of a set """
        return self.con.sismember(key, member)

    def zadd(self, key, score, value):
        self.con.zadd(key, {value: score})

    def zrange(self, key, start, end, desc=True):
        if desc is True:
            return self.con.zrevrange(key, start, end)
        else:
            return self.con.zrange(key, start, end)

    def flushall(self):
        """ Clear the database of all keys """
        return self.con.flushall()
