import PySimpleGUI as sg
import front_end as f_end


window = sg.Window('Window Title', f_end.layout_main_screen)

i = 1

while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == '-ADD COL-':
        new_task_window = sg.Window('Window Title', f_end.layout_create_new_task())
        while True:             # Event Loop
            event, values = new_task_window.read()
            if event in (sg.WIN_CLOSED, 'Cancelar'):
                break
            if event == 'Criar tarefa':
                nome_tarefa = values['-NOMETAREFA-']
                referencia = values['-REFERENCIA-']
                prioridade = values['PRIORIDADE'][0]
                tipo_tarefa = values['TIPOTAREFA'][0]

                new_task_window.close()
        window.extend_layout(window['-COL-'], [[sg.T(i), sg.B(nome_tarefa, key=f'botao_tarefa{i}'), sg.T(f'{referencia} | {prioridade} | {tipo_tarefa}')]])
        window.visibility_changed()
        window['-COL-'].contents_changed()
    elif event[0:12] == 'botao_tarefa':
        tarefa_numero = event[12:]
        decr_window = sg.Window('Window Title', f_end.open_task_description())
        while True:             # Event Loop
            event, values = decr_window.read()
            if event in (sg.WIN_CLOSED, 'Voltar'):
                break
            elif event == 'Criar descrição':
                create_description_window = sg.Window('Window Title', f_end.create_task_description())
                while True:
                    event, values = create_description_window.read()
                    if event in (sg.WIN_CLOSED, 'Voltar'):
                        break    
                    elif event == "Salvar":
                        descricao_tarefa = values['descr_tarefa']
                        create_description_window.close()
                        decr_window['open_descr_tarefa'].update(descricao_tarefa)
                        break
        
    i += 1

window.close()