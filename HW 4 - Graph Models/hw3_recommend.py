"""
filename: hw3_recommend.py

This file It builds the person/book network and obtains book recommendations for Spencer.

Homework 4: Graph Models
Avril Mauro & Katelyn Donn
"""

from hw3_api import UserAPI


def main():
    # log into the database
    api = UserAPI(port=6379, host="localhost")

    # flush the server
    api.clear()

    # add nodes
    api.add_node('Emily', 'person')
    api.add_node('Spencer', 'person')
    api.add_node('Brenden', 'person')
    api.add_node('Trevor', 'person')
    api.add_node('Paxton', 'person')
    api.add_node('Cosmos', 'book')
    api.add_node('Database Design', 'book')
    api.add_node('The Life of Cronkite', 'book')
    api.add_node('DNA & You', 'book')

    # add edges
    api.add_edge('Emily', 'Database Design', 'bought')
    api.add_edge('Spencer', 'Cosmos', 'bought')
    api.add_edge('Spencer', 'Database Design', 'bought')
    api.add_edge('Brenden', 'Database Design', 'bought')
    api.add_edge('Brenden', 'DNA & You', 'bought')
    api.add_edge('Trevor', 'Cosmos', 'bought')
    api.add_edge('Trevor', 'Database Design', 'bought')
    api.add_edge('Paxton', 'Database Design', 'bought')
    api.add_edge('Paxton', 'The Life of Cronkite', 'bought')
    api.add_edge('Emily', 'Spencer', 'knows')
    api.add_edge('Spencer', 'Emily', 'knows')
    api.add_edge('Spencer', 'Brenden', 'knows')

    # generate recommendation for Spencer
    print('Book Recommendations for Spencer:\n', api.get_recommendation('Spencer'))


if __name__ == '__main__':
    main()