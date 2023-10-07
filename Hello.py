import streamlit as st
#import tensorflow as tf
from transformers import RobertaTokenizer
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Affichage d'un échantillon des données
st.title("Projet 10 : Détectez les Bad Buzz grâce au Deep Learning")

# Charger les données
path = "https://github.com/SaraSarahB/Projet10/MyData.csv"
data = pd.read_csv(path, encoding='ISO-8859-1')


st.subheader("Présentation des données Data")
st.dataframe(Data.sample(5))
# Affichage de la forme des données (nombre de lignes et de colonnes)
st.write("Data.shape :", Data.shape)

# Création du graphique de distribution de la colonne 'target'
st.subheader("Compteur de distribution de target")
sns.set(style="whitegrid")
fig, ax = plt.subplots(figsize=(8, 6))
sns.countplot(data=Data, x='target', palette='Set1', ax=ax)
plt.xlabel("Target")
plt.ylabel("Count")
plt.xticks(rotation=45)
st.pyplot(fig)

# Exécution de l'application Streamlit
if __name__ == "__main__":
    st.sidebar.title("Paramètres")
    st.sidebar.write("Personnalisez les paramètres ici, si nécessaire.")





    )


if __name__ == "__main__":
    run()
