import sqlite3
import os
from pathlib import Path

ABSOLUTE_PATH = Path(__file__).parent.parent

def set_file_path(file_name):
    file_name = file_name + ".db"
    folder_name = "configuration"
    full_path_file = os.path.join(ABSOLUTE_PATH, folder_name, file_name)
    return full_path_file

def input_data_base(name_data_base, data, nome, status, prioridade, tipo, referencias=None, conteudo=None, foto=None):  # create an data base
    full_path_file = set_file_path(name_data_base)
    conn = sqlite3.connect(full_path_file)
    
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            data DATE,
            nome TEXT,
            status TEXT,
            prioridade TEXT,
            referencias TEXT,
            tipo TEXT,
            conteudo TEXT,
            foto BLOB)''')
   
    # input datas
    cursor.execute("INSERT INTO tasks (data, nome, status, prioridade, referencias, tipo, conteudo, foto) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", 
        (data, nome, status, prioridade, tipo, referencias, conteudo, foto))
    
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
    return listing_datas
        # print(type(row))

    # close data base
    conn.close()

if __name__ == "__main__":
    input_data_base('leo_task_list', "2023-01-20","projetar peça","Proximo","Média","1F14000","Projetos")
    input_data_base('leo_task_list', "2023-01-20","comprar mp","Fazendo","Alta","RAG30","Compras")
    input_data_base('leo_task_list', "2023-01-20","fazer debug de app","Concluído","Baixa","StockBuyRep","Programação")
    input_data_base('leo_task_list', "2023-01-20","iniciar um novo mes","Proximo","Media","centur 30","Manutenção")
    input_data_base('leo_task_list', "2023-01-20","trocar gas","Proximo","Baixa","","Outros")
    print(read_data_base('leo_task_list'))