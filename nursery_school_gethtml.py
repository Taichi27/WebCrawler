# coding: utf-8

from bs4 import BeautifulSoup
import urllib.request
from urllib.request import urlopen
from urllib.error import URLError
import re
import os
import datetime
import time











address = {"01":"Hokkaido","02":"Aomori","03":"Iwate","04":"Miyagi","05":"Akita","06":"Yamagata",
"07":"Fukushima","08":"Ibaraki","09":"Tochigi","10":"Gunma","11":"Saitama","12":"Chiba",
"13":"Tokyo","14":"Kanagawa","15":"Niigata","16":"Toyama","17":"Ishikawa","18":"Fukui",
"19":"Yamanashi","20":"Nagano","21":"Gifu","22":"Shizuoka","23":"Aichi","24":"Mie",
"25":"Shiga","26":"Kyoto","27":"Osaka","28":"Hyogo","29":"Nara","30":"Wakayama",
"31":"Tottori","32":"Shimane","33":"Okayama","34":"Hiroshima","35":"Yamaguchi","36":"Tokushima",
"37":"Kagawa","38":"Ehime","39":"Kouchi","40":"Fukuoka","41":"Saga","42":"Nagasaki","43":"Kumamoto",
"44":"Oita","45":"Miyazaki","46":"Kagoshima","47":"Okinawa"}


today = str(datetime.date.today())
replace_today = today.replace("-","")



if not os.path.exists("/nursery_school/"+replace_today+"nursery_school_html"+"/"):
    os.makedirs("/nursery_school/"+replace_today+"nursery_school_html"+"/")


for pref_num in ['01','02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15',
    '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32',
    '33', '34', '35', '36', '37', '38', '39', '40','41', '42', '43', '44', '45', '46', '47']:
    
    
    if not os.path.exists("/nursery_school/"+replace_today+"nursery_school_html"+"/"+replace_today+address[pref_num]+"/"):
        os.makedirs("/nursery_school/"+replace_today+"nursery_school_html"+"/"+replace_today+address[pref_num]+"/")

    
    city_urllist = []
    city_num = []


    get_url_for_city = "http://nursery.a-lot.jp/search"+str(pref_num)+".html"
    useragent = 'Mozilla/5.0'
    req = urllib.request.Request(get_url_for_city)
    req.add_header("User-agent",useragent)
    time.sleep(1)
    res = urllib.request.urlopen(req)
    soup = BeautifulSoup(res.read().decode('shift-jis'),"html.parser")
    select_soup = soup.find_all("select",{"name":"address2_cd"})

    
    if (select_soup):

        
        for option_soup in select_soup:
            option_num = option_soup.find_all('option')


            for opt in option_num:
                code = opt['value']
                city_num.append(code)
                print(code)


    for city_num_num in city_num:
        city_urllist.append("http://nursery.a-lot.jp/search"+str(pref_num)+"-"+str(city_num_num)+".html")

    
    for end_url in city_urllist:
        print(end_url)
        useragent = 'Mozilla/5.0'
        req = urllib.request.Request(end_url)
        req.add_header("User-agent",useragent)
        time.sleep(1)
        
        
        try:
            res = urllib.request.urlopen(req)
            soup = BeautifulSoup(res.read().decode('shift-jis',errors='ignore'),"html.parser")
            tr_soup = soup.findAll("tr",{"class":"v-bottom"})

            for a_soup in tr_soup:
                a_a_soup = a_soup.findAll("a",href=True)
                for get_links in a_a_soup:
                    get_links_get = get_links.get('href')
                    urlname = "http://nursery.a-lot.jp/"+str(get_links_get)
                    print(urlname)
                    "".join(urlname)
                    useragent = 'Mozilla/5.0'
                    req = urllib.request.Request(urlname)
                    req.add_header("Useragent",useragent)
                    time.sleep(1)
                    res = urllib.request.urlopen(req)
                    html = res.read().decode("shift-jis",errors='ignore')
                    filename = "/nursery_school/"+replace_today+"nursery_school_html"+"/"+replace_today+address[pref_num]+"/"+str(get_links_get)+".html"
                    htmlfile = open(filename,"w",encoding="shift-jis",errors="ignore")
                    htmlfile.write(html)
                    htmlfile.close()
                    print("end")

        
        except URLError as e:
            if hasattr(e, 'reason'):
                print('We failed to reach a server.')
                print('Reason: ', e.reason)

        
            elif hasattr(e, 'code'):
                print('The server could not fulfill the request.')
                print('Eroor code: ', e.code)
