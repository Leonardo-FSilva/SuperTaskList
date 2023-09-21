import PySimpleGUI as sg
from datetime import datetime

from front_end import main_screen, popup_create_new_task,popup_task
import database_manager as dm


sg.theme('dark')
window = sg.Window('Window Title', main_screen(), resizable=True)

_visibility=''

while True:
    event, values = window.read()
    print('\nevent: ', event, '\nvalue: ', values)
    if event in (sg.WIN_CLOSED, 'Sair'):
        break
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
            event, values = win_new_desk.read()
            print('\nevent: ', event, '\nvalue: ', values)
            if event in (sg.WIN_CLOSED, 'Sair'):
                break
            elif event == '-createtask-':
                _today_date = datetime.today()
                _today_date = str(_today_date)[:10]
                dm.input_data_base(
                    'leo_task_list', 
                    _today_date, 
                    values['-newtaskname-'],
                    "Proximo",
                    values['-newtasktipo-'],
                    values['-newtaskprioridade-'])
                win_new_desk.close()
                window['table_task_list'].update(
                    values=dm.read_data_base('leo_task_list'))
                break
    elif '+CLICKED+' in event:
        if isinstance(event[2][0], int):
            if event[2][0] == -1:
                ...  # cabeçalho
            elif event[2][0] >= 0:
                id_item = dm.read_data_base('leo_task_list')
                id_item = id_item[event[2][0]][0]
                window_task = sg.Window('Tarefa', popup_task(), resizable=True)
                while True:
                    event, values = window_task.read()
                    if event in (sg.WIN_CLOSED, 'Sair'):
                        break   
                    elif event == 'Apagar tarefa':
                        dm.delete_item('leo_task_list', id_item)
                        print(id_item)
                        window['table_task_list'].update(
                            values=dm.read_data_base('leo_task_list'))
                        window_task.close()
window.close()