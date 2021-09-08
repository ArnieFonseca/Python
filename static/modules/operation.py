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

    def div(x:int, y:int)->int:
        return int(x / y)

    def mod(x:int, y:int)->int:
        return x % y
    
    def gcd(x:int, y:int)->int:
        return x if y == 0 else gcd(y, x%y)
 
    rst =  eval(oper)(x,y) # Dynamically execute

    # Send back the answer
    return rst