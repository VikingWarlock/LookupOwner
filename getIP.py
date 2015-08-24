# -*- coding: utf-8 -*-

__author__ = 'vkwk'
import re
import urllib
import sys
import socket

socket.setdefaulttimeout(0.5)

def getHtml(ip):
    try:
        page=urllib.urlopen('http://ip.chinaz.com/?IP='+ip)
        html=page.read()
        return html
    except socket.timeout:
        print "timeout.retry"
        return getHtml(ip)

def getInfo(html):
    reg=r'class="red">查询结果\[1\](.+?)<'
    r=re.compile(reg)
    itemlist=re.findall(r,html)
    return itemlist[0]


def search(ip):
    body=getHtml(ip)
    return getInfo(body)

def getIp(line):
    reg=r'client: (.+?),'
    r=re.compile(reg)
    try:
        itemlest=re.findall(r,line)
        return itemlest[0]
    except Exception:
        return "none"

def searchFile(filename):
    file1=open(filename)
    count=0
    for line in file1:
        count=count+1
        ip=getIp(line)
        if ip in searched:
            number=times[ip]
            number=number+1
            times[ip]=number
            continue
        if ip!="none":
            searched.append(ip)
            times[ip]=1
            res=search(ip)
            print str(count)+res

    print 'Search Complete!'

searched=[]
times={}
writeFile = None

if len(sys.argv)> 2:
    writeFile=sys.argv[2]

try:
    searchFile(sys.argv[1])
except KeyboardInterrupt:
    print ""
    print "scan result:"
    for ip in searched:
        print ip+' '+str(times[ip])+' times'