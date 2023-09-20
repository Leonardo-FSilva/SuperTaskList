import PySimpleGUI as sg
from front_end import main_screen


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
    elif '+CLICKED+' in event:
        if isinstance(event[2][0], int):
            if event[2][0] == -1:
                ...  # cabeçalho
            elif event[2][0] >= 0:
                ...  # linhas
window.close()