from webcalc import app
from flask import request, render_template
from webcalc.modules.operation import performCalc
import json

JSON_RESPONSE = str

#-----------------------------------------
# Web API for Get Operations
# Method: Http Post
# Data: {first:#, second:#, operation:str}
#-----------------------------------=-----
@app.route('/calculate', methods=['POST'])
def doCalculation()->JSON_RESPONSE:
    """ 
      Perform the operation using a Web API Call 
    """ 

    # Get JSON data from client
    first:int = int(request.json['first'])
    second:int = int(request.json['second'])
    oper:str = request.json['operation']

    rst:int  =  performCalc(first, second, oper)

    # Prepare the return structure
    result:dict[str,int] = {"result":rst}

    # Send JSON back to the client
    return json.dumps(result)

#----------------------------------------
# Web API for Get Operations
# Method: Http Get
#----------------------------------------
@app.route('/operations', methods=['GET'])
def getOperations()->JSON_RESPONSE:

    # Load Key/Value pairs for the operations   
    operations:list[dict[str,str]] = [{"add" : "Addition"},  
                  {"sub" : "Subtraction"}, 
                  {"mul" : "Multiplication"},  
                  {"div" : "Division"},  
                  {"mod" : "Remaider"},
                  {"gcd" : "GCD"}] 
    
    # Prepare the return structure
    result:dict[str, list[dict[str,str]]] = {"result":operations}

    # Send JSON back to the client
    return  json.dumps(result)

#--------------
# Default Route
#--------------
@app.route('/')
def index():
    """
      Home route for the site
    """

    # Display default page
    return render_template('index.html')
