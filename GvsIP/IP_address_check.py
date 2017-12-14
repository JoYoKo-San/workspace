# -*- coding:utf-8 -*-
'''
Created on 2017年11月28日

@author: xuyh
'''
import os
import urllib2
import httplib

'''从VPN上获取已经添加的IP地址并添加到列表fp_new中'''
pagehandler = urllib2.urlopen("http://slt.6luyou.com/ly_fyx/getVpnAddress?companyID=1490838811999&code=lksdf23xi9&userName=1").read()
#统计pagehandler中的长度（len），并提取出最后一个IP地址“]”的位置。
endnum = len(pagehandler) - 14
f = open('pagehandler.txt','wb')
for i in pagehandler[12:endnum]:
    f.write(i)
f.close()
fp = open('pagehandler.txt','r')
sourceInLines = fp.readlines()
fp.close()
#删除txt文件。
# os.remove('pagehandler.txt')
OLD_IPS = []
for linedata in sourceInLines:
    #以','为标志，将每行分割成列表，返回的temp1为一个列表。
    temp1 = linedata.split(',')
#遍历temp1列表中的每一个元素。
for sourceIp in temp1:
    #temp2和temp3去除每一行的双引号。
    temp2 = sourceIp.lstrip('"')
    temp3 = temp2.rstrip('"')
    print(temp3)
    OLD_IPS.append(temp3)
x = len(OLD_IPS)
print(x)
