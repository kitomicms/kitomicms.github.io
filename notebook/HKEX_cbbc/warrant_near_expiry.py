
# coding: utf-8

# In[1]:

import pandas as pd
import urllib
import requests
from bs4 import BeautifulSoup as bs
import datetime
#https://www.hkex.com.hk/chi/cbbc/newissue/newlaunch_c.htm


# In[2]:

url_cbbcs = 'https://www.hkex.com.hk/eng/dwrc/expire/expiring.htm'
thepage_cbbcs = urllib.urlopen(url_cbbcs)
soup_cbbcs = bs(thepage_cbbcs,"html.parser")


# In[10]:

records = []
for tr in soup_cbbcs.findAll("tr"):
    trs = tr.findAll("td")
    record = []
    try:
        for x in range(0,12):
            record.append(trs[x].text.strip())
            
            #record.append(datetime.datetime.strptime(trs[3],'%d/%m/%y'))
        records.append(record)
    except:
        pass
    
df = pd.DataFrame(data=records)
df2 = df[4:]
df2.columns = df.iloc[3]
df2.index = range(0,len(df2))
#print (pd.DataFrame(data=records)).ix(3)
#housekeep the df

#df.columns = ['STOCK CODE', 'NAME','LOT','EXPIRY']
#df['LOT'] = df['LOT'].str.replace(',','').astype('int')
#df['EXPIRY'] = df['EXPIRY'].apply(lambda x:datetime.datetime.strptime(x, '%d/%m/%Y'))


# In[12]:

df2


# In[ ]:



