
# coding: utf-8

# In[4]:

import pandas_datareader.data as web
import datetime    

start = datetime.datetime(2013, 1, 1)
end = datetime.datetime(2016, 1, 27)
df = web.DataReader("GOOGL", 'yahoo', start, end)

dates =[]
for x in range(len(df)):
    newdate = str(df.index[x])
    newdate = newdate[0:10]
    dates.append(newdate)

df['dates'] = dates

print df.head()
print df.tail()


# In[8]:

web.DataReader("1171.HK", 'yahoo', start, end)


# In[ ]:



