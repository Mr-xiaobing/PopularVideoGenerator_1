#爬取gif图
import re
import requests
import os

#获取url_list,就是所有的图片链接
def get_url(url):
    response = requests.get(url)
    response.encoding='utf-8'
    url_addr = r'	<img class="lazy" src="(.*?)" data-original=".*?" alt=".*搞笑.*" oncontextmenu="return false;" ondragstart="return false;" />'
    url_list = re.findall(url_addr,response.text) #通过正则表达式查找
    return url_list
#下载保存一张图片
def getOneGIF(url,a):
    # 获取图片
    response = requests.get(url)
    os.makedirs("./gif/",exist_ok=True)
    with open("./gif/%d.gif"%a,'wb') as file:
        file.write(response.content)

#程序开始
def getGIF():
    a=1
    # 只爬取30页算了  我爬取的都是搞笑gif图
    for i in range(1,30):
        # i=i+17
        url = 'https://www.soogif.com/gif/10623-%d-0-0.html'%i
        print(url)
        url_list = get_url(url)
        print(url_list)
        for url in url_list:
            # url= url.replace('_1',"")
            url = url
            print(url)
            getOneGIF(url,a)
            a+=1
    return a