# Import modules
import flask
import flask_pymongo
from flask import Flask,render_template,jsonify
from flask_pymongo import PyMongo
from flask.globals import request
from jinja2.utils import is_undefined
from pymongo import mongo_client


# Set up mongodb
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/todos"
mongodb_client = PyMongo(app)
db=mongodb_client.db

# Route
@app.route('/',methods=['GET','POST'])
def home():
    textinput=request.form.get('intxt')
    if (textinput!=None) and textinput!="":
        todo=db.todo.insert_one({'content':textinput})
    todos_l=db.todo.find()
    textinput=""
    return render_template('index.html',todos=todos_l)
# Run server
app.run(debug=True)
