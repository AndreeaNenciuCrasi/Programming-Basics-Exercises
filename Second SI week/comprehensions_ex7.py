# Create a string which contains the first ten positive integers separated by commas and spaces. Remember that you can’t
# join numbers – you have to convert them to strings first. Print the output string.
# Rewrite the calendar program from exercise 3 using nested comprehensions instead of nested loops. Try to append a string
# to one of the week lists, to make sure that you haven’t reused the same list instead of creating a separate list for
# each week.
# Now do something similar to create a calendar which is a list with 52 empty sublists (one for each week in the whole year).
# Hint: how would you modify the nested for loops?

number_string = ', '.join(str(n) for n in range(1, 11))
print(number_string)

(January, February, March, April, May, June, July, August,
 September, October, November, December) = range(12)
(week_1, week_2, week_3, week_4) = range(4)

# calendar = []
# for m in range(12):
#     month = []
#     for w in range(4):
#         month.append([])
#     calendar.append(month)
calendar = [[[] for w in range(4)] for m in range(12)]
calendar[July][week_2].append('Holiday!')
print(calendar)
calendar1 = [[] for w in range(4) for m in range(12)]
print(calendar1)
