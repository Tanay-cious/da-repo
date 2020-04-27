# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 20:25:09 2020

@author: Tanay Kedia
"""

import requests
import bs4
import json
List = []
vals = []
docs = {}
indocs = {}
res = requests.get('http://www.burjeel.com/abu-dhabi/doctors/')
soup = bs4.BeautifulSoup(res.text, 'html.parser') #converting from txt to bs4 type#
for hi in soup.find_all('div', class_="col-lg-4 col-md-4 col-sm-6 col-xs-12 list_wrapper innercommon"):
        List.append(hi.a.h4.text)
#print(List)
for hi in soup.find_all('div', class_="col-lg-4 col-md-4 col-sm-6 col-xs-12 list_wrapper innercommon"):
    indocs = {
        'Name': hi.a.h4.text,
        'Spec': hi.h5.text,
        'Pic': 'http://www.burjeel.com/abu-dhabi/' + hi.img['src'],
        'Profile' : 'http://www.burjeel.com/abu-dhabi/' + hi.a['href']
    }
    vals.append(indocs)
#print(vals)
for key,val in zip(List, vals):
    docs[key] = val
#print(docs)    
final = json.dumps(docs, indent = 3)
print(final)
print(str(len(docs.keys())) + ' doctors registered on the site.')
