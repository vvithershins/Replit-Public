import inspect

def sepfunc():
  global var3
  var3 = "variable 3"
sepfunc()
var1 = "variable 1"

var2 = "variable 2"

def getVarNames(variable):
  
  
  src = inspect.findsource(getVarNames)
  detupled = src[0]
  for part in detupled:
   # print(part)
    if "=" in part and "==" not in part:
      vname = part.split("=")
      V = vname[0].strip()
      #print(V,"this is the part")
      idofV = id(eval(V))
      #print(idofV,"id of v")
      #print(id(variable),"id of variable")
      if idofV == id(variable):
        print(V)#this is the variable name
      
    
    

   
      
getVarNames(var1)
getVarNames(var2)
getVarNames(var3)
