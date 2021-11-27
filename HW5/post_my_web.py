import requests
import lxml

if __name__=='__main__':
    url='http://127.0.0.1:2020/post'
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.34'
    }
    data="choose post"
    response=requests.post(url,headers=headers,data=data)
    page_text=response.text
    # encode编码，将ISO-8859-1编码成unicode
    page_text = page_text.encode(response.encoding)
    # decode解码,将unicode解码成utf-8
    page_text = page_text.decode("utf-8")
    with open("./webs/post_way.html",'w',encoding='utf-8') as f:
        f.write(page_text)
