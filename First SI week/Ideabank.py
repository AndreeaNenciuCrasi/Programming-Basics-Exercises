# Write an application that can save the given text into a local file. After saving the idea, it 
# should show the existing ideas as well. The app should append the new idea into the file, to 
# allow multiple ideas to be saved.

# In these extensions, you will need to use command line arguments.
# 1. Add the option to list all the existing ideas with command line argument without adding a new # one.
# 2. Add an option to remove an idea by the id of it. Use console arguments.

import sys
print('Number of arguments: {}'.format(len(sys.argv)))
print('Argument(s) passed: {}'.format(str(sys.argv)))

option = ["-c", "-l", "-a", "-d"]
error = "Argument not recognized."
idea = sys.argv[2:]

def create():
    file = open("text.txt", "w")
    for l in idea:
        file.write(l)
        file.write("\n")
    file.close()


def list():
    final_list = []
    file = open("text.txt", "r")
    i = 1
    print("\n Your ideabank: \n")
    for line in file:
        print(str(i) + ". " + line)
        final_list.append(line)
        i += 1
    file.close()
    return final_list


def add():
    x = sys.argv[2]
    idea.append(x)
    file = open("text.txt", "a")
    file.write(x)
    file.write("\n")
    file.close()


def delete():
    temp = int(sys.argv[2])
    list_idea = list()
    list_to_write = []
    l = 0
    while l < len(list_idea):
        if l != temp - 1:
            list_to_write.append(list_idea[l])
        l += 1
    file = open("text.txt", "w")
    for i in list_to_write:
        file.write(i)
    file.close()

sys_argv = {option[0]: create,
            option[1]: list,
            option[2]: add, 
            option[3]: delete}

try:
    sys_argv[sys.argv[1]]()
except:
    print('%s ' % (error))
    print('You entered:' + sys.argv[1])
    print('The available arguments are: %s' % (option))
    print("""
            -c = creat file
            -l = list file
            -a = add in file
            -d = delete from file
            """)
