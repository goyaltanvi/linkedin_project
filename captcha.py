# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 10:21:51 2020

@author: tanvi
"""
from PIL import Image
import pytesseract
from io import BytesIO
import time
from selenium import webdriver

URL = 'https://www.skyexchange.com/verifycode.gr?v=1578034337798'

driver=webdriver.Chrome("C:/Users/tanvi/Desktop/python/chromedriver_win32/chromedriver.exe")
driver.get(URL)
captcha = driver.find_element_by_xpath('/html/body/img')
#location = captcha.location
#size = captcha.size
#driver.save_screenshot('screenshot.png')
captcha.screenshot(f'captcha.png')
#captcha.clear()

img = Image.open(f'captcha.png')
text = pytesseract.image_to_string(img, lang='eng', config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
print(text)

