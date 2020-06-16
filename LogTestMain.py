from const import *
from custLogger import log
from tempExceptionThrowing import hitIt
import time


class abvd:
    def addPerson(self):
        # add person logic here

        #log changes
        log("New person added, without filename")
        log("New person added, with filename",filename)
    
    
abcdEnt = abvd()
abcdEnt.addPerson()

try:
    hitIt()
except RuntimeError as ex:
    print("Error in main",ex)
except Exception as e:
    print(e)
