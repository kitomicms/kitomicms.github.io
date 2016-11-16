
# coding: utf-8

# In[22]:

import pandas as pd
import urllib
import requests
from bs4 import BeautifulSoup as bs
import datetime
#https://www.hkex.com.hk/chi/cbbc/newissue/newlaunch_c.htm
import functions


# In[81]:

url1 = 'http://www.hkex.com.hk/chi/market/sec_tradinfo/stockcode/eisdeqty_c.htm'
thepage1 = urllib.urlopen(url1)
soup1 = bs(thepage1,"html.parser")
url2 = 'http://www.hkex.com.hk/eng/market/sec_tradinfo/stockcode/eisdeqty.htm'
thepage2 = urllib.urlopen(url2)
soup2 = bs(thepage2,"html.parser")


# In[92]:

records1 = []
for tr in soup1.findAll("tr"):
    trs = tr.findAll("td")
    record1 = []
    try:
        for x in range(0,7):
            record1.append(trs[x].text)
        records1.append(record1)
    except:
        pass
records2 = []
for tr in soup2.findAll("tr"):
    trs = tr.findAll("td")
    record2 = []
    try:
        for x in range(0,7):
            record2.append(trs[x].text)
        records2.append(record2)
    except:
        pass
dfc = pd.DataFrame(data=records1)
dfe = pd.DataFrame(data=records2)


# In[95]:

dfe['ChineseName'] = dfc[1]


# In[106]:

dfe.columns = ['StockCode','EnglishName','Lot','Note1','Note2','Note3','Note4','ChineseName']
df = dfe.reindex(columns=['StockCode','EnglishName','ChineseName','Lot','Note1','Note2','Note3','Note4'])


# In[107]:

df.drop(df.index[0:3])


# In[ ]:



