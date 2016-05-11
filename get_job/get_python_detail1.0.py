#coding=utf-8"
#引入相关的包
import urllib.request
import urllib.parse
#定义访问函数
def main(start_page,stop_page):
    for page in range(start_page,stop_page):
        if page ==1:
            true_or_false = 'true'
        else:
            true_or_false = 'false'
        data = urllib.parse.urlencode([
            ('first', true_or_false),
            ('pn', page),
            ('kd', 'Python')
        ])
        url =r"http://www.lagou.com/jobs/positionAjax.json?"
        header ={
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                            'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
            'Connection':'keep-alive',
            'Host':'www.lagou.com'
                }
        req = urllib.request.Request(url,headers=header)
        response = urllib.request.urlopen(req,data=data.encode("utf-8"))
        html = response.read()
        print(html.decode("utf-8"))
        print(page)
main(start_page=1,stop_page=50)
