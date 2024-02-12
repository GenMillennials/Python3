# Calculate the shortest distance on Earth with latitude an longitude

import math

t1 = math.radians(int(input("Input a latitude the first point in degree ")))
g1 = math.radians(int(input("Input a longitude the first point in degree ")))
t2 = math.radians(int(input("Input a latitude the second point in degree ")))
g2 = math.radians(int(input("Input a longitude the second point in degree ")))
distance = round(6371.01 * math.acos((math.sin(t1) * math.sin(t2) + math.cos(t1) * math.cos(t2) * math.cos(g1 - g2))), 2)
print("The shortest distance between two points on the Earth is", distance, "km")