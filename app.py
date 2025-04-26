# pylint: disable=missing-module-docstring
import logging
import os

import duckdb
import streamlit as st

con = duckdb.connect(database="data/exercises_sql_tables.duckdb", read_only=False)

st.write(
    """
# SQL SRS
Spaced Repetition System SQL Practice
"""
)

if "data" not in os.listdir():
    print("creating folder data")
    logging.error(os.listdir())
    logging.error("creating folder data")
    os.mkdir("data")

if "exercises_sql_tables.duckdb" not in os.listdir("data"):
    exec(open("init_db.py").read())
    # subprocess.run(["python", "init_db.py"])

con = duckdb.connect(database="data/exercises_sql_tables.duckdb", read_only=False)

with st.sidebar:
    theme = st.selectbox(
        "What would you like to review ?",
        ("cross_joins", "Group By", "Window Functions"),
        index=None,
        placeholder="Select a theme...",
    )

    st.write("You selected:", theme)
    exercise = con.execute(f"select * from memory_state where theme = '{theme}'").df().sort_values(
        "last_reviewed").reset_index()
    st.write(exercise)

    exercise_name = exercise.loc[0, "exercise_name"]
    with open(f"answers/{exercise_name}.sql", "r") as f:
        answer = f.read()

    solution_df = con.execute(answer).df()

st.header("Enter your code:")
query = st.text_area(label="votre code SQL ici", key="user_input")

if query:
    result = con.execute(query).df()
    st.dataframe(result)

    if len(result.columns) != len(solution_df.columns):
        st.write("Some columns are missing")

    try:
        result = result[solution_df.columns]
        result.compare(solution_df)
    except KeyError as e:
        st.write("some columns are missing")

    n_lignes_difference = result.shape[0] - solution_df.shape[0]
    if n_lignes_difference != 0:
        st.write(
            f"Result has a {n_lignes_difference} lines difference with the solution_df"
        )

tab1, tab2 = st.tabs(["Tables", "Solution"])
# data = {"a": [1, 2, 3]}
# df = pd.DataFrame(data)

with tab1:
    exercise_tables = exercise.loc[0, "tables"]
    for table in exercise_tables:
        st.write(f"Table : {table}")
        df_table = con.execute(f"select * from {table}").df()
        st.dataframe(df_table)
    # st.dataframe(salaries)
#     st.write("Expected :")
#     st.dataframe(solution_df)

with tab2:
    st.write(answer)
