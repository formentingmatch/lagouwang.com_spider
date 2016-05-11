from selenium import webdriver
import json
import re
with open("python.txt","w") as f:
    for i in range(1,95):
        driver = webdriver.Firefox()
        driver.get("http://www.lagou.com/jobs/positionAjax.json?first=false&pn="+str(i)+"&kd=Python")
        false = False
        true = True
        null = None
        rel = re.compile("</head><body><pre>.*")
        dic = re.search(rel,driver.page_source).group()
        dic = dic[18:-20]
        dic = eval(dic)
        print(type(dic))
        html = json.dumps(dic,sort_keys = True, indent = 4,ensure_ascii=False)
        html = json.loads(html)
        for b in range(0,15):
            a = html['content']['result'][b]
            f.write(str(a)+"\n")