#This program returns RSI of a crypto
#method of calculation taken from https://www.macroption.com/rsi-calculation/
import datetime
from datetime import timedelta
from datetime import date
import json
import cryptocompare 
from main import coin
N = 14 
lprices = []
lups = []
ldns = []
avgu=0
avgdn=0
def change(date1, date2):
   price = cryptocompare.get_historical_price('XMR', 'USD', (date1)) - cryptocompare.get_historical_price('XMR', 'USD', (date2)) 
   return price
def prices(date1, date2):
    list1 = []
    date1 = date2 = 0
    for x in range(N, 0):
        date1 = datetime.datetime.now() - timedelta(days=x)
        date2 = datetime.datetime.now() - timedelta(days=x+1)
        list1.append(change(date1, date2))
    list1 = lprices
def ups():
    list1 = []
    for x in range(0, len(lprices)):
        if list1[x] > 0:
            list1.append(list1[x])
    list1 = lups
def dns():
    list1 = []
    for x in range(0, len(lprices)):
        if list1[x] <= 0:
            list1.append(list1[x])
    list1 = ldns
def avgups():
    sum = 0
    for x in range(0, len(lups)):
        sum += ups()[x]
    avg = sum/N
    avgu = avg
def avgdns():
    sum = 1
    for x in range(0, len(ldns)):
        sum += dns()[x]
    avg = sum/N
    avgd = avg
def getRSI():
    RS = avgu/avgd
    RSI = 100-100/(1+RS)
    return RSI

