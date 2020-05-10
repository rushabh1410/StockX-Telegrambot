import json
import datetime
import requests
from bs4 import BeautifulSoup

def parsePrice(fname):
    x=getshort(fname)
    if x == "" :
        return "0"
    url = 'https://finance.yahoo.com/quote/'+x
    r= requests.get(url)
    data=r.text
    soup=BeautifulSoup(data,features="lxml")
    price = soup.find('div',{'class': 'My(6px) Pos(r) smartphone_Mt(6px)'}).find('span').text
    return price

def getshort(fname):
    y=""
    url = 'https://finance.yahoo.com/quote/'+fname
    r= requests.get(url)
    data=r.text
    soup=BeautifulSoup(data,features="lxml")
    if soup.find('td',{'class' : 'data-col0 Ta(start) Pstart(6px) Pend(15px)'}) is not None:
        y = soup.find('td',{'class' : 'data-col0 Ta(start) Pstart(6px) Pend(15px)'}).text
    return y

def get_response(msg):
    z=parsePrice(msg)
    return z