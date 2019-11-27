# Your boss is obsessed with mathematics and he likes challenging you with math exercises. This 
# week, he walks around the office and asks for specific Fibonacci numbers from everyone in your 
# department. To trick him, you decided to write a magical program (python script) that calculates # some of them and share it with your colleagues, so everyone can answer immediately. Hopefully, 
# he stops his weird bullying after he sees that all the people in his office know these numbers :)

total = int(input('Number: '))
i = 0
nr1 = 0
nr2 = 1
nr3 = 0
list1 = []


while i < total:
    list1.append(nr3)
    nr1 = nr2
    nr2 = nr3
    nr3 = nr1 + nr2
    i += 1

j = 1   

while j < total:
    for l1 in list1:
        print(str(j) + ':' + "{: >30}".format(l1))
        j +=1
