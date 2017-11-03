#Python 3 cheat sheet, Dated: 23rd Oct 2017

#LISTS
squares = [x*x for x in range(1,11)]
new_squares = squares[:] #that's how you copy or else it returns a pointer i.e. changes in new list will affect the original
#print(squares[from:to:step])
#squares.remove(36)#del squares[4]
#print(sorted(squares,reverse=True))
#squares.sort(reverse=True)
#print(squares)
#squares.reverse()
#print(squares)
#print(squares,file=open("output.txt","w"))# w to overwrite, a to append, r by default to read

#FILE INPUT
b = open("output.txt").read()
#print(b)

#FILE OUTPUT 
filename="new_out.txt"
with open(filename,'w') as file:
	file.write("This is how you write to files.")

#DICTIONARY
mydict = {'a':1,'b':2,'c':3} #mydict = dict(a=1,b=2,c=3) #same thing
mydict['d']=4 #adding new key value
#for var,val in mydict.items(): #to iterate through key and value both, mydict.keys(): for keys only & mydict.values() for values only
#	print(var,val,sep="->")
#if('a' in mydict.keys() and 1 in mydict.values()): #find by keys or by values
#	print('Found it')

#EXCEPTION HANDLING 
#try:
#	print(lol+1+asd)
#except Exception as e:
#	print("Something went wrong! it says:",e)