import os
import pickle
import csv
list = []

with open('theme_list.pkl','rb') as theme_list_file:
    theme_list = pickle.load(theme_list_file)
print('总计工作分类数目：'+str(len(theme_list)))
with open('工作数目统计.txt','w') as q:
    s = 0
    for a in theme_list:
        a_1 = str(a).replace('/','+')
        a_2 = 'ALL+'+a_1+'.pkl'
        with open(a_2,'rb') as f:
            list = pickle.load(f)
        job_num = len(list)
        s+=job_num
        job_con = a_1+':'+str(job_num)+'\n'
        q.writelines(job_con)
    zongshu = '总工作数目：'+str(s)
    q.writelines(zongshu)