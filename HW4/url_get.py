import re
import requests
import urllib.request


def getlink(url):
    headers = ("User-Agent",
               "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    urllib.request.install_opener(opener)
    file = urllib.request.urlopen(url).read()
    file = file.decode('utf-8')
    pattern = '(https?://[^\s)";]+(\.(\w|/)*))'
    linklist = re.compile(pattern).findall(file)
    # 去重
    # link = list(set(link))
    print(linklist[0])
    return linklist


url = "http://www.weather.com.cn/weather/101020100.shtml"
linklist = getlink(url)
count=0
for link in linklist:
    if link[1]=='.shtml':
        url=link[0]
        count+=1
        if count>=70:
            break
        print(url)
        response=requests.get(url=url)
        page_text=response.text
        # encode编码，将ISO-8859-1编码成unicode
        page_text = page_text.encode(response.encoding)
        # decode解码,将unicode解码成utf-8
        page_text = page_text.decode("utf-8")

        with open ('related_pages_save/'+link[0][-15:],'w',encoding='utf-8') as f:
            f.write(page_text)
