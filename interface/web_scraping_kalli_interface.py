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
from webcolors import rgb_to_name
from scipy.spatial import KDTree
from PySimpleGUI import PySimpleGUI as sg
import pyautogui
import openpyxl
#Telas
sg.theme('Reddit')
layoutQtdProd = [
  [
    sg.Text('Qtd produtos: '), sg.Input(key='qtdprodutos',size=(20,1)), 
    sg.Button('Confirmar'),
  ]
]
layoutLoading = [
              [sg.Text('Carregando:')],
              [sg.Text() , sg.Input(key='qtdprodloading')]
]
janela2 = sg.Window('Inserir quantidade de produtos',layoutQtdProd)
janela3 = sg.Window('Carregando',layoutLoading)

#Ler eventos
while True:
    eventos2, valores2 = janela2.read()
    if valores2['qtdprodutos'] != '':
      janela2.close()
      
    
      
      




      options = webdriver.FirefoxOptions()
      options.add_argument("--headless")
      navegador = webdriver.Firefox(executable_path=r'C:\Users\juces\AppData\Local\Programs\Python\Python310\geckodriver.exe')

      #Pesquisa pelo site
      navegador.get('https://v.vesti.mobi/kalli/catalogo')
      time.sleep(3)
      pyautogui.keyDown('ctrl')
      pyautogui.press('-')
      pyautogui.press('-')
      pyautogui.press('-')
      pyautogui.press('-')
      pyautogui.keyUp('ctrl')
      print('Aplicou zoom')
      
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
      inputLoginCatalogo.send_keys(cpf)#sem aspas
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
      inputSenhaCatalogo.send_keys('pass')#com aspas
      time.sleep(0.5)

      #clique continuar: Acessa o catalogo completo (Login efetuado)
      navegador.find_element_by_xpath('//*[@id="main-content"]/app-auth/ion-router-outlet/user-auth/ion-content/app-content-wrapper/div/div/form/ion-button').click()

      qtdprodutosinfo = int(valores2['qtdprodutos'])
      dados_produtos = []
      format_xpath = '//*[@id="main-content"]/app-catalog/ion-content/app-content-wrapper/div/div/div/app-catalog-products/div/div[{numero}]/div/div[1]/img'
      format_xpath_color = '//*[@id="main-content"]/app-catalog-product-view/ion-content/app-content-wrapper/div/div/div/div/div[2]/div[3]/div/cart-product-grade/div/table/tbody/tr[{numero}]/td[1]'
      time.sleep(7)
      #Loop para navegar entre os produtos e pegar informações para as colunas.
      for i in range(qtdprodutosinfo):
        
       
        i += 1

        xpath = format_xpath.format(numero=i)
        

        time.sleep(1)
        navegador.find_element_by_xpath(xpath).click()
        time.sleep(0.7)
        
        


        page_content = navegador.page_source


        site = BeautifulSoup(page_content,'lxml')
        

        
        
        try:
          print('\n','Carregando produto: {numero}',xpath)
          produto_preco = site.find("div", attrs={'class' : 'prices'})
          produto_cod = site.find("div", attrs={'class' : 'code'})
          produto_descricao = site.find("div", attrs={'class' : 'description'})
          produto_composição = site.find("div", attrs={'class' : 'composition'})
          produto_fotox = site.find("img", attrs={'class' : 'multipleImg'})
          produto_foto = produto_fotox['src']
          produto_tamanhos = site.find("div", attrs={'class' : 'table-container'})
          corlista = []
        
          #Loop para pegar cores do produto
          for index in range(15):
            
            try:
                index += 1
                xpath = format_xpath_color.format(numero=index)

                time.sleep(0.2)
                navegador.find_element_by_xpath(xpath).click()
                cor = navegador.find_element_by_xpath('//*[@id="ProductColorZoomComponent"]/div[2]/app-product-color-zoom/ion-content/div/div/ion-title')
                corlista.append(cor.text)
                time.sleep(0.6)
                navegador.back()
                time.sleep(0.6)
            except Exception:
                time.sleep(0.1)
                pass
                
                  
          #tamanhos
          df = pd.read_html(page_content,header=0,flavor='bs4')[0]
          df_P = df[['P']]
          df_M = df[['M']]
          df_G = df[['G']]
          df_GG = df[['GG']]
              
        except Exception:
          time.sleep(0.1)
          pass    
          
            
            

        navegador.back()

        

        try:
          dados_produtos.append([produto_cod.text,produto_preco.text,produto_descricao.text,produto_composição.text,produto_foto,corlista,df_P.to_string(index=False),df_M.to_string(index=False),df_G.to_string(index=False),df_GG.to_string(index=False)])#itens linha
        except Exception:
          pass
          
        
        
      #Inseri colunas e salva dados no csv
      dados = pd.DataFrame(dados_produtos ,columns=['Codigo','Preço','Descrição','Composição','Link','Cor','P','M','G','GG'])
      dados.to_excel("produtoskalli_kalli_teste_1904.xlsx") #nome do arquivo que será salvo
      print(dados_produtos)


