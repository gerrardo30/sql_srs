import duckdb as db
import pandas as pd
import streamlit as st

st.write("Hello world")

tab1, tab2 = st.tabs(["cat", "dog"])
data = {"a": [1, 2, 3]}
df = pd.DataFrame(data)

with tab1:
    st.dataframe(df)

    input_query = st.text_area(label="Veuillez entrer votre requête SQL")

    st.write(f"Vous avez entré la query suivante: {input_query}")

    if input_query: st.dataframe(db.query(input_query))
