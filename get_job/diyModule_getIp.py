#coding=utf-8
#每天自动获取ip并保存到响应文件夹
import urllib.request
import re
import random
import time
import os
#首次调用会自动更新ip库
# 更新ip库
def updateIp():
    list=[]
    url="http://fs.xicidaili.com/nn/"
    for i in range(1,4):
        url+=str(i)
        req = urllib.request.Request(url)
        req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0")
        response = urllib.request.urlopen(req)
        html = response.read().decode("utf-8")
        re1=re.compile(r"(([01]{0,1}\d{0,1}[0-9]|2{0,1}[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}[0-9]|2[0-4]\d|25[0-5])</td>\n(\s){1,}<td>\d{1,5}")
        for each_ip in re.finditer(re1,html):
            list.append(each_ip.group().replace("</td>\n      <td>",":"))
    unit = ["年" , "月" , "日" , "时" , "分" , "秒"]
    time1 = time.localtime()
    result = ""
    for i in range(6):
        result += str(time1[i])+str(unit[i])
    print("ip库更新的时间为："+result+"  ip库存："+str(len(list)))
    return list
iplist = updateIp()
#从IP库里随机获取ip
def getIp():
    return random.choice(iplist)
print (getIp())
