from webcalc import app 
from typing import Final

PORT_NUMBER:Final = 5555
HOST:Final = 'localhost'


if __name__ == "__main__":
  print('******************************************')
  print('=========================================*')
  print()
  print(f'Running in {HOST} on port:{PORT_NUMBER}\n') 

  app.run(debug=True, host=HOST, port=PORT_NUMBER)

