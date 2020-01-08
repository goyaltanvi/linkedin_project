# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 16:11:11 2020

@author: tanvi
"""

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import selenium.webdriver.common.keys
from selenium.webdriver.common.keys import Keys
import time
import re


browser=webdriver.Chrome("C:/Users/tanvi/Desktop/python/chromedriver_win32/chromedriver.exe")
browser.get('https://www.linkedin.com/')
login_ele=browser.find_element_by_xpath('/html/body/nav/a[3]')
login_ele.click()




email=browser.find_element_by_xpath('//*[@id="username"]')
password=browser.find_element_by_xpath('//*[@id="password"]')
login=browser.find_element_by_xpath('//*[@id="app__container"]/main/div/form/div[3]/button')

ActionChains(browser).move_to_element(email).click()\
     .send_keys('email')\
     .move_to_element(password).click()\
     .send_keys('password')\
     .perform()
     
ActionChains(browser).move_to_element(login).click().perform()


search_engine=browser.find_element_by_id('ember31')
ActionChains(browser).move_to_element(search_engine).click()\
      .send_keys('#web development')\
      .perform()
try:
    search=browser.find_element_by_xpath('//*[@id="ember31"]/div[2]')
except:
    search=browser.find_element_by_xpath('//*[@id="ember29"]/div[2]')
ActionChains(browser).move_to_element(search).click().perform()
browser.maximize_window()
scroll=browser.find_element_by_tag_name('html')
scroll.send_keys(Keys.END)
browser.find_element_by_tag_name('html').send_keys(Keys.CONTROL + Keys.HOME)
button=browser.find_elements_by_tag_name('button')
see_more = []
for elem in button:
    if elem.text == '…see more':
        see_more.append(elem)
for x in see_more:
    x.click()
    time.sleep(1)
html = browser.find_element_by_tag_name('html')
html.send_keys(Keys.HOME)
time.sleep(1)
try:
    all_text = browser.find_element_by_xpath('/html/body/div[5]/div[4]/div[3]/div/div[2]/div/div[2]/div/div/div/div/ul').text
except:
    all_text = browser.find_element_by_xpath('/html/body/div[6]/div[4]/div[3]/div/div[2]/div/div[2]/div/div/div/div/ul').text
email = re.findall(r'\S+@\S+', all_text)
f = open('test.txt', 'a+')
for i in email: 
      f.write(i)
      f.write("\n")
f.close()    