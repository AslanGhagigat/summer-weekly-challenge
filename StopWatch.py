import PySimpleGUI as sg
from time import time

sg.theme('black')

layout = [
    [sg.Push(),sg.Image('Cross.png', key='-CLOSE-', pad=0, enable_events=True,)],
    [sg.VPush()],
    [sg.Text('Timer', font = "Young 40", key='-TIME-')],
    [
        sg.Button('Start', button_color=('#ffffff','#ff0000'), border_width=0, key='-STARTSTOP-'),
        sg.Button('Lap', button_color=('#ffffff','#ff0000'), border_width=0, key='-LAP-', visible= False)
    ],
    [sg.Text(key='-LAPTIME-')],
    [sg.VPush()],
]

window = sg.Window("Stopwatch", layout, size=(300,300), no_titlebar= True,element_justification='center')

start_time = 0
active = False
lap_time = ''
lap_count = 1

while True:
    event, values = window.read(timeout= 10)
    if event in (sg.WIN_CLOSED, '-CLOSE-'):
        break

    if event == '-STARTSTOP-':
        if active:
            # Timer is active
            active = False
            start_time = time()
            window['-STARTSTOP-'].update('Reset')
            window['-LAP-'].update(visible = False)
        else:
            # Reset Timer
            if start_time > 0:
                window['-TIME-'].update('Timer')
                window['-STARTSTOP-'].update('Start')
                lap_time = ''
                window['-LAPTIME-'].update(lap_time)
                lap_count = 1
                start_time = 0
            # Start Timer
            else:
                start_time = time()
                active = True
                window['-STARTSTOP-'].update('Stop')
                window['-LAP-'].update(visible = True)
        
    
    if event == '-LAP-':
        lap_time += f'{lap_count} | {str(round(time() - start_time, 1))}\n'
        window['-LAPTIME-'].update(lap_time)
        lap_count += 1
        
    if active:
        elapsed_time = round(time() - start_time, 1)
        window['-TIME-'].update(elapsed_time)
    


window.close()