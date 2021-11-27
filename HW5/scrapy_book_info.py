import requests
from bs4 import BeautifulSoup
from lxml import etree
import string
import pymysql

#连接到mysql
conn=pymysql.connect(host='localhost',db='data_mining',user='root',passwd='67537mcl',charset='utf8')
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
def insert(name,writer,isbn,content):
    sql="insert into book(name,writer,isbn,content) values(\"{}\",\"{}\",\"{}\",\"{}\")".format(name,writer,isbn,content)
    #执行sql语句
    cur.execute(sql)
    #向数据库提交数据
    conn.commit()
    print("insert success!!!")

if __name__=='__main__':
    url='https://book.douban.com/top250'
    #将参数单独字典，方便修改
    param={
        'start':'0',#开始位置
    }
    #UA伪装
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 Edg/96.0.1054.26'
    }
    #发送请求
    response=requests.get(url,params=param,headers=headers)
    #返回json数据,返回的是一个列表
    page_text=response.text
    tree=etree.HTML(page_text)
    # title=tree.xpath('//div[@class="pl2"]/a[1]/text()')
    # print(title)
    r = tree.xpath('//div[@class="pl2"]/a[1]/@href')

    for detail_url in r:
        response=requests.get(detail_url,headers=headers)
        detail_text=response.text
        tree = etree.HTML(detail_text)
        #获取书名
        name=tree.xpath('//h1/span[@property="v:itemreviewed"]/text()')[0]
        name = strip_character(name)
        print(name)
        # 获取作者
        try:
            try:
                writer = tree.xpath('// *[ @ id = "info"] / span[1] / a[1]/text()')[0]
            except:
                writer = tree.xpath('//*[@id="info"]/a[1]/text()')[0]
        except:
            writer=''
        writer = strip_character(writer)
        print(writer)
        # 获取isbn
        isbn=tree.xpath('//*[@id="info"]/text()')[-2]
        isbn=strip_character(isbn)
        print(isbn)
        # 获取简介
        try:
            try:
                content = tree.xpath('// *[ @ id = "link-report"] / div[1] / div / p / text()')[0]
            except:
                content = tree.xpath('//*[@id="link-report"]/span[1]/div/p[1]/text()')[0]
        except:
            content=''
        print(content)
        insert(name,writer,isbn,content)
        # insert(lis)

    print('over!!!')