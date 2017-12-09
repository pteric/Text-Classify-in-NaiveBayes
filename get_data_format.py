#!/usr/bin/python
# -*- coding:utf-8 -*-  
  
import os  
from xml.dom import minidom  
from urlparse import urlparse  
import codecs  
import importlib,sys
  
def file_fill(file_dir): #得到文本.txt的路径
    count = 0
    for root, dirs, files in os.walk(file_dir):
        for f in files:
            tmp_dir ='/Users/pengtuo/Downloads/allsites_after/' + f  # 加上标签后的文本
            text_init_dir = file_dir + '/' + f  #原始文本
            file_source = open(text_init_dir, 'r')  
            ok_file = open(tmp_dir, 'a+')
            start = '<docs>\n'
            end = '</docs>'
            line_content = file_source.readlines()
            ok_file.write(start)
            for lines in line_content:
                text = lines.replace('&', '')
                ok_file.write(text)
            ok_file.write(end)  
  
            file_source.close()  
            ok_file.close()


def sougou_file_read(file_dir): #得到文本.txt的路径
    text_count  = 0
    for root, dirs, files in os.walk(file_dir):  
        for f in files:  
            tmp_file = file_dir + "/" + f
            print '-' * 25
            print 'Dealing with %s' % f
            try:
                doc = minidom.parse(tmp_file)
                root = doc.documentElement
                claimtitle = root.getElementsByTagName("contenttitle")
                claimtext = root.getElementsByTagName("content")  
                claimurl = root.getElementsByTagName("url")  
                for index in range(0, len(claimurl)):
                    if (claimtext[index].firstChild == None or claimtitle[index].firstChild == None):  
                        continue
                    claim_url = claimurl[index].firstChild.data
                    url = urlparse(claim_url)
                    if dicurl.has_key(url.hostname):
                        file_url = path + dicurl[url.hostname]
                        if not os.path.exists(file_url):
                            os.makedirs(file_url)
                        fp_in = file(file_url + "/%d.txt" % (len(os.listdir(path + dicurl[url.hostname])) + 1),"w")
                        fp_in.write((claimtitle[index].firstChild.data).encode('utf8'))
                        fp_in.write((claimtext[index].firstChild.data).encode('utf8'))                
            except (xml.parsers.expat.ExpatError, NameError) as e:
                print '*' * 40
                print 'Whoops, there is an error ---->', e
                print '*' * 40
            else:
                text_count += 1
                print "Successed! %s has been writen, no.%d " % (f, text_count)
            print '-' * 25


if __name__=="__main__":
    file_fill("/Users/pengtuo/Downloads/allsites_all")
    
    path = "/Users/pengtuo/Downloads/allsites_classification/"

    #建立url和类别的映射词典  
    dicurl_sohu = { 
        'auto.sohu.com':'qiche',
        'it.sohu.com':'it',
        'health.sohu.com':'jiankang',
        'sports.sohu.com':'tiyu',
        'travel.sohu.com':'lvyou',
        'learning.sohu.com':'jiaoyu',
        'career.sohu.com':'zhaopin',
        'cul.sohu.com':'wenhua',
        'mil.news.sohu.com':'junshi',
        'house.sohu.com':'fangchan',
        'yule.sohu.com':'yule',
        'women.sohu.com':'shishang',
        'media.sohu.com':'chuanmei',
        'gongyi.sohu.com':'gongyi',
        '2008.sohu.com':'aoyun',
        'business.sohu.com': 'shangye'
    }
 
    sougou_file_read("/Users/pengtuo/Downloads/sougou_after")
