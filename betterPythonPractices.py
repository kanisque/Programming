#Better Python practices 
#Shift space to run file in terminal (or set shortcut first)

names = ['bob','ross','mat','jack','karen','jess']
colors = ['red','green','blue','yellow','grey','white','black']

#iterating normally
for color in colors:
    print(color)
print("----------------")

#iterating in reverse
for color in reversed(colors):
    print(color)
print("----------------")

#enumerating 
for i,color in enumerate(colors):
    print(i,color)
print("----------------")

#looping over two collections
for name,color in zip(names,colors):
    print(name,color)
print('----------------')

#looping in sorted order
for color in sorted(colors):
    print(color)
print('----------------')

#looping in reverse order
for color in sorted(colors, reverse=True):
    print(color)
print('----------------')

#custom sort 
print(sorted(colors,key =len))

#for-else to distinguish multiople exit points in loops
def find(color):
    for i,value in enumerate(colors):
        if value == color:
            return ('Found at '+str(i))
    else:
        return('Not found')
#use keyword arguments in functions i.e find(color='_name_of_color')
print('Calling for Green:',find(color='green'))
print('Calling for Brown:',find(color='brown'))
print('----------------')

#creating dictionary from lists
d = dict(zip(names,colors))

#looping over dictionary keys
#if not mutating while looping
for k in d:
    print(k)
print('----------------')

#if mutating d while looping use d.keys(), makes a copy of keys
for k in d.keys():
    print(k)
print('----------------')

#looping over dictionary values
for k,v in d.items():
    print(k,v)
print('----------------')

#counting the occurance of same keys 
colors.append('red')
colors.append('green')
colors.append('red')
d2 = {}
for color in colors:
    if color not in d2:
        d2[color] = 0
    d2[color] += 1
print(d2)
print('----------------')

#alternative 
d2.clear()
for color in colors:
    d2[color] = d2.get(color,0) + 1 #get returns value for the key and returns second argument if key not found i.e. 0 here
colors.remove('red')
colors.remove('green')
colors.remove('red')
print(d2)
print('----------------')

#grouping with dictionaries
from collections import defaultdict
d3 = defaultdict(list)
for name in names:
    key = len(name)
    d3[key].append(name)
print(d3)
print('----------------')

#use named tuples
from collections import namedtuple
TestResults = namedtuple('TestResults',['failed','attempted'])
testcase1 = TestResults(0,4)
print(testcase1.failed,testcase1.attempted)
print(testcase1)
print('----------------')

#use unpacking for atomic transitions (x,y shoud update at once in code below)
def fibonacci(n):
    x,y = 0,1
    for i in range(n):
        print(x)
        x,y = y, x+y
fibonacci(n=10)

#use @cache to remove recalling of any function which returns same value for same call

