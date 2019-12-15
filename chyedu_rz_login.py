'''
注销信息
http://10.26.13.2:801/eportal/?c=Portal&a=logout&callback=dr1576372586702&login_method=1&user_account=drcom&user_password=123&ac_logout=1&register_mode=1&wlan_user_ip=58.116.49.88&wlan_user_ipv6=&wlan_vlan_id=0&wlan_user_mac=000000000000&wlan_ac_ip=&wlan_ac_name=&jsVersion=3.3.1&_=1576371944556
作者：hifuer
版本：1.0
联系方式：hifuer@qq.com
功能：朝阳网认证自动化认证
使用环境：安装 并配置好 python3.7  和requests 库  环境

使用方法：修改 name :手机号   password: 密码  ip:要上网主机IP地址 3个参数
    
    name='xxxxxxxxxxxx'  
    password='xxxxxx'
    ip='xxx.xxx.xxx.xxx'

方法1：cmd 下
python chyeedu_rz_login.py

简单的方法：配置好login.py 默认 python打开   并添加到开始启动项  
'''
import requests
name='xxxxxxxxxxx'
password='xxxxxx'
ip='xxx.xxx.xxx.xxx'
url='http://10.26.13.2:801/eportal/?c=Portal&a=login&callback=dr1576333369207&login_method=1c=Portal&a=login&callback=dr1576333369207&login_method=1&user_account={}&user_password={}&wlan_user_ip={}&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=&wlan_ac_name=&jsVersion=3.3.1&_=1576333337764'.format(name,password,ip)
header={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
#认证
try:
    r=requests.get(url,headers=header)
    #作者不易，请把下面地址设为主页，赞助一下。
    url='https://hao.360.com/?src=lm&ls=n792a71ec92'
    r=requests.get(url,headers=header)
    #print(r.text[361:706])
except:
    pass