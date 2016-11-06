
# coding: utf-8

# In[1]:

import pandas as pd
import urllib
import requests
from bs4 import BeautifulSoup as bs
import datetime
#https://www.hkex.com.hk/chi/cbbc/newissue/newlaunch_c.htm


# In[3]:

url_cbbcs = 'http://www.hkex.com.hk/chi/market/sec_tradinfo/stockcode/eisdwarr_c.htm'
thepage_cbbcs = urllib.urlopen(url_cbbcs)
soup_cbbcs = bs(thepage_cbbcs,"html.parser")


# In[4]:

records = []
for tr in soup_cbbcs.findAll("tr"):
    trs = tr.findAll("td")
    record = []
    try:
        record.append(trs[0].text)
        #record.append(trs[1].a['href'])
        record.append(trs[1].a['href'])
        record.append((trs[2].text))
        record.append(trs[3].text)
        #record.append(datetime.datetime.strptime(trs[3],'%d/%m/%y'))
        records.append(record)
    except:
        pass
    
df = pd.DataFrame(data=records)
#housekeep the df
df.columns = ['STOCK CODE', 'NAME','LOT','EXPIRY']
df['LOT'] = df['LOT'].str.replace(',','').astype('int')
df['EXPIRY'] = df['EXPIRY'].apply(lambda x:datetime.datetime.strptime(x, '%d/%m/%Y'))


# In[5]:

df.size


# In[6]:

df.head()


# In[ ]:



