#!/usr/bin/env python
#
# A simple example of using api.senticrypt.com:
# 1) Buy if the average sentiment percentage change is >= 50%
# 2) Sell when the average sentiment percentage change is <= -10%
#

import os, sys, requests, json, time

def pchange(old, new):
    try:
        return ((new - old) / float(old)) * 100.0
    except:
        new = new + 0.00001
        old = old + 0.00001
        return ((new - old) / float(old)) * 100.0

def main():
    bought = None
    bought_sent = None
    wallet = 1000.00

    while 1:
        r = requests.get('http://api.senticrypt.com/beta/day/')
        j = r.json()['items']
        cur = j[-1]
        prev = j[-5]
        if bought is None:
            p = pchange(prev['average'], cur['average'])
            if p >= 50:
                bought = cur['btc_price']
                bought_sent = cur
                print('BOUGHT: %.2f pc=%.2f avg=%.3f sum=%.3f wallet=%.2f' % (
                    bought, p, cur['average'], cur['sum'], wallet))
        elif bought is not None:
            p = pchange(bought_sent['average'], cur['average'])
            if p <= -10:
                profit = wallet * (pchange(bought, cur['btc_price'])/100.0)
                wallet += profit
                print('SOLD: profit=%.2f pc=%.2f avg=%.3f sum=%.3f wallet=%.2f' % (
                    profit, p, cur['average'], cur['sum'], wallet))
                bought = None
        print('p=%.4f bought=%s wallet=%.2f btc_price=%.2f average=%.4f prev_avg=%.4f' % (
            p, bought, wallet, cur['btc_price'], cur['average'], prev['average']))
        time.sleep(10)

if __name__ == '__main__':
    main()
