# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 16:11:11 2020

@author: tanvi
"""

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import selenium.webdriver.common.keys

browser=webdriver.Chrome("C:/Users/tanvi/Desktop/python/chromedriver_win32/chromedriver.exe")
browser.get('https://www.linkedin.com/')
login_ele=browser.find_element_by_xpath('/html/body/nav/a[3]')
login_ele.click()




email=browser.find_element_by_xpath('//*[@id="username"]')
password=browser.find_element_by_xpath('//*[@id="password"]')
login=browser.find_element_by_xpath('//*[@id="app__container"]/main/div/form/div[3]/button')

ActionChains(browser).move_to_element(email).click()\
     .send_keys('tanvigoyal036@gmail.com')\
     .move_to_element(password).click()\
     .send_keys('Tanu@225')\
     .perform()
     
ActionChains(browser).move_to_element(login).click().perform()


search_engine=browser.find_element_by_id('ember31')
ActionChains(browser).move_to_element(search_engine).click()\
      .send_keys('#app development')\
      .perform()
search=browser.find_element_by_xpath('//*[@id="ember29"]/div[2]')
ActionChains(browser).move_to_element(search).click().perform()


content=browser.find_element_by_id('ember793')

ActionChains(browser).move_to_element(content).click().perform()
