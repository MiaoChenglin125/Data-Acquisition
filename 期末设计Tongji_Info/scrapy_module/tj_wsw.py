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
def insert(title,author,publish_time,content,url,key_word):
    sql="insert into `guanchazhe`(title,author,publish_time,content,url,key_word) values(\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\")".format(title,author,publish_time,content,url,key_word)
    #执行sql语句
    with open("sql.txt","a") as f:
        f.write(sql)
    print(sql)
    cur.execute(sql)
    print("excute success!!!")
    #向数据库提交数据
    conn.commit()
    print("insert success!!!")

start_url = "https://fao.tongji.edu.cn/4111/list.htm"

# 控制chrome浏览器
driver = webdriver.Chrome(r'C:\Program Files\Google\Chrome\Application\chromedriver.exe')
# 输入网址
driver.get(start_url)
idx=0
while idx<=20:
    idx+=1
    # 停一下，等待加载完毕
    time.sleep(2)
    # 获取网页内容Elements
    content = driver.page_source
    with open("tj_cwc.html","w",encoding="utf-8") as f:
        f.write(content)
    # 提取数据
    # data_list = etree.HTML(content).xpath('//div[@class="item-root"]')[1:]
    data_list = etree.HTML(content).xpath('//*[@id="dgNewsList"]//a/@href')
    for item in data_list:
        link='https://fao.tongji.edu.cn'+item
        # print(link)
        r=requests.get(link)
        r.encoding = 'utf-8'
        child_content=r.text
        # child_content = child_content.encode('utf-8','ignore').decode('utf-8','ignore').encode('GBK','ignore')
        child_data = etree.HTML(child_content)
        try:
            item = {}
            item["title"] = child_data.xpath('//*[@id="lblTitle"]/text()')[0]
            item["author"] = "同济大学外事办公室"
            item["publish_time"] = child_data.xpath('//*[@id="mainwh"]/table/tbody/tr/td[2]/div/div/table/tbody/tr[1]/td/text()')[1]
            item["publish_time"]=item["publish_time"].strip('发布时间：')
            item["content"] = child_data.xpath('//*[@id="mainwh"]/table/tbody/tr/td[2]/div/div/table/tbody/tr[2]/td/div//text()')
            str=''
            for content in item['content']:
                content=content.strip()
                str+=content
            item["content"]=str
            item["url"] = link
            key_word=''
            item["keyword"]=jieba.lcut(item["title"])[:3]
            for key in item['keyword']:
                key_word+=(key+',')
            item["keyword"]=key_word
            print(item)
            insert(item["title"], item["author"], item["publish_time"], item["content"], item["url"], item["keyword"])
            sleep(1)
        except:
            continue
    next = driver.find_element_by_xpath('//*[@id="wp_paging_w4"]/ul/li[2]/a[3]')
    # 判断
    if next.get_attribute("href"):
        # 单击
        next.click()
    else:
        # 跳出循环
        break
# 结束
driver.quit()
