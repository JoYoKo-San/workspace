# -*- coding:utf-8 -*-
'''
Created on 2017年11月22日

@author: xuyh
'''
import os
import urllib2
import httplib


'''导入数据源“SourceIP.txt”，并对其进行导入成列表并查重处理。'''
file_name = raw_input(u"请输入需要处理的文件名：")
SourIP = open(file_name + '.txt','r')
IP_InLines = SourIP.readlines()
SourIP.close()
temp_IP = []
NEW_IPS = []
for IP_Data in IP_InLines:
    temp = IP_Data.strip('\n')
    temp_IP.append(temp + "/32")
for fi in temp_IP:
    if fi not in NEW_IPS:
        NEW_IPS.append(fi)
# print(NEW_IPS)

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
os.remove('pagehandler.txt')
OLD_IPS = []
for linedata in sourceInLines:
    #以','为标志，将每行分割成列表，返回的temp1为一个列表。
    temp1 = linedata.split(',')
#遍历temp1列表中的每一个元素。
for sourceIp in temp1:
    #temp2和temp3去除每一行的双引号。
    temp2 = sourceIp.lstrip('"')
    temp3 = temp2.rstrip('"')
    OLD_IPS.append(temp3)

Pos_IP = []
#查看列表NEW_IPS中的IP是否已经存在于列表OLD_IPS中。
def Compare_files(new_ips, old_ips):
    for i in new_ips:
        if i not in old_ips:
            Pos_IP.append(i)
        
Compare_files(NEW_IPS, OLD_IPS)
print(Pos_IP)

for i in Pos_IP:
    url = "http://slt.6luyou.com/ly_fyx/addVPN?companyID=1490838811999&code=lksdf23xi9&vpn=" + i +"&remark=" + file_name
    conn = httplib.HTTPConnection("slt.6luyou.com")
    conn.request(method="GET",url=url) 
    response = conn.getresponse()
    res= response.read()
    print res

print(u"IP地址添加完毕")
num = len(Pos_IP)
print(u"总共添加IP：%s")%int(num)
    