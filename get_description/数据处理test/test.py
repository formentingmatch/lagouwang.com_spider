#coding=utf-8
import pickle
a = {}
a = set(a)
print(type(a))
def chuli(failname):
    with open(failname,'rb') as f:
        job_list = pickle.load(f)
        for index,job in enumerate(job_list):
            #print(str(index)+':'+str(job['workYear']))
            #for i in job['companyLabelList']:
            a.add(job['positionFirstType'])
        print(a)
    #for key,value in job_list[0].items():
        #print('key=',key,'   ','value=',value)
chuli('ALL+Python.pkl')