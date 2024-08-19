import PySimpleGUI as sg

def create_window(theme):
    sg.theme(theme)
    sg.set_options(font=('Calibri 14'),button_element_size=(20,3))
    btn_size = (6,3)
    layout = [
        [sg.Text('', font= 'Franklin 14', justification='right', expand_x=True, pad=(10,(20,5)), right_click_menu=theme_menu, key='-TEXT1-', background_color='gray')],
        [sg.Text('', font= 'Franklin 26', justification='right', expand_x=True, pad=(10,20), right_click_menu=theme_menu, key='-TEXT2-')],
        [sg.Button('Clear',expand_x= True, expand_y=True),sg.Button('Enter',expand_x= True, expand_y=True)],
        [sg.Button(7, size= btn_size),sg.Button(8, size= btn_size),sg.Button(9, size= btn_size),sg.Button('/', size= btn_size)],
        [sg.Button(4, size= btn_size),sg.Button(5, size= btn_size),sg.Button(6, size= btn_size),sg.Button('*', size= btn_size)],
        [sg.Button(1, size= btn_size),sg.Button(2, size= btn_size),sg.Button(3, size= btn_size),sg.Button('-', size= btn_size)],
        [sg.Button(0, expand_x= True, expand_y=True),sg.Button('.', size= btn_size),sg.Button('+', size= btn_size)],
    ]
    
    return sg.Window('Calculator', layout)

theme_menu = ['menu', ['LightGrey6', 'DarkTeal12', 'DarkGrey7', 'LightBrown8', 'random']]

window = create_window('LightGrey6')

nums_button = list(map(str, range(0,10)))
nums_button += ['.']

current_input = ''
full_input = ''

while True:
    event, values = window.read()
    
    if event in sg.WINDOW_CLOSED:
        break
    
    if event in theme_menu[1]:
        window.close()
        window = create_window(event)
        current_input = ''
        full_input = ''
    
    if event in nums_button:
        current_input += event
        window['-TEXT2-'].update(current_input)
    
    if event in ['*','/','+','-']:
        current_input += event
        full_input += current_input
        window['-TEXT1-'].update(full_input)
        current_input = ''
        window['-TEXT2-'].update(current_input)
        
    if event == 'Enter':
        full_input += current_input
        current_input = ''
        window['-TEXT1-'].update(full_input)
        full_input = str(eval(full_input))
        window['-TEXT2-'].update(full_input)
    
    if event == 'Clear':
        window['-TEXT1-'].update('')
        window['-TEXT2-'].update('')
        current_input = ''
        full_input = ''
        
    
window.close()