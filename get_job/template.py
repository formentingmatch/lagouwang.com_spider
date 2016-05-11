import urllib.request as request
import urllib.parse as parse

url = r'http://www.lagou.com/jobs/positionAjax.json?'
# 拉钩网的招聘信息都是动态获取的，所以需要通过post来递交json信息，默认城市为北京


def read_page(url, page_num, keyword):  # 模仿浏览器post需求信息，并读取返回后的页面信息
    page_headers = {
        'Host': 'www.lagou.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
        'Connection':'keep-alive'
        }
    if page_num == 1:
        boo = 'true'
    else:
        boo = 'false'
    page_data = parse.urlencode([   # 通过页面分析，发现浏览器提交的FormData包括以下参数
         ('first', boo),
         ('pn', page_num),
         ('kd', keyword)
        ])
    req = request.Request(url, headers=page_headers)
    page = request.urlopen(req, data=page_data.encode('utf-8')).read()
    page = page.decode('utf-8')
    return page
for i in range(95):
    print(read_page(url,i,"Python"))