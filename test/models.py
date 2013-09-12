'''
Created on 2013-9-12

@author: Administrator
'''
from flask_mongoengine import Document
from mongoengine.fields import StringField


class Post(Document):
    title = StringField(max_length=60,required=True) 