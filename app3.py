import streamlit as st
import pandas as pd
import numpy as np
import os

st.set_page_config(layout="wide", page_title="Identificador de Drosophila")

# Versão do Aplicativo
VERSION = "v0.5.1-beta"

@st.cache_data
def carregar_dados():
    df = pd.read_csv("chave.csv")
    return df

df = carregar_dados()
coluna_especie = df.columns[0]
caracteristicas = df.columns[1:]

st.sidebar.markdown(f"**Versão:** `{VERSION}`")
st.title("🔬 Identificador de Espécies de Drosophila")
st.write(
"""
Sistema digital de identificação taxonômica baseado em
características morfológicas. Selecione os atributos observados abaixo.
"""
)

st.divider()

st.subheader("📋 Selecione ou digite as características observadas")
entrada_usuario = {}
num_colunas = 3
cols = st.columns(num_colunas)

for i, c in enumerate(caracteristicas):
    with cols[i % num_colunas]:
        # Tenta carregar uma imagem de ajuda para a característica
        img_ajuda = f"ajuda/{c.replace(' ', '_').lower()}.png"
        if os.path.exists(img_ajuda):
            st.image(img_ajuda, caption=f"Guia: {c}", width=150)
            
        if c.lower() == "i. costal":
            valor = st.text_input(
                c,
                placeholder="Digite o valor observado",
                key=c
            )
        else:
            opcoes = df[c].dropna().unique()
            valor = st.selectbox(
                c,
                ["Desconhecido"] + list(opcoes),
                key=c
            )
        entrada_usuario[c] = valor

def calcular_similaridade(linha, entrada):
    total = 0
    match = 0
    for c in caracteristicas:
        valor_usuario = str(entrada[c]).strip().lower()
        if valor_usuario == "" or valor_usuario == "desconhecido":
            continue
        total += 1
        valor_base = str(linha[c]).strip().lower()
        if valor_usuario in valor_base:
            match += 1
    if total == 0:
        return 0
    return match / total

st.divider()

if st.button("🚀 Identificar Espécie", use_container_width=True):
    resultados = []
    for i, linha in df.iterrows():
        score = calcular_similaridade(linha, entrada_usuario)
        resultados.append({
            "Espécie": linha[coluna_especie],
            "Similaridade": score
        })
    
    resultados = pd.DataFrame(resultados)
    resultados = resultados.sort_values("Similaridade", ascending=False)
    
    melhor = resultados.iloc[0]
    
    if melhor["Similaridade"] == 0:
        st.warning("⚠️ Dados insuficientes para a classificação. Por favor, selecione mais características.")
    else:
        st.header("🏆 Resultado da Identificação")
        
        col_res1, col_res2 = st.columns([1, 1])
        
        with col_res1:
            st.subheader("Espécie mais provável")
            st.success(
                f"**{melhor['Espécie']}**\n\n"
                f"Similaridade: {round(melhor['Similaridade']*100,1)}%"
            )
            
            # Lógica para mostrar foto da espécie
            especie_formatada = melhor['Espécie'].replace(" ", "_")
            caminho_foto = f"fotos/{especie_formatada}.jpg"
            
            if os.path.exists(caminho_foto):
                st.image(caminho_foto, caption=f"Espécime de {melhor['Espécie']}", use_container_width=True)
            else:
                st.info(f"📸 Foto de *{melhor['Espécie']}* ainda não disponível na pasta `/fotos`.")

        with col_res2:
            st.subheader("Espécies semelhantes")
            top5 = resultados.head(5).copy()
            top5["Similaridade (%)"] = (top5["Similaridade"] * 100).round(1)
            st.dataframe(
                top5[["Espécie", "Similaridade (%)"]],
                use_container_width=True,
                hide_index=True
            )
            
            st.subheader("Gráfico de Similaridade")
            st.bar_chart(resultados.head(10).set_index("Espécie")["Similaridade"])

        st.divider()
        with st.expander("Ver Ranking Completo"):
            resultados_view = resultados.copy()
            resultados_view["Similaridade (%)"] = (resultados_view["Similaridade"] * 100).round(1)
            st.dataframe(resultados_view[["Espécie", "Similaridade (%)"]], use_container_width=True)
