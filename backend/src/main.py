from .entities.entity import Session, engine, Base
from .entities.exam import Exam, ExamSchema, Customer, CustomerSchema, Orders, OrdersSchema, Test, TestSchema
from flask_cors import CORS
from flask import Flask, jsonify, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
import simplejson as json
from sqlalchemy.sql import select
from datetime import date
from sqlalchemy import Date
import datetime as dt
import sqlalchemy as sa
import os
from flask import send_from_directory


# generate database schema
Base.metadata.create_all(engine)

UPLOAD_FOLDER = '/tmp/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

# start session
session = Session()


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file', filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

@app.route('/exams')
def get_exams():
    session = Session()
    exam_objects = session.query(Exam).all()

    schema = ExamSchema(many=True)
    exams = schema.dump(exam_objects)

    session.close()
    return jsonify(exams.data)

@app.route('/customers')
def get_customers():
    session = Session()
    customers_objects = session.query(Customer).all()

    schema = CustomerSchema(many=True)
    customers = schema.dump(customers_objects)

    session.close()
    return jsonify(customers.data)

@app.route('/test')
def get_tests():
    session = Session()
    test_objects = session.query()


    return jsonify('am realizat')

    # session = Session()
    # test_objects = session.query(Test).filter(Test.id=='2').all()

    # schema = TestSchema(many=True)
    # tests = schema.dump(test_objects)

    # session.close()
    # return jsonify(tests.data)

@app.route('/orders/<ide>')
def get_orders(ide):
    a = json.dumps(Orders.ef_time, indent=4, sort_keys=True, default=str)
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


@app.route('/exams', methods=['POST'])
def add_exam():
    # mount exam object
    posted_exam = ExamSchema(only=('title', 'description'))\
        .load(request.get_json())

    exam = Exam(**posted_exam.data, created_by="HTTP post request")

    # persist exam
    session = Session()
    session.add(exam)
    session.commit()

    # return created exam
    new_exam = ExamSchema().dump(exam).data
    session.close()
    return jsonify(new_exam), 201