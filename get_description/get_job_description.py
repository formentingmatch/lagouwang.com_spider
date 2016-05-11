import pickle
import requests
import re
import os
def chaxun(file_name):
    list=[]
    with open(file_name,"rb")as f:
        print("正在加载"+str(file_name)+"文件")
        job_list = pickle.load(f)
        rel = re.compile("<p class="">.*</p>")
        job_description = ''
        job_number =len(job_list)
        headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
                'Connection':'keep-alive',
                 }
        for i,job in enumerate(job_list):
            print("正在visit"+file_name+":"+str(i)+'/'+str(job_number))
            job_id = str(job['positionId'])
            url = 'http://www.lagou.com/jobs/'+job_id+'.html'
            try:
                html = requests.get(url=url,headers=headers)
                html.encoding = 'utf-8'
            except:
                html = requests.get(url=url,headers=headers)
                html.encoding = 'utf-8'
            html = html.text
            for content in (re.finditer(rel,html)):
                job_description+=content
            job["job_description"] = job_description
            list.append(job)
        file_name = "all"+file_name
        with open(file_name,"wb") as z:
            pickle.dump(list,z)
            z.close()
'''
with open("theme_list.pkl","rw") as x:
    theme_list = pickle.load(x)
for i in theme_list:
    file_name = str(i).replace("/","+")
    chaxun(file_name)
'''
chaxun('APP设计师.pkl')