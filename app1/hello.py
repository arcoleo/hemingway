from flask import Flask
from flask.ext.admin import Admin, BaseView, expose


app = Flask(__name__)
admin = Admin(app)


class MyView(BaseView):
    @expose('/')
    def index(self):
        return self.render('index.html')



@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello World!'



admin.add_view(MyView(name='Hello'))


if __name__ == '__main__':
    app.run(debug=True)
