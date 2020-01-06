# https://docs.python.org/3/library/os.path.html paths documentation

import os
os.getcwd()  #prints cwd
print('                                    ')
print('____________________________________')
print('                                    ')
print('                                    ')

print('origin directory   '+ os.getcwd() )

os.chdir('../')  # changes directory

print('After Changing    '+ os.getcwd() )

print('                                    ')
print('____________________________________')
print('                                    ')
print('                                    ')

print(os.path.join('these', 'paths', 'are', 'returned'))

# os.makedirs('C:\\delicious\\walnut\\waffles') # This will create not just the C:\delicious folder but also a walnut folder inside C:\delicious and a waffles folder inside C:\delicious\walnut. That is, os.makedirs() will create any necessary intermediate folders in order to ensure that the full path exists.
print('                                    ')
print('____________________________________')
print('                                    ')
print('                                    ')

calcFilePath = 'C:\\Windows\\System32\\calc.exe'


print("this is the name and base name together of calc.exe   ")
print( os.path.split(calcFilePath))  #

# ('C:\\Windows\\System32', 'calc.exe')
print('                                    ')
print('____________________________________')
print('                                    ')
print('                                    ')


# fekFile = open('C:\\Users\\tor00\\fuk.txt', 'r')  # read mode   - Opens file for reading.
# fekFile = open('C:\\Users\\tor00\\fuk.txt', 'w')  # write mode  - Overwrites current file contents   -- If the file does not exist will create new blank file   
# fekFile = open('C:\\Users\\tor00\\fuk.txt', 'a')  # append mode - Appends to current file contents   -- If the file does not exist will create new blank file 


# stupid = fekFile.read()
#print(stupid)
print('origin directory   ' + os.getcwd())


baconFile = open('bacon.txt', 'w')
baconFile.write('Hello world!\n')

baconFile.close()
baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable.')

baconFile.close()
baconFile = open('bacon.txt')
content = baconFile.read()
baconFile.close()
print(content)



print('                                    ')
print('____________________________________')
print('                                    ')
print('                                    ')


