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

    def set(self, key, value):
        """ store a value to a key """
        self.con.set(key, value)

    def get(self, key):
        """ get a value of a key """
        return self.con.get(key)

    def hset(self, key, field, value):
        """ get a value to a field of a hash """
        self.con.hset(key, field, value)

    def hget(self, key, field):
        """ get a value from a field of a hash """
        return self.con.hget(key, field)

    def flushall(self):
        """ clear the server contents """
        self.con.flushall()




