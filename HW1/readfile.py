import pandas as pd     #引入pandas包
citys=pd.read_table('book.txt',sep='\t',encoding='utf-8')     #读入txt文件，分隔符为\t
citys=citys[:-1]

citys.columns=['序号']
citys['书名']=None
citys['分类']=None
for i in range(len(citys)):         #遍历每一行
    coordinate = citys['序号'][i].split() #分开第i行，x列的数据。split()默认是以空格等符号来分割，返回一个列表
    citys['序号'][i]=coordinate[0]        #分割形成的列表第一个数据给x列
    citys['书名'][i]=coordinate[1]        #分割形成的列表第二个数据给y列
    citys['分类'][i] = coordinate[2]  # 分割形成的列表第二个数据给y列

target=citys.to_html(index=None)
#print(target)

