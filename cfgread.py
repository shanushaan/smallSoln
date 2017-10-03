import ConfigParser
cfgParser = ConfigParser.ConfigParser()

parsed=cfgParser.read("cfg.cfg")

x=cfgParser.get("Users","get")

#y=cfgParser.items=("Users")

import ast
print (ast.literal_eval(x))


def su(x,y):
    return x+y

class A(object):
    def __init__(self):
        self.x=2
        self.y=3
        
    def s(self):
        return su(self.x,self.y)

class B(A):
    def __init__(self):
        self.x=5
        self.y=6
        
    def s(self):
        self.x+=2
        self.y+=3
        print self.x,self.y
        return super(B,self).s()
        
a =B()
print a.s()
