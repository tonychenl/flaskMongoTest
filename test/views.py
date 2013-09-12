'''
Created on 2013-9-12

@author: Administrator
'''
from flask import request
from flask.views import MethodView
from flask_mongoengine.wtf.orm import model_form
from test.models import Post


class DetailView(MethodView):
    
    form = model_form(Post)

    def get_context(self):
        form = self.form(request.values)
        context = {
            "form": form
        }
        return context
    
    def post(self):
        context = self.get_context()
        form = context.get('form')
        post = Post(title='xxx')
        form.populate_obj(post)
        post.save()
        return post.to_json()

