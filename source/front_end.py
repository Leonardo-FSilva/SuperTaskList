import PySimpleGUI as sg


layout_main_screen = [  [sg.Text('My Window')],
            [sg.Col([[sg.T('Tarefas'), sg.Push()]], scrollable=True, key='-COL-', s=(500,250))],
            [sg.Text('Click to add a row inside the Column'), sg.B('+', key='-ADD COL-')]]

def layout_create_new_task():
    new_task_layout =   [[sg.T('Nome da tarefa:'), sg.I(size=(25), key='-NOMETAREFA-')],
                        [sg.Push(), sg.T('Referencias:'), sg.I(size=(25), key='-REFERENCIA-')],
                        [sg.Combo([['Baixa'], ['Media'], ['Alta']], size=(8), key='PRIORIDADE'),
                        sg.Combo([['Projetos'], ['Compras'], ['Manutenção'], ['Outros']], size=(10), key='TIPOTAREFA')],
                        [sg.B('Criar tarefa'), sg.B('Cancelar')]]
    return new_task_layout

def open_task_description():
    layout  =  [[sg.T('descição da tarefa:')],
                [sg.T('Sem Descrição...', size=(65,15), key='open_descr_tarefa')],
                [sg.B('Criar descrição'), sg.B('Voltar')]]
    return layout

def create_task_description():
    layout =   [[sg.T('descição da tarefa:')],
                [sg.I(size=(50,25), key='descr_tarefa')],
                [sg.B('Salvar'), sg.B('Voltar')]]
    return layout

if __name__ == '__main__':
    layout = open_task_description()

    window = sg.Window('Window Title', layout)
    while True:
        event, values = window.read()
        print('\nevent: ', event, '\nvalue: ', values)
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
    window.close()