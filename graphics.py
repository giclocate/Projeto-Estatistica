import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np

def plot_histogram(data, xlabel, ylabel, title):
    """
    Cria um histograma.
    
    Args:
        data: Dados a serem plotados.
        xlabel: Rótulo do eixo x.
        ylabel: Rótulo do eixo y.
        title: Título do gráfico.
        
    Returns:
        Exibe o histograma.
    """
    plt.figure(figsize=(10, 8))
    plt.hist(data, bins=20, edgecolor='black')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()

def plot_scatter(x, y, xlabel, ylabel, title):
    """
    Cria um gráfico de dispersão.
    
    Args:
        x: Dados do eixo x.
        y: Dados do eixo y.
        xlabel: Rótulo do eixo x.
        ylabel: Rótulo do eixo y.
        title: Título do gráfico.
        
    Returns:
        Exibe o gráfico de dispersão.
    """
    plt.figure(figsize=(10, 8))
    plt.scatter(x, y, alpha=0.7)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
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
        q1: Primeiro quartil (opcional).
        mediana: Mediana (opcional).
        q3: Terceiro quartil (opcional).
        
    Returns:
        Exibe o gráfico de boxplot.
    """
    plt.figure(figsize=(10, 8))
    sns.boxplot(data=data)
    plt.ylabel(ylabel)
    plt.title(title)
    if q1 is not None and mediana is not None and q3 is not None:
        plt.axhline(q1, color='r', linestyle='--', label=f'Q1 ({q1:.2f})')
        plt.axhline(mediana, color='g', linestyle='--', label=f'Mediana ({mediana:.2f})')
        plt.axhline(q3, color='b', linestyle='--', label=f'Q3 ({q3:.2f})')
        plt.legend()
    plt.show()

def plot_linechart(x, y, xlabel, ylabel, title, label=None):
    """
    Cria um gráfico de linha.
    
    Args:
        x: Dados do eixo x.
        y: Dados do eixo y.
        xlabel: Rótulo do eixo x.
        ylabel: Rótulo do eixo y.
        title: Título do gráfico.
        label: Rótulo da linha (opcional).
        
    Returns:
        Exibe o gráfico de linha.
    """
    plt.figure(figsize=(10, 8))
    plt.plot(x, y, label=label)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    if label:
        plt.legend()
    plt.show()

def plot_unilateral_test(data, media_hipotetica, tipo, titulo):
    """
    Plota o gráfico de teste unilateral e exibe os resultados do teste.
    
    Args:
        data: Dados da amostra.
        media_hipotetica: Média hipotética para comparação.
        tipo: Tipo de teste ('menor', 'maior', 'diferente').
        titulo: Título do gráfico.
        
    Returns:
        Exibe o gráfico do teste e imprime o resultado.
    """
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
    else:
        raise ValueError("Tipo de teste deve ser 'menor', 'maior' ou 'diferente'.")

    # Gráfico
    x = np.linspace(min(data), max(data), 1000)
    y = stats.norm.pdf(x, np.mean(data), np.std(data))

    plt.figure(figsize=(10, 8))
    plt.plot(x, y, label='Distribuição Normal dos Tempos de Resposta')
    plt.axvline(media_hipotetica, color='r', linestyle='--', label=f'Média Hipotética ({media_hipotetica} seg)')
    plt.axvline(media_amostral, color='g', linestyle='--', label=f'Média Amostral ({media_amostral:.5f} seg)')

    if tipo == "menor":
        plt.fill_between(x, y, where=(x < media_hipotetica), color='red', alpha=0.3)
    elif tipo == "maior":
        plt.fill_between(x, y, where=(x > media_hipotetica), color='red', alpha=0.3)
    elif tipo == "diferente":
        plt.fill_between(x, y, where=(x > media_hipotetica), color='red', alpha=0.3)
        plt.fill_between(x, y, where=(x < media_hipotetica), color='red', alpha=0.3)

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
