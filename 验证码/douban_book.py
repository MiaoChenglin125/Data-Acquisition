# encoding: utf-8
'''
  @author 李华鑫
  @create 2020-10-09 11:34
  Mycsdn：https://buwenbuhuo.blog.csdn.net/
  @contact: 459804692@qq.com
  @software: Pycharm
  @file: 豆瓣图书.py
  @Version：1.0

'''
from selenium import webdriver
from lxml import etree
import os
import time
import requests
import re
import csv

start_url = "https://book.douban.com/subject_search?search_text=python&cat=1001&start=%25s0"

# 控制chrome浏览器
driver = webdriver.Chrome(r'C:\Program Files\Google\Chrome\Application\chromedriver.exe')
# 输入网址
driver.get(start_url)
while True:
    # 停一下，等待加载完毕
    time.sleep(2)
    # 获取网页内容Elements
    content = driver.page_source
    # 提取数据
    data_list = etree.HTML(content).xpath('//div[@class="item-root"]')[1:]
    for data in data_list:
        item = {}
        item["name"] = data.xpath("./div/div[1]/a/text()")[0]
        item["score"] = data.xpath("./div/div[2]/span[2]/text()")[0]
        with open("./豆瓣图书.csv", "a", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(item.values())
        print(item)
    # 找到后页
    next = driver.find_element_by_xpath('//a[contains(text(),"后页")]')
    # 判断
    if next.get_attribute("href"):
        # 单击
        next.click()
    else:
        # 跳出循环
        break
# 结束
driver.quit()
