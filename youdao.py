"""
#分析网站数据
http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule
POST
#传递的数据
i:hello
from:AUTO
to:AUTO
smartresult:dict
client:fanyideskweb
salt:15761578912312
sign:383e5638269a55bbe4f77463d417281e
ts:1576157891231
bv:ab57a166e6a56368c9f95952de6192b5
doctype:json
version:2.1
keyfrom:fanyi.web
action:FY_BY_CLICKBUTTION
#返回的结果
{"translateResult":[[{"tgt":"你好","src":"hello"}]],"errorCode":0,"type":"en2zh-CHS","smartResult":{"entries":["","n. 表示问候， 惊奇或唤起注意时的用语\r\n","int. 喂；哈罗\r\n","n. (Hello)人名；(法)埃洛\r\n"],"type":1}}

"""

import requests
import time
import random
import hashlib
"""
导入4个模块，
requests爬虫模块：与网站建立连接 ，
time时间模块：创建时间戳，
random：创建随机数
hashlib ：创建md5加密
"""


#伪装浏览器
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
    'Cookie':'OUTFOX_SEARCH_USER_ID=1448645893@10.108.160.19; JSESSIONID=aaaJ7duJ3Yqum7MD1w67w; OUTFOX_SEARCH_USER_ID_NCOO=1173179798.1008027; ___rl__test__cookies=1576158376640',
    'Referer':'http://fanyi.youdao.com/'
}

#连接地址
url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

'''
参考js加密 
var t = n.md5(navigator.appVersion),
r = "" + (new Date).getTime(),
i = r + parseInt(10 * Math.random(), 10);
return {
    ts: r,
    bv: t,
    salt: i,
    sign: n.md5("fanyideskweb" + e + i + "n%A-rKaT5fb[Gy?;N5@Tj")
}
'''
# 根据上面参考创建参数
word=input("请输入要翻译单词：")
ts = int(time.time() * 10000)
salt=ts + int(random.random() * 10)
sign="fanyideskweb" + word + str(salt) + "n%A-rKaT5fb[Gy?;N5@Tj"
sign= hashlib.md5(sign.encode('utf-8')).hexdigest()
#传递的数据
data={
    'i':word,
    'from':'AUTO',
    'to':'AUTO',
    'smartresult':'dict',
    'client':'fanyideskweb',
    'salt':None,
    'sign':None,
    'ts':None,
    'bv':'ab57a166e6a56368c9f95952de6192b5',
    'doctype':'json',
    'version':'2.1',
    'keyfrom':'fanyi.web',
    'action':'FY_BY_CLICKBUTTION'
}
data['salt']=salt
data['sign']=sign
data['ts']=ts

#建立连接爬取数据
r=requests.post(url,headers=header,data=data)
#<Response [200]>
#测试打印
#print(r.json())
t=r.json()
tgt=t['translateResult'][0][0]['tgt']
src=t['translateResult'][0][0]['src']
print("您输入的词是: {} , 翻译: {}".format(src,tgt))
