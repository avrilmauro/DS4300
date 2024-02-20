"""
filename: dbutils.py
Requires the driver:  conda install pymongo

description: A collection of database utilities to make it easier
to implement a database application

Homework 3: MongoTutorial
Avril Mauro & Katelyn Donn
"""


from pymongo import MongoClient


class DBUtils:

    def __init__(self, database, collection):
        """ Open a connection (client) """
        self.client = MongoClient()
        self.db = self.client[database]
        self.collection = self.db[collection]

    def close(self):
        """ Close connection """
        self.client.close()
        self.client = None

    def find(self, criteria, display, sort_by):
        """ Query """
        if sort_by is None:
            return self.collection.find(criteria, display)
        else:
            return self.collection.find(criteria, display).sort(sort_by[0], sort_by[1])

    def distinct(self, d_field, criteria):
        return self.collection.distinct(d_field, criteria)

    def aggregate(self, query):
        return self.collection.aggregate(query)
