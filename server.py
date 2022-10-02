import os
import sys
sys.path.insert(0, '/Users/allon/pwa/scraping-online-stores/gym-shark/')
from scrape import gym_shark_scrape
from flask_mysqldb import MySQL
from flask import Flask
from flask_cors import CORS, cross_origin # prevent cors policy blocks
import logging # useful for logging info
from dotenv import load_dotenv

# take environment variables from .env.
load_dotenv() 

# config for logging server informations
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('HELLO WORLD')

# flask server instance
app = Flask(__name__)

# setup db configuruations
app.config.update({
    'MYSQL_HOST': os.getenv('MYSQL_HOST'),
    'MYSQL_USER': os.getenv('MYSQL_USER'),
    'MYSQL_PASSWORD': os.getenv('MYSQL_PASSWORD'),
    'MYSQL_DB': os.getenv('MYSQL_DB')
  })

# mysql db instance
mysql = MySQL(app)

# test function
@app.route('/get-gymshark', methods=['GET'])
def get_gym_shark():

  # create cursor connection
  cursor = mysql.connection.cursor()

  cursor.execute(''' INSERT INTO scrape_data.gym_shark VALUES (%s,%s)''', (5, 'Allonie'))
  mysql.connection.commit()
  cursor.close()
  response = gym_shark_scrape()
  return response

if __name__ == "__main__":
    app.secret_key = os.getenv('SECRET_KEY', os.urandom(24))
    app.run(debug = True, host = "0.0.0.0", port = 9000, use_reloader = True)

flask_cors.CORS(app, expose_headers='Authorization')
