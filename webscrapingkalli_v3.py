from cgitb import reset
from attr import attr
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from time import sleep
import time
import pandas as pd

options = webdriver.FirefoxOptions()
navegador = webdriver.Chrome(chrome_options=options, executable_path=r'C:\Users\juces\AppData\Local\Programs\Python\Python310\geckodriver.exe')

#Pesquisa pelo site
navegador.get('https://v.vesti.mobi/kalli/catalogo')
time.sleep(2)
#seleciona produto
navegador.find_element_by_xpath("//*[@id='main-content']/app-catalog/ion-content/app-content-wrapper/div/div/div/app-catalog-products/div/div[1]/div/div[1]/img").click()
time.sleep(1)

#seleciona campo cpf
inputLoginCatalogo = navegador.find_element_by_xpath('//*[@id="main-content"]/app-auth/ion-router-outlet/user-auth/ion-content/app-content-wrapper/div/div/form/div/ion-item/ion-input/input').click()
time.sleep(1)

#seleciona o input do campo cpf
inputLoginCatalogo = navegador.find_element_by_class_name('native-input.sc-ion-input-md') 
time.sleep(0.1)

#Escreve o login 
inputLoginCatalogo.send_keys('inserir aqui cpf,cnpf ou e-mail')
time.sleep(0.5)

#clique continuar
navegador.find_element_by_xpath('//*[@id="main-content"]/app-auth/ion-router-outlet/user-auth/ion-content/app-content-wrapper/div/div/form/ion-button').click()
time.sleep(1)

#seleciona campo senha
navegador.find_element_by_xpath('/html/body/app-root/ion-app/ion-router-outlet/app-store/ion-router-outlet/app-auth/ion-router-outlet/user-auth/ion-content/app-content-wrapper/div/div/form/ion-item[2]/ion-input').click()
time.sleep(1)

#seleciona o input do campo senha
inputSenhaCatalogo = navegador.find_element_by_xpath('/html/body/app-root/ion-app/ion-router-outlet/app-store/ion-router-outlet/app-auth/ion-router-outlet/user-auth/ion-content/app-content-wrapper/div/div/form/ion-item[2]/ion-input/input')
time.sleep(0.1)
#Escreve o senha 
inputSenhaCatalogo.send_keys('inserir aqui senha')
time.sleep(0.5)

#clique continuar: Acessa o catalogo completo (Login efetuado)
navegador.find_element_by_xpath('//*[@id="main-content"]/app-auth/ion-router-outlet/user-auth/ion-content/app-content-wrapper/div/div/form/ion-button').click()


dados_produtos = []
format_xpath = '//*[@id="main-content"]/app-catalog/ion-content/app-content-wrapper/div/div/div/app-catalog-products/div/div[{numero}]/div/div[1]/img'
time.sleep(4)


for i in range(3):#Range defini a quantidade de produtos, para pegar as informações.
    
  
  i += 1

  xpath = format_xpath.format(numero=i)
  

  time.sleep(0.2)
  navegador.find_element_by_xpath(xpath).click()
  time.sleep(0.7)
  navegador.find_element_by_xpath('//*[@id="main-content"]/app-catalog-product-view/ion-content/app-content-wrapper/div/div/div/div')


  page_content = navegador.page_source


  site = BeautifulSoup(page_content,'lxml')
  
  
  
  
  
  print(xpath)
  produto_preco = site.find("div", attrs={'class' : 'prices'})
  produto_cod = site.find("div", attrs={'class' : 'code'})
  produto_descricao = site.find("div", attrs={'class' : 'description'})
  produto_composição = site.find("div", attrs={'class' : 'composition'})
  produto_tamanhos = site.find("div", attrs={'class' : 'table-container'})

  

  
  

  
  #volta para o catalogo
  navegador.back()
  
  try:
    dados_produtos.append([produto_cod.text,produto_preco.text,produto_descricao.text,produto_composição.text,produto_tamanhos.text])
  except Exception:
    pass

  
  
  
#Inseri colunas e salva dados no csv
dados = pd.DataFrame(dados_produtos, columns=['Codigo','Preço','Descrição','Composição','Tamanhos'])
dados.to_csv("produtoskalli_teste.csv", index=False)
print(dados_produtos)
