'''
Created on 2013-9-12

@author: Administrator
'''
from flask.app import Flask
from test import testxx
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['SECRET_KEY'] = '1asdfj0123asdf'
app.config["MONGODB_SETTINGS"] = {"DB": "test"}

db = MongoEngine(app)

app.register_blueprint(testxx)

if __name__ == '__main__':
    app.run(debug=True,port=5000)