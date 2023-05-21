from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import requests
from bs4 import BeautifulSoup
import pandas as pd
import urllib.request
from selenium.webdriver.support.ui import WebDriverWait
import shutil
import os

options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_experimental_option('excludeSwitches', ['enable-logging'])



driver = webdriver.Chrome(options=options)
url_login = 'https://estudante.estacio.br/login'
url_tema = 'https://estudante.estacio.br/disciplinas'


email = input('digite o email do usuario: ')
password = input("digite a sua senha: ")


class Extrai:
    def __init__(self, email, password, driver):
        self.email = email
        self.password = password
        self.driver = driver



    def login(self):

     self.driver.get(url_login)
     sleep(10)

     button_entrar = self.driver.find_element(By.XPATH, '//*[@id="section-login"]/div/div/div/section/div[1]/button')
     button_entrar.click()

     sleep(10)

     login = self.driver.find_element(By.NAME, 'loginfmt')
     login.send_keys(self.email)
     button_avancar_email = self.driver.find_element(By.ID, 'idSIButton9')
     button_avancar_email.click()
     sleep(2)
     senha = self.driver.find_element(By.NAME, 'passwd')
     senha.send_keys(self.password)
     sleep(2)

     button_avancar_senha = self.driver.find_element(By.ID, 'idSIButton9')
     button_avancar_senha.click()

     button_nao = self.driver.find_element(By.ID, 'idBtn_Back')
     button_nao.submit()

     sleep(10)



    def estudante_tema(self):
     self.driver.get(url_tema)
     sleep(10)
     disc = self.driver.find_element(By.XPATH, '//*[@id="card-entrega-ARA0066"]')
     disc.click()
     sleep(5)

     tema = self.driver.find_element(By.XPATH, '//*[@id="temas-lista-topicos"]/li[5]/a/div')
     tema.click()
     sleep(5)

     pag = driver.find_element(By.XPATH, '//*[@id="segunda-tab"]').click()
     sleep(2)

     download = driver.find_element(By.XPATH, '//*[@id="acessar-conteudo-complementar-arquivo-64615eb275e90c00266b9ff9"]').click()
     sleep(250)






    def  extrai_dados():
       print()










extrai = Extrai(email, password, driver)

extrai.login()
extrai.estudante_tema()



