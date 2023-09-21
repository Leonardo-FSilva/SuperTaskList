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
        [sg.Button('Próximos', button_color=('black', 'lightgray'),size=(10,2))],
        [sg.Button('Fazendo', button_color=('black', 'yellow'),size=(10,2))],
        [sg.Button('Concluídos', button_color=('black', 'green'),size=(10,2))],
        [sg.Text()],
        [sg.Button('Outros', button_color=('black', '#FFA500'),size=(10,1))],
        [sg.Button('Compras', button_color=('white', '#0000FF'),size=(10,1))],
        [sg.Button('Projetos', button_color=('black', '#FFFF00'),size=(10,1))],
        [sg.Button('Manutenção', button_color=('black', '#FF0000'),size=(10,1))],
        [sg.Button('Programação', button_color=('black', '#00FF00'),size=(10,1))]]

def right_block():
    return [
        [sg.Table(
            justification='left',
            key='table_task_list',
            values=dm.read_data_base('leo_task_list'),
            headings=('Id','Data','Nome','Status','Prioridade','Referencias'),
            size=(60,20),
            enable_click_events=True,
            enable_events=True,
            expand_x=True)
        ]
    ]

def popup_task(nome, status, prioridade, referencia, tipo, conteudo, foto=''):
    return [
        [sg.Text('None da tarefa:'), sg.Input(key='-newtaskname-',size=(31), default_text=nome), sg.Push(), sg.Text('Prioridade:'), sg.Combo(['Alta','Media','Baixa'],readonly=True,key='-newtaskprioridade-', default_value=prioridade)],
        [sg.Text('Referencias:'),sg.Input(key='-newtaskreference-',size=(20), default_text=referencia), sg.Push(),sg.Text('Status:'),sg.Combo(['Proximo','Fazendo','Concluído'],default_value=status,readonly=True,key='-newtaskstatus-'), sg.Text('Tipo:'), sg.Combo(['Manutenção','Compras','Projetos','Programação','Outros'],default_value=tipo,readonly=True,key='-newtasktipo-')],
        # [ sg.Push(),sg.Text('Leonardo Felipe da Silva'), sg.Push()],
        [sg.Multiline(size=(75,20),
                	expand_y=True,
                    expand_x=True,
                    default_text=conteudo,
                    key='-newtaskconteudo-')],
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
    window = sg.Window('Window Title', popup_task('gg','gg','f','d','s','d\nkhu','w'))

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
