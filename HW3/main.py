import requests
import re
import time
import json


def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'}
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            return res.text
        else:
            return None
    except RequestException:
        print("请求错误")


def jx_html(text):
    restr = re.compile(
        'href.*?title="(.*?)".*?</a>.*?pl.*?>(.*?)</p>.*?rating_nums.*?>(.*?)</span>.*?inq.*?>(.*?)</span>', re.S)
    result = re.findall(restr, text)
    for ree in result:
        yield {'bookname': ree[0], 'author': ree[1], 'score': ree[2], 'expl': ree[3]}


def save_fil(content):
    with open('book250.txt', 'a', encoding='utf-8')as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def main(offset):
    url = 'https://book.douban.com/top250?start=' + str(offset)
    html = get_one_page(url)
    df = jx_html(html)
    for dff in df:
        save_fil(dff)


if __name__ == '__main__':
    for i in range(0, 10):
        main(offset=i * 25)
        time.sleep(1)  # 调用time休眠1S，防止因请求过快出发反爬虫
