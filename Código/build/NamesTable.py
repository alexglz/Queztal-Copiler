from MemoryManager import *

class NamesTable():
    def __init__(self):
        self.functionsT = dict()
        self.globalsT = dict()
        self.actualT = None
        ##Auxiliares de funciones
        self.parameterC = 0
        self.actualFuncName = ""
        self.varCnt = 0
        self.constantsT = dict()
        ##Auxiliares de variables
        self.dimensions = []
        self.actualR = 1
        self.varSize = 1
    
    def addFunction(self,newFunct,type,position): #function to register a newFunction
        if newFunct in self.functionsT or newFunct in self.globalsT: #checks if name of function already exists in functinosT or in globalsT
            raise Exception("Function '" + newFunct + "' already exists") #display exception
        else:
            self.functionsT[newFunct] = {}
            self.functionsT[newFunct]["type"] = type #add function to functionsT
            self.functionsT[newFunct]["position"] = position
            self.functionsT[newFunct]["parameters"] = []
            self.actualFuncName = newFunct
            if(type != "void"): ##AGREGAR LA VARIABLE GLOBAL DE LA FUNCION CUANDO TIENE RETURN
                memLocation = Memory.assignMemory("Global",type,1)
                self.dimentionDef()
                self.globalsT[newFunct] = {"type":type,"dir":memLocation,"dim":self.dimensions}
                self.functionsT[newFunct]["varPosition"] = memLocation
                return True
            
            return True
    def addDimension(self,dimSize):
        dimSize = int(dimSize)
        self.varSize = dimSize * self.varSize
        self.dimensions.append({"ls":dimSize-1,"m":1})
        self.actualR = self.actualR * dimSize
    
    def dimentionDef(self):
        suma = 0
        for i in range(0,len(self.dimensions)):
            self.dimensions[i]["m"] = self.actualR/(self.dimensions[i]["ls"]+1)
            self.actualR= self.dimensions[i]["m"]
        
        

    def addLocalVar(self,newVar,type): #function to register a new Local Variable
        if self.actualT == None: self.actualT = dict() 
        if (newVar in self.actualT) or (newVar in self.globalsT) or (newVar in self.functionsT): #checks if name of is not already defined in local, global context or as a name of a function
            raise Exception("Variable '" + newVar + "' already defined") #display exception
        else:
            virtualAdd = Memory.assignMemory("Local",type,self.varSize)
            self.dimentionDef()
            
            
            self.actualT[newVar] = type #add variable to actual local variables table (actualT)
            self.actualT[newVar] = {"type":type,"dir":virtualAdd,"dim":self.dimensions}

            #Reiniciar auxiliares
            self.dimensions = []
            self.actualR = 1
            self.varSize = 1

            return virtualAdd

    def addGlobalVar(self,newVar,type):
#function to register a ne
        if (newVar in self.globalsT or newVar in self.functionsT):
            raise Exception("Variable '" + newVar + "' already defined")
        else:
            memLocation = Memory.assignMemory("Global",type,self.varSize)
            self.dimentionDef()
            self.globalsT[newVar] = {"type":type,"dir":memLocation,"dim":self.dimensions}
            #Reiniciar auxiliares
            self.dimensions = []
            self.actualR = 1
            self.varSize = 1
            return True

    #Identifica el contexto actual de la creación de variables, posteriormente guarda la variable como local
    #o global según sea el caso
    def addVar(self,newVar,type):
        if self.actualT == None:
            self.addGlobalVar(newVar,type)
        else:
            self.varCnt +=1
            return self.addLocalVar(newVar,type)
            
    
    def addParameter(self,newVar,type):
        address = self.addVar(newVar,type)
        self.parameterC += 1
        self.functionsT[self.actualFuncName]["parameters"].append((newVar,type,address))

    def exitParams(self):
        self.functionsT[self.actualFuncName]["parNum"] = self.parameterC
        

    #Inicializa la tabla de variables locales
    def initLocalT(self):
        self.actualT = dict()
        self.parameterC = 0

