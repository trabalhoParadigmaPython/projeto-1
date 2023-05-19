from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import requests
from bs4 import BeautifulSoup
import pandas as pd


email = input('digite o email do usuario: ')
password = input("digite a sua senha: ")


class Extrai:
    def _init_(self, email, password):
        self.email
        self.password

    def estudante(self):
      url = 'https://estudante.estacio.br/login'
      driver = webdriver.Chrome()
      driver.get(url)
      login = driver.find_element(By.NAME, 'loginfmt')
      login.send_keys(self.email)
      button_avancar_email = driver.find_element(By.ID, 'idSIButton9')
      button_avancar_email.submit()

      senha = driver.find_element(By.NAME, 'passwd')
      senha.send_keys(self.password)

      btn = driver.find_element(By.ID, 'idSIButton9')
      btn.submit()







extrai = Extrai(email, password)
login = extrai.estudante()