"""
filename: mongo_tools.py
Homework 3: MongoTutorial
Avril Mauro & Katelyn Donn

This file contains a set of functions to make
it easier to build mongo queries
"""


def query_type(input_type):
    """ User input for query type """
    if input_type == 1:
        return 'find'
    if input_type == 2:
        return 'distinct'
    if input_type == 3:
        return 'aggregate'


def build_filters():
    """
        From user input, structure query dictionary for criteria
        Allows for and/or differentiation in query
    """
    filters = (input('What are your filters? (Format: field=value, field=value, ...)\n')).split(", ")

    query = {}

    if len(filters) > 1:
        logic = input('Should all or any of the above filters apply? (Reply all or any)\n')
        filter_query = [{f.split('=')[0]: f.split('=')[1]} for f in filters]

        if logic == 'all':
            query['$and'] = filter_query
        if logic == 'any':
            query['$or'] = filter_query

    else:
        query[filters[0].split('=')[0]] = filters[0].split('=')[1]

    return query


def select_fields(q_type):
    """
        Include/Exclude specific fields from query return
        Default query returns all fields (none excluded)
    """
    if q_type == 'distinct':
        distinct_select = input('What field do you want to return?\n')
        return distinct_select
    else:
        select = input('What field(s) do you want to return? (start entry with "exclude" or include is default)\n')
        if select == "":
            return None
        elif 'exclude' in select:
            return dict.fromkeys([field for field in select[8:].split(", ")], 0)
        else:
            return dict.fromkeys([field for field in select.split(", ")], 1)


def define_sort(q_type):
    """ Sort data ascending/descending based on user-inputted field """
    if q_type != 'find':
        return None

    else:
        sort_by = input('How do you want to sort the data? (Format: field ascending or descending)\n')

        if sort_by == "":
            return None

        else:
            field, direction = sort_by.split(" ")[0], sort_by.split(" ")[1]
            if direction == 'ascending':
                return field, 1
            if direction == 'descending':
                return field, -1


def build_match():
    """ Structure match dictionary for aggregate operation """
    query = {'$match': build_filters()}
    return query


def define_group():
    """ Structure group dictionary for aggregate operation """
    group_field = input('What field are you grouping by?\n')
    agg_method = input('How will the data be aggregated? (count, sum, or avg)\n')

    if agg_method == 'count':
        agg_field = {}
        agg_label = f'count'
    else:
        agg_field = input('What field are you aggregating?\n')
        agg_label = f'{agg_method}_{agg_field}'
        agg_field = f'${agg_field}'

    query = {'$group': {'_id': f'${group_field}', agg_label: {f'${agg_method}': agg_field}}}
    return query


def define_limit():
    """ Caps number of query returns """
    limit = int(input('How many results do you want to see?\n'))
    return limit
