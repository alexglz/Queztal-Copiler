class NamesTable():
    def __init__(self):
        self.functionsT = dict()
        self.globalsT = dict()
        self.actualT = None
    
    def addFunction(self,newFunct,type): #function to register a newFunction
        if newFunct in self.functionsT or newFunct in self.globalsT: #checks if name of function already exists in functinosT or in globalsT
            raise Exception("Function '" + newFunct + "' already exists") #display exception
        else:
            self.functionsT[newFunct] = type #add function to functionsT
            return True
        

    def addLocalVar(self,newVar,type): #function to register a new Local Variable
        if self.actualT == None: self.actualT = dict() 
        if (newVar in self.actualT) or (newVar in self.globalsT) or (newVar in self.functionsT): #checks if name of is not already defined in local, global context or as a name of a function
            raise Exception("Variable '" + newVar + "' already defined") #display exception
        else:
            self.actualT[newVar] = type #add function to local actualT
            return True

    def addGlobalVar(self,newVar,type): #function to register a neW Global Variable
        if (newVar in self.globalsT or newVar in self.functionsT): #checks if name of is not already defined in global context or as a name of a function
            raise Exception("Variable '" + newVar + "' already defined") #display exception
        else:
            self.globalsT[newVar] = type #add function to global globalsT
            return True

    #Inicializa la tabla de variables locales
    def clearLocalT(self):
        self.actualT = dict()

