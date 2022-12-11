import PySimpleGUI as sg
from PySimpleGUI import Push, VSeparator
from time import sleep

# Criando a tabela de classificação de IMC
def tabela():

    # Definindo o tema do programa
    sg.theme('black')

    # Criando o 1° layout da tabela
    layout1 = [        
        [sg.HSep(color='#ff1493')],
        [sg.Text('Classificação', font='Times 30 bold', size=15, text_color='#ff1493')],
        [sg.HSeparator(color='#ff1493')],

        [sg.Text('Abaixo do Peso', font='Times 20')],
        [sg.HSeparator(color='#ff1493')],
        
        [sg.Text('Peso Normal', font='Times 20')],
        [sg.HSeparator(color='#ff1493')],

        [sg.Text('Sobrepeso', font='Times 20')],
        [sg.HSeparator(color='#ff1493')],

        [sg.Text('Obesidade (Grau I)', font='Times 20')],
        [sg.HSeparator(color='#ff1493')],

        [sg.Text('Obesidade (Grau II)', font='Times 20')],
        [sg.HSeparator(color='#ff1493')],

        [sg.Text('Obesidade (Grau III)', font='Times 20')]
    ]

# Criando o 2° layout da tabela
    layout2 = [
        # Criando o título do programa
        [sg.HSeparator(color='#ff1493')],
        [Push(), sg.Text('IMC', font='Times 30 bold', text_color='#ff1493'), Push()],
        [sg.HSeparator(color='#ff1493')],

        [Push(), sg.Text('Abaixo de 18,5', font='Times 20'), Push()],
        [sg.HSeparator(color='#ff1493')],

        [Push(), sg.Text('18,5 - 24,9', font='Times 20'), Push()],
        [sg.HSeparator(color='#ff1493')],

        [Push(), sg.Text('25 - 29,9', font='Times 20'), Push()],
        [sg.HSeparator(color='#ff1493')],

        [Push(), sg.Text('30 - 34,9', font='Times 20'), Push()],
        [sg.HSeparator(color='#ff1493')],

        [Push(), sg.Text('35 - 39,9', font='Times 20'), Push()],
        [sg.HSeparator(color='#ff1493')],

        [Push(), sg.Text('Maior ou Igual à 40', font='Times 20'), Push()]
    ]

# Criando o layout completo da tabela unidos os dois anteriores
    mainly_layout = [[sg.Column(layout1),
                     VSeparator(color='#ff1493'),
                     sg.Column(layout2)]]

# Criando a janela que irá interagir com o usuário
    window1 = sg.Window('Para Fazer Um Novo Cálculo Feche Essa Janela',
                        layout=mainly_layout, border_depth=3,
                        location=(600, 120), finalize=True)

    window1.bind('<Escape>', '_esc')

    while True:
        event, values = window1.read()

        if event == sg.WIN_CLOSED:
            break
        elif event == '_esc':
            window1.close()


# ----- Mainly Program -----
def calculo_imc():
    # Layout principal do programa
    layout = [
        [sg.Text('__' * 32, text_color='#ff1493', background_color='#000')],

        [Push(background_color='#000'),
         sg.Text('Calculadora IMC'.center(25), font='Times 30 bold',
         background_color='#000', size=(18, 1), text_color='#FF1493'),
         Push(background_color='#000')],

        [sg.Text('__' * 32, text_color='#ff1493', background_color='#000')],

        [sg.Text('Sexo ', font='Times 40', background_color='#000',
         text_color='#F8F8FF', size=5),
         sg.Checkbox('♂', 'group 1', background_color='black',
                  text_color='#00FFFF', key='masc', font='Times 20'),
         sg.Checkbox('♀', 'group 2', background_color='black',
                  text_color='#ff1493', key='fem', font='Times 20')],

        [sg.Text('Idade', font='Times 40', background_color='#000',
         text_color='#F8F8FF', size=5),
         sg.I(font='Times 30', size=6)],

        [sg.Text('Peso', font='Times 40', background_color='#000',
         text_color='#F8F8FF', size=5),
         sg.I(font='Times 30', size=6, key='kg'),
         sg.Text('Kg', font='Times 40', background_color='#000',
         text_color='#ff1493')],

        [sg.Text('Altura', font='Times 40', background_color='#000',
         text_color='#F8F8FF', size=5),
         sg.I(font='Times 30', size=6, key='altura'),
         sg.Text('M', font='Times 40', background_color='#000',
         text_color='#FF1493')],

        [Push(background_color='#000'),
         sg.B('Calcular IMC', size=(50, 2), key='IMC',
         button_color='#FF1493', font='Times 11', border_width=15),
         Push(background_color='#000')],

        [Push(background_color='#000'),
         sg.Text(font='Times 25', background_color='#000',
         text_color='#f8f8ff', key='output'),
         Push(background_color='#000')]
    ]

    # Janela do programa 
    window = sg.Window('Calculadora IMC do Tom',
                       layout=layout, background_color='#000', border_depth=6,
                       location=(100, 120), finalize=True)

    while True:
        events, values = window.read()

        if events == sg.WIN_CLOSED:
            break
        elif events in 'IMC':
            p = str(values['kg']).replace(',', '.')
            a = str(values['altura']).replace(',', '.')
            peso = float(p)
            altura = float(a)
            imc = peso / (altura * altura)
            window['output'].update(f'O seu IMC é {float(imc):.2f}')
            tabela()


calculo_imc()