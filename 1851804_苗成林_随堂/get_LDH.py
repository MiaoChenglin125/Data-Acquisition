import requests
from bs4 import BeautifulSoup

def getHTML(url):
    try:
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.44'
        ,'Cookie':'zhishiTopicRequestTime=1636541389794; zhishiTopicRequestTime=1636541424042; BAIKE_SHITONG=%7B%22data%22%3A%22a69b85c667bb24f8f2a53768d7c5472b1b5a40cddec693167011f0b1f298328dcbf1bd2f866fa13d4bbcd17246bf9ef6698a46f54cc9fad6041fbb4d52677190d6b06f8ded4aa23960924a7ba9a5d81ababbb53ad3ebae90554205f1186e037dc69bbd2986e53e51be3d4aa3cc4944e89fa6aa0f3cdcfde553ae6dae3437f410%22%2C%22key_id%22%3A%2210%22%2C%22sign%22%3A%225ddd058f%22%7D; BIDUPSID=413AAAEADFC09A23D4B153634ECA8314; PSTM=1564653571; BK_SEARCHLOG=%7B%22key%22%3A%5B%22%E7%8E%B0%E4%BB%A3%E4%B8%9D%E7%BB%B8%E4%B9%8B%E8%B7%AF%22%5D%7D; __yjs_duid=1_b572587a31590410f95be8a028a9325d1620485618734; BAIDUID=EE09A38CCD079F09AA870EDA13282029:FG=1; channel=baidusearch; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; H_PS_PSSID=31660_26350; BDRCVFR[k2U9xfnuVt6]=mk3SLVN4HKm; delPer=0; PSINO=1; BA_HECTOR=alah20a40020a08lt11gon99t0q; __yjs_st=2_YzQ0ZGRjZWNlZmU0ODZmYWFkY2U2ODliYmRhYjc1N2ViOWQ0M2JiMjY2MzY3YzM4YTJiZjQ0ZDA1OTIyOTczNTk4ZDI4ZTA4MDQ4ZGRmMjQ0OGMxYzBhN2IzYjg0MmExZDBkMzY1Mzc1ZTNkNmY5NGQ1YmRlNmVkZThiMWUwOGZlOTNhYzY2ZWY4NzAxOGIxOWE2N2IwYTJlZTBhN2U5OTkxMjg2ZjQ3MTlkMWFlNWYyNmYxZmRkMzA5NjdjZDgxMWVlNTRhNjE2NWI4NjM0ZjUzZjA0YjQ4MDhhNmVmNTBmOTMyMGE1ZTAwNWI3ZmEyODYwMmQ3NmYwYTE0ZDg1Zl83Xzk4NTQ4YzNj; Hm_lvt_55b574651fcae74b0a9f1cf9c8d7c93a=1635780296,1636527976,1636541389,1636542408; Hm_lpvt_55b574651fcae74b0a9f1cf9c8d7c93a=1636542408; baikeVisitId=4d25409b-6dfc-4237-bd89-35e202f7b3cc; ab_sr=1.0.1_YjdhYTk0ZjYzMjAwZTY0ZGE5ZmYzMmZiZThhMzlmMTQxYTI0ODg4NmY0OGM4M2NmNWE5MTJiOTc2ZjE0N2M2ZGZjY2JhNzg3NDZjZDA5ZmFmYTFkYThjN2JhNTQzZWVlMmFlN2EwOGIxZDI2YTI1NWM3OWY4NDE0ZGU4YjE0NDM0YjRiNGJkM2M4Mjc2NDg1YTY5ZmI0NzY0YTlkNjM0Mw=='}
        r=requests.get(url,headers=headers)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        already_url.append(url)
        return r.text
    except:
        return None
    
def beautiful_soup(html):
    soup = BeautifulSoup(html)
    return soup

def get_all_url(soup):
    for a in soup.find_all('a',target="_blank",href=True):
        if ('https://baike.baidu.com'+a['href'])=='https://baike.baidu.com/item/%E5%88%98%E5%BE%B7%E5%8D%8E/114923':
            with open('LDH.html','w') as f:
                url='https://baike.baidu.com/item/%E5%88%98%E5%BE%B7%E5%8D%8E/114923'
                response = requests.get(url=url)
                page_text = response.text
                # encode编码，将ISO-8859-1编码成unicode
                page_text = page_text.encode(response.encoding)
                # decode解码,将unicode解码成utf-8
                page_text = page_text.decode("utf-8")
                f.write(page_text)
            print("找到刘德华，结束")
            return True
        if ('https://baike.baidu.com'+a['href']) not in already_url:
            url_lst.append('https://baike.baidu.com'+a['href'])
    return False
already_url=[]
url_lst=[]
start_url='https://baike.baidu.com/item/%E9%BB%84%E6%B8%A4/7212966?fr=aladdin'
url_lst.append(start_url)
while(1):
    now_url=url_lst.pop(0)
    html=getHTML(now_url)
    if html==None:
        continue
    soup=beautiful_soup(html)
    if(get_all_url(soup)):
        break
    #print(len(url_lst))