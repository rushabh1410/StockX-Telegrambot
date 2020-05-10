import requests
from bs4 import BeautifulSoup


def get_response(msg):
    y=""
    url = 'https://finance.yahoo.com/quote/'+msg
    r= requests.get(url)
    data=r.text
    soup=BeautifulSoup(data,features="lxml")
    if soup.find('td',{'class' : 'data-col0 Ta(start) Pstart(6px) Pend(15px)'}) is not None:
        y = soup.find('td',{'class' : 'data-col0 Ta(start) Pstart(6px) Pend(15px)'}).text
    return y