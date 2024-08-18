import PySimpleGUI as sg
from numpy import full

# ['Black', 'Black2', 'BlueMono', 'BluePurple', 'BrightColors', 'BrownBlue', 'Dark', 'Dark2', 'DarkAmber', 'DarkBlack', 'DarkBlack1', 'DarkBlue', 'DarkBlue1', 'DarkBlue10', 'DarkBlue11', 'DarkBlue12', 'DarkBlue13', 'DarkBlue14', 'DarkBlue15', 'DarkBlue16', 'DarkBlue17', 'DarkBlue18', 'DarkBlue2', 'DarkBlue3', 'DarkBlue4', 'DarkBlue5', 'DarkBlue6', 'DarkBlue7', 'DarkBlue8', 'DarkBlue9', 'DarkBrown', 'DarkBrown1', 'DarkBrown2', 'DarkBrown3', 'DarkBrown4', 'DarkBrown5', 'DarkBrown6', 'DarkBrown7', 'DarkGreen', 'DarkGreen1', 'DarkGreen2', 'DarkGreen3', 'DarkGreen4', 'DarkGreen5', 'DarkGreen6', 'DarkGreen7', 'DarkGrey', 'DarkGrey1', 'DarkGrey10', 'DarkGrey11', 'DarkGrey12', 'DarkGrey13', 'DarkGrey14', 'DarkGrey15', 'DarkGrey16', 'DarkGrey2', 'DarkGrey3', 'DarkGrey4', 'DarkGrey5', 'DarkGrey6', 'DarkGrey7', 'DarkGrey8', 'DarkGrey9', 'DarkPurple', 'DarkPurple1', 'DarkPurple2', 'DarkPurple3', 'DarkPurple4', 'DarkPurple5', 'DarkPurple6', 'DarkPurple7', 'DarkRed', 'DarkRed1', 'DarkRed2', 'DarkTanBlue', 'DarkTeal', 'DarkTeal1', 'DarkTeal10', 'DarkTeal11', 'DarkTeal12', 'DarkTeal2', 'DarkTeal3', 'DarkTeal4', 'DarkTeal5', 'DarkTeal6', 'DarkTeal7', 'DarkTeal8', 'DarkTeal9', 'Default', 'Default1', 'DefaultNoMoreNagging', 'GrayGrayGray', 'Green', 'GreenMono', 'GreenTan', 'HotDogStand', 'Kayak', 'LightBlue', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4', 'LightBlue5', 'LightBlue6', 'LightBlue7', 'LightBrown', 'LightBrown1', 'LightBrown10', 'LightBrown11', 'LightBrown12', 'LightBrown13', 'LightBrown2', 'LightBrown3', 'LightBrown4', 'LightBrown5', 'LightBrown6', 'LightBrown7', 'LightBrown8', 'LightBrown9', 'LightGray1', 'LightGreen', 'LightGreen1', 'LightGreen10', 'LightGreen2', 'LightGreen3', 'LightGreen4', 'LightGreen5', 'LightGreen6', 'LightGreen7', 'LightGreen8', 'LightGreen9', 'LightGrey', 'LightGrey1', 'LightGrey2', 'LightGrey3', 'LightGrey4', 'LightGrey5', 'LightGrey6', 'LightPurple', 'LighthonPlus', 'Reddit', 'Reds', 'SandyBeach', 'SystemDefault', 'SystemDefault1', 'SystemDefaultForReal', 'Tan', 'TanBlue', 'TealMono', 'Topanga']

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
    
    if event == sg.WINDOW_CLOSED:
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