"""
filename: hw3_api.py

This file define the class UserAPI which will be used to
create nodes and edges in a database and generate recommendations

Homework 4: Graph Models
Avril Mauro & Katelyn Donn
"""

from dbutils import DBUtils


class UserAPI:

    def __init__(self, port, host="localhost"):
        self.dbu = DBUtils(port, host)
        self.edge_id = 10000000
        self.edges = list()

    def add_node(self, name, type):
        """ Add a node to the database of a given name and type """
        self.dbu.set(name, type)

    def add_edge(self, name1, name2, type):
        """ Add an edge between nodes named name1 and name2 """
        self.dbu.hset(self.edge_id, 'node1', name1)
        self.dbu.hset(self.edge_id, 'node2', name2)
        self.dbu.hset(self.edge_id, 'type', type)
        self.edges.append(self.edge_id)
        self.edge_id += 1

    def get_adjacent(self, name, node_type=None, edge_type=None):
        """ Get the names of all adjacent nodes.
        User may optionally specify that the adjacent nodes are
        of a given type and/or only consider edges of a given type."""
        adjacent = []
        for id in self.edges:

            if self.dbu.hget(id, 'node1') == str(name):
                adj_node = self.dbu.hget(id, 'node2')

                if ((edge_type is None) and (node_type is None)) or \
                        ((edge_type is not None) and (self.dbu.hget(id, 'type') == edge_type)) or \
                        ((node_type is not None) and (self.dbu.get(adj_node) == node_type)):
                    adjacent.append(adj_node)

        return adjacent

    def get_recommendation(self, name):
        """ Get all books purchased by people that a given person knows
            but exclude books already purchased by that person """
        knows = self.get_adjacent(name, edge_type='knows')
        bought = set(self.get_adjacent(name, edge_type='bought'))

        books = set()
        for person in knows:
            books = books.union(set(self.get_adjacent(person, edge_type='bought')))

        return books.difference(bought)

    def clear(self):
        self.dbu.flushall()

    def close(self):
        self.dbu.close()
