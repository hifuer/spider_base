"""
pearvideo视频下载 js破解
"""
import requests
from lxml import etree  #xpath
import re  #正则表达式
from urllib.request import urlretrieve  #保存

#1.分析网站获取视频地址源码
url='https://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=8&start=12'
def get_heml(url):
    re=requests.get(url)
    if re.status_code==200:
        # print(re.text)
        return re.text  #获取源码
    else:
        return None

#2.获取视频播放地址
def get_video():
    html=get_heml(url) #调用连接
    #// *[ @ id = "categoryList"] / li[13] / div / a  右键copy xpath
    html = etree.HTML(html)
    video_id = html.xpath('//div[@class="vervideo-bd"]/a/@href')
    #print(video_id) #获取href
    video_url=[]
    starturl='https://www.pearvideo.com/'
    for id in video_id:
        newurl = starturl+id
        video_url.append(newurl)
        #print(newurl)

#3.抓包分析，获取标题和视频
        for play_url in video_url:
            html=get_heml(play_url) #获取视频源码
            real_url=re.compile('srcUrl="(.*?)"') #编译正则，提高效率
            real_url=re.findall(real_url,html)  #从后者html 找到正则匹配内容
            #print(real_url) #视频地址
            video_name=re.compile('<h1 class="video-tt">(.*?)</h1>')
            video_name=re.findall(video_name,html)
        # print(video_name,real_url)
#4.下载视频 open urllib-urllibretrieve

        for name,link in zip(video_name,real_url):
            #print(name,link)
            urlretrieve(link, "video\\{}.mp4".format(name))  #下载保存

if __name__ == '__main__':
    html=get_heml(url)
    get_video()