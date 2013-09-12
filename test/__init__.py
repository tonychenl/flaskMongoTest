from flask.blueprints import Blueprint
from test.views import DetailView

testxx = Blueprint("test", __name__)

testxx.add_url_rule('/',view_func=DetailView.as_view('detail'))
