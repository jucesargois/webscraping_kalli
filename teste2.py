import requests
from bs4 import BeautifulSoup
from selenium import webdriver
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
inputLoginCatalogo.send_keys('')
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
inputSenhaCatalogo.send_keys('')
time.sleep(0.5)

#clique continuar: Acessa o catalogo completo (Login efetuado)
navegador.find_element_by_xpath('//*[@id="main-content"]/app-auth/ion-router-outlet/user-auth/ion-content/app-content-wrapper/div/div/form/ion-button').click()


dados_produtos = []
format_xpath = '//*[@id="main-content"]/app-catalog/ion-content/app-content-wrapper/div/div/div/app-catalog-products/div/div[{numero}]/div/div[1]/img'
time.sleep(7)


for i in range(1):#Range defini a quantidade de produtos, para pegar as informações.
    
  
  i += 1

  xpath = format_xpath.format(numero=i)
  

  time.sleep(0.2)
  navegador.find_element_by_xpath(xpath).click()
  time.sleep(0.7)
  navegador.find_element_by_xpath('//*[@id="main-content"]/app-catalog-product-view/ion-content/app-content-wrapper/div/div/div/div')
  time.sleep(0.2)
  


  page_content = navegador.page_source


  site = BeautifulSoup(page_content,'lxml')

  
  df = pd.read_html(page_content,index_col=0)
  


print(df[0])


dados = pd.DataFrame(df,columns={})
dados.to_csv("teste_concat_table_p.csv",index=False,)