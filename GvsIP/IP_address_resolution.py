# -*- coding:utf-8 -*-
'''
Created on 2017年11月28日

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
    
#解析抓包文件中的目的IP地址。
file_name = raw_input(u"请输入需要处理的文件名：")
Parse_Data_Pak(file_name)
