#!/usr/bin/python
# -*- coding: UTF-8 -*-
import subprocess  
import os  
import sys

if len(sys.argv)<2:
    print ("argument error!\n Use as :1.py orim3u newm3u")
    sys.exit()

ncmdump = u"ncmdump-windows-386.exe"

ori_m3u = open(sys.argv[1],'r', encoding='UTF-8')
new_m3u_str = sys.argv[1][:-4]+"_dump.m3u"
if (len(sys.argv)>2):
    new_m3u = sys.argv[2]
new_m3u = open(new_m3u_str,'w', encoding='utf_8_sig') 

new_m3u.writelines(ori_m3u.readline())#先复制第一行

for  line in  ori_m3u.readlines():
    if line[-1]==u'\n':
        line = line[:-1]
    if line[-3:]=="ncm":
        exe=ncmdump+' "'+line+'"'
        child = subprocess.Popen(exe, stderr=subprocess.PIPE)#那个ncmdump是通过stderr通道输出的，不是stdout
        child.wait()
        nout=u""
        for out in child.stderr.readlines():
            nout=out[20:-1].decode("UTF-8")#出来之后要将其编码
        print(nout)
        new_m3u.writelines(nout+u'\n')
    else :
        print(line)
        new_m3u.writelines(line+u'\n')
print("\n"+'*'*40+"\nSuccess! Already dump All *.ncm & Generate New m3u :"+new_m3u_str)