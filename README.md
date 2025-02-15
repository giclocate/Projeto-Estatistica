# Análise de Desempenho do Tempo de Resposta do Algoritmo de Reconhecimento de Voz em Dispositivos IoT: Estudo de Caso da Alexa 

## Resumo 
O avanço da Internet das Coisas (IoT) tem transformado a interação entre humanos e dispositivos, promovendo uma automação mais eficiente e uma experiência de usuário mais intuitiva. Este estudo teve como objetivo analisar o desempenho do algoritmo de reconhecimento de voz da Alexa, focando no tempo de resposta a comandos de voz em um ambiente controlado.

Foram coletados dados de tempo de resposta e analisados estatisticamente utilizando bibliotecas Python. Utilizando um gráfico Q-Q plot, verificou-se que os tempos de resposta seguem uma distribuição normal, com a maioria dos pontos alinhados à linha diagonal, indicando que os dados observados estão próximos dos quantis esperados de uma distribuição normal.

Além disso, foi realizado um teste de hipótese para comparar o tempo médio de resposta com um valor de referência de 1.2 segundos. A análise revelou que o tempo médio de resposta da Alexa é significativamente diferente e inferior ao valor de referência, com uma média amostral de 1.13090 segundos e um valor z calculado de aproximadamente -6.89. Para um teste bicaudal com α = 0.05, o valor crítico de z é ±1.96. Como o valor absoluto de z calculado é maior que 1.96, rejeitamos a hipótese nula.

## Bibliotecas Utilizadas
* Matplotlib
* Numpy
* Scipy
* Seaborn
  
## Estrutura
#### algoritmo.txt
Contém o conjunto de dados analisados.

#### graphics.py
Contém as funções para a criação dos gráficos.

#### main.py 
Função principal onde o programa é executado.

#### README.md
Breve resumo sobre o estudo.

## Execução
1.  Possuir o Python instalado no computador
2.  Instalar as bibliotecas necessárias (Matplotlib, Numpy, Scipy, Seaborn)
3.  Iniciar o código pelo VSCode

## Contribuidores
</br>Amós Kinsley Barbosa de Santana - akbs@cin.ufpe.br</br> 
</br>Giovanna Clócate Cavalcante de Almeida - lss11@cin.ufpe.br</br> 
</br>Lucas dos Santos da Silva - lss11@cin.ufpe.br</br>
