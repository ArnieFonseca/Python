from logging import DEBUG
from flask import Flask, render_template, request
from waitress import serve
from static.modules.operation import performCalc
from typing import Final

import json

JSON_RESPONSE = str

app = Flask(__name__)

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


PORT_NUMBER:Final = 5555
PROD:Final  = 'PROD' 
TEST:Final  = 'TEST'

MODE:Final  = TEST
 
if __name__ == "__main__":
  print('******************************************')
  print('=========================================*')
  print()
  print(f'Running in {MODE} on port:{PORT_NUMBER}\n') 

  if MODE == PROD:    
    serve(app, host='0.0.0.0', port=PORT_NUMBER)
  else:
    app.run(debug=True, port=PORT_NUMBER)
