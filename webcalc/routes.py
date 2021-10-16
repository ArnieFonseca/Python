from webcalc import app
from flask import render_template

import webcalc.services  as services
import json

JSON_RESPONSE = str

#-----------------------------------=-----
@app.route('/calculate', methods=['POST'])
def doCalculation()->JSON_RESPONSE:
    """ 
      Web API for perform calculation
      Method: Http Post
      Data: {first: int, second: int, operation: str}

      Perform the operation using a Web API Call 
    """ 

    # Call service for calculation
    result:dict[str,int] = services.doCalculation()

    # Send JSON back to the client
    return json.dumps(result)


#----------------------------------------
@app.route('/operations', methods=['GET'])
def getOperations()->JSON_RESPONSE:
    """
     Web API for Get Operations
     Method: Http Get
    """

    # Call service to get all operation
    result:dict[str, list[dict[str,str]]] = services.getOperations() 

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
