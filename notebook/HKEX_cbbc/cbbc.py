
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


# In[27]:

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


# In[28]:

df2 = df

#df2.loc[:,'Underlying Quote'] = pd.Series(cbbc_loop(df2['STOCK CODE']),len(df2))


# In[29]:

df2.head()


# In[30]:

xl = pd.ExcelFile("pandas_simple.xlsx")

excel_result = xl.parse("Sheet2")
excel_result.tail()


# In[45]:

#[Task] Find out what is outstanding

len(excel_result[excel_result['w'] == 'None'])


# In[46]:

outstanding = excel_result['STOCK CODE'][excel_result['w']=='None']
outstanding.head()


# In[48]:

#foo = cbbc_loop(df3['STOCK CODE'])
#df3.loc[:,'Q'] = pd.Series(foo,range(0,len(df3)))
functions.cbbc_loop(outstanding[0:10])


#[Next time] Next step how to update value of filtered result


# In[69]:

#boo = cbbc_loop(df2['STOCK CODE'][0:499])


# In[138]:

# Create a Pandas dataframe from some data.
df3 = df2[['STOCK CODE','Quote']]

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df_new.to_excel(writer, sheet_name='Sheet2')

# Close the Pandas Excel writer and output the Excel file.
writer.save()


# In[1]:

df


# In[ ]:



