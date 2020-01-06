import shelve

print('                                    ')
print('____________________________________')
print('                                    ')
print('                                    ')

shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']

print(cats)

print('                                    ')
print('____________________________________')
print('                                    ')
print('                                    ')


shelfFile['cats'] = cats
shelfFile.close()

print('                                    ')
print('____________________________________')
print('                                    ')
print('                                    ')

shelfFile = shelve.open('mydata')
type(shelfFile)
<class 'shelve.DbfilenameShelf' >
shelfFile['cats']
['Zophie', 'Pooka', 'Simon']
shelfFile.close()

print('                                    ')
print('____________________________________')
print('                                    ')
print('                                    ')

shelfFile = shelve.open('mydata')
list(shelfFile.keys())
['cats']
list(shelfFile.values())
[['Zophie', 'Pooka', 'Simon']]
shelfFile.close()

print('                                    ')
print('____________________________________')
print('                                    ')
print('                                    ')
