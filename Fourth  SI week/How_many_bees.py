# How many bees are in the beehive?
# bees can be facing UP, DOWN, LEFT, or RIGHT
# bees can share parts of other bees
# Examples
# Ex1

# bee.bee
# .e..e..
# .b..eeb
# Answer: 5

# Ex2 ``` bee.bee e.e.e.e eeb.eeb ``` *Answer: 8*
# Notes
# The hive may be empty or null/None/nil/...
# Python: the hive is passed as a list of lists (not a list of strings)

hive = ["bee.bee",
        ".e..e..",
        ".b..eeb"]

hive2 = ["bee.bee",
         "e.e.e.e",
         "eeb.eeb"]


def how_many_bees(hive):
    bee_row_string = ''
    bee_column_string = ''
    for i in hive:
        bee_row_string += i
    nr_of_bee = bee_row_string.count('bee') + bee_row_string.count('eeb')
    list_0 = list(hive[0])
    list_1 = list(hive[1])
    list_2 = list(hive[2])

    for j in range(7):
        bee_column_string += list_0[j] + list_1[j] + list_2[j]
    nr_of_bee += bee_column_string.count('bee') + \
        bee_column_string.count('eeb')
    return nr_of_bee


print(how_many_bees(hive))
print(how_many_bees(hive2))
