import random

# Constant settings
RADIUS = 1
TOTAL_POINTS = 1000000
AREA_FACTOR = 4
SQUARE_EXPONENT = 2
POINT_COUNT_INCREMENT = 1

points_inside_circle = 0

# Randomly generate points and count those inside the circle
for point in range(TOTAL_POINTS):
    x = random.uniform(-RADIUS, RADIUS)
    y = random.uniform(-RADIUS, RADIUS)
    if x**SQUARE_EXPONENT + y**SQUARE_EXPONENT <= RADIUS**SQUARE_EXPONENT:
        points_inside_circle += POINT_COUNT_INCREMENT

# Estimate pi based on the number of points inside the circle
pi = (points_inside_circle / TOTAL_POINTS) * AREA_FACTOR

print(f"Estimated value of pi is: {pi}")
