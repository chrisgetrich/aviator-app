import streamlit as st
import numpy as np

# Configuration de la page
st.set_page_config(
    page_title="Aviator Predictor by Chris",
    page_icon="✈️",
    layout="centered"
)

# Style CSS personnalisé pour un thème Aviator
st.markdown("""
    <style>
        body {
            background-color: #000000;
            color: #ffffff;
        }
        .stApp {
            background-color: #000000;
        }
        h1, h2, h3 {
            color: #ff4444;
        }
        .stButton>button {
            background-color: #ff0000;
            color: white;
            font-size: 18px;
            border-radius: 8px;
            height: 3em;
            width: 100%;
        }
        .css-2trqyj {
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# Logo
st.image("https://www.pngmart.com/files/22/Aviator-Logo-PNG.png", width=180)

# Titre
st.title("✈️ Aviator Predictor by Chris")
st.subheader("Optimisé pour détecter les cotes 2")

st.markdown("**Entre les 10 dernières cotes de BetPawa :**")

# Champs pour les 10 dernières cotes
cotes = []
cols = st.columns(5)
for i in range(10):
    with cols[i % 5]:
        cote = st.number_input(f"Cote {i+1}", min_value=0.01, format="%.2f", key=f"cote_{i}")
        cotes.append(cote)

# Analyse
if st.button("Analyser les cotes"):
    if all(cote > 0 for cote in cotes):
        moyenne = np.mean(cotes)
        derniere = cotes[-1]

        # Logique prédictive optimisée
        if derniere < moyenne * 0.85:
            st.success("✈️ Décision : **JOUER** — Probabilité d’un x2 bientôt")
        else:
            st.warning("⛔ Décision : **ATTENDS** — Trop risqué pour un x2 maintenant")
    else:
        st.error("⚠️ Remplis toutes les cotes avec des valeurs valides.")
