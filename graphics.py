# graphics.py

import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np


def plot_histogram(data, xlabel, ylabel, title):
    """
    Cria um gráfico de histograma.
    
    Args:
        data: Dados a serem plotados.
        xlabel: Rótulo do eixo x.
        ylabel: Rótulo do eixo y.
        title: Título do gráfico.
        
    Returns:
        Exibe o gráfico de histograma.
    """
    ax = sns.histplot(data, kde=True)
    ax.set(title=title, xlabel=xlabel, ylabel=ylabel)
    plt.show()

def plot_scatter(x, y, xlabel, ylabel, title):
    """
    Cria um gráfico de dispersão.
    
    Args:
        x: Dados para o eixo x.
        y: Dados para o eixo y.
        xlabel: Rótulo do eixo x.
        ylabel: Rótulo do eixo y.
        title: Título do gráfico.
        
    Returns:
        Exibe o gráfico de dispersão.
    """
    plt.scatter(x, y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def plot_boxplot(data, ylabel, title, q1=None, mediana=None, q3=None):
    """
    Cria um gráfico de boxplot.
    
    Args:
        data: Dados a serem plotados.
        ylabel: Rótulo do eixo y.
        title: Título do gráfico.
        
    Returns:
        Exibe o gráfico de boxplot.
    """
    plt.figure(figsize=(12, 6))
    box = plt.boxplot(data, vert=True, patch_artist=True)
    plt.title(title)
    plt.ylabel(ylabel)
    plt.grid(True)
    
    # Adicionar linhas horizontais para os quartis, se fornecidos
    if q1 is not None:
        plt.axhline(y=q1, color='r', linestyle='--', label='Q1 (25º Percentil)')
    if mediana is not None:
        plt.axhline(y=mediana, color='g', linestyle='--', label='Mediana (50º Percentil)')
    if q3 is not None:
        plt.axhline(y=q3, color='b', linestyle='--', label='Q3 (75º Percentil)')
    
    plt.legend()
    plt.show()
    
def plot_linechart(x, y, xlabel, ylabel, title, label):
    """
    Cria um gráfico de linha.
    
    Args:
        x: Dados para o eixo x.
        y: Dados para o eixo y.
        xlabel: Rótulo do eixo x.
        ylabel: Rótulo do eixo y.
        title: Título do gráfico.
        
    Returns:
        Exibe o gráfico de linha.
    """
    plt.plot(x, y, label=label)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.show()
    
    
# Funções para os gráficos
def plot_unilateral_test(data, media_hipotetica, tipo, titulo):
    desvio_padrao = np.std(data)
    media_amostral = np.mean(data)
    n = len(data)
    alpha = 0.05

    if tipo == "menor":
        z = (media_amostral - media_hipotetica) / (desvio_padrao / np.sqrt(n))
        z_critico = stats.norm.ppf(alpha)
    elif tipo == "maior":
        z = (media_amostral - media_hipotetica) / (desvio_padrao / np.sqrt(n))
        z_critico = stats.norm.ppf(1 - alpha)
    elif tipo == "diferente":
        z = (media_amostral - media_hipotetica) / (desvio_padrao / np.sqrt(n))
        z_critico = stats.norm.ppf(1 - alpha / 2)

    # Gráfico
    x = np.linspace(min(data), max(data), 1000)
    y = stats.norm.pdf(x, np.mean(data), np.std(data))

    plt.plot(x, y, label='Distribuição Normal dos Tempos de Resposta')
    plt.axvline(media_hipotetica, color='r', linestyle='--', label=f'Média Hipotética ({media_hipotetica} seg)')
    plt.axvline(media_amostral, color='g', linestyle='--', label=f'Média Amostral ({media_amostral:.5f} seg)')
    
    if tipo == "menor":
        plt.fill_betweenx(y, x, media_hipotetica, where=(x < media_hipotetica), color='red', alpha=0.3)
    elif tipo == "maior":
        plt.fill_betweenx(y, x, media_hipotetica, where=(x > media_hipotetica), color='red', alpha=0.3)
    elif tipo == "diferente":
        plt.fill_betweenx(y, x, media_hipotetica, where=(x > media_hipotetica), color='red', alpha=0.3)
        plt.fill_betweenx(y, x, media_hipotetica, where=(x < media_hipotetica), color='red', alpha=0.3)

    plt.title(titulo)
    plt.xlabel('Tempo de Resposta (segundos)')
    plt.ylabel('Densidade de Probabilidade')
    plt.legend()
    plt.show()

    print(f"Valor z: {z:.5f}")
    if tipo == "menor" or tipo == "maior":
        print(f"Valor z crítico: {z_critico:.5f}")
        if (tipo == "menor" and z < z_critico) or (tipo == "maior" and z > z_critico):
            print("Rejeitamos a hipótese nula (H0)")
        else:
            print("Não rejeitamos a hipótese nula (H0)")
    elif tipo == "diferente":
        print(f"Valor z crítico: ±{z_critico:.5f}")
        if abs(z) > z_critico:
            print("Rejeitamos a hipótese nula (H0)")
        else:
            print("Não rejeitamos a hipótese nula (H0)")