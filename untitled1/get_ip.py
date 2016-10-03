# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import pymongo

client = pymongo.MongoClient('localhost', 27017)
ip = client['ip']
ip_url = ip['ip_url']

data = requests.get('http://www.youdaili.net/Daili/http/4797.html')
soup = BeautifulSoup(data.text, 'lxml')
ip_list = soup.select('body > div.container > div.content_full > div > div.content_newslist > div.newsdetail_cont > div.cont_font > p')
daili_ip_list = str(ip_list[0]).split('<br/>')[1: -1]
ip = [i.split('\n')[1] for i in daili_ip_list]
str_ip = [i.split('@')[0] for i in ip]


if __name__ == '__main__':
    print daili_ip_list
    print ip
    print str_ip, '\n', len(str_ip)
    for i in str_ip:
        ip_url.insert_one({'url': i})






'''
body > div.container > div.content_full > div > div.content_newslist > div.newsdetail_cont > div.cont_font > p > br:nth-child(1)
[<p><br/>\r\n121.41.110.73:8080@HTTP#\xe6\xb5\x99\xe6\xb1\x9f\xe7\x9c\x81\xe6\x9d\xad\xe5\xb7\x9e\xe5\xb8\x82 \xe9\x98\xbf\xe9\x87\x8c\xe4\xba\x91BGP\xe6\x95\xb0\xe6\x8d\xae\xe4\xb8\xad\xe5\xbf\x83<br/>\r\n121.69.25.58:8118@HTTP#\xe3\x80\x90\xe5\x8c\xbf\xe3\x80\x91\xe5\x8c\x97\xe4\xba\xac\xe5\xb8\x82 \xe5\x8c\x97\xe4\xba\xac\xe5\xae\xbd\xe5\xb8\xa6\xe9\x80\x9a\xe7\x94\xb5\xe4\xbf\xa1\xe6\x8a\x80\xe6\x9c\xaf\xe6\x9c\x89\xe9\x99\x90\xe5\x85\xac\xe5\x8f\xb8<br/>\r\n122.72.18.160:80@HTTP#\xe5\x8c\x97\xe4\xba\xac\xe5\xb8\x82 \xe9\x93\x81\xe9\x80\x9a\xe6\x95\xb0\xe6\x8d\xae\xe4\xb8\xad\xe5\xbf\x83<br/>\r\n122.96.59.102:81@HTTP#\xe3\x80\x90\xe5\x8c\xbf\xe3\x80\x91\xe6\xb1\x9f\xe8\x8b\x8f\xe7\x9c\x81\xe5\x8d\x97\xe4\xba\xac\xe5\xb8\x82 \xe8\x81\x94\xe9\x80\x9a<br/>\r\n122.96.59.102:82@HTTP#\xe6\xb1\x9f\xe8\x8b\x8f\xe7\x9c\x81\xe5\x8d\x97\xe4\xba\xac\xe5\xb8\x82 \xe8\x81\x94\xe9\x80\x9a<br/>\r\n122.96.59.102:843@HTTP#\xe3\x80\x90\xe5\x8c\xbf\xe3\x80\x91\xe6\xb1\x9f\xe8\x8b\x8f\xe7\x9c\x81\xe5\x8d\x97\xe4\xba\xac\xe5\xb8\x82 \xe8\x81\x94\xe9\x80\x9a<br/>\r\n122.96.59.105:80@HTTP#\xe3\x80\x90\xe5\x8c\xbf\xe3\x80\x91\xe6\xb1\x9f\xe8\x8b\x8f\xe7\x9c\x81\xe5\x8d\x97\xe4\xba\xac\xe5\xb8\x82 \xe8\x81\x94\xe9\x80\x9a<br/>\r\n122.96.59.105:81@HTTP#\xe3\x80\x90\xe5\x8c\xbf\xe3\x80\x91\xe6\xb1\x9f\xe8\x8b\x8f\xe7\x9c\x81\xe5\x8d\x97\xe4\xba\xac\xe5\xb8\x82 \xe8\x81\x94\xe9\x80\x9a<br/>\r\n122.96.59.105:82@HTTP#\xe6\xb1\x9f\xe8\x8b\x8f\xe7\x9c\x81\xe5\x8d\x97\xe4\xba\xac\xe5\xb8\x82 \xe8\x81\x94\xe9\x80\x9a<br/>\r\n122.96.59.105:83@HTTP#\xe3\x80\x90\xe5\x8c\xbf\xe3\x80\x91\xe6\xb1\x9f\xe8\x8b\x8f\xe7\x9c\x81\xe5\x8d\x97\xe4\xba\xac\xe5\xb8\x82 \xe8\x81\x94\xe9\x80\x9a<br/>\r\n122.96.59.106:82@HTTP#\xe3\x80\x90\xe5\x8c\xbf\xe3\x80\x91\xe6\xb1\x9f\xe8\x8b\x8f\xe7\x9c\x81\xe5\x8d\x97\xe4\xba\xac\xe5\xb8\x82 \xe8\x81\x94\xe9\x80\x9a<br/>\r\n122.96.59.106:843@HTTP#\xe3\x80\x90\xe5\x8c\xbf\xe3\x80\x91\xe6\xb1\x9f\xe8\x8b\x8f\xe7\x9c\x81\xe5\x8d\x97\xe4\xba\xac\xe5\xb8\x82 \xe8\x81\x94\xe9\x80\x9a<br/>\r\n122.224.209.98:3128@HTTP#\xe6\xb5\x99\xe6\xb1\x9f\xe7\x9c\x81\xe6\x9d\xad\xe5\xb7\x9e\xe5\xb8\x82 \xe7\x94\xb5\xe4\xbf\xa1<br/>\r\n122.226.141.67:3128@HTTP#\xe6\xb5\x99\xe6\xb1\x9f\xe7\x9c\x81\xe5\x8f\xb0\xe5\xb7\x9e\xe5\xb8\x82 \xe7\x94\xb5\xe4\xbf\xa1<br/>\r\n122.226.203.70:3128@HTTP#\xe6\xb5\x99\xe6\xb1\x9f\xe7\x9c\x81\xe9\x87\x91\xe5\x8d\x8e\xe5\xb8\x82 \xe7\x94\xb5\xe4\xbf\xa1<br/>\r\n122.227.171.22:9797@HTTP#\xe6\xb5\x99\xe6\xb1\x9f\xe7\x9c\x81\xe5\xae\x81\xe6\xb3\xa2\xe5\xb8\x82 \xe7\x94\xb5\xe4\xbf\xa1<br/>\r\n123.56.28.196:8888@HTTP#\xe5\x8c\x97\xe4\xba\xac\xe5\xb8\x82 \xe9\x98\xbf\xe9\x87\x8c\xe4\xba\x91BGP\xe6\x95\xb0\xe6\x8d\xae\xe4\xb8\xad\xe5\xbf\x83<br/>\r\n123.124.168.149:80@HTTP#\xe3\x80\x90\xe5\x8c\xbf\xe3\x80\x91\xe5\x8c\x97\xe4\xba\xac\xe5\xb8\x82 \xe8\x81\x94\xe9\x80\x9a<br/>\r\n123.125.226.132:9999@HTTP#\xe5\x8c\x97\xe4\xba\xac\xe5\xb8\x82 \xe8\x81\x94\xe9\x80\x9a<br/>\r\n123.139.59.242:9999@HTTP#\xe9\x99\x95\xe8\xa5\xbf\xe7\x9c\x81\xe8\xa5\xbf\xe5\xae\x89\xe5\xb8\x82 \xe8\x81\x94\xe9\x80\x9a<br/>\r\n123.146.128.15:3128@HTTP#\xe9\x87\x8d\xe5\xba\x86\xe5\xb8\x82 \xe8\x81\x94\xe9\x80\x9a<br/>\r\n123.157.99.139:3128@HTTP#\xe6\xb5\x99\xe6\xb1\x9f\xe7\x9c\x81\xe8\xa1\xa2\xe5\xb7\x9e\xe5\xb8\x82 \xe8\x81\x94\xe9\x80\x9a<br/>\r\n124.88.67.30:80@HTTP#\xe3\x80\x90\xe5\x8c\xbf\xe3\x80\x91\xe6\x96\xb0\xe7\x96\x86\xe4\xb9\x8c\xe9\xb2\x81\xe6\x9c\xa8\xe9\xbd\x90\xe5\xb8\x82 \xe8\x81\x94\xe9\x80\x9a<br/>\r\n124.206.56.125:3128@HTTP#\xe5\x8c\x97\xe4\xba\xac\xe5\xb8\x82 \xe7\x94\xb5\xe4\xbf\xa1\xe9\x80\x9a<br/>\r\n124.206.119.123:3128@HTTP#\xe5\x8c\x97\xe4\xba\xac\xe5\xb8\x82 \xe7\x94\xb5\xe4\xbf\xa1\xe9\x80\x9a<br/>\r\n124.206.133.227:80@HTTP#\xe5\x8c\x97\xe4\xba\xac\xe5\xb8\x82 \xe7\x94\xb5\xe4\xbf\xa1\xe9\x80\x9a<br/>\r\n124.244.77.129:80@HTTP#\xe3\x80\x90\xe5\x8c\xbf\xe3\x80\x91\xe9\xa6\x99\xe6\xb8\xaf \xe5\x9f\x8e\xe5\xb8\x82\xe7\x94\xb5\xe8\xae\xaf\xe6\x9c\x89\xe9\x99\x90\xe5\x85\xac\xe5\x8f\xb8<br/>\r\n125.65.112.201:8008@HTTP#\xe3\x80\x90\xe5\x8c\xbf\xe3\x80\x91\xe5\x9b\x9b\xe5\xb7\x9d\xe7\x9c\x81\xe7\xbb\xb5\xe9\x98\xb3\xe5\xb8\x82 \xe7\x94\xb5\xe4\xbf\xa1<br/>\r\n125.217.199.148:80@HTTP#\xe3\x80\x90\xe5\x8c\xbf\xe3\x80\x91[C]\xe5\xb9\xbf\xe4\xb8\x9c\xe7\x9c\x81\xe5\xb9\xbf\xe5\xb7\x9e\xe5\xb8\x82 \xe5\xb9\xbf\xe4\xb8\x9c\xe5\xa4\x96\xe8\xaf\xad\xe8\x89\xba\xe6\x9c\xaf\xe8\x81\x8c\xe4\xb8\x9a\xe5\xad\xa6\xe9\x99\xa2<br/>\r\n125.253.32.158:3128@HTTP#\xe6\xbe\xb3\xe5\xa4\xa7\xe5\x88\xa9\xe4\xba\x9a<br/>\r\n130.94.148.99:80@HTTP#\xe7\xbe\x8e\xe5\x9b\xbd \xe7\xa7\x91\xe7\xbd\x97\xe6\x8b\x89\xe5\xa4\x9a\xe5\xb7\x9e\xe9\x98\xbf\xe6\x8b\x89\xe5\xb8\x95\xe9\x9c\x8d\xe5\x8e\xbf\xe6\xa0\xbc\xe6\x9e\x97\xe4\xbc\x8d\xe5\xbe\xb7\xe6\x9d\x91\xe5\xb8\x82NTT\xe7\xbe\x8e\xe5\x9b\xbd\xe8\x82\xa1\xe4\xbb\xbd\xe6\x9c\x89\xe9\x99\x90\xe5\x85\xac\xe5\x8f\xb8<br/>\r\n131.108.164.124:8080@HTTP#\xe5\x8c\x97\xe7\xbe\x8e\xe5\x9c\xb0\xe5\x8c\xba<br/>\r\n134.196.214.127:3128@HTTP#\xe4\xb8\xad\xe5\x9b\xbd<br/>\r\n137.135.166.225:8118@HTTP#\xe3\x80\x90\xe5\x8c\xbf\xe3\x80\x91\xe6\xac\xa7\xe6\xb4\xb2 Microsoft\xe5\x85\xac\xe5\x8f\xb8<br/>\r\n137.135.166.225:8123@HTTP#\xe3\x80\x90\xe5\x8c\xbf\xe3\x80\x91\xe6\xac\xa7\xe6\xb4\xb2 Microsoft\xe5\x85\xac\xe5\x8f\xb8<br/>\r\n137.135.166.225:8128@HTTP#\xe3\x80\x90\xe5\x8c\xbf\xe3\x80\x91\xe6\xac\xa7\xe6\xb4\xb2 Microsoft\xe5\x85\xac\xe5\x8f\xb8<br/>\r\n138.0.24.242:8080@HTTP<br/>\r\n138.0.89.102:8080@HTTP<br/>\r\n138.94.155.201:8080@HTTP#\xe5\x8c\x97\xe7\xbe\x8e\xe5\x9c\xb0\xe5\x8c\xba<br/>\r\n144.76.232.58:3128@HTTP#\xe5\xbe\xb7\xe5\x9b\xbd<br/>\r\n150.107.149.56:8080@HTTP#\xe6\xac\xa7\xe6\xb4\xb2<br/>\r\n154.65.4.90:8080@HTTP#\xe9\x9d\x9e\xe6\xb4\xb2<br/>\r\n154.73.44.113:8080@HTTP#\xe9\x9d\x9e\xe6\xb4\xb2<br/>\r\n154.73.220.137:8080@HTTP#\xe9\x9d\x9e\xe6\xb4\xb2<br/>\r\n162.223.88.243:80@HTTP#\xe5\x8c\x97\xe7\xbe\x8e\xe5\x9c\xb0\xe5\x8c\xba<br/>\r\n177.5.219.112:8080@HTTP#\xe5\xb7\xb4\xe8\xa5\xbf<br/>\r\n177.22.111.113:3128@HTTP#\xe5\xb7\xb4\xe8\xa5\xbf<br/>\r\n177.39.186.59:8008@HTTP#\xe5\xb7\xb4\xe8\xa5\xbf<br/>\r\n177.43.212.44:3128@HTTP#\xe5\xb7\xb4\xe8\xa5\xbf<br/>\r\n177.74.117.142:3128@HTTP#\xe5\xb7\xb4\xe8\xa5\xbf<br/>\r\n177.87.72.1:8081@HTTP#\xe5\xb7\xb4\xe8\xa5\xbf<br/>\r\n177.87.241.226:8080@HTTP#\xe3\x80\x90\xe5\x8c\xbf\xe3\x80\x91\xe5\xb7\xb4\xe8\xa5\xbf<br/>\r\n177.130.59.66:3128@HTTP#\xe5\xb7\xb4\xe8\xa5\xbf<br/>\r\n177.189.240.163:3128@HTTP#\xe5\xb7\xb4\xe8\xa5\xbf<br/>\r\n178.18.32.137:8080@HTTP#\xe6\x91\xa9\xe5\xb0\x94\xe5\xa4\x9a\xe7\x93\xa6<br/>\r\n178.22.148.122:3129@HTTP#\xe6\xb3\x95\xe5\x9b\xbd<br/>\r\n178.34.176.86:8080@HTTP#\xe4\xbf\x84\xe7\xbd\x97\xe6\x96\xaf<br/>\r\n179.96.255.28:8080@HTTP#\xe5\xb7\xb4\xe8\xa5\xbf<br/>\r\n180.250.163.34:8888@HTTP#\xe5\x8d\xb0\xe5\xba\xa6\xe5\xb0\xbc\xe8\xa5\xbf\xe4\xba\x9a<br/>\r\n180.250.212.242:8080@HTTP#\xe5\x8d\xb0\xe5\xba\xa6\xe5\xb0\xbc\xe8\xa5\xbf\xe4\xba\x9a<br/>\r\n181.62.252.85:8081@HTTP#\xe5\x93\xa5\xe4\xbc\xa6\xe6\xaf\x94\xe4\xba\x9a<br/>\r\n181.143.9.91:8080@HTTP#\xe5\x93\xa5\xe4\xbc\xa6\xe6\xaf\x94\xe4\xba\x9a<br/>\r\n181.229.140.11:8085@HTTP#\xe9\x98\xbf\xe6\xa0\xb9\xe5\xbb\xb7<br/>\r\n182.23.52.252:80@HTTP#\xe5\x8d\xb0\xe5\xba\xa6\xe5\xb0\xbc\xe8\xa5\xbf\xe4\xba\x9a<br/>\r\n183.61.236.53:3128@HTTP#\xe3\x80\x90\xe5\x8c\xbf\xe3\x80\x91\xe5\xb9\xbf\xe4\xb8\x9c\xe7\x9c\x81\xe4\xb8\x9c\xe8\x8e\x9e\xe5\xb8\x82 \xe7\x94\xb5\xe4\xbf\xa1<br/>\r\n183.61.236.55:3128@HTTP#\xe3\x80\x90\xe5\x8c\xbf\xe3\x80\x91\xe5\xb9\xbf\xe4\xb8\x9c\xe7\x9c\x81\xe4\xb8\x9c\xe8\x8e\x9e\xe5\xb8\x82 \xe7\x94\xb5\xe4\xbf\xa1<br/>\r\n183.62.9.84:8080@HTTP#\xe5\xb9\xbf\xe4\xb8\x9c\xe7\x9c\x81\xe5\xb9\xbf\xe5\xb7\x9e\xe5\xb8\x82 \xe7\x94\xb5\xe4\xbf\xa1<br/>\r\n183.62.58.250:9797@HTTP#\xe5\xb9\xbf\xe4\xb8\x9c\xe7\x9c\x81\xe5\xb9\xbf\xe5\xb7\x9e\xe5\xb8\x82 \xe7\x94\xb5\xe4\xbf\xa1<br/>\r\n183.131.151.208:80@HTTP#\xe6\xb5\x99\xe6\xb1\x9f\xe7\x9c\x81\xe6\xb8\xa9\xe5\xb7\x9e\xe5\xb8\x82 \xe7\x94\xb5\xe4\xbf\xa1<br/>\r\n183.239.167.122:8080@HTTP#\xe3\x80\x90\xe5\x8c\xbf\xe3\x80\x91\xe5\xb9\xbf\xe4\xb8\x9c\xe7\x9c\x81 \xe7\xa7\xbb\xe5\x8a\xa8<br/>\r\n184.69.67.122:80@HTTP#\xe3\x80\x90\xe5\x8c\xbf\xe3\x80\x91\xe5\x8a\xa0\xe6\x8b\xbf\xe5\xa4\xa7<br/>\r\n186.10.5.140:8080@HTTP#\xe6\x99\xba\xe5\x88\xa9<br/>\r\n186.67.158.43:3128@HTTP#\xe6\x99\xba\xe5\x88\xa9<br/>\r\n186.103.169.164:8080@HTTP#\xe6\x99\xba\xe5\x88\xa9<br/>\r\n186.226.252.203:3128@HTTP#\xe5\xb7\xb4\xe8\xa5\xbf<br/>\r\n186.250.96.66:8080@HTTP#\xe5\xb7\xb4\xe8\xa5\xbf<br/>\r\n187.45.112.5:3128@HTTP#\xe5\xb7\xb4\xe8\xa5\xbf<br/>\r\n187.60.40.113:8080@HTTP#\xe5\xb7\xb4\xe8\xa5\xbf<br/>\r\n187.60.170.22:3128@HTTP#\xe5\xb7\xb4\xe8\xa5\xbf<br/>\r\n189.7.33.134:3129@HTTP#\xe5\xb7\xb4\xe8\xa5\xbf<br/>\r\n189.85.20.21:8080@HTTP#\xe5\xb7\xb4\xe8\xa5\xbf<br/>\r\n190.3.127.21:80@HTTP#\xe3\x80\x90\xe5\x8c\xbf\xe3\x80\x91\xe9\x98\xbf\xe6\xa0\xb9\xe5\xbb\xb7<br/>\r\n190.82.94.13:80@HTTP#\xe3\x80\x90\xe5\x8c\xbf\xe3\x80\x91\xe6\x99\xba\xe5\x88\xa9<br/>\r\n190.144.241.197:3128@HTTP#\xe5\x93\xa5\xe4\xbc\xa6\xe6\xaf\x94\xe4\xba\x9a<br/>\r\n190.151.10.226:8080@HTTP#\xe6\x99\xba\xe5\x88\xa9<br/>\r\n190.181.18.232:80@HTTP#\xe7\x8e\xbb\xe5\x88\xa9\xe7\xbb\xb4\xe4\xba\x9a<br/>\r\n190.221.23.158:80@HTTP#\xe3\x80\x90\xe5\x8c\xbf\xe3\x80\x91\xe9\x98\xbf\xe6\xa0\xb9\xe5\xbb\xb7<br/>\r\n190.228.33.114:8080@HTTP#\xe9\x98\xbf\xe6\xa0\xb9\xe5\xbb\xb7<br/>\r\n190.248.135.134:8080@HTTP#\xe5\x93\xa5\xe4\xbc\xa6\xe6\xaf\x94\xe4\xba\x9a<br/>\r\n191.5.114.138:8080@HTTP#\xe6\x8b\x89\xe7\xbe\x8e\xe5\x9c\xb0\xe5\x8c\xba<br/>\r\n192.99.160.45:8080@HTTP#\xe5\x8a\xa0\xe6\x8b\xbf\xe5\xa4\xa7 \xe9\xad\x81\xe5\x8c\x97\xe5\x85\x8b\xe7\x9c\x81\xe8\x92\x99\xe7\x89\xb9\xe5\x88\xa9\xe5\xb0\x94\xe5\xb8\x82OVH\xe6\x95\xb0\xe6\x8d\xae\xe4\xb8\xad\xe5\xbf\x83<br/>\r\n193.179.1.114:8080@HTTP#\xe6\x8d\xb7\xe5\x85\x8b<br/>\r\n193.194.87.227:8080@HTTP#\xe9\x98\xbf\xe5\xb0\x94\xe5\x8f\x8a\xe5\x88\xa9\xe4\xba\x9a<br/>\r\n194.85.37.90:3128@HTTP#[C]\xe4\xbf\x84\xe7\xbd\x97\xe6\x96\xaf Moscow State University<br/>\r\n195.34.238.154:8080@HTTP#\xe4\xbf\x84\xe7\xbd\x97\xe6\x96\xaf<br/>\r\n195.177.126.149:8080@HTTP#\xe4\xb9\x8c\xe5\x85\x8b\xe5\x85\xb0<br/>\r\n196.11.90.57:8080@HTTP#\xe9\x9d\x9e\xe6\xb4\xb2<br/>\r\n197.210.246.30:8080@HTTP#\xe5\xb0\xbc\xe6\x97\xa5\xe5\x88\xa9\xe4\xba\x9a<br/>\r\n197.211.45.4:8080@HTTP#\xe5\xb0\xbc\xe6\x97\xa5\xe5\x88\xa9\xe4\xba\x9a<br/>\r\n197.243.50.242:3129@HTTP#\xe5\x8d\xa2\xe6\x97\xba\xe8\xbe\xbe<br/>\r\n198.50.211.54:80@HTTP#\xe3\x80\x90\xe5\x8c\xbf\xe3\x80\x91\xe5\x8a\xa0\xe6\x8b\xbf\xe5\xa4\xa7<br/>\r\n200.46.86.66:3128@HTTP#\xe5\xb7\xb4\xe6\x8b\xbf\xe9\xa9\xac<br/>\r\n200.61.47.14:3128@HTTP#\xe9\x98\xbf\xe6\xa0\xb9\xe5\xbb\xb7<br/>\r\n200.85.59.198:3128@HTTP#\xe5\xb7\xb4\xe6\x8b\x89\xe5\x9c\xad<br/>\r\n200.87.139.101:8080@HTTP#\xe7\x8e\xbb\xe5\x88\xa9\xe7\xbb\xb4\xe4\xba\x9a<br/>\r\n200.150.68.126:3128@HTTP#\xe5\xb7\xb4\xe8\xa5\xbf \xe5\x9c\xa3\xe4\xbf\x9d\xe7\xbd\x97<br/>\r\n201.159.19.141:8080@HTTP#\xe5\xa2\xa8\xe8\xa5\xbf\xe5\x93\xa5<br/>\r\n202.29.221.90:3128@HTTP#[C]\xe6\xb3\xb0\xe5\x9b\xbd Inter-university network<br/>\r\n202.29.233.110:3128@HTTP#[C]\xe6\xb3\xb0\xe5\x9b\xbd Inter-university network<br/>\r\n202.69.38.82:8080@HTTP#\xe5\xb7\xb4\xe5\x9f\xba\xe6\x96\xaf\xe5\x9d\xa6<br/>\r\n202.77.57.124:3128@HTTP#\xe3\x80\x90\xe5\x8c\xbf\xe3\x80\x91\xe9\xa6\x99\xe6\xb8\xaf \xe7\x89\xb9\xe5\x88\xab\xe8\xa1\x8c\xe6\x94\xbf\xe5\x8c\xba<br/>\r\n202.78.206.70:8080@HTTP#\xe5\x8d\xb0\xe5\xba\xa6\xe5\xb0\xbc\xe8\xa5\xbf\xe4\xba\x9a<br/>\r\n202.78.206.81:8080@HTTP#\xe5\x8d\xb0\xe5\xba\xa6\xe5\xb0\xbc\xe8\xa5\xbf\xe4\xba\x9a<br/>\r\n202.99.172.165:8081@HTTP#\xe6\xb2\xb3\xe5\x8c\x97\xe7\x9c\x81\xe9\x82\xa2\xe5\x8f\xb0\xe5\xb8\x82 \xe8\x81\x94\xe9\x80\x9a<br/>\r\n202.100.167.142:80@HTTP#\xe6\x96\xb0\xe7\x96\x86\xe4\xb9\x8c\xe9\xb2\x81\xe6\x9c\xa8\xe9\xbd\x90\xe5\xb8\x82 \xe7\x94\xb5\xe4\xbf\xa1<br/>\r\n202.100.167.144:80@HTTP#\xe6\x96\xb0\xe7\x96\x86\xe4\xb9\x8c\xe9\xb2\x81\xe6\x9c\xa8\xe9\xbd\x90\xe5\xb8\x82 \xe7\x94\xb5\xe4\xbf\xa1<br/>\r\n202.100.167.145:80@HTTP#\xe6\x96\xb0\xe7\x96\x86\xe4\xb9\x8c\xe9\xb2\x81\xe6\x9c\xa8\xe9\xbd\x90\xe5\xb8\x82 \xe7\x94\xb5\xe4\xbf\xa1<br/>\r\n202.100.167.149:80@HTTP#\xe6\x96\xb0\xe7\x96\x86\xe4\xb9\x8c\xe9\xb2\x81\xe6\x9c\xa8\xe9\xbd\x90\xe5\xb8\x82 \xe7\x94\xb5\xe4\xbf\xa1<br/>\r\n202.100.167.159:80@HTTP#\xe6\x96\xb0\xe7\x96\x86\xe4\xb9\x8c\xe9\xb2\x81\xe6\x9c\xa8\xe9\xbd\x90\xe5\xb8\x82 \xe7\x94\xb5\xe4\xbf\xa1<br/>\r\n202.100.167.160:80@HTTP#\xe6\x96\xb0\xe7\x96\x86\xe4\xb9\x8c\xe9\xb2\x81\xe6\x9c\xa8\xe9\xbd\x90\xe5\xb8\x82 \xe7\x94\xb5\xe4\xbf\xa1<br/>\r\n202.100.167.180:80@HTTP#\xe6\x96\xb0\xe7\x96\x86\xe4\xb9\x8c\xe9\xb2\x81\xe6\x9c\xa8\xe9\xbd\x90\xe5\xb8\x82 \xe7\x94\xb5\xe4\xbf\xa1<br/>\r\n202.105.179.164:3128@HTTP#\xe5\xb9\xbf\xe4\xb8\x9c\xe7\x9c\x81\xe7\x8f\xa0\xe6\xb5\xb7\xe5\xb8\x82 \xe7\x94\xb5\xe4\xbf\xa1IDC\xe6\x9c\xba\xe6\x88\xbf<br/>\r\n202.106.16.36:3128@HTTP#\xe5\x8c\x97\xe4\xba\xac\xe5\xb8\x82 \xe8\x81\x94\xe9\x80\x9a<br/>\r\n202.137.15.93:8080@HTTP#\xe5\x8d\xb0\xe5\xba\xa6\xe5\xb0\xbc\xe8\xa5\xbf\xe4\xba\x9a<br/>\r\n202.148.4.26:8080@HTTP#\xe5\x8d\xb0\xe5\xba\xa6\xe5\xb0\xbc\xe8\xa5\xbf\xe4\xba\x9a<br/>\r\n202.159.6.98:8080@HTTP#\xe5\x8d\xb0\xe5\xba\xa6\xe5\xb0\xbc\xe8\xa5\xbf\xe4\xba\x9a<br/>\r\n202.159.42.246:3128@HTTP#\xe3\x80\x90\xe5\x8c\xbf\xe3\x80\x91\xe5\x8d\xb0\xe5\xba\xa6\xe5\xb0\xbc\xe8\xa5\xbf\xe4\xba\x9a<br/>\r\n202.167.248.186:80@HTTP#\xe3\x80\x90\xe5\x8c\xbf\xe3\x80\x91\xe6\x96\xb0\xe5\x8a\xa0\xe5\x9d\xa1<br/>\r\n202.179.184.66:8080@HTTP#\xe5\x8d\xb0\xe5\xba\xa6\xe5\xb0\xbc\xe8\xa5\xbf\xe4\xba\x9a<br/>\r\n203.88.170.183:8080@HTTP#\xe3\x80\x90\xe5\x8c\xbf\xe3\x80\x91\xe9\xa6\x99\xe6\xb8\xaf i-Care\xe5\xae\xbd\xe9\xa2\x91\xe7\x94\xa8\xe6\x88\xb7<br/>\r\n203.91.121.74:3128@HTTP#[C]\xe5\x8c\x97\xe4\xba\xac\xe5\xb8\x82 \xe6\xb8\x85\xe5\x8d\x8e\xe5\xa4\xa7\xe5\xad\xa6FIT\xe4\xb8\xad\xe5\xbf\x83<br/>\r\n203.114.110.83:8080@HTTP#\xe6\xb3\xb0\xe5\x9b\xbd \xe6\x9b\xbc\xe8\xb0\xb7TOT\xe5\x85\xac\xe5\x85\xb1\xe6\x9c\x89\xe9\x99\x90\xe5\x85\xac\xe5\x8f\xb8<br/>\r\n203.129.224.79:80@HTTP#\xe3\x80\x90\xe5\x8c\xbf\xe3\x80\x91\xe5\x8d\xb0\xe5\xba\xa6<br/>\r\n203.160.172.163:8090@HTTP#\xe8\x8f\xb2\xe5\xbe\x8b\xe5\xae\xbe \xe7\x94\xb5\xe6\x8a\xa5\xe7\x94\xb5\xe8\xaf\x9d\xe5\x85\xac\xe5\x8f\xb8\xe7\xbd\x91\xe7\xbb\x9c<br/>\r\n203.189.130.125:8080@HTTP#\xe6\x9f\xac\xe5\x9f\x94\xe5\xaf\xa8<br/>\r\n207.5.112.114:8080@HTTP#\xe7\xbe\x8e\xe5\x9b\xbd<br/>\r\n209.173.8.221:8080@HTTP#\xe3\x80\x90\xe5\x8c\xbf\xe3\x80\x91\xe7\xbe\x8e\xe5\x9b\xbd<br/>\r\n210.91.41.60:3128@HTTP#\xe9\x9f\xa9\xe5\x9b\xbd<br/>\r\n211.103.148.66:3128@HTTP#\xe5\x8c\x97\xe4\xba\xac\xe5\xb8\x82 \xe7\x94\xb5\xe4\xbf\xa1\xe9\x80\x9a<br/>\r\n211.218.126.189:3128@HTTP#\xe9\x9f\xa9\xe5\x9b\xbd KT\xe7\x94\xb5\xe4\xbf\xa1<br/>\r\n212.12.31.26:8080@HTTP#\xe4\xbf\x84\xe7\xbd\x97\xe6\x96\xaf<br/>\r\n212.46.199.10:8080@HTTP#\xe3\x80\x90\xe5\x8c\xbf\xe3\x80\x91\xe4\xbf\x84\xe7\xbd\x97\xe6\x96\xaf<br/>\r\n213.57.89.97:18000@HTTP#\xe3\x80\x90\xe5\x8c\xbf\xe3\x80\x91\xe4\xbb\xa5\xe8\x89\xb2\xe5\x88\x97<br/>\r\n213.57.90.10:18000@HTTP#\xe3\x80\x90\xe5\x8c\xbf\xe3\x80\x91\xe4\xbb\xa5\xe8\x89\xb2\xe5\x88\x97<br/>\r\n218.7.170.190:3128@HTTP#\xe9\xbb\x91\xe9\xbe\x99\xe6\xb1\x9f\xe7\x9c\x81\xe7\xbb\xa5\xe5\x8c\x96\xe5\xb8\x82 \xe8\x81\x94\xe9\x80\x9a<br/>\r\n218.29.237.206:3128@HTTP#\xe6\xb2\xb3\xe5\x8d\x97\xe7\x9c\x81\xe9\x83\x91\xe5\xb7\x9e\xe5\xb8\x82 \xe8\x81\x94\xe9\x80\x9a<br/>\r\n218.32.94.77:8080@HTTP#\xe3\x80\x90\xe5\x8c\xbf\xe3\x80\x91\xe5\x8f\xb0\xe6\xb9\xbe\xe7\x9c\x81\xe5\x8f\xb0\xe5\x8c\x97\xe5\xb8\x82 \xe6\x96\xb0\xe4\xb8\x96\xe7\xba\xaa\xe8\xb5\x84\xe9\x80\x9a\xe8\x82\xa1\xe4\xbb\xbd\xe6\x9c\x89\xe9\x99\x90\xe5\x85\xac\xe5\x8f\xb8<br/>\r\n218.56.132.157:8080@HTTP#\xe5\xb1\xb1\xe4\xb8\x9c\xe7\x9c\x81\xe4\xb8\xb4\xe6\xb2\x82\xe5\xb8\x82 \xe8\x81\x94\xe9\x80\x9a<br/>\r\n218.90.174.167:3128@HTTP#[C]\xe6\xb1\x9f\xe8\x8b\x8f\xe7\x9c\x81\xe6\x97\xa0\xe9\x94\xa1\xe5\xb8\x82 \xe7\xa7\x91\xe6\x8a\x80\xe8\x81\x8c\xe4\xb8\x9a\xe5\xad\xa6\xe9\x99\xa2<br/>\n</p>]
'''