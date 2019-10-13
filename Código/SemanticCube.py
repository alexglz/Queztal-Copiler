class SemanticCube():
    def __init__(self):
        self.cube = dict()
        ###########INT 
        ##INT-INT
        self.cube["int"]={"int":{"+":"int"}}
        self.cube["int"]={"int":{"-":"int"}}
        self.cube["int"]={"int":{"*":"int"}}
        self.cube["int"]={"int":{"/":"int"}}
        self.cube["int"]={"int":{">":"bool"}}
        self.cube["int"]={"int":{"<":"bool"}}
        self.cube["int"]={"int":{"==":"bool"}}
        self.cube["int"]={"int":{"!=":"bool"}}
        self.cube["int"]={"int":{"&&":None}}
        self.cube["int"]={"int":{"||":None}}
        ##INT-FLOAT
        self.cube["int"]={"float":{"+":"float"}}
        self.cube["int"]={"float":{"-":"float"}}
        self.cube["int"]={"float":{"*":"float"}}
        self.cube["int"]={"float":{"/":"float"}}
        self.cube["int"]={"float":{">":"bool"}}
        self.cube["int"]={"float":{"<":"bool"}}
        self.cube["int"]={"float":{"==":"bool"}}
        self.cube["int"]={"float":{"!=":"bool"}}
        self.cube["int"]={"float":{"&&":None}}
        self.cube["int"]={"float":{"||":None}}
        ##INT-BOOL
        self.cube["int"]={"bool":{"+":None}}
        self.cube["int"]={"bool":{"-":None}}
        self.cube["int"]={"bool":{"*":None}}
        self.cube["int"]={"bool":{"/":None}}
        self.cube["int"]={"bool":{">":None}}
        self.cube["int"]={"bool":{"<":None}}
        self.cube["int"]={"bool":{"==":None}}
        self.cube["int"]={"bool":{"!=":None}}
        self.cube["int"]={"bool":{"&&":None}}
        self.cube["int"]={"bool":{"||":None}}
        ##INT-COLOR
        self.cube["int"]={"bool":{"+":None}}
        self.cube["int"]={"bool":{"-":None}}
        self.cube["int"]={"bool":{"*":None}}
        self.cube["int"]={"bool":{"/":None}}
        self.cube["int"]={"bool":{">":None}}
        self.cube["int"]={"bool":{"<":None}}
        self.cube["int"]={"bool":{"==":None}}
        self.cube["int"]={"bool":{"!=":None}}
        self.cube["int"]={"bool":{"&&":None}}
        self.cube["int"]={"bool":{"||":None}}

x = dict()
x.update(
{"int":
    {"int":
        {
            "+":"int",
            "-":"int",
            "*":"int",
            "/":"float",
            ">":"bool",
            "<":"bool",
            ">=":"bool",
            "<=":"bool",
            "==":"bool",
            "!=":"bool",
            "&&":None,
            "||":None
        },
    "float":
        {
            "+":"float",
            "-":"float",
            "*":"float",
            "/":"float",
            ">":"bool",
            "<":"bool",
            ">=":"bool",
            "<=":"bool",
            "==":"bool",
            "!=":"bool",
            "&&":None,
            "||":None            
        },
    "bool":
        {
            "+":None,
            "-":None,
            "*":None,
            "/":None,
            ">":None,
            "<":None,
            ">=":None,
            "<=":None,
            "==":None,
            "!=":None,
            "&&":None,
            "||":None            
        },
    "color":
        {
            "+":None,
            "-":None,
            "*":None,
            "/":None,
            ">":None,
            "<":None,
            ">=":None,
            "<=":None,
            "==":None,
            "!=":None,
            "&&":None,
            "||":None            
        }
    }
})
"float":
    {"int":
        {
            "+":"float",
            "-":"float",
            "*":"float",
            "/":"float",
            ">":"bool",
            "<":"bool",
            ">=":"bool",
            "<=":"bool",
            "==":"bool",
            "!=":"bool",
            "&&":None,
            "||":None            
        }
    },
    {"float":
        {
            "+":"float",
            "-":"float",
            "*":"float",
            "/":"float",
            ">":"bool",
            "<":"bool",
            ">=":"bool",
            "<=":"bool",
            "==":"bool",
            "!=":"bool",
            "&&":None,
            "||":None            
        }
    },
    {"bool":
        {
            "+":None,
            "-":None,
            "*":None,
            "/":None,
            ">":None,
            "<":None,
            ">=":None,
            "<=":None,
            "==":None,
            "!=":None,
            "&&":None,
            "||":None            
        }
    },
    {"color":
        {
            "+":None,
            "-":None,
            "*":None,
            "/":None,
            ">":None,
            "<":None,
            ">=":None,
            "<=":None,
            "==":None,
            "!=":None,
            "&&":None,
            "||":None            
        }
    }
},
"bool":
    {"int":
        {
            "+":None,
            "-":None,
            "*":None,
            "/":None,
            ">":None,
            "<":None,
            ">=":None,
            "<=":None,
            "==":None,
            "!=":None,
            "&&":None,
            "||":None            
        }
    },
    {"float":
        {
            "+":None,
            "-":None,
            "*":None,
            "/":None,
            ">":None,
            "<":None,
            ">=":None,
            "<=":None,
            "==":None,
            "!=":None,
            "&&":None,
            "||":None            
        }
    },
    {"bool":
        {
            "+":None,
            "-":None,
            "*":None,
            "/":None,
            ">":None,
            "<":None,
            ">=":None,
            "<=":None,
            "==":None,
            "!=":None,
            "&&":None,
            "||":None            
        }
    },
    {"color":
        {
            "+":None,
            "-":None,
            "*":None,
            "/":None,
            ">":None,
            "<":None,
            ">=":None,
            "<=":None,
            "==":None,
            "!=":None,
            "&&":None,
            "||":None       
        }
    }
},
"color":
    {"int":
        {
            "+":None,
            "-":None,
            "*":None,
            "/":None,
            ">":None,
            "<":None,
            ">=":None,
            "<=":None,
            "==":None,
            "!=":None,
            "&&":None,
            "||":None         
        }
    },
    {"float":
        {
            "+":None,
            "-":None,
            "*":None,
            "/":None,
            ">":None,
            "<":None,
            ">=":None,
            "<=":None,
            "==":None,
            "!=":None,
            "&&":None,
            "||":None          
        }
    },
    {"bool":
        {
            "+":None,
            "-":None,
            "*":None,
            "/":None,
            ">":None,
            "<":None,
            ">=":None,
            "<=":None,
            "==":None,
            "!=":None,
            "&&":None,
            "||":None           
        }
    },
    {"color":
        {
            "+":"color",
            "-":"color",
            "*":"color",
            "/":"color",
            ">":bool,
            "<":bool,
            ">=":bool,
            "<=":bool,
            "==":None,
            "!=":None,
            "&&":None,
            "||":None          
        }
    }
},
)


print(x)
