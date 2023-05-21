from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import requests
from bs4 import BeautifulSoup
import pandas as pd
import urllib.request
from selenium.webdriver.support.ui import WebDriverWait

options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)


url = 'https://estudante.estacio.br/login'
driver.get(url)

sleep(8)
button_estcaio = driver.find_element(By.XPATH, '//*[@id="section-login"]/div/div/div/section/div[1]/button')
button_estcaio.click()

sleep(5)

email_input = driver.find_element(By.NAME, 'loginfmt')
email_input.send_keys('202203366841@alunos.estacio.br')

submit_button = driver.find_element(By.ID, 'idSIButton9')
submit_button.click()


senha_input = driver.find_element(By.NAME, 'passwd')
senha_input.send_keys('BateraDeus3#')

sleep(2)

submit_senha = driver.find_element(By.ID, 'idSIButton9')
submit_senha.click()

sleep(1)

submit_neg = driver.find_element(By.ID, 'idBtn_Back')
submit_neg.click()

sleep(10)

disc = driver.find_element(By.XPATH, '//*[@id="card-entrega-ARA0066"]').click()

sleep(2)

tema = driver.find_element(By.XPATH, '//*[@id="temas-lista-topicos"]/li[5]/a/div').click()
sleep(1)

pag = driver.find_element(By.XPATH, '//*[@id="segunda-tab"]').click()
sleep(2)

download = driver.find_element(By.XPATH, '//*[@id="acessar-conteudo-complementar-arquivo-64615eb275e90c00266b9ff9"]').click()
sleep(250)

driver.quit()
