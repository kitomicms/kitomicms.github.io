
# coding: utf-8

# In[3]:

import pandas as pd
import urllib
import requests
from bs4 import BeautifulSoup as bs
import datetime
#https://www.hkex.com.hk/chi/cbbc/newissue/newlaunch_c.htm


# In[4]:

def find_between(s, first,last):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""
    
def find_between2(s, start, end):
    return (s.split(start))[1].split(end)[0]


# In[5]:

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

