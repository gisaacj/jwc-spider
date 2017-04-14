# -*- coding=utf-8 -*-
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import http.cookiejar
import urllib.parse
import getpass

cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)

une=''
pwd=''
#une=input()
#pwd=getpass.getpass()

global pages
header={
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Connection':'keep-alive',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
        'Host':'sso.jwc.whut.edu.cn',
        'Referer':'http://sso.jwc.whut.edu.cn/Certification//toIndex.do',
        'Upgrade-Insecure-Requests':'1',
}
data={
        'systemId':'',
        'xmlmsg':'',
        'userName':une,
        'password':pwd,
        'type':'xs'
    }
data = urllib.parse.urlencode(data).encode('utf-8')
req = urllib.request.Request("http://sso.jwc.whut.edu.cn/Certification/login.do",headers=header,data=data)
html = urllib.request.urlopen(req)
bsObj = BeautifulSoup(html,"html.parser")
tab=bsObj.find('table',{'class':'mytable'})
l=len(tab.findAll('td'))/8-1
for i in range(int(l)):
    print((tab.findAll('td')[(i+1)*8]).get_text().replace(u'\xa0', u' ').encode('gbk').decode('gbk'))
header={
        'Host':'202.114.90.180',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Connection':'keep-alive',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
        'Referer':'http://sso.jwc.whut.edu.cn/Certification/login.do',
        'Upgrade-Insecure-Requests':'1',
}
req = urllib.request.Request("http://202.114.90.180/Score/",headers=header)
html = urllib.request.urlopen(req).geturl()
html = urllib.request.urlopen(html)
header={
        'Host':'202.114.90.180',
        'Accept':'*/*',
        'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Connection':'keep-alive',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
        'Upgrade-Insecure-Requests':'1',
        'X-Requested-With':'XMLHttpRequest'
}
req = urllib.request.Request("http://202.114.90.180/Score/lscjList.do",headers=header,data=urllib.parse.urlencode({'numPerPage':'20','temp':'true','xn':'','xnxq':'2016-2017-1'}).encode('utf-8'))
html = urllib.request.urlopen(req)
bsObj = BeautifulSoup(html,"html.parser")
tab=bsObj.find('table',{'class':"table"})
l=len(tab.findAll('td'))/13
for i in range(int(l)):
    print((tab.findAll('td')[i*13+2]).get_text().replace(u'\xa0', u' ').encode('gbk').decode('gbk')+':'+(tab.findAll('td')[i*13+5]).get_text().replace(u'\xa0', u' ').encode('gbk').decode('gbk'))
