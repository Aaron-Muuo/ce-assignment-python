# Question - 2
# A function that returns speeds at any given density value
# Greenshields model: u = 65.1(1 - 0.0075k)
# Greenberg model: u = 62.1 ln(157/k)

import math

def calculate_speed(density):

    Greenshields_model_speed = 65.1 * (1 - (0.0075 * density))
    Greenberg_model_speed = 62.1 * math.log(157 / density)

    return Greenshields_model_speed, Greenberg_model_speed

# Test data
densities = [43, 50, 8, 31]

# Call the function for each density value
for density in densities:

    print("Speed is: ",calculate_speed(density))
