import streamlit as st
import json
import random

# Carrega as estatísticas dos jogadores
def carregar_dados():
    with open("players_stats.json", "r") as f:
        return json.load(f)

jogadores_stats = carregar_dados()

# Função que prevê gols com base nos atributos
def prever_gols(stats):
    ataque = stats.get("ataque", 0)
    finalizacao = stats.get("finalizacao", 0)
    forma = stats.get("forma", 0)

    media = (ataque * 0.4 + finalizacao * 0.4 + forma * 100 * 0.2) / 100
    desvio_padrao = 0.6
    gols_estimados = round(random.gauss(media, desvio_padrao))
    return max(0, min(gols_estimados, 5))  # limitar entre 0 e 5

# Interface Streamlit
st.set_page_config(page_title="Previsor de Gols FIFA", layout="centered")
st.title("🔮 Previsão de Gols em Partidas de FIFA (SuperBet)")

jogadores = list(jogadores_stats.keys())

col1, col2 = st.columns(2)
with col1:
    jogador1 = st.selectbox("Selecione o Jogador 1", jogadores)
with col2:
    jogador2 = st.selectbox("Selecione o Jogador 2", jogadores)

if st.button("🔎 Prever Resultado"):
    stats1 = jogadores_stats[jogador1]
    stats2 = jogadores_stats[jogador2]

    gols1 = prever_gols(stats1)
    gols2 = prever_gols(stats2)

    st.subheader("⚽ Resultado Estimado:")
    st.markdown(f"### {jogador1} **{gols1} x {gols2}** {jogador2}")

    st.divider()
    st.subheader("📊 Estatísticas Individuais")

    col3, col4 = st.columns(2)
    with col3:
        st.markdown(f"**{jogador1}**")
        for k, v in stats1.items():
            st.text(f"{k.capitalize()}: {v}")
    with col4:
        st.markdown(f"**{jogador2}**")
        for k, v in stats2.items():
            st.text(f"{k.capitalize()}: {v}")