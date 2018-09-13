from .entities.entity import Session, engine, Base
from .entities.orders import Orders, OrdersSchema
from flask_cors import CORS
from flask import Flask, jsonify, request, flash, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
import simplejson as json
from sqlalchemy.sql import select
from datetime import date
from sqlalchemy import Date, text
import datetime as dt
import sqlalchemy as sa
import os
import psycopg2
import csv
from configparser import ConfigParser

Base.metadata.create_all(engine)

CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'database.ini')
UPLOAD_FOLDER = './path/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app)

def config(filename=CONFIG_PATH, section='postgresql'):

    parser = ConfigParser()
    parser.read(filename)

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
 
    return db

@app.route('/')
def index():
    session = Session()
    order_objects = session.query(Orders).from_statement(
        text("SELECT * FROM ord7 where simbol=:name")
    ).params(name="ALR").all()
    schema = OrdersSchema(many=True)
    orders = schema.dump(order_objects)

    session.close()

    return jsonify(orders.data)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def read():
    with open('./path/ord.txt','r') as f:
        reader = csv.reader(f, delimiter='\t')
        next(reader, None)
        ordine_noi = []
        ordine_modif = []
        included = [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 20, 34, 35, 36, 43, 46, 49]
        content = []
        for row in reader:
            if row[34] == '1':
                content = list(row[i] for i in included)
                ordine_noi.append(tuple(content))
            elif row[34] == '2':
                content = list(row[i] for i in included)
                ordine_modif.append(tuple(content))
    sql = """INSERT INTO ord8(status, order_no, simbol, simbol_type, market, ef_time, side, price, volum, order_term, ticket, update_type, update_time, trader, internal_account, cant_exec, order_status) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # cur.execute(sql, customer)
        cur.executemany(sql, ordine_noi)
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

@app.route('/txtupload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'txtFileFilter' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['txtFileFilter']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            read()
            return jsonify("upload reusit")

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

@app.route('/orders/<ide>')
def get_orders(ide):
    # a = json.dumps(Orders.ef_time, indent=4, sort_keys=True, default=str)
    session = Session()
    starttime = dt.datetime.strptime(ide, "%Y-%m-%d")
    endtime = starttime+dt.timedelta(days=1)
    condition = sa.and_(Orders.ef_time>=starttime, Orders.ef_time<endtime)
    orders_objects = session.query(Orders).filter(condition).all()
    schema = OrdersSchema(many=True)
    orders = schema.dump(orders_objects)

    session.close()

    #return jsonify(orders.data)
    return json.dumps(orders.data)