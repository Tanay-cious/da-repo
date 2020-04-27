# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 20:14:37 2020

@author: Tanay Kedia
"""

import requests
import json
res = requests.get('https://api.nobelprize.org/2.0/laureates')
a = json.loads(res.text)
b = a['laureates']
for key in b:
    print("\n" + key['fullName']['en'] + ", " + key['birth']['date'][0:4] + ", " + key['birth']['place']['country']['en'] + ".")