import streamlit as st              # Framework para criar aplicações web interativas
import numpy as np                  # Biblioteca para operações matemáticas e de álgebra linear
import matplotlib.pyplot as plt     # Biblioteca para criações de gráficos 
from scipy.stats import poisson     # Biblioteca para cálculos estatísticos usando a ditribioção de Poisson 

st.set_page_config(page_title="Probabilidade de Falhas em Equipamentos")    # Define o título da página do aplicativo
st.title("Probabilidade de Falhas em Equipamentos")                         # Define o título principal exibido no aplicativo


# Bloco de configuração no painel lateral
# with = uma estrutura de controle de contexto.
# st.sidebar = Cria um painel lateral para componentes interativos no Streamlit.
with st.sidebar:
    st.header("Configurações")  # Exibe um cabeçalho no painel lateral
    # Opção para o usuário selecionar o tipo de cálculo desejado
    tipo = st.radio("Selecione o Cálculo", options=["Prob. Exata","Menos que","Mais que"])
    # Entrada para o usuário definir o número médio de ocorrências (λ)
    ocorrencia = st.number_input("Ocorrência Atual",min_value=1,max_value=99, value=2, step=1)
    # Botão para acionar o processamento
    processar = st.button("Processar")


# Bloco principal de processamento: será executado ao clicar no botão "Processar"
if processar:
    # Configuração inicial para cálculo
    lamb = ocorrencia   # Atribui o valor inserido pelo usuário à taxa média de ocorrência λ
    inic = lamb -2      # Define o valor inicial do intervalo como λ - 2
    fim = lamb + 2      # Define o valor final do intervalo como λ + 2
    x_vals = np.arange(inic,fim+1)  # Cria um array de valores de ocorrência dentro do intervalo


    # Bloco de cálculo das probabilidades baseado no tipo selecionado
    if tipo == "Prob. Exata":
        # Calcula a probabilidade exata para cada valor usando a PMF
        probs = poisson.pmf(x_vals, lamb)
        tit = "Probabilidades de Ocorrência"  # Título do gráfico para esse cálculo
    elif tipo == "Menos que":
        # Calcula a probabilidade acumulada até cada valor usando o CDF
        probs = poisson.cdf(x_vals, lamb)
        tit = "Probabilidades de Ocorrência Igual ou Menor que:"
    else:
        # Calcula a probabilidade complementar (maior que) usando a SF
        probs = poisson.sf(x_vals, lamb)
        tit = "Probabilidades de Ocorrência Maior que:"

    # Preparação dos rótulos para exibição
    z_vals = np.round(probs, 4)  # Arredonda as probabilidades para quatro casas decimais
    # Cria os rótulos formatados com o valor e a probabilidade correspondente
    labels = [f"{i} prob.: {p}" for i, p in zip(x_vals, z_vals)]

    # Bloco para criação do gráfico de barras
    fig, ax = plt.subplots()  # Cria uma figura e eixos para o gráfico
    # Desenha as barras com as probabilidades calculadas
    ax.bar(
        x_vals, probs, tick_label=labels,
        color=plt.cm.gray(np.linspace(0.4, 0.8, len(x_vals)))  # Define uma paleta de cores gradiente
    )
    ax.set_title(tit)  # Define o título do gráfico
    plt.xticks(rotation=45, ha="right")  # Ajusta os rótulos do eixo X para melhor visualização
    plt.tight_layout()  # Ajusta o layout para evitar cortes nos rótulos
    st.pyplot(fig)  # Exibe o gráfico no aplicativo Streamlit