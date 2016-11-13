
# coding: utf-8

# In[1]:

import pandas as pd
import urllib
import requests
from bs4 import BeautifulSoup as bs
import datetime
#https://www.hkex.com.hk/chi/cbbc/newissue/newlaunch_c.htm
import functions


# In[2]:

url_cbbcs = 'http://www.hkex.com.hk/eng/market/sec_tradinfo/stockcode/eisdcbbc.htm'
thepage_cbbcs = urllib.urlopen(url_cbbcs)
soup_cbbcs = bs(thepage_cbbcs,"html.parser")


# In[3]:

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
df['STOCK CODE'] = df['STOCK CODE'].astype('int')


# In[6]:

df.tail()


# In[32]:

searchList = list(df['STOCK CODE'][0:201])


# In[34]:

searchListResult = functions.cbbc_loop(searchList)


# In[50]:

df['underlying'] = 'None'


# In[54]:

df.loc[0:200,'underlying'] = searchListResult


# In[59]:

df


# In[ ]:



