import streamlit as st

# Initialisation des cotes et de l'historique
if "cotes" not in st.session_state:
    st.session_state.cotes = ["", "", "", "", ""]

if "historique" not in st.session_state:
    st.session_state.historique = []

st.set_page_config(page_title="Aviator Predictor", page_icon="✈️", layout="centered")

# Style
st.markdown("""
    <h1 style='text-align: center; color: red;'>✈️ Aviator Predictor Betpawa ✈️</h1>
    <h3 style='text-align: center; color: white;'>Optimisé pour prédire quand miser sur le 2x</h3>
""", unsafe_allow_html=True)

st.divider()

st.write("**Entrez vos 5 dernières cotes :**")

# Affichage des 5 champs
for i in range(5):
    st.session_state.cotes[i] = st.text_input(f"Cote {i+1}", value=st.session_state.cotes[i], key=f"cote_{i}")

# Choix du nombre de cotes à analyser
nombre_cotes = st.selectbox(
    "Choisissez combien de cotes récentes analyser :", 
    options=[2, 3, 4, 5], 
    index=3
)

# Fonction d'analyse
def analyser_cotes(cotes, nb):
    try:
        # Nettoyer et transformer en float
        recent_cotes = [float(c) for c in cotes[-nb:] if c != ""]
        if len(recent_cotes) < nb:
            return "Pas assez de cotes"
        
        moyenne = sum(recent_cotes) / len(recent_cotes)
        derniere = recent_cotes[-1]

        if moyenne < 2.0 and derniere < 1.8:
            return "ATTENDRE"
        elif 2.0 <= moyenne <= 2.5 and 1.5 <= derniere <= 2.0:
            return "MISER"
        elif moyenne > 2.5 and derniere > 2.0:
            return "ATTENDRE"
        else:
            return "ATTENDRE"
    except:
        return "Erreur d'analyse"

# Quand on clique sur "Analyser"
if st.button("Analyser"):
    decision = analyser_cotes(st.session_state.cotes, nombre_cotes)
    
    if decision != "Pas assez de cotes" and decision != "Erreur d'analyse":
        st.success(f"**Décision : {decision} pour le prochain tour !**")

        # Déplacer les cotes : 
        st.session_state.cotes = st.session_state.cotes[1:] + [""]
        
        # Ajouter la décision à l'historique
        st.session_state.historique.append(decision)
    else:
        st.warning("Merci de remplir assez de cotes pour analyser.")

st.divider()

# Affichage de l'historique
st.write("### Historique des décisions :")
if st.session_state.historique:
    for i, action in enumerate(reversed(st.session_state.historique[-10:]), 1):
        st.write(f"{i}. {action}")
else:
    st.write("Aucune analyse effectuée pour le moment.")

# Petit rappel
st.caption("Développé pour Betpawa Aviator - Stratégie optimisée sur les cotes de 2x.")
