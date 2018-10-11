# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 22:38:05 2018

@author: vishal
"""

from selenium import webdriver
# Using Chrome to access web
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(r"C:\Users\visha\chromedriver",chrome_options = chrome_options)
driver.get('https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRE55YXpBU0FtVnVLQUFQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen')
headlines = []

for i in range(1,30):
    link = '//*[@id="yDmH0d"]/c-wiz/div/c-wiz/div/div[2]/div/main/c-wiz/div[1]/div['+str(i)+']/div/article/div[1]/div/h3/a/span'
    head = driver.find_element_by_xpath(link)
    k = head.text
    headlines.append(k)
    
txtfile = open("C:\\Users\\visha\\Desktop\\news_today.txt", "w")
for i in headlines:
  txtfile.write(i)
  txtfile.write("\n")
txtfile.close()

import os
os.startfile('C:\\Users\\visha\\Desktop\\news_today.txt')




