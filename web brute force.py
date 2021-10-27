import re
import requests
from selenium import webdriver
import time

def capture():
    raw = 'https://raw.githubusercontent.com/bensooter/URLchecker/master/top-1000-websites.txt'
    resp = requests.get(raw)
    topTen = resp.text
    topTen = topTen.split()
    del topTen[10:len(topTen)]
    
    browser = webdriver.Chrome()
    for each in topTen:
        print('https://www.'+each)
        browser.get('https://www.'+each)
        time.sleep(1)
        browser.get_screenshot_as_file(str(time.time())+".png")

capture()