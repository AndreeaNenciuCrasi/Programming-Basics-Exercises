numbers = [-5, 23, 0, -9, 12, 99, 105, -43]
max = numbers[0]
i = 1
while i < len(numbers):
    if numbers[i] > max:
        max = numbers[i]
    i += 1
print(max)

min = numbers[0]
j = 1
while j < len(numbers):
    if numbers[j] < min:
        min = numbers[j]
    j += 1
print(min)

average = 0
sum = numbers[0]
k = 1
while k < len(numbers):
    sum = sum + numbers[k]
    k += 1
average = sum / len(numbers)
print(average)
