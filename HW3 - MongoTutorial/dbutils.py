"""
filename: dbutils.py
Homework 3: MongoTutorial
Avril Mauro & Katelyn Donn

This file contains a collection of database utilities to make
it easier to implement a database application

requires the driver:  conda install pymongo
required libraries: pymongo
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
        """ Query search based on user-specified criteria """
        if sort_by is None:
            return self.collection.find(criteria, display)
        else:
            return self.collection.find(criteria, display).sort(sort_by[0], sort_by[1])

    def distinct(self, d_field, criteria):
        """ Query unique values based on user-specified criteria """
        return self.collection.distinct(d_field, criteria)

    def aggregate(self, query):
        """ Aggregate values based on user-specified criteria """
        return self.collection.aggregate(query)
