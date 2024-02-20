"""
filename: mongo_main.py
Homework 3: Mongo Tutorial
Avril Mauro & Katelyn Donn

This file allows a user to investigate a database
without requiring knowledge of mongo

required files: mongo_tools.py, yelp_mongo.py
"""

from yelp_mongo import UserAPI
import mongo_tools as mt


def main():

    # Initialize the connection
    api = UserAPI(database='yelp', collection='yelp')

    # User-input for query types
    q_type = mt.query_type(int(input('How do you want to explore the data?\n'
                                     '\t[1] Search with criteria'
                                     '\n\t[2] Search for distinct results'
                                     '\n\t[3] Aggregate results'
                                     '\nEnter a number from above: ')))

    # Execute queries accordingly
    if q_type == 'aggregate':
        api.execute_aggregate(group=mt.define_group(),
                              match=mt.build_match())
    else:
        api.execute_query(criteria=mt.build_filters(),
                          display=mt.select_fields(q_type),
                          type=q_type,
                          sort_by=mt.define_sort(q_type),
                          limit=mt.define_limit())

    # Close the connection
    api.close()


if __name__ == '__main__':
    main()
