# Sistema de Cálculo e Visualização de Distribuição de Poisson

Este repositório contém um sistema desenvolvido em **Python** e **Streamlit** para realizar cálculos e visualizações relacionadas à distribuição de Poisson.

---

## Estrutura do Projeto

```
project-poisson/
├── .streamlit/               # Configurações do Streamlit
│   └── config.toml           # Arquivo de configuração do Streamlit
├── equipamento.py            # Código principal do aplicativo
├── LICENSE                   # Licença do projeto
├── poetry.lock               # Arquivo de dependências gerenciado pelo Poetry
```

---

## Funcionalidades

O sistema permite:

1. **Escolha Interativa do Tipo de Cálculo**:
    - Probabilidade exata.
    - Probabilidade acumulada ("Menos que").
    - Probabilidade complementar ("Mais que").

2. **Entrada de Dados**:
    - Inserção do valor de ocorrência (k).
    - Inserção da taxa média de ocorrência (λ).

3. **Visualização Gráfica**:
    - Exibição das probabilidades em um gráfico de barras.

---

## Como Executar o Projeto

### 1. Clonar o Repositório
```bash
 git clone <URL_DO_REPOSITORIO>
 cd project-poisson
```

### 2. Instalar Dependências

Usando `requirements.txt`:
```bash
 pip install -r requirements.txt
```

### 3. Executar o Sistema

```bash
 streamlit run main.py
```

O aplicativo estará disponível no navegador em `http://localhost:8501`.

---

## Principais Funções do Projeto

### 1. Configuração da Página e Título

- **`st.set_page_config`**:
    - Define as configurações iniciais da página, como o título da aba do navegador.
- **`st.title`**:
    - Adiciona o título principal do aplicativo na interface.

### 2. Painel Lateral Interativo (`st.sidebar`)

- **`st.sidebar`**:
    - Cria um painel lateral para organizar entradas e opções do usuário.
- **`st.radio`**:
    - Permite ao usuário selecionar uma opção entre várias (tipo de cálculo).
- **`st.number_input`**:
    - Cria uma entrada numérica para o usuário inserir a taxa média de ocorrência (λ).
- **`st.button`**:
    - Cria um botão que aciona o processamento dos cálculos ao ser clicado.

### 3. Processamento de Dados

- **`poisson.pmf`** (Probabilidade Exata):
    - Calcula a probabilidade de um valor específico usando a Distribuição de Poisson.
- **`poisson.cdf`** (Menos que):
    - Calcula a probabilidade acumulada até um valor específico.
- **`poisson.sf`** (Mais que):
    - Calcula a probabilidade complementar (maior que o valor especificado).

### 4. Formatação e Preparação

- **`np.arange`**:
    - Cria um array de valores inteiros dentro de um intervalo especificado.
- **`np.round`**:
    - Arredonda as probabilidades calculadas para 4 casas decimais.
- **List comprehension**:
    - Formata rótulos associados aos valores de ocorrência e suas probabilidades.

### 5. Visualização do Gráfico

- **`plt.subplots`**:
    - Cria uma figura e eixos para o gráfico.
- **`ax.bar`**:
    - Plota um gráfico de barras com as probabilidades calculadas.
- **`st.pyplot`**:
    - Exibe o gráfico gerado na interface Streamlit.

### 6. Resultado Final

As principais interações do projeto são:

1. **Entrada do usuário**:
    - Escolha do tipo de cálculo.
    - Inserção do valor de ocorrência (k) e taxa média (λ).

2. **Cálculo das probabilidades** com base na escolha do usuário.

3. **Exibição visual** dos resultados em um gráfico de barras.

---

## Contato

Caso tenha dúvidas ou sugestões, sinta-se à vontade para entrar em contato.

Licença: Este projeto está sob a licença MIT.