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
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title(title)
    plt.axis('equal')
    plt.show()

def plot_boxplot(data, ylabel, title):
    """
    Cria um gráfico de boxplot.
    
    Args:
        data: Dados a serem plotados.
        ylabel: Rótulo do eixo y.
        title: Título do gráfico.
        
    Returns:
        Exibe o gráfico de boxplot.
    """
    plt.boxplot(data)
    plt.title(title)
    plt.ylabel(ylabel)
    plt.show()
