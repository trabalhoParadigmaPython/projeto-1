from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import requests
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome()

url = 'https://imendes.bmtcloud.com.br/apex/vdesk/f?p=138:LOGIN::::::'
driver.get(url)

login = driver.find_element('name', 'P101_USERNAME')
login.send_keys("imds_elias")

senha = driver.find_element('name', 'P101_PASSWORD')
senha.send_keys('123')

btn = driver.find_element(By.TAG_NAME, 'Button')
btn.click()
