from crypt import methods
from flask import Flask, abort, redirect, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/index/')
def hello():
    return '<h1>Hello, World!</h1>'

@app.route('/about/')
def about():
    return '<h3>This is a Flask web application.</h3>'

@app.route("/capitalize/<word>")
def capitalise(word):
    return "<pre>{}</pre>".format(str(word).upper())

@app.route("/add/<int:num1>/<int:num2>")
def add(num1, num2):
    return "<h4>Sum is <code>{}</code>".format(num1+num2)


@app.route("/users/<int:user_id>")
def check_user(user_id):
    users = ["Rama", "Sita", "Lakshman"]
    try:
        user = users[user_id]
        return "<h1>{}</h1>".format(user)
    except Exception as e:
        print(e)
        abort(404)

@app.route('/dashboard/<name>')
def dashboard(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['username']
      return redirect(url_for('dashboard',name = user))
   else:
      user = request.args.get('name')
      return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True, port=8080)