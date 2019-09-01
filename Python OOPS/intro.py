# Design patterns video tutorial (Derek Banas) https://www.youtube.com/watch?v=vNHpsC5ng_E&list=PLF206E906175C7E07

class animal:
    def __init__(self,name,height,weight,sound):
        # double __ is for private and 
        # single _ is for protected,
        # everything else is just public
        self.setName(name)
        self.setHeight(height)
        self.setWeight(weight)
        self.setSound(sound)

    # we use getters and setters for encapsulation
    # so that user shouldn't set invalid values
    # e.g. setting weight as a negative value
    def setName(self,name):
        self.__name = name

    def getName(self):
        return self.__name
    
    def setHeight(self,height):
        self.__height = height
        
    def getHeight(self):
        return self.__height

    def setWeight(self,weight):
        if weight > 0:
            self.__weight = weight
        else:
            print("Can't set weight less than 0")
    
    def getWeight(self):
        return self.__weight
    
    def setSound(self,sound):
        self.__sound = sound
        
    def getSound(self):
        return self.__sound
