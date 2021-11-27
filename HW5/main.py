import pymysql
from flask import Flask
import os
import sys

import requests
os.chdir(sys.path[0])
from flask_bootstrap import Bootstrap
from flask import Flask, request, jsonify
from flask import render_template
import json

import pymysql
app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    conn=pymysql.connect(host='localhost',db='data_mining',user='root',passwd='67537mcl',charset='utf8')
    cur = conn.cursor()
    sql = "SELECT * FROM book"
    cur.execute(sql)
    u = cur.fetchall()
    print(u)
    conn.close()
    request_way='get'
    return render_template('index.html',u=u,request_way=request_way)

@app.route('/post',methods=['post'])
def post():
    if  not request.data:   #检测是否有数据
        return ('fail')
    post_data = request.data.decode('utf-8')
    #获取到POST过来的数据，因为我这里传过来的数据需要转换一下编码。根据晶具体情况而定
    # data_json = json.loads(post_data)
    #把区获取到的数据转为JSON格式。

    conn=pymysql.connect(host='localhost',db='data_mining',user='root',passwd='67537mcl',charset='utf8')
    cur = conn.cursor()
    sql = "SELECT * FROM book"
    cur.execute(sql)
    u = cur.fetchall()
    conn.close()
    request_way=post_data
    return render_template('index.html',u=u,request_way=request_way)

if __name__ == '__main__':
    app.run(port=2020, host="127.0.0.1", debug=True)
