# import requests
#
# #批量获取企业id号
# url='http://scxk.nmpa.gov.cn:81/xk/'
# headers={
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.35 Safari/537.36 Edg/96.0.1054.13'
# }
#
# response=requests.get(url=url,headers=headers)
# page_text=response.text
# # # encode编码，将ISO-8859-1编码成unicode
# # page_text = page_text.encode(response.encoding)
# # # decode解码,将unicode解码成utf-8
# # page_text = page_text.decode("gbk")
# with open('makeup.html','w',encoding='utf-8') as f:
#     f.write(page_text)
#     #ajax动态请求，更新局部页面


str='1050.20元'

students = [('john', 'A', '15.8元'), ('jane', 'B', '12.00元'), ('dave', 'B', '100.5元')]
#students = sorted(students, key=lambda student : float(student[2].split('元')[0]))


#方法一
lis=str.split('元')
print(float(lis[0]))

#方法二
def draw_num(str):
    tmp=''
    for item in str:
        if (item>='0' and item<='9') or item=='.':
            tmp+=item

    return float(tmp)

students = sorted(students, key=lambda student : draw_num(student[2]))
print(students)

num=draw_num(str)
print(num)

