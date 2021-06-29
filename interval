#代码整理

import pandas as pd
data = pd.read_excel('./data5/interval.xlsx')
#取出time_break
t = data['time_break'].values.tolist()
#初始化
group = []
n = 1
#通过time_break判断创建分组
for num in range(len(data)):
    if t[num] == 0:
        group.append(n)
    else:
        n = n+1
        group.append(n)
#将分组放入原数据新增一列
data['group'] = group
#导出文件
writer = pd.ExcelWriter('./data5/group.xlsx')
data.to_excel(writer,float_format='%.5f')
writer.save()






#整理脚本，解决读取超过65535行csv数据

import pandas as pd
import numpy as np


#使用chunksize分块读取大型csv文件，这里每次读取chunksize为100万
data_chunk = pd.read_csv('./data5/all.csv', chunksize=1000000, iterator = True)

chunk_list = [] 

for chunk in data_chunk:
    chunk_list.append(chunk)
    
#再把这些块组合成一个DataFrame
data = pd.concat(chunk_list) 

#取出time_break
t = data['time_break'].values.tolist()
#初始化
group = []
n = 1
#通过time_break判断创建分组
for num in range(len(data)):
    if t[num] == 0:
        group.append(n)
    else:
        n = n+1
        group.append(n)
#将分组放入原数据新增一列
data['group'] = group

#导出文件
data.to_csv('./data5/all_group.csv')
