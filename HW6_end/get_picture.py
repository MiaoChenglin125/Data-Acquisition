import requests
import re
from lxml import etree
from bs4 import BeautifulSoup
import time
import threading

counter = 1
lock = threading.Lock()

def get_html_tiezi(url):
    cookies = {
    }

    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.20 Safari/537.36 Edg/97.0.1072.21'
    }
    
   
    try:
        r = requests.get(url,headers=headers,cookies=cookies)
        r.raise_for_status()
        r.encoding = r.apparent_encoding

        return r.text,""
    except Exception as result:
        return "",result

def get_html_tieba(url):
    headers = {
    }
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding

        return r.text,""
    except Exception as result:
        return "",result

def get_pic(html_tiezi,counter1):

    selector = etree.HTML(html_tiezi) #可xpath对象
    #先尝试爬楼主
    #firstpic=selector.xpath('//div[@class="l_post j_l_post l_post_bright noborder "]/div[@class="d_post_content_main d_post_content_firstfloor "]/div/cc/div[@class="d_post_content j_d_post_content  clearfix"]/img')
    firstpic = selector.xpath('//img[@class="BDE_Image"]/@src')

    for i,j in zip(firstpic,range(counter1,counter1+len(firstpic))):
        print("存储图片：",j, "......")
        response = requests.get(i)
        img = response.content
        # 将他拷贝到本地文件 w 写  b 二进制  wb代表写入二进制文本
        with open( r'.\picOf11\{}.jpg'.format(j),'wb' ) as f:
            f.write(img)
    return counter1+len(firstpic)

def get_more_url_fromtibeba(html_tieba):
    link_list=[]
    selector = etree.HTML(html_tieba)
    # print(html_tieba)
    # with open("11.html",'w',encoding="utf-8") as f:
    #     f.write(html_tieba)
    for i in selector.xpath('//div[@class="threadlist_lz clearfix"]/div/a/@href'):
        link_list.append('https://tieba.baidu.com/'+i+'?pn=1')  #帖子的首页
    return link_list

def get_more_url_fromtiezi(html_tiezi): #只要帖子不同页
    selector = etree.HTML(html_tiezi)
    link_list=[]
    for i in selector.xpath('//*[@id="thread_theme_5"]/div[1]/ul/li[1]/a/@href'):
        link_list.append('https://tieba.baidu.com/'+i)
    return link_list

def thread1(list_url,list_stop):
    global counter
    #while(list_url): 
    # for i in range(1000):
    # print("休眠中")
    # time.sleep(1)
    # print("恢复")
    print("thread1")

    lock.acquire()
    url = list_url.pop(0)
    list_stop.add(url)
    lock.release()

    if re.match(r'.*/p/.*',url): ##是帖子
        html_tiezi,strr=get_html_tiezi(url)
        lock.acquire()
        counter =  get_pic(html_tiezi,counter)
        lock.release()
        # 获取不同页数url
        for i in get_more_url_fromtiezi(html_tiezi):
            if i not in list_stop:
                lock.acquire()
                list_url.append(i)
                lock.release()
            
    else:                        ##是贴吧目录
        html_tieba,strr=get_html_tieba(url)
        #获取目录下帖子
        for i in get_more_url_fromtibeba(html_tieba):
            if i not in list_stop:
                lock.acquire()
                list_url.append(i)
                lock.release()
        #贴吧目录图片可以不爬
        #贴吧目录下一页要存
        if url.replace(re.findall(r'.*&pn=(.*)',url)[0], str(int(re.findall(r'.*&pn=(.*)',url)[0])+50)) not in list_stop:
            lock.acquire()
            list_url.append(url.replace(re.findall(r'.*&pn=(.*)',url)[0], str(int(re.findall(r'.*&pn=(.*)',url)[0])+50)))
            lock.release()

if __name__ == "__main__":
    start_url = 'https://tieba.baidu.com/f?ie=utf-8&kw=%E5%90%8C%E6%B5%8E%E5%A4%A7%E5%AD%A6&fr=search'
    #start_url = 'https://tieba.baidu.com/p/3548250800'
    list_url=[] #待拓展节点
    list_stop=set() #已拓展节点
    list_url.append(start_url)
    while list_url or (threading.activeCount()>1):
        while list_url==[]:
            continue
        w=threading.Thread(target=thread1,args=(list_url,list_stop,))
        w.daemon=True
        w.start()
        time.sleep(1)
    w.join()
    print('finish')

    


            


    
     
            

    




