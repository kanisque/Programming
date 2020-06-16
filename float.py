x = float("inf") 
print(x)
print(x,"inf", x == "inf")
print(type(x),type("inf"))
print(x-1 == x == x+1)
print( x-1 < x < x+1)
print( 1-1 < 1 < 1+1)
print( 4 ^ 1)

x = {i:j for i,j in zip([1,2,3,1],['a','b','c','d'])}
print(x)
    