
# coding: utf-8

# In[1]:

import pandas as pd
import urllib
import requests
from bs4 import BeautifulSoup as bs
import datetime
#https://www.hkex.com.hk/chi/cbbc/newissue/newlaunch_c.htm


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


# In[5]:

def find_between(s, first,last):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""
    
def find_between2(s, start, end):
    return (s.split(start))[1].split(end)[0]



# In[44]:

def cbbc_loop(cbbcs):
    result = []
    for cbbc in cbbcs:
        url_cbbc = "".join(str(v) for v in ["http://www.hkex.com.hk/eng/invest/company/profile_page_e.asp?WidCoID=" , cbbc , "&WidCoAbbName=&Month=&langcode=e"])
        thepage_cbbc = urllib.urlopen(url_cbbc)
        soup_cbbc = bs(thepage_cbbc,"html.parser")

        records_cbbc = []
        for tr in soup_cbbc.findAll("tr"):
            trs = tr.findAll("td")
            record_cbbc = []
            try:
                record_cbbc.append((''.join(trs[0].text.split())).strip())
                records_cbbc.append(record_cbbc)

            except:
                pass
        
        result.append(find_between(str(records_cbbc[0]),'UnderlyingAssetCode:','UnderlyingAssetPrice'))
    return result


# In[64]:

df2 = df
df2.loc[:,'Underlying Quote'] = pd.Series(cbbc_loop(df2['STOCK CODE']),len(df2))


# In[37]:

print cbbc_info('60000')


# In[39]:

df3 = df2.head()


# In[61]:

foo = cbbc_loop(df3['STOCK CODE'])
df3.loc[:,'Q'] = pd.Series(foo,range(0,len(df3)))
#pd.Series(np.random.randn(sLength))                        


# In[63]:

df2


# In[ ]:



