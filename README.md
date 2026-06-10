# Identificador de Espécies de Drosophila

**Versão atual:** `v0.5.1-beta`

Este projeto é um sistema digital de identificação taxonômica para espécies de *Drosophila*, baseado em características morfológicas. A aplicação utiliza a biblioteca Streamlit para fornecer uma interface web intuitiva onde os usuários podem selecionar características observadas e obter a espécie mais provável.

## 🚀 Funcionalidades

- **Identificação por Características:** Seleção de múltiplos atributos morfológicos.
- **Cálculo de Similaridade:** Algoritmo que compara a entrada do usuário com uma base de dados (`chave.csv`).
- **Ranking de Espécies:** Exibe as espécies mais prováveis com porcentagem de similaridade.
- **Visualização:** Gráficos de barras comparando a similaridade entre diferentes espécies.

## 🛠️ Tecnologias Utilizadas

- **Python**
- **Streamlit** (Interface Web)
- **Pandas** (Manipulação de dados)
- **Numpy**

## 📋 Pré-requisitos

Certifique-se de ter o Python instalado em sua máquina. É recomendado o uso de um ambiente virtual.

## 🔧 Instalação

1. **Clone o repositório:**
   ```bash
   git clone git@github.com:izareginabios/App-chave-de-identifica-o-drosofilideos.git
   cd App-chave-de-identifica-o-drosofilideos
   ```

2. **Crie e ative um ambiente Conda:**
   ```bash
   conda create -n drosophila python=3.10
   conda activate drosophila
   ```

3. **Instale as dependências:**
   ```bash
   conda install --file requeriments.txt -c conda-forge
   ```
   *Nota: O arquivo `requeriments.txt` foi simplificado para garantir compatibilidade com Windows, macOS e Linux.*

## 💻 Como Usar

1. **Inicie a aplicação:**
   ```bash
   streamlit run app3.py
   ```

2. **Interaja com a interface:**
   - Selecione as características morfológicas observadas nos menus suspensos.
   - Para "I. Costal", digite o valor observado.
   - Clique no botão **"Identificar Espécie"**.
   - Veja o resultado da espécie mais provável e o ranking de similaridade.

## 📂 Estrutura do Projeto

- `app3.py`: Código principal da aplicação Streamlit.
- `chave.csv`: Base de dados taxonômica.
- `requeriments.txt`: Lista de dependências do projeto.
- `README.md`: Documentação do projeto.

---
Autora Principal: Iza Regina ([izareginabios](https://github.com/izareginabios))
