import requests
import re
import pickle
import lxml.etree
url = 'http://www.lagou.com'
html = requests.get(url=url)
rel = re.compile('class="">.*</a>')
list = []
for index,i in enumerate(re.finditer(rel,html.text)):
    list.append(i.group()[9:-4])
    print(index)
with open("theme_list.pkl","wb") as f:
    pickle.dump(list,f)
    f.close()


