import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Função para carregar dados de um arquivo
def carregar_dados(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8-sig') as file:
        dados = file.readlines()
    # Converter os dados para float
    dados = [float(linha.strip()) for linha in dados if linha.strip()]
    return np.array(dados)

def plot_bilateral_test(data, media_hipotetica, titulo):
    desvio_padrao = np.std(data)
    media_amostral = np.mean(data)
    n = len(data)
    alpha = 0.05

    z = (media_amostral - media_hipotetica) / (desvio_padrao / np.sqrt(n))
    z_critico = stats.norm.ppf(1 - alpha / 2)

    # Gráfico
    x = np.linspace(0, 2.5, 1000)
    y = stats.norm.pdf(x, media_hipotetica, desvio_padrao)

    plt.plot(x, y, label='Distribuição Normal', color='blue')
    plt.fill_between(x, y, where=(x < media_hipotetica - z_critico * desvio_padrao) | (x > media_hipotetica + z_critico * desvio_padrao), color='red', alpha=0.3, label='Área Periférica')
    plt.axvline(media_hipotetica - z_critico * desvio_padrao, color='green', linestyle='--', label='Limite Inferior (95%)')
    plt.axvline(media_hipotetica + z_critico * desvio_padrao, color='brown', linestyle='--', label='Limite Superior (95%)')

    plt.title(titulo)
    plt.xlabel('Tempo (segundos)')
    plt.ylabel('Densidade de Probabilidade')
    plt.legend(loc='upper right')
    plt.show()

# Função main para chamar o código de gráficos
def main():
    caminho_arquivo = 'algoritmo.txt'  # Caminho absoluto
    data = carregar_dados(caminho_arquivo)
    media_hipotetica = 1.1309 
    titulo = 'Distribuição Normal com Valor Crítico z'
    plot_bilateral_test(data, media_hipotetica, titulo)

if __name__ == "__main__":
    main()
