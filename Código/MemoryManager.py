class Memory:
    Reference= dict()
    Directions = dict()
    MemSize = 10000000
    counter = 1
    scopes = ["Global","Local","Temp","Constant"]
    types = ["int","float","bool","color","tag"]
    for scope in scopes:
        Directions[scope] = dict()
        for type in types:
            Directions[scope][type] = {"dir":MemSize*counter,"declared":0}
            counter+=1

    @staticmethod
    def assignMemory(scope,type,size):
        direccion = Memory.Directions[scope][type]["dir"] + Memory.Directions[scope][type]["declared"]
        Memory.Directions[scope][type]["declared"] += size
        ##NOT SURE IF THIS GOES HERE
        #if(Memory.Directions[scope][type]["declared"] >= Memory.MemSize):
        #   raise Exception("Stack Overflow")        
        return direccion
    
    @staticmethod
    def resetMemory(scope): #used to clean temps and local variables
        for k in Memory.Directions[scope].keys():
            Memory.Directions[scope][k]["declared"] = 0
