import numpy as np
import matplotlib.pyplot as plt

def main():
    # Leitura dos dados do arquivo
    with open('algoritmo.txt', 'r', encoding='utf-8-sig') as file:
        data = [float(line.strip()) for line in file]

    # Conversão dos dados para um array numpy para facilitar os cálculos estatísticos
    data_array = np.array(data)

    # Cálculo das estatísticas
    media = np.mean(data_array)
    mediana = np.median(data_array)
    desvio_padrao = np.std(data_array)
    variancia = np.var(data_array)
    minimo = np.min(data_array)
    maximo = np.max(data_array)
    amplitude = maximo - minimo

    # Cálculo dos quartis
    q1 = np.percentile(data_array, 25)
    q3 = np.percentile(data_array, 75)

    # Exibição das estatísticas
    print(f"Média: {media}")
    print(f"Mediana: {mediana}")
    print(f"Desvio Padrão: {desvio_padrao}")
    print(f"Variância: {variancia}")
    print(f"Mínimo: {minimo}")
    print(f"Máximo: {maximo}")
    print(f"Amplitude: {amplitude}")
    print(f"Primeiro Quartil (Q1): {q1}")
    print(f"Terceiro Quartil (Q3): {q3}")

    # Gráfico de linha
    plt.figure(figsize=(12, 6))
    plt.plot(data_array, label='Tempos de Execução')
    plt.title('Gráfico de Linha dos Tempos de Execução')
    plt.xlabel('Execução')
    plt.ylabel('Tempo (segundos)')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Histograma
    plt.figure(figsize=(12, 6))
    plt.hist(data_array, bins=30, edgecolor='black')
    plt.title('Histograma dos Tempos de Execução')
    plt.xlabel('Tempo (segundos)')
    plt.ylabel('Frequência')
    plt.grid(True)
    plt.show()

   # Gráfico de pizza (distribuição percentual)
    bins = [0, 0.5, 1, 1.5, 2, 2.5, 3, np.inf]  # Ajuste os intervalos conforme necessário
    labels = ['< 0.5s', '0.5-1s', '1-1.5s', '1.5-2s', '2-2.5s', '2.5-3s', '> 3s']
    data_binned = np.histogram(data_array, bins=bins)[0]
    plt.figure(figsize=(12, 6))
    plt.pie(data_binned, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Gráfico de Pizza dos Tempos de Execução')
    plt.show()

    # Boxplot
    plt.figure(figsize=(12, 6))
    box = plt.boxplot(data_array, vert=True, patch_artist=True)
    plt.title('Boxplot dos Tempos de Execução')
    plt.ylabel('Tempo (segundos)')
    plt.grid(True)

    # Adicionar linhas horizontais para os quartis
    plt.axhline(y=q1, color='r', linestyle='--', label='Q1 (25º Percentil)')
    plt.axhline(y=mediana, color='g', linestyle='--', label='Mediana (50º Percentil)')
    plt.axhline(y=q3, color='b', linestyle='--', label='Q3 (75º Percentil)')
    plt.legend()
    plt.show()

    # Gráfico de dispersão
    plt.figure(figsize=(12, 6))
    plt.scatter(range(len(data_array)), data_array, label='Tempos de Execução', alpha=0.5)
    plt.title('Gráfico de Dispersão dos Tempos de Execução')
    plt.xlabel('Execução')
    plt.ylabel('Tempo (segundos)')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
