import sqlite3
import os
from pathlib import Path

ABSOLUTE_PATH = Path(__file__).parent.parent

def set_file_path(file_name):
    file_name = file_name + ".db"
    folder_name = "configuration"
    full_path_file = os.path.join(ABSOLUTE_PATH, folder_name, file_name)
    return full_path_file

def input_data_base(name_data_base, data, nome, status, prioridade, tipo, referencias='', conteudo='', foto=''):  # create an data base
    full_path_file = set_file_path(name_data_base)
    conn = sqlite3.connect(full_path_file)
    
    cursor = conn.cursor()
    # cursor.execute('''
    #     CREATE TABLE IF NOT EXISTS tasks (
    #         id INTEGER PRIMARY KEY,
    #         data DATE,
    #         nome TEXT,
    #         status TEXT,
    #         prioridade TEXT,
    #         referencias TEXT,
    #         tipo TEXT,
    #         conteudo TEXT,
    #         foto BLOB)''')
   
    # input datas
    cursor.execute("INSERT INTO tasks (data, nome, status, prioridade, referencias, tipo, conteudo, foto) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", 
        (data, nome, status, prioridade, referencias, tipo, conteudo, foto))
    
    # save datas
    conn.commit()

    # close data base
    conn.close()

def read_data_base(name_data_base):
    full_path_file = set_file_path(name_data_base)
    conn = sqlite3.connect(full_path_file)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()

    listing_datas = []
    for row in rows:
        listing_datas.append(list(row))
    conn.close()

    return listing_datas
        # print(type(row))

def delete_item(name_db, id_a_excluir):
    full_path_file = set_file_path(name_db)
    # Conectar ao banco de dados
    conn = sqlite3.connect(full_path_file)
    cursor = conn.cursor()

    # Excluir um registro com base no critério (nesse caso, pelo id)
    
    cursor.execute("DELETE FROM tasks WHERE id=?", (id_a_excluir,))

    # Confirmar a transação e fechar a conexão
    conn.commit()
    conn.close()

def edit_item(name_data_base, _id, nome, status, prioridade, referencias, tipo, conteudo):
    full_path_file = set_file_path(name_data_base)
    # Conectar ao banco de dados
    conn = sqlite3.connect(full_path_file)
    cursor = conn.cursor()

    # Execute a instrução SQL UPDATE
    cursor.execute("UPDATE tasks SET nome=?, status=?, prioridade=?, referencias=?, tipo=?, conteudo=? WHERE id=?", (nome, status, prioridade, referencias, tipo, conteudo, _id))

    # Confirmar a transação e fechar a conexão
    conn.commit()
    conn.close()

if __name__ == "__main__":
    # conn = sqlite3.connect(set_file_path('leo_task_list'))
    # input_data_base('leo_task_list', "2023-01-20","projetar peça","Proximo","Média","1F14000","Projetos")
    # input_data_base('leo_task_list', "2023-01-20","comprar mp","Fazendo","Alta","RAG30","Compras")
    # input_data_base('leo_task_list', "2023-01-20","fazer debug de app","Concluído","Baixa","StockBuyRep","Programação")
    # input_data_base('leo_task_list', "2023-01-20","iniciar um novo mes","Proximo","Media","centur 30","Manutenção")
    # input_data_base('leo_task_list', "2023-01-20","trocar gas","Proximo","Baixa","","Outros")
    print(read_data_base('leo_task_list'))