class SemanticCube():
    def __init__(self):
        self.cube = dict()
        ###########INT 
        self.cube.update(
        {"int":
            {"int": ##INT-INT
                {   "+":"int",
                    "-":"int",
                    "*":"int",
                    "/":"int",
                    ">":"bool",
                    "<":"bool",
                    ">=":"bool",
                    "<=":"bool",
                    "==":"bool",
                    "!=":"bool",
                    "&&":None,
                    "||":None,
                    "=":"int" 
                },
            "float": ##INT-FLOAT
                {  "+":"float",
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
                    "||":None,
                    "=":None            
                },
            "bool": ##INT-BOOL
                {   "+":None,
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
                    "||":None,
                    "=":None        
                },
            "color": ##INT-COLOR
                {   "+":None,
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
                    "||":None,
                    "=":None              
                },
            "tag": ##INT-TAG
                {   "+":None,
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
                    "||":None,
                    "=":None              
                }
            }
        })
        ###############FLOAT
        self.cube.update({
            "float":##FLOAT-INT
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
                        "||":None,  
                        "=":"float"            
                    }
                ,
                "float":###FLOAT-FLOAT
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
                        "||":None ,
                        "=":"float"           
                    },
                "bool":###FLOAT-BOOL
                    {   "+":None,
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
                        "||":None,
                        "=":None              
                    },
                "color":###FLOAT-COLOR
                    {   "+":None,
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
                        "||":None,
                        "=":None             
                    },
            "tag": ##
                {   "+":None,
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
                    "||":None,
                    "=":None              
                }          
            }
        })
        #######BOOL
        self.cube.update(
            {"bool":
                {"int":
                    {   "+":None,
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
                        "||":None,
                        "=":None              
                    },
                "float":
                    {   "+":None,
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
                        "||":None,
                        "=":None             
                    },
                "bool":
                    {   "+":None,
                        "-":None,
                        "*":None,
                        "/":None,
                        ">":None,
                        "<":None,
                        ">=":None,
                        "<=":None,
                        "==":"bool",
                        "!=":"bool",
                        "&&":"bool",
                        "||":"bool",
                        "=":"bool"              
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
                        "||":None,
                        "=":None                         
                    },
            "tag": 
                {   "+":None,
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
                    "||":None,
                    "=":None              
                }
                
            }
        })
        ############COLOR
        self.cube.update(
            {"color":
                {"int":###
                    {   "+":None,
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
                        "||":None,
                        "=":None           
                    },
                "float":
                    {   "+":None,
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
                        "||":None,
                        "=":None          
                    },
                "bool":
                    {   "+":None,
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
                        "||":None,
                        "=":None             
                    },
                "color":
                    {   "+":"color",
                        "-":"color",
                        "*":"color",
                        "/":"color",
                        ">":bool,
                        "<":bool,
                        ">=":bool,
                        "<=":bool,
                        "==":bool,
                        "!=":None,
                        "&&":None,
                        "||":None,
                        "=":"color"            
                    },
            "tag": 
                {   "+":None,
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
                    "||":None,
                    "=":None              
                }
                }
            })


