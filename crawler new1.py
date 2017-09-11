# coding: utf-8

# In[7]:

import requests
import json
import csv


# In[4]:

url_twse ='http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20170501&stockNo=2330&'
res = requests.get(url_twse)
s = json.loads(res.text)
