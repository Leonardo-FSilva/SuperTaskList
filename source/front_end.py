import PySimpleGUI as sg
from back_end import update_report

def main_screen():
    return [
        [sg.Menu([['Arquivo',['Local do arquivo','Requisitos de sistema','Creditos']],
                  ['Exibir',['Historico de concluidos','Log de erros']],
                  ['Sistema',['Sair','Trocar usuario', 'Adicionar lembretes']]])],

        [sg.Push(), sg.Text('\n-- SUPER TASK LIST --',font=('Roboto Condensed', 20, 'bold')), sg.Push()],
        [sg.Push(), sg.Text(key='-sub_title-',font=('Roboto Condensed', 12)), sg.Push()],
        [sg.Col(left_block()),sg.Col(right_block())],
        [sg.Push(),sg.Button('Add tarefa'),sg.Button('Sair')]]

def left_block():
    return [
        [sg.Button('Manutenção', button_color=('black', 'red'),size=(10,3))],
        [sg.Button('Compras', button_color=('black', 'green'),size=(10,3))],
        [sg.Button('Projetos', button_color=('white', 'blue'),size=(10,3))],
        [sg.Button('Programação', button_color=('black', 'orange'),size=(10,3))],
        [sg.Button('Outros', button_color=('black', 'yellow'),size=(10,3))],
    ]

def right_block():
    return [
        [sg.Table(
            justification='left',
            key='-table_task_list-',
            values=update_report(),
            headings=('Data','Nome','Status','Prioridade','Tipo','Referencias'),
            size=(50,20),
            enable_click_events=True,
            enable_events=True)
        ]
    ]


if __name__ == '__main__':
    sg.theme('dark')
    window = sg.Window('Window Title', main_screen())

    _visibility=False

    while True:
        event, values = window.read()
        print('\nevent: ', event, '\nvalue: ', values)
        if event in (sg.WIN_CLOSED, 'Sair'):
            break
        elif event == 'Todos':
            if _visibility:
                window['-table_task_list-'].update(visible=False)
                window['-sub_title-'].update('')
                _visibility = False
            else:
                window['-table_task_list-'].update(visible=True)
                window['-sub_title-'].update('Abaixo todas as tarefas')
                _visibility = True
    window.close()
