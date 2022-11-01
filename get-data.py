#!python
# -*- coding: utf-8 -*-
import warnings
warnings.filterwarnings('ignore')
import os
from datetime import date
import requests
import pandas as pd
from bs4 import BeautifulSoup
import csv

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
# url = 'https://marketdata.set.or.th/mkt/sectorquotation.do?sector=SET100&language=th&country=TH'
url = 'https://classic.set.or.th/mkt/sectorquotation.do?sector=MAI&language=th&country=TH'
r = requests.get(url, verify=False, headers=headers)
r.encoding = "utf-8"
soup = BeautifulSoup(r.content, 'lxml')

table = soup.find_all('table', class_="table-info")[2]
thead = table.find_all('thead')
tbody = table.tbody

row_marker = 0
i = 1
res = ""
column_marker = 1
for row in tbody.find_all('tr'):
    
    col0 = row.find_all('td')[0]
    col5 = row.find_all('td')[5]

    str0 = col0.get_text().replace(" ","").replace("\n","").replace("\r","")
    str5 = col5.get_text().replace(" ","").replace("\n","").replace("\r","")
    
    res +=  str(column_marker) + ':' + str0 + ',' + str5 + "\n\n"
    column_marker = column_marker + 1

res
