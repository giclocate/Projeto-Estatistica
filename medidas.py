import pandas as pd
import numpy as np
from scipy import stats
import sqlite3

def calcular_medidas(df, coluna):
    medidas = {}
    
    medidas['média'] = df[coluna].mean()
    medidas['mediana'] = df[coluna].median()
    medidas['moda'] = df[coluna].mode()[0]
    medidas['desvio padrão'] = df[coluna].std()
    medidas['variância'] = df[coluna].var()
    medidas['coeficiente de variação'] = (df[coluna].std() / df[coluna].mean()) * 100
    medidas['1º quartil'] = df[coluna].quantile(0.25)
    medidas['2º quartil'] = df[coluna].quantile(0.5)
    medidas['3º quartil'] = df[coluna].quantile(0.75)
    medidas['4º quartil'] = df[coluna].quantile(1.0)
    medidas['curtose'] = df[coluna].kurtosis()
    
    return medidas

def salvar_no_banco(medidas, db_name='medidas_estatisticas.db'):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    
    c.execute('''
    CREATE TABLE IF NOT EXISTS medidas (
        medida TEXT,
        valor REAL
    )
    ''')
    
    for medida, valor in medidas.items():
        c.execute('''
        INSERT INTO medidas (medida, valor)
        VALUES (?, ?)
        ''', (medida, valor))
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    data = {
        'valores': [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 10]
    }
    df = pd.DataFrame(data)
    
    medidas = calcular_medidas(df, 'valores')
    
    for medida, valor in medidas.items():
        print(f"{medida}: {valor}")
    
    salvar_no_banco(medidas)
