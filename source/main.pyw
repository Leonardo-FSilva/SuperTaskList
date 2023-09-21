import PySimpleGUI as sg
from datetime import datetime

from front_end import main_screen, popup_create_new_task,popup_task
import database_manager as dm


sg.theme('dark')
window = sg.Window('Super Task List', main_screen(), resizable=True)

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
                    values['-newtaskprioridade-'],
                    values['-newtasktipo-'],
                    values['-newtaskreference-'])

                win_new_desk.close()
                window['table_task_list'].update(
                    values=dm.read_data_base('leo_task_list'))
                break
    elif '+CLICKED+' in event:
        if isinstance(event[2][0], int):
            if event[2][0] == -1:
                ...  # cabeçalho
            elif event[2][0] >= 0:
                _index = event[2][0]

                _task_report = dm.read_data_base('leo_task_list')
                _id_item = _task_report[_index][0]
                _data = _task_report[_index][1]
                _nome = _task_report[_index][2]
                _status = _task_report[_index][3]
                _prioridade = _task_report[_index][4]
                _referencia = _task_report[_index][5]
                _tipo = _task_report[_index][6]
                _conteudo = _task_report[_index][7]
                _foto = _task_report[_index][8]

                window_task = sg.Window('Tarefa', popup_task(_nome, _status, _prioridade, _referencia, _tipo, _conteudo, _foto), resizable=True)
                while True:
                    event, values = window_task.read()
                    if event in (sg.WIN_CLOSED, 'Sair'):
                        break   
                    elif event == '-savetask-':
                        new_nome = values['-newtaskname-']
                        new_status = values['-newtaskstatus-']
                        new_prioridade = values['-newtaskprioridade-']
                        new_referencia = values['-newtaskreference-']
                        new_tipo = values['-newtasktipo-']
                        new_conteudo = values['-newtaskconteudo-']

                        dm.edit_item('leo_task_list', int(_id_item), str(new_nome), str(new_status),
                        str(new_prioridade), str(new_referencia), str(new_tipo), str(new_conteudo))

                        window['table_task_list'].update(
                            values=dm.read_data_base('leo_task_list'))
                        window_task.close()

                    elif event == 'Apagar tarefa':
                        dm.delete_item('leo_task_list', id_item)
                        window['table_task_list'].update(
                            values=dm.read_data_base('leo_task_list'))
                        window_task.close()
window.close()