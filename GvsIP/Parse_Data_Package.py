# -*- coding:utf-8 -*-
'''
Created on 2017年11月22日

@author: xuyh
'''
import re
import time
import urllib2
import pandas as pda

def Parse_Data_Pak(file_name):
#    '''导入CSV格式数据包，并将CSV包中的目的IP提取出来保存到file_name.txt文件中'''
    #导入数据包
    print(u"Starting Parse_Data_Pak:")
    ImportFile = pda.read_csv(file_name)
    print(u"Step1: ImportFile------>>Import data successfully。")
    #提取第三列的目的地址数据。
    DataFile = ImportFile.iloc[: ,3]

    f = open(file_name + ".txt",'wb')
    print(u"Step2: TXT_file-------->>Success new txt_file named:%s。"%file_name)
    fdi = []
    new_fdi = []
    for i in DataFile:
        fdi.append(i)
    for fd in fdi:
        if fd not in new_fdi:
            new_fdi.append(fd)
    for i in new_fdi:
        Len_IP = len(i)
        if 8< Len_IP < 15:
#             print(i)
            f.write(i + '\n')
        else:
            continue
    f.close()
    print(u"Step3: Add_IP_in_TXT--->>Success add ip in %s"%file_name + u".txt。")
    
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
    time.sleep(0.1)
    Attribution_Data = Response_Find_Data[0]
#     print(Attribution_Data)
    IP_Attribution = Attribution_Data[5:]
#     return x
    return ip + "\t" + IP_Attribution

# def IP_Check_Heavy(SourceIP_filename):
# #     '''导入数据源“SourceIP.txt”，并对其进行导入成列表并查重处理。'''
#     filename = SourceIP_filename + ".txt"
#     SourIP = open(filename,'r')
#     IP_InLines = SourIP.readlines()
#     SourIP.close()
#     temp_IP = []
#     new_IP = []
#     for IP_Data in IP_InLines:
#         temp = IP_Data.strip('\n')
#         temp_IP.append(temp + "/32")
#     for fi in temp_IP:
#         if fi not in new_IP:
#             new_IP.append(fi)
#     print(new_IP)
# #     

#解析抓包文件中的目的IP地址。
file_name = raw_input(u"请输入需要处理的文件名：")
Parse_Data_Pak(file_name)
#去除IP后面的“\n”换行符。并保存到列表temp_IP。
filename = file_name + ".txt"
StrangeIP = open(filename,'r')
IP_InLines = StrangeIP.readlines()
StrangeIP.close()
temp_IP = []
for IP_Data in IP_InLines:
    temp = IP_Data.strip('\n')
    temp_IP.append(temp)
#     temp_IP.append(temp + "/32")
#查找IP归属地。
ip_Addr_TXT = open(file_name + "_Addr.txt",'wb')
for i in temp_IP:
    ip_Addr = Find_IP_Attribution(i)
    print(ip_Addr)
    ip_Addr_TXT.write(ip_Addr + '\n')
ip_Addr_TXT.close()
# print temp_IP
print(u"IP归属地查询完毕")
