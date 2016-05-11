#coding=utf-8
import urllib.request
import urllib.parse
import http.cookiejar
import python.diyModule_getIp


def getUrlByAgentIP(url,data):
    ip = python.diyModule_getIp.getIp()
    proxy_support = urllib.request.ProxyHandler({"http":ip})
    opener = urllib.request.build_opener(proxy_support)
    opener.addheaders=[
          ("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0"),
          ("Accept","text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"),
          ("Accept-Encoding",	"gzip, deflate"),
          ("Connection","keep-alive"),
          ("Host","www.lagou.com"),
          ("X-Forwarded-For",ip)
    ]
    urllib.request.install_opener(opener)
    response = urllib.request.urlopen(url,data=data)
    html = response.read()
    return html
for i in range(2,50):
    data = urllib.parse.urlencode([
            ('first', 'false'),
            ('pn', i),
            ('kd', 'Python')
        ])
    res = getUrlByAgentIP(url =r"http://www.lagou.com/jobs/positionAjax.json?",data=data.encode("utf-8"))
    print(res.decode("utf-8"))