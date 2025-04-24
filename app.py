import duckdb as db
import pandas as pd
import streamlit as st

st.write("""
# SQL SRS
Spaced Repetition System SQL Practice
"""
         )

option = st.selectbox(
    "What would you like to review ?",
    ("Joins", "Group By", "Window Functions"),
    index=None,
    placeholder="Select a theme..."
)

st.write("You selected:", option)

tab1, tab2 = st.tabs(["cat", "dog"])
data = {"a": [1, 2, 3]}
df = pd.DataFrame(data)

with tab1:
    st.dataframe(df)

    input_query = st.text_area(label="Veuillez entrer votre requête SQL")

    st.write(f"Vous avez entré la query suivante: {input_query}")

    if input_query: st.dataframe(db.query(input_query))
