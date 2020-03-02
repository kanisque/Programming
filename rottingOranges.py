#Rotting oranges

from queue import Queue

class Solution:
    global rottenQueue
    rottenQueue = Queue()
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minute = 0
        allCount = 0
        rottenCount = 0
        for y,row in enumerate(grid):
            for x,val in enumerate(row):
                if val == 2:
                    rottenQueue.put([x,y,minute])
                    grid[y][x] = -1
        while not rottenQueue.empty():
            minute = self.processRotten(rottenQueue.get(),grid,rottenQueue)
        
        return minute if self.checkGrid(grid) else -1
    
    def processRotten(self,pos,grid,rottenQueue):
        x,y,minute = pos
        print(x,y,minute,len(grid),len(grid[0]))
        
        if (x-1 > -1) and (grid[y][x-1] == 1):
            rottenQueue.put([x-1,y,minute+1])
            grid[y][x-1] = -1
            
        if (y-1 > -1) and (grid[y-1][x] == 1):
            rottenQueue.put([x,y-1,minute+1])
            grid[y-1][x] = -1
            
        if ( x+1 < len(grid[0]) ) and (grid[y][x+1] == 1):
            rottenQueue.put([x+1,y,minute+1])
            grid[y][x+1] = -1
            
        if ( y+1 < len(grid) ) and (grid[y+1][x] == 1):
            rottenQueue.put([x,y+1,minute+1])
            grid[y+1][x] = -1
            
        return(minute)
    
    def checkGrid(self,grid):
        for row in grid:
            for val in row:
                if val == 1:
                    return False
        return True