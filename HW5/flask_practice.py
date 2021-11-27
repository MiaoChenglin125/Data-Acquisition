import os
import sys
os.chdir(sys.path[0])

from flask import Flask,render_template,jsonify,redirect,url_for

app=Flask(__name__,template_folder='templates')

#传入数据类型：
# int
# float
# path
# uuid

@app.route('/')
def index(userid):
    f=open("./static/js/test.json").read()
    return jsonify(f)

@app.route('/home')
def home():
    html=open("./templates/index.html",encoding='utf-8').read()
    return html

@app.route('/miao')
def miao():
    return render_template('index.html')


@app.route('/direct')
def direct():
    return redirect(location=url_for('str',userid='777'))

@app.route('/str/<int:userid>')
def str(userid):
    # s=(1,2,3)
    # return '<h1>hello{}</h1>'.format(userid)
    return redirect(location=url_for('home'))

if __name__=="__main__":
    app.run(port=2020, host="127.0.0.1", debug=True)