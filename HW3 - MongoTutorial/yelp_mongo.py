"""
filename: yelp_mongo.py
Homework 3: MongoTutorial
Avril Mauro & Katelyn Donn

This file defines the class UserAPI which will be used to query a Mongo database

required files: dbutils.py
required libraries: pprint
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
        """ Exectutes find and distinct queries """
        result = []
        if type == 'find':
            result = self.dbu.find(criteria, display, sort_by)
        if type == 'distinct':
            result = self.dbu.distinct(display, criteria)

        return [pp.pprint(r) for r in result[:limit]]

    def execute_aggregate(self, group, match):
        """ Execute aggregate query """
        agg_query = [match, group]
        result = self.dbu.aggregate(agg_query)
        return [pp.pprint(r) for r in result]
