import requests
import pickle
import time
with open("theme_list.pkl","rb") as f:
    theme_list = pickle.load(f)
    f.close()
def get_itemslist(theme,page):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
        'Connection':'keep-alive',
            }
    url = r"http://www.lagou.com/jobs/positionAjax.json?"
    if page ==1:
        f_or_t = "true"
    else:
        f_or_t = "false"
    data = {
        'first':f_or_t,
        'pn':page,
        'kd': theme
    }
    try:
        html = requests.post(url,data=data,headers=headers)
        html.encoding = 'utf-8'
    except:
        html = requests.post(url,data=data,headers=headers)
        html.encoding = 'utf-8'
    return html.json()['content']
#theme_list =
if __name__ == '__main__':

    maxnum = len(theme_list)
    for theme_index,theme in enumerate(theme_list):
        theme = str(theme).replace("/","+")
        main_job_list = []
        print("正在访问主题：NO."+str(theme_index)+"/"+str(maxnum)+"  名称："+str(theme)+"   时间："+time.strftime('%c',time.localtime(time.time())))
        filename = str(theme)+".pkl"
        with open(filename,"wb") as theme_file:
            for page in range(1,10000):
                print("正在访问页码："+str(page)+"   时间："+time.strftime('%c',time.localtime(time.time())))
                job_list = get_itemslist(theme,page)['result']
                if len(job_list)==0:
                    break
                else:
                    main_job_list += job_list
            pickle.dump(main_job_list,theme_file)
