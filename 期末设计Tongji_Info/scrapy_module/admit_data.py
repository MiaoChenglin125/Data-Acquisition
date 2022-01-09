# encoding: utf-8
import pymysql
from selenium import webdriver
from lxml import etree
import os
import time
import requests
import re
import csv
import jieba
import string
from time import sleep

#连接到mysql
conn=pymysql.connect(host='localhost',db='tj_news',user='root',passwd='67537mcl',charset='utf8')
cur=conn.cursor()

#关闭数据库连接
def closeDB():
    conn.close()

#去除特殊字符
def strip_character(str):
    stay=string.punctuation
    new_string = ''.join(char for char in str if (char.isalnum() or char in stay))
    return new_string

#单条数据存储到sql
def insert(graduate_school,graduate_major,undergraduate_school,undergraduate_major,url,background):
    sql="insert into `admit_data`(graduate_school,graduate_major,undergraduate_school,undergraduate_major,url,background) values(\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\")".\
        format(graduate_school,graduate_major,undergraduate_school,undergraduate_major,url,background)
    #执行sql语句
    with open("sql.txt","a") as f:
        f.write(sql)
    cur.execute(sql)
    #向数据库提交数据
    conn.commit()
    print("insert success!!!")

start_url = "http://www.compassedu.hk/offer_12_1_0_0"
r=requests.get(start_url)
r.encoding = 'utf-8'
content=r.text
# 停一下，等待加载完毕
time.sleep(2)
# 获取网页内容Elements
links = etree.HTML(content).xpath('//*[@class="all aif"]/@href')
for link in links:
    r = requests.get('http://' + link[2:])
    r.encoding = 'utf-8'
    content = r.text
    data = etree.HTML(content)
    dict = {}
    try:
        admit = data.xpath('//div[@class="spani"]/text()')
        dict['graduate_school'] = admit[3]
        dict['graduate_major'] = admit[-1].strip()
        dict['undergraduate_school'] = admit[1]
        dict['undergraduate_major'] = admit[2]
        dict['background'] = data.xpath('//div[@class="spani ben-spani"]/text()')[0]
        dict['url'] = 'http://' + link[2:]
        print(dict)
        insert(dict['graduate_school'], dict['graduate_major'], dict['undergraduate_school'],
               dict['undergraduate_major'], dict['url'], dict['background'])
    except:
        continue
# for coun in range(1,12):
#     params={
#         'ctry': '12',
#         'count':coun,
#         'major': '1',
#         'univ': '0',
#         'gpa': '0'
#     }
#     post_url = "http://www.compassedu.hk/mainvl_succlazy"
#     r=requests.post(post_url,params)
#     r.encoding = 'utf-8'
#     content = r.text
#     # 停一下，等待加载完毕
#     time.sleep(2)
#     links = etree.HTML(content).xpath('//*[@class="lazya all hif"]/@href')
#     for link in links:
#         r = requests.get('http://'+link[2:])
#         r.encoding = 'utf-8'
#         content = r.text
#         data = etree.HTML(content)
#         dict={}
#         try:
#             admit=data.xpath('//div[@class="spani"]/text()')
#             dict['graduate_school']=admit[3]
#             dict['graduate_major'] = admit[-1].strip()
#             dict['undergraduate_school'] = admit[1]
#             dict['undergraduate_major'] = admit[2]
#             dict['background'] = data.xpath('//div[@class="spani ben-spani"]/text()')[0]
#             dict['url']='http://'+link[2:]
#             print(dict)
#             insert(dict['graduate_school'], dict['graduate_major'], dict['undergraduate_school'], dict['undergraduate_major'] , dict['url'], dict['background'])
#         except:
#             continue

