import os
import urllib.request
import urllib.parse


def handle_request(url,page,baname):
    pn=(page-1)*50
    #拼接url
    data={
        'kw':baname,
        'pn':pn,
    }
    url+=urllib.parse.urlencode(data)
    #print(url)
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
    }
    request=urllib.request.Request(url=url,headers=headers)
    return request


def download(request,baname,page):
    response=urllib.request.urlopen(request)
    if not os.path.exists(baname):
        os.mkdir(baname)
    filename='第%s页.html' % page
    filepath = os.path.join(baname,filename)
    with open(filepath,'wb') as fp:
         fp.write(response.read())


def main():
    baname=input('输入下载的贴吧名字：')
    start_page=int(input('输入开始页码：'))
    end_page=int(input('输入结束页码：'))
    url = 'https://tieba.baidu.com/f?kw=&'
    for page in range(start_page,end_page+1):
        print('正在下载%s页...' % page)
        request=handle_request(url,page,baname)
        download(request,baname,page)
        print('结束下载%s页' % page)


if __name__ == '__main__':
  main()