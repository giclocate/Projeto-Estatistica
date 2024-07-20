import numpy as np
import matplotlib.pyplot as plt
from graphics import plot_histogram, plot_scatter, plot_pie, plot_boxplot, plot_linechart

def main():
    # Leitura dos dados do arquivo
    with open('algoritmo.txt', 'r', encoding='utf-8-sig') as file:
        data = [float(line.strip()) for line in file]

    # Conversão dos dados para um array numpy para facilitar os cálculos estatísticos
    data_array = np.array(data)

    # Cálculo das estatísticas utilizando a lib numpy
    media = np.mean(data_array)
    mediana = np.median(data_array)
    desvio_padrao = np.std(data_array)
    variancia = np.var(data_array)
    minimo = np.min(data_array)
    maximo = np.max(data_array)
    amplitude = maximo - minimo

    # Cálculo dos quartis
    q1 = np.percentile(data_array, 25)
    q2 = np.percentile(data_array, 50)
    q3 = np.percentile(data_array, 75)
    q4 = np.percentile(data_array, 100)

    # Exibição das estatísticas
    print(f"Média: {media:.4f}")
    print(f"Mediana: {mediana:.4f}")
    print(f"Desvio Padrão: {desvio_padrao:.4f}")
    print(f"Variância: {variancia:.4f}")
    print(f"Mínimo: {minimo:.4f}")
    print(f"Máximo: {maximo:.4f}")
    print(f"Amplitude: {amplitude:.4f}")
    print(f"Primeiro Quartil (Q1): {q1:.4f}")
    print(f"Segundo Quartil (Q2): {q2:.4f}")
    print(f"Terceiro Quartil (Q3): {q3:.4f}")
    print(f"Quarto Quartil (Q4): {q4:.4f}")

    # Gráfico de linha
    plot_linechart(range(len(data_array)), data_array, 'Execução', 'Tempo (segundos)', 'Gráfico de Linha dos Tempos de Execução', label='Tempos de Execução')

    # Histograma
    plot_histogram(data_array, 'Tempo (segundos)', 'Frequência', 'Histograma dos Tempos de Execução')

    # Gráfico de pizza (distribuição percentual)
    bins = [0, 0.5, 1, 1.5, 2, 2.5, 3, np.inf]  # Ajuste os intervalos conforme necessário
    labels = ['< 0.5s', '0.5-1s', '1-1.5s', '1.5-2s', '2-2.5s', '2.5-3s', '> 3s']
    data_binned = np.histogram(data_array, bins=bins)[0]
    plot_pie(labels, data_binned, 'Gráfico de Pizza dos Tempos de Execução')

    # Boxplot
    plot_boxplot(data_array, 'Tempo (segundos)', 'Boxplot dos Tempos de Execução', q1, mediana, q3)

    # Gráfico de dispersão
    plot_scatter(range(len(data_array)), data_array, 'Execução', 'Tempo (segundos)', 'Gráfico de Dispersão dos Tempos de Execução')

if __name__ == "__main__":
    main()
