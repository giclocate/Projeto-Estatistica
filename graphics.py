# graphics.py

import seaborn as sns
import matplotlib.pyplot as plt

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

def plot_pie(labels, sizes, title):
    """
    Cria um gráfico de pizza.
    
    Args:
        labels: Rótulos para cada fatia.
        sizes: Tamanhos das fatias (percentuais).
        title: Título do gráfico.
        
    Returns:
        Exibe o gráfico de pizza.
    """
    plt.figure(figsize=(10, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, labeldistance=1.2)
    plt.title(title)
    plt.axis('equal')
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