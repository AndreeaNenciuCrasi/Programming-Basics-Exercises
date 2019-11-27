# Create a script file that welcomes the user given to it. If no name was given, then it welcomes the whole world.

name = input('Name:')
if name:
  print('Hello ' + name + '!')
else:
  name = 'world!'
  print('Hello ' + name)
