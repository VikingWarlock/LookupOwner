# -*- coding: utf-8 -*-

__author__ = 'vkwk'
import re
import sys
import json
import requests


reload(sys)
sys.setdefaultencoding('utf8')


def getHtml(ip):
        # print ip
        page = requests.get('http://ip.taobao.com/service/getIpInfo.php?ip=' + ip)
        if page.status_code==200:
            return page.content
        else:
            # print page.status_code
            return getHtml(ip)


def getInfo(html):
    try:
        dic=json.loads(html)
        country=dic["data"]["country"]
        region=dic["data"]["region"]
        city=dic["data"]["city"]
        isp=dic["data"]["isp"]
        address=dic["data"]["ip"]
        res= address+' -> '+country+region+city+isp
        if fileToWrite != None:
            fileToWrite.write(str(res)+"\n")
        return res
    except Exception,e:
        print e
        return html

def search(ip):
    body = getHtml(ip)
    return getInfo(body)


def getIp(line):
    # reg = r'client: (.+?),'
    # if regTag == True:
    #     reg = r'(.+?) \- '
    # r = re.compile(reg)
    reg = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
    r=re.compile(reg)
    try:
        itemlest = re.findall(r, line)
        item = itemlest[0]
        return item
    except IndexError:
        return line


def searchFile(filename):
    file1 = open(filename)
    allCount = len(open(filename,'rU').readlines())
    lineCount=0
    for line in file1:
        lineCount = lineCount + 1
        ip = getIp(line)
        if ip in searched:
            number = times[ip]
            number = number + 1
            times[ip] = number
            continue
        if ip != "none":
            searched.append(ip)
            times[ip] = 1
            res = search(ip)
            percent=lineCount*1.0/allCount*100
            print '['+str(lineCount) +']: '+ res + " 完成:"+str(round(percent,2))+"%"

    print 'Search Complete!'
    if fileToWrite != None:
        fileToWrite.close()
    file1.close()

searched = []
times = {}
writeFile = None
regTag = True
startLine=0
fileToWrite = None

if len(sys.argv) > 2:
    startLine = sys.argv[2]

if len(sys.argv) > 3:
    writeFile = sys.argv[3]
    fileToWrite=open(writeFile,'w')


try:
    searchFile(sys.argv[1])
except KeyboardInterrupt:
    print ""
    print "scan result:"
    for ip in searched:
        print ip + ' ' + str(times[ip]) + ' times'
