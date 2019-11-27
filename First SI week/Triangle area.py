# Write a program which takes 6 integers a, b, c, d, e, f - the coordinates of the vertices of the # triangle (a, b), (c, d) and (e, f), and prints the value of its area. The coordinates of the 
# vertices of the triangle are numbers in the range from -100 to 100. For example, for numbers 0 0 # 0 3 5 0 Your program should print 7.5, but for numbers 0 0 2 2 4 0 Your program should print 4.

import random
def triangle_area(tri):
    y_list = [tri[0][1], tri[1][1], tri[2][1]]
    x_list = [tri[0][0], tri[1][0], tri[2][0]]
    height = max(y_list) - min(y_list)
    width = max(x_list) - min(x_list)
    return height * width / 2

my_tri = [[random.randint(-100, 100), random.randint(-100, 100)], [random.randint(-100, 100), random.randint(-100, 100)],
 [random.randint(-100, 100), random.randint(-100, 100)]]
print(triangle_area(my_tri))
