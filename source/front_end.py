import PySimpleGUI as sg
from back_end import update_report
import database_manager as dm

def main_screen():
    return [
        [sg.Menu([['Arquivo',['Local do arquivo','Requisitos de sistema','Créditos']],
                  ['Exibir',['Históricos de concluídos','Log de erros']],
                  ['Sistema',['Sair','Trocar usuário', 'Adicionar lembretes']]])],

        [sg.Push(), sg.Text('\n-- SUPER TASK LIST --',font=('Roboto Condensed', 20, 'bold')), sg.Push()],
        [sg.Push(), sg.Text(key='-sub_title-',font=('Roboto Condensed', 12)), sg.Push()],
        [sg.Col(left_block()),sg.Col(right_block())],
        [sg.Push(),sg.Button('Add tarefa'),sg.Button('Sair')]]

def left_block():
    return [
        [sg.Button('Próximos', button_color=('black', 'lightgray'),size=(10,3))],
        [sg.Button('Fazendo', button_color=('black', 'yellow'),size=(10,3))],
        [sg.Button('Concluídos', button_color=('black', 'green'),size=(10,3))],
    ]

def right_block():
    return [
        [sg.Table(
            justification='left',
            key='table_task_list',
            values=dm.read_data_base('leo_task_list'),
            headings=('Índice','Data','Nome','Status','Prioridade','Referencias'),
            size=(60,20),
            enable_click_events=True,
            enable_events=True,
            expand_x=True)
        ]
    ]

def popup_task():

    return [
        [sg.Text('None da tarefa:'), sg.Input(key='-newtaskname-',size=(31)), sg.Push(), sg.Text('Prioridade:'), sg.Combo(['Alta','Média','Baixa'],readonly=True,key='-newtaskprioridade-')],
        [sg.Text('Referencias ou observações:'),sg.Input(key='-newtaskreference-',size=(20)), sg.Push(), sg.Text('Tipo:'), sg.Combo(['Manutenção','Compras','Projetos','Programação','Outros'],readonly=True,key='-newtasktipo-')],
        # [ sg.Push(),sg.Text('Leonardo Felipe da Silva'), sg.Push()],
        [sg.Multiline(size=(75,20),
                	expand_y=True,
                    expand_x=True)],
        [sg.Button("Anexar Imagem"), sg.Push(),sg.Button("Apagar tarefa"),sg.Button('Salvar',key='-savetask-'),sg.Button('Sair')]        
    ]
def popup_create_new_task():
    return [
        [sg.Text('None da tarefa:'), sg.Input(key='-newtaskname-',size=(30))],
        [sg.Text('Prioridade:'), sg.Combo(['Alta','Média','Baixa'],readonly=True,key='-newtaskprioridade-'), sg.Text('Tipo:'), sg.Combo(['Manutenção','Compras','Projetos','Programação','Outros'],readonly=True,key='-newtasktipo-')],
        [sg.Text('Referencias ou observações:'),sg.Input(key='-newtaskreference-',size=(20))],
        [sg.Button('Criar tarefa',key='-createtask-'),sg.Button('Sair')]
    ]


if __name__ == '__main__':
    sg.theme('dark')
    window = sg.Window('Window Title', popup_task())

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
