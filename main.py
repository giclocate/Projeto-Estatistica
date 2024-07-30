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
    desvio_padrao = 0.3171  # Atualizado para o valor correto
    media_amostral = np.mean(data)
    n = len(data)
    alpha = 0.05

    # Calcular o valor crítico z
    z_critico = stats.norm.ppf(1 - alpha / 2)

    # Calcular os limites críticos
    limite_inferior = media_hipotetica - z_critico * desvio_padrao
    limite_superior = media_hipotetica + z_critico * desvio_padrao

    # Gráfico
    x_min = media_hipotetica - 4 * desvio_padrao
    x_max = media_hipotetica + 4 * desvio_padrao
    x = np.linspace(x_min, x_max, 1000)
    y = stats.norm.pdf(x, media_hipotetica, desvio_padrao)

    plt.plot(x, y, label='Distribuição Normal', color='blue')
    plt.fill_between(x, y, where=(x < limite_inferior) | (x > limite_superior), color='red', alpha=0.3, label='Área Periférica')
    plt.axvline(limite_inferior, color='green', linestyle='--', label='Limite Inferior (95%)')
    plt.axvline(limite_superior, color='brown', linestyle='--', label='Limite Superior (95%)')

    plt.title(titulo)
    plt.xlabel('Tempo (segundos)')
    plt.ylabel('Densidade de Probabilidade')
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.show()

# Função main para chamar o código de gráficos
def main():
    caminho_arquivo = 'algoritmo.txt'  # Caminho absoluto
    data = carregar_dados(caminho_arquivo)
    media_hipotetica = 1.13  # Atualizado para 1.13
    titulo = 'Distribuição Normal com Valor Crítico z'
    plot_bilateral_test(data, media_hipotetica, titulo)

if __name__ == "__main__":
    main()
