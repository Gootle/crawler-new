
# coding: utf-8

# In[7]:


###http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20170605&stockNo=2330


# In[8]:


###https://www.youtube.com/watch?v=kurBNu1qobM&t=71s

import requests
import json
import csv
import time, datetime,os
from bs4 import BeautifulSoup as bs
import urllib2


# In[9]:


id_list = ['3437','2330'] #input the stock IDs
now = datetime.datetime.now()
year_list = range (2016,now.year+1) #since 2016 to this year
month_list = range(1,13)  # 12 months


# In[10]:


dt = datetime.datetime.now()
dt.year
dt.month


# In[11]:


#standard web crawing process
def get_webmsg (year, month, stock_id):
    date = str (year) + "{0:0=2d}".format(month) +'01' ## format is yyyymmdd
    sid = str(stock_id)
    url_twse = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date='+date+'&stockNo='+sid
    res =requests.post(url_twse,)
    soup = bs(res.text , 'html.parser')
    smt = json.loads(soup.text)     #convert data into json
    return smt


# In[14]:


def write_csv(stock_id,directory,filename,smt) :
    writefile = directory + filename               #set output file name
    outputFile = open(writefile,'w',newline='')
    outputWriter = csv.writer(outputFile)
    head = ''.join(smt['title'].split())
    a = [head,""]
    outputWriter.writerow(a)
    outputWriter.writerow(smt['fields'])
    for data in (smt['data']):
        outputWriter.writerow(data)

    outputFile.close()


# In[15]:


#create a directory in the current one doesn't exist
def makedirs (year, month, stock_id):
    sid = str(stock_id)
    yy      = str(year)
    mm       = str(month)
    directory = 'D:/stock'+'/'+sid +'/'+ yy
    if not os.path.isdir(directory):
        os.makedirs (directory)  # os.makedirs able to create multi folders


# In[16]:


for stock_id in id_list:
    for year in year_list:
        for month in month_list:
            if (dt.year == year and month > dt.month) :break  # break loop while month over current month
            sid = str(stock_id)
            yy  = str(year)
            mm  = month
           # directory = 'D:/stock'+'/'+sid +'/'+yy +'/'       #setting directory
            directory = 'D:/stock'+'/'+sid +'/'       #setting directory
            filename = str(yy)+str("%02d"%mm)+'.csv'          #setting file name
            smt = get_webmsg(year ,month, stock_id)           #put the data into smt 
            makedirs (year, month, stock_id)                  #create directory function
            write_csv (stock_id,directory, filename, smt)    # write files into CSV
            time.sleep(1)

