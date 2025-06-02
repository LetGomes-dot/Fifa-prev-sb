# 🏆 Previsor de Gols FIFA - SuperBet

Este é um app desenvolvido com Streamlit que prevê o placar estimado entre dois jogadores profissionais de FIFA (eSoccer), com base em estatísticas personalizadas como ataque, finalização e forma recente.

## 📁 Estrutura do Projeto

```
.
├── app.py                # Código principal do app
├── players_stats.json    # Estatísticas dos jogadores
└── requirements.txt      # Dependências para instalar
```

## 🚀 Como rodar localmente

1. Clone ou baixe este repositório.
2. Instale o Streamlit (se ainda não tiver):

```bash
pip install -r requirements.txt
```

3. Rode o aplicativo com:

```bash
streamlit run app.py
```

## ⚙️ Como funciona

- O app lê as estatísticas dos jogadores a partir do `players_stats.json`.
- Ao selecionar dois jogadores, ele estima o placar com base nos atributos ofensivos e na forma.
- Um modelo simples com distribuição Gaussiana (normal) é usado para simular os gols prováveis.

## ✨ Melhorias futuras

- Integração com dados reais da SuperBet via scraping ou API.
- Histórico de partidas e gráficos.
- Sistema de favoritos e estatísticas em tempo real.

---

Desenvolvido com ❤️ para análise de partidas eSoccer.