import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Manipulation de données et création de graphiques")

datasets = sns.get_dataset_names()
dataset_choisi = st.selectbox("Quel dataset veux-tu utiliser", datasets,
                              index=datasets.index("flights") if "flights" in datasets else 0)

df = sns.load_dataset(dataset_choisi)
st.dataframe(df)

colonnes = df.columns.tolist()
col_x = st.selectbox("Choisissez la colonne X", colonnes)
col_y = st.selectbox("Choisissez la colonne Y", colonnes, index=1 if len(colonnes) > 1 else 0)

type_graphique = st.selectbox("Quel graphique veux-tu utiliser ?",
                              ["scatter_chart", "bar_chart", "line_chart"])

if type_graphique == "scatter_chart":
    st.scatter_chart(df, x=col_x, y=col_y)
elif type_graphique == "bar_chart":
    st.bar_chart(df, x=col_x, y=col_y)
elif type_graphique == "line_chart":
    st.line_chart(df, x=col_x, y=col_y)

if st.checkbox("Afficher la matrice de corrélation"):
    st.subheader("Matrice de corrélation")
    df_numerique = df.select_dtypes(include="number")
    fig, ax = plt.subplots()
    sns.heatmap(df_numerique.corr(), annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)
