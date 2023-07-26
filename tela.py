import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        
        #layout
        layout =[
            [sg.Text('Nome',size=(5,0)), sg.Input(size=(15,0),key='nome')],
            [sg.Text('idade',size=(5,0)), sg.Input(size=(15,0),key='idade')],
            [sg.Text('Quais provedores são aceitos')],
            [sg.Checkbox('Gmail',key='gmail'),sg.Checkbox('Outlook',key='outlook'),sg.Checkbox('Yahoo',key='yahoo')],
            [sg.Text('Aceita cartão')],
            [sg.Radio('Sim','cartao',key='aceitaCartao'),sg.Radio('Não','cartao',key='naoAceitaCartao')],            
            [sg.Slider(range=(0,255),default_value=0,orientation='h',size=(15,20),key='sliderVelocidade')],
            [sg.Button('Enviar dados')],
            [sg.Output(size=(300,200))]
        ]
        #Janela
        self.janela = sg.Window('Dados do usuario',size=(800,600)).layout(layout)
        

    def iniciar(self):
        while True:
            # Extrair os dados da tela
            self.button, self.values = self.janela.read()

            nome = self.values['nome']
            idade = self.values['idade']
            aceita_gmail = self.values['gmail']
            aceita_outlook = self.values['outlook']
            aceita_yahoo = self.values['yahoo']
            aceita_cartao = self.values['aceitaCartao']
            nao_aceita_cartao = self.values['naoAceitaCartao']
            velocidade_script = self.values['sliderVelocidade']
            print(f'Nome: {nome}')
            print(f'Ideade: {idade}')
            print(f'Aceita gmail {aceita_gmail}')
            print(f'Aceita outlook {aceita_outlook}')
            print(f'Aceita yahoo {aceita_yahoo}')
            print(f'Aceita Cartão {aceita_cartao}')
            print(f'Nao Aceita Cartão {nao_aceita_cartao}')
            print(f'Velocidade Script: {velocidade_script}')



tela = TelaPython()
tela.iniciar()



