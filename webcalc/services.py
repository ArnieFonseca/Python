from flask import request
from webcalc.models import Operation


def getOperations()->dict:
    """
    Get the operation from the database
    """

    # Load Key/Value pairs for the operations   
    operations:list[dict[str,str]] = []
    rows = Operation.query.all()
    for row in rows:
       operations.append({row.oper: row.description})

    # Prepare the return structure
    result:dict[str, list[dict[str,str]]] = {"result":operations}

    return result

def doCalculation()->dict:
    """
    Retrieve data from the AJAX call and return the calculation based on the operation parameter
    """
    
    # Get JSON data from client
    first:int = int(request.json['first'])
    second:int = int(request.json['second'])
    oper:str = request.json['operation']

    rst:int  =  performCalc(first, second, oper)

    # Prepare the return structure
    result:dict[str,int] = {"result":rst}

    return result

def performCalc(x:int, y:int, oper:str)->int:
    """ 
      Calculation are done using helper inner functions  
    """ 
    def add(x:int, y:int)->int:
        return x + y

    def sub(x:int, y:int)->int:
        return x - y

    def mul(x:int, y:int)->int:
        return x * y

    def min(x:int, y:int)->int:
        return x if (x <= y) else y 

    def max(x:int, y:int)->int:
        return x if (x >= y) else y
        
    def div(x:int, y:int)->int:
        return x // y
        
    def mod(x:int, y:int)->int:
        return x % y
    
    def gcd(x:int, y:int)->int:
        return x if y == 0 else gcd(y, x%y)
 
    rst =  eval(oper)(x,y) # Dynamically execute

    # Send back the answer
    return rst