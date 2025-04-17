import streamlit as st
import numpy as np

st.title("Aviator Predictor by Chris")

st.write("**Entre les 10 dernières cotes Aviator (ex: 1.25, 1.48, etc.)**")
user_input = st.text_input("Cotes séparées par des virgules")

def analyse_cotes(cotes):
    cotes = np.array(cotes)
    moyenne = np.mean(cotes)
    derniere = cotes[-1]

    if derniere < moyenne * 0.85:
        return "JOUER"
    else:
        return "ATTENDS"

if user_input:
    try:
        cotes = [float(x.strip()) for x in user_input.split(",") if x.strip()]
        if len(cotes) < 5:
            st.warning("Entre au moins 5 cotes.")
        else:
            decision = analyse_cotes(cotes)
            st.success(f"Décision : **{decision}**")
    except ValueError:
        st.error("Format invalide. Assure-toi d’entrer des nombres séparés par des virgules.")
