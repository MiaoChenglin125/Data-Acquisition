from flask import Flask, render_template,request,redirect,url_for,session,g
from readfile import target
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", data='1851804 苗成林')

@app.route('/table')
def table():
    return render_template("table.html")

if __name__ == "__main__":
    app.run(port=2020, host="127.0.0.1", debug=True)