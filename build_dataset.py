import json
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

browsers = '/home/rmccormack/git/useragent_spoofing/browsers.json'
checked = []

with open(browsers) as data_file:    
    caps = json.load(data_file)

js_tests = pd.DataFrame()

for i in range(len(caps)):

    desired_cap = { str(key):str(value) for key,value in caps[i].items() }
    
    driver = webdriver.Remote(
        command_executor='PASSWORDHERE',
        desired_capabilities=desired_cap)
    
    driver.get("http://kangax.github.io/js-checker/")
    useragent = driver.execute_script("return navigator.userAgent")
    html = driver.page_source
    driver.quit()

    soup = BeautifulSoup(str(html))
    for j in soup.findAll('code')[2:]:
        if 'strong' in str(j.contents[0]):
            x = j.contents[0].contents[0]
            try:
                test = j.contents[3]
                test = 1
            except:
                test = 0
            js_tests.set_value(useragent, x, test)
            
    checked.append(caps[i])
    print len(caps) - i
