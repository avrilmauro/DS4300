"""
filename: yelp_mongo.py

This file defines the class UserAPI which will be used to query a Mongo database

Homework 3: MongoTutorial
Avril Mauro & Katelyn Donn
"""

from dbutils import DBUtils
import pprint as pp


class UserAPI:

    def __init__(self, database, collection):
        """ Open connection """
        self.dbu = DBUtils(database, collection)

    def close(self):
        """ Close connection """
        self.dbu.close()

    def execute_query(self, criteria, display, type, sort_by, limit):
        result = []
        if type == 'find':
            result = self.dbu.find(criteria, display, sort_by)
        if type == 'distinct':
            result = self.dbu.distinct(display, criteria)

        return [pp.pprint(r) for r in result[:limit]]

    def execute_aggregate(self, group, match):
        agg_query = [match, group]
        result = self.dbu.aggregate(agg_query)
        return [pp.pprint(r) for r in result]

    def clear(self):
        """ Clear the database of all tweets and users """
        pass