import PySimpleGUI as sg

unit_combo = ['Length', 'Mass'] #, 'Speed', 'Area'
dict = {'Length': ['Kilometer - km', 'Meter - m', 'Mile - mi'], 'Mass': ['Kilogram - kg', 'Pound - lb']}
source_combo = []
goal_combo = []
layout = [
    [sg.Text("Please select Unit :"), sg.Combo(unit_combo, key='-UNIT-COMBO-', readonly=True), sg.Button('Submit', key='btn1')],
    [sg.Combo(values= source_combo, key='-SOURCE-COMBO-', size=(15,3), readonly= True), sg.Input(key= '-SOURCE-INPUT-', size=(25,3)), sg.Button('Convert', key='btn2')],
    [sg.Combo(values= goal_combo, key='-GOAL-COMBO-', size=(15,3), readonly= True), sg.Text(key= '-GOAL-TEXT-')]
]

window = sg.Window("Converter", layout, size=(400,110))

def print_text(n: float):
    window['-GOAL-TEXT-'].update(f'Answer is => {n:.2f} {values['-GOAL-COMBO-'][-2:]}')

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
    
    if event == 'btn1':
        if values['-UNIT-COMBO-'] == 'Mass':
            window['-SOURCE-COMBO-'].update(values=dict['Mass'], value='Kilogram - kg', size=(15,3))
            window['-GOAL-COMBO-'].update(values=dict['Mass'], value='Pound - lb', size=(15,3))
        elif values['-UNIT-COMBO-'] == 'Length':
            window['-SOURCE-COMBO-'].update(values=dict['Length'], value='Kilometer - km', size=(15,3))
            window['-GOAL-COMBO-'].update(values=dict['Length'], value='Mile - mi', size=(15,3))
    
    if event == 'btn2' and values['-SOURCE-INPUT-']:
        input = values['-SOURCE-INPUT-']
        if input.isnumeric():
            input = int(input)
            if values['-SOURCE-COMBO-'] == values['-GOAL-COMBO-']:
                print_text(input)

            elif values['-UNIT-COMBO-'] == 'Mass':
                if values['-SOURCE-COMBO-'] == 'Kilogram - kg' and values['-GOAL-COMBO-'] == 'Pound - lb':
                    print_text(input*2.20462262)
                elif values['-SOURCE-COMBO-'] == 'Pound - lb' and values['-GOAL-COMBO-'] == 'Kilogram - kg':
                    print_text(input*0.45359237)

            elif values['-UNIT-COMBO-'] == 'Length':
                if values['-SOURCE-COMBO-'] == 'Kilometer - km' and values['-GOAL-COMBO-'] == 'Meter - m':
                    print_text(input*1000)
                elif values['-SOURCE-COMBO-'] == 'Kilometer - km' and values['-GOAL-COMBO-'] == 'Mile - mi':
                    print_text(input*0.621371192)
                elif values['-SOURCE-COMBO-'] == 'Meter - m' and values['-GOAL-COMBO-'] == 'Kilometer - km':
                    print_text(input*0.001)
                elif values['-SOURCE-COMBO-'] == 'Meter - m' and values['-GOAL-COMBO-'] == 'Mile - mi':
                    print_text(input*0.000621371192)
                elif values['-SOURCE-COMBO-'] == 'Mile - mi' and values['-GOAL-COMBO-'] == 'Kilometer - km':
                    print_text(input*1.609344)
                elif values['-SOURCE-COMBO-'] == 'Mile - mi' and values['-GOAL-COMBO-'] == 'Meter - m':
                    print_text(input*1609.344)

window.close()