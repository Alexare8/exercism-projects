"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: - arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(args)
    #Did they want something else here or is the point just to use *args?


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :parm each_wagons_id: list - the list of wagons.
    :parm missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    wagon_one, wagon_two, locomotive, *rest_wagons = each_wagons_id
    return [locomotive, *missing_wagons, *rest_wagons, wagon_one, wagon_two]
     

def add_missing_stops(route, **kwargs):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param kwargs: dict - arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    stops = list(kwargs.values())
    route["stops"] = stops
    return route
    # Again, not sure this is what they wanted,
    # but it took me way to long to arrive at anything that worked at all 


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    return {**route, **more_route_information}


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    # This is not what the exercise wants but I don't know how to do what it does want.
    correct_rows = [[],[],[]]
    for row in wagons_rows:
        for i, wagon in enumerate(row):
            correct_rows[i].append(wagon)
    return correct_rows
    
        

