from collections import namedtuple
from functools import lru_cache
import timeit

items = []
def main():
    #inputs
    costs = [1,2,3,1,2,3,5,2,7,1]
    weights = [2,1,4,5,2,6,1,3,6,3]
    capacity = 10

    #Named Tuples for readability
    itemTuple = namedtuple('itemTuple',['cost','weight'])
    
    for cost,weight in zip(costs,weights):
        items.append(itemTuple(cost,weight))
    printTuple(items)
    print("Result: ",knapsack(capacity)," Time taken for 10000 iterations:˜",timeit.timeit('knapsack(10)', globals=globals(), number = 10000))

@lru_cache()
def knapsack(capacity,startFrom=0):
    if(startFrom==len(items)):
        return 0;

    costIfPicked,costIfLeft = 0,0
    #if item is picked
    if(capacity-items[startFrom].weight >= 0):
        costIfPicked = items[startFrom].cost + knapsack(capacity-items[startFrom].weight,startFrom+1)
    #if item is left
    costIfLeft = knapsack(capacity,startFrom+1)

    return max(costIfPicked,costIfLeft)

def printTuple(items):
    for i,item in enumerate(items):
        print("Items",i,": Cost",item.cost," Weight",item.weight)    

if __name__ == "__main__":
    main()