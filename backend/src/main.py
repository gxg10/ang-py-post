from .entities.entity import Session, engine, Base
from .entities.exam import Exam, ExamSchema, Customer, CustomerSchema, Orders, OrdersSchema
from flask_cors import CORS
from flask import Flask, jsonify, request
import simplejson as json

# generate database schema
Base.metadata.create_all(engine)

# start session
session = Session()

# orderss = session.query(Orders).all()
# for o in orderss:
#     print(f'({o.id}) {o.simbol}')

# check for existing data
# exams = session.query(Exam).all()

# cust = session.query(Customer).all()

# for c in cust:
#     print(f'({c.id}) {c.firstname}')

app = Flask(__name__)
CORS(app)

# if len(exams) == 0:
#     # create and persist dummy exam
#     python_exam = Exam("SQLAlchemy Exam", "Test your knowledge about SQLAlchemy.", "script")
#     session.add(python_exam)
#     session.commit()
#     session.close()

#     # reload exams
#     exams = session.query(Exam).all()

# show existing exams
# print('### Exams:')
# for exam in exams:
#     print(f'({exam.id}) {exam.title} - {exam.description}')

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

@app.route('/orders/<ide>')
def get_orders(ide):
    session = Session()
    # orders_objects = session.query(Orders).all()
    orders_objects = session.query(Orders).filter(Orders.data == ide)

    schema = OrdersSchema(many=True)
    orders = schema.dump(orders_objects)

    session.close()

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