# -*- coding:utf-8 -*-
'''
Created on 2017年11月22日

@author: xuyh
'''
import re
import urllib2

def Find_IP_Attribution(ip):
    '''
           查找IP的归属地址并以：“IP + 地址”的格式返回    
    '''
    #发送含IP地址的url请求。
    url = "http://www.ip138.com/ips1388.asp?ip="+ip+"&action=2"
    
    headers = {
        "User-Agent":" Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": "pgv_pvi=8624876544; pgv_si=s5868361728; ASPSESSIONIDCCDDSTBC=HKBECNFBFPJHKNANKNFNPKOD",
        }
    
    request = urllib2.Request(url, headers = headers)
    response = urllib2.urlopen(request)
    
    content = response.read().decode("gbk")
    
    #处理请求返回的信息，获取IP地址归属地。
    Response_Find_Data = re.findall(r"<li>(.*?)</li>", content)
    Attribution_Data = Response_Find_Data[0]
    IP_Attribution = Attribution_Data[5:]
    return ip + "\t" + IP_Attribution

t = Find_IP_Attribution("218.88.124.188")
print(t)

