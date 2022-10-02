from flaskext.mysql import MySQL
from flask import Flask
from flask_cors import CORS, cross_origin # prevent cors policy blocks
import logging # useful for logging info
import os

#config for logging server informations
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('HELLO WORLD')

# flask server instance
app = Flask(__name__)

# mysql db instance
mysql = MySQL()
mysql.init_app(app)

# test function
@app.route('/', methods=['GET'])
def hello_world():
  return 'Hello World!'

if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run(debug = True, host = "0.0.0.0", port = 9000, use_reloader = True)

flask_cors.CORS(app, expose_headers='Authorization')
