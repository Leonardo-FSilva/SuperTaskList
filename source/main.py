import PySimpleGUI as sg
from datetime import datetime

from front_end import main_screen, popup_create_new_task
import database_manager


sg.theme('dark')
window = sg.Window('Window Title', main_screen())

_visibility=''

while True:
    event, values = window.read()
    print('\nevent: ', event, '\nvalue: ', values)
    if event in (sg.WIN_CLOSED, 'Sair'):
        break
    elif event == 'Manutenção':
        if _visibility == 'Manutenção':
            window['-table_task_list-'].update(visible=False)
            window['-sub_title-'].update('')
            _visibility = ''
        else:
            window['-table_task_list-'].update(visible=True)
            window['-sub_title-'].update('Abaixo todas as tarefas')
            _visibility = 'Manutenção'
    elif event == 'Compras':
        if _visibility == 'Compras':
            window['-table_task_list-'].update(visible=False)
            window['-sub_title-'].update('')
            _visibility = ''
        else:
            window['-table_task_list-'].update(visible=True)
            window['-sub_title-'].update('Abaixo todas as tarefas')
            _visibility = 'Compras'
    elif event == 'Projetos':
        if _visibility == 'Projetos':
            window['-table_task_list-'].update(visible=False)
            window['-sub_title-'].update('')
            _visibility = ''
        else:
            window['-table_task_list-'].update(visible=True)
            window['-sub_title-'].update('Abaixo todas as tarefas')
            _visibility = 'Projetos'
    elif event == 'Outros':
        if _visibility == 'Outros':
            window['-table_task_list-'].update(visible=False)
            window['-sub_title-'].update('')
            _visibility = ''
        else:
            window['-table_task_list-'].update(visible=True)
            window['-sub_title-'].update('Abaixo todas as tarefas')
            _visibility = 'Outros'
    elif event == 'Todos':
        if _visibility == 'Todos':
            window['-table_task_list-'].update(visible=False)
            window['-sub_title-'].update('')
            _visibility = ''
        else:
            window['-table_task_list-'].update(visible=True)
            window['-sub_title-'].update('Abaixo todas as tarefas')
            _visibility = 'Todos'
    elif event == 'Add tarefa':
        win_new_desk = sg.Window('Criar uma nova tarefa', popup_create_new_task())
        while True:
            events, values = win_new_desk.read()
            print('\nevent: ', event, '\nvalue: ', values)
            if event in (sg.WIN_CLOSED, 'Sair'):
                break
            elif event == 'Add tarefa':
                _today_date = datetime.today()
                print(_today_date)
                # database_manager.input_data_base('leo_task_list', _today_date)
    elif '+CLICKED+' in event:
        if isinstance(event[2][0], int):
            if event[2][0] == -1:
                ...  # cabeçalho
            elif event[2][0] >= 0:
                ...

window.close()