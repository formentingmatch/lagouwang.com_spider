#coding=utf-8
import _thread
import requests
import lxml.etree
import pickle
import time
#打开文件名列表
'''
with open('theme_list.pkl','rb') as theme_list_file:
    theme_list = pickle.load(theme_list_file)
'''
theme_list =['物流', '采购专员', '采购经理', '商品经理', '分析师', '投资顾问', '投资经理', '人事/HR', '薪资福利经理', '绩效考核经理', '人力资源', '招聘', '助理', '财务', '结算', '行政总监/经理', '财务总监/经理', 'HRD/HRM', '投资经理', '分析师', '投资助理', '行业研究', '投资者关系', '资产管理', '理财顾问', '律师', '审计', '法务', '会计', '投资总监', '融资总监', '并购总监', '风控总监', 'Java']
#传入工作的id 返回工作描述的字符串
def get_detail(positionID):
    #define the  headers for the function of get_detaail
    headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
                'Connection':'keep-alive',
                 }
    #post the ID into the url
    url = 'http://www.lagou.com/jobs/'+str(positionID)+'.html'
    #get url
    try:
        html = requests.get(url=url,headers=headers)
    #if failed return None
    except:
        return str(None)
    html.encoding = 'utf-8'
    html = html.text
    #lxml
    html = lxml.etree.HTML(html.lower())
    details = html.xpath('//dd[@class="job_bt"]//text()')
    #define the variate to collect all the string
    main_detail = ''

    for detail in details:
        main_detail=main_detail+detail
    #replace the title
    main_detail = main_detail.replace(r'职位描述','').replace(' ','').replace('\n','')
    return main_detail
def main(job_list_file):
    with open(job_list_file,'rb') as job_list_file:
        job_list = pickle.load(job_list_file)
    job_list_len = len(job_list)
    new_job_list = []
    for job_list_index,job in enumerate(job_list):
        print(str(job_list_file.name)+'  page:'+str(job_list_index)+'/'+str(job_list_len) +time.strftime('%c',time.localtime(time.time())))
        job_description = get_detail(job['positionId'])
        job['description'] = job_description
        new_job_list.append(job)
    new_job_list_file = "ALL+"+str(job_list_file.name)
    with open(new_job_list_file,'wb') as new_job_list_file:
        pickle.dump(new_job_list,new_job_list_file)
'''
for i in theme_list:
    file_name = str(i).replace("/","+")+'.pkl'
    _thread.start_new_thread(main,(file_name,))
while(1):
    pass
'''
for i in theme_list:
    file_name = str(i).replace("/","+")+'.pkl'
    main(file_name)