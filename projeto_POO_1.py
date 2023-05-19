from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import requests
from bs4 import BeautifulSoup
import pandas as pd


email = input('digite o email do usuario: ')
password = input("digite a sua senha: ")


class Extrai:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def login(self):

      url_login = 'https://estudante.estacio.br/login'
      driver = webdriver.Chrome()
      driver.get(url_login)
      sleep(10)

      button_entrar = driver.find_element(By.XPATH, '//*[@id="section-login"]/div/div/div/section/div[1]/button')
      button_entrar.click()

      sleep(10)

      login = driver.find_element(By.NAME, 'loginfmt')
      login.send_keys(self.email)
      button_avancar_email = driver.find_element(By.ID, 'idSIButton9')
      button_avancar_email.submit()
      sleep(2)
      senha = driver.find_element(By.NAME, 'passwd')
      senha.send_keys(self.password)
      sleep(2)

      button_avancar_senha = driver.find_element(By.ID, 'idSIButton9')
      button_avancar_senha.submit()

      button_nao = driver.find_element(By.ID, 'idBtn_Back')
      button_nao.submit()

    def estudante():
      url_estudante = 'https://estudante.estacio.br/disciplinas/estacio_7495786/temas/5'
      driver = webdriver.Chrome()
      driver.get(url_estudante)
      sleep(10)


    def  extrai_dados():
       print()










extrai = Extrai(email, password)
login = extrai.login()
estudante = extrai.estudante()



