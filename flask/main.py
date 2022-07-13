import os, pika, json

from producer import product_create
from flask import Flask, request
# from flask_sqlalchemy import SQLAlchemy 
from flask_cors import CORS

# from urllib.parse import quote_plus


# rabbitmq
params = pika.URLParameters('amqp://user:pass@rabbitmq')

# postgres
# postgres_password = quote_plus(os.environ.get('POSTGRES_PASSWORD'))
# postgres_user = os.environ.get('POSTGRES_USER')

# flask
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://db/db?user={postgres_user}&password={postgres_password}'
CORS(app)

@app.route('/', methods=['POST'])
def index():
    data = request.data
    product_create(params, data)
    print(data)
    return f'Message {data} have been received'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)





