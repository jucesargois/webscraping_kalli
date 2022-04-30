from PySimpleGUI import PySimpleGUI as sg

#LayoutLogin
sg.theme('Reddit')
teste = '2'
layoutLogin = [
    [sg.Text('Usuário'), sg.Input(key='usuario')],
    [sg.Text('Senha'), sg.Input(key='senha',password_char='*')],
    [sg.Button('Entrar')],
    
]

#LayoutQtdProd
layoutQtdProd = [
  [
    sg.Text('Qtd produtos:'), sg.Input(key='qtdprodutos',size=(20,1)), 
    sg.Button('Confirmar'),
  ]
]
#Layoutloading
layoutLoading = [
  [sg.Text('Carregando:')],
  [sg.Text(teste)]

]



#Janela
janela1 = sg.Window('Login site(Utilizar login e senha que foram cadastrados no site)',layoutLogin)
janela2 = sg.Window('Inserir quantidade de produtos',layoutQtdProd)
janela3 = sg.Window('Carregando',layoutLoading)
#Ler eventos
while True:
  eventos1, valores1 = janela1.read()
  if eventos1 == sg.WIN_CLOSED:
    break
  if eventos1 == 'Entrar':
    if valores1['usuario'] != '' and valores1['senha'] != '':
      janela1.close()
      eventos2, valores2 = janela2.read()
      if valores2['qtdprodutos'] != '':
          eventos3, valores3 = janela3.read()
        
        

      