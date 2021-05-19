# compose_flask/app.py
from flask import Flask
# import flask_sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
from flask import jsonify

config = {
    'host': 'db',
    'port': 3306,
    'user': 'root',
    'password': 'example',
    'database': 'classicmodels',
}

db_user = config.get('user')
db_pwd = config.get('password')
db_host = config.get('host')
db_port = config.get('port')
db_name = config.get('database')

app = Flask(__name__)

connection_str = f'mysql+pymysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}'
engine = create_engine(connection_str)
connection = engine.connect()
Session = sessionmaker(bind=engine)
Base = automap_base()
Base.prepare(engine, reflect=True)
Customer = Base.classes.customers
Employee = Base.classes.employees
Offices = Base.classes.offices
OrderDetail = Base.classes.orderdetails
Order = Base.classes.orders
Payment = Base.classes.payments
ProductLine = Base.classes.productlines
Product = Base.classes.products

@app.route('/')
def index():
    return ' - - - MYSQL Database `classicmodels` connection ok - - - '


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)