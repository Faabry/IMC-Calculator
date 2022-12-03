import PySimpleGUI as sg
from PySimpleGUI import Push


layout = [
    [sg.Text('__' * 32, text_color='#ff1493', background_color='#000')],

    [Push(background_color='#000'),
     sg.Text('Calculadora IMC'.center(25), font='Times 30 bold',
     background_color='#000', size=(18, 1), text_color='#FF1493'),
     Push(background_color='#000')],

    [sg.Text('__' * 32, text_color='#ff1493', background_color='#000')],

    [sg.Text('Sexo ', font='Times 40', background_color='#000',
     text_color='#F8F8FF', size=5),
     sg.B('♂', size=(6, 2), button_color='#48d1cc on #000',
     font='Times', key='masc'),
     sg.B('♀', size=(6, 2), button_color='#ff1493 on #000',
     font='Times', key='fem')],

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

window = sg.Window('Calculadora IMC do Tom',
                   layout=layout, background_color='#000', border_depth=6)


while True:
    events, values = window.read()

    if events == sg.WIN_CLOSED or events == 'Sair':
        break
    elif events == 'IMC':
        p = str(values['kg']).replace(',', '.')
        a = str(values['altura']).replace(',', '.')
        peso = float(p)
        altura = float(a)
        imc = peso / (altura * altura)
        window['output'].update(f'O seu IMC é {float(imc):.2f}')
