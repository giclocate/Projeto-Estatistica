import os
import sqlite3

def create_database_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def read_algoritmo_file(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return data

def create_and_populate_database(db_path, data):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS algoritmo (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content TEXT NOT NULL
    )
    ''')
    
    for line in data:
        cursor.execute('INSERT INTO algoritmo (content) VALUES (?)', (line.strip(),))
    
    conn.commit()
    conn.close()

def integrate_database_with_code(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM algoritmo')
    rows = cursor.fetchall()
    
    for row in rows:
        print(row)
    
    conn.close()

pasta = 'create_database'
arquivo = 'algoritmo.txt'
caminho_bd = os.path.join(pasta, 'algoritmo.db')

# create_database_folder(pasta)
# data = read_algoritmo_file(arquivo)
# create_and_populate_database(caminho_bd, data)
# integrate_database_with_code(caminho_bd)
