#Edit distance
import timeit

def editDistance(str1,str2,memo):
    if (str1,str2) in memo.keys():
        return memo[(str1,str2)]
    
    if len(str1) == 0:
        return( len(str2) ) 
    if len(str2) == 0:
        return( len(str1) ) 

    if str1[0] == str2[0]:
        return editDistance(str1[1:],str2[1:],memo)
    else:
        modifyCost = 1 + editDistance(str1[1:],str2[1:],memo)
        insertCost =  1 + editDistance(str1,str2[1:],memo)
        deleteCost =  1 + editDistance(str1[1:],str2,memo)
        minCost = min( modifyCost , deleteCost, insertCost )
    
    memo[(str1,str2)] = minCost
    return(memo[(str1,str2)])

def main():
    str1 , str2 = "cart" , "march"
    str1,str2 = str1.lower(), str2.lower()
    print( editDistance(str1,str2,{}) )

if __name__ == '__main__':
    main()