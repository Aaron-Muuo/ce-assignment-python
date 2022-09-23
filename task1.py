# Question - 1
# Compute average speed required required to drive on each route and identify the route that has the highest average speed.

from operator import itemgetter


def truck_average_speed(route_data):

    higest_speed_route = 0
    higest_speed = 0

    for route in route_data:

        speed = route['distance'] / route['time']

        if(speed > higest_speed):
            higest_speed = speed
            higest_speed_route = route['route']

    return higest_speed_route

# Test data
route_data = [
    {"route": 1, "distance": 560, "time": 10.3},
    {"route": 2, "distance": 440, "time": 8.2},
    {"route": 3, "distance": 490, "time": 9.1},
    {"route": 4, "distance": 530, "time": 10.1},
    {"route": 5, "distance": 370, "time": 7.5},
    ]

# Call the function and print the output
print("Highest speed route is: ",truck_average_speed(route_data))
