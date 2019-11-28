# Create a tuple of month names and a tuple of the number of days in each month (assume that February has 28 days).
# Using a single for loop, construct a dictionary which has the month names as keys and the corresponding day numbers
# as values.
# Now do the same thing without using a for loop.

months = ('January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December')
days = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
month_dic = {}
for month, day in zip(months, days):
    month_dic[month] = day
print(month_dic)
year = {months[0]: days[0],
        months[1]: days[1],
        months[2]: days[2],
        months[3]: days[3],
        months[4]: days[4],
        months[5]: days[5],
        months[6]: days[6],
        months[7]: days[7],
        months[8]: days[8],
        months[9]: days[9],
        months[10]: days[10],
        months[11]: days[11]}
print(year)
