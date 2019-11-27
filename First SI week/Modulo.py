# Write a program which prints the top 25 three-digit natural numbers divisible by 7 or by 9. Each # number should be displayed in a separate line.

list = []
i = 0
for x in range(100, 300):
    if (x % 7 == 0) and i < 25:
        i += 1
        list.append(str(x))
        print(x)          
