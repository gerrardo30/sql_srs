# pylint: disable=missing-module-docstring

import duckdb
import streamlit as st

con = duckdb.connect(database="data/exercises_sql_tables.duckdb", read_only=False)

ANSWER_STR = """
SELECT * FROM salaries
CROSS JOIN seniorities
"""

# solution_df = db.sql(ANSWER_STR).df()

st.write(
    """
# SQL SRS
Spaced Repetition System SQL Practice
"""
)

with st.sidebar:
    theme = st.selectbox(
        "What would you like to review ?",
        ("cross_joins", "Group By", "Window Functions"),
        index=None,
        placeholder="Select a theme...",
    )

    st.write("You selected:", theme)
    exercise = con.execute(f"select * from memory_state where theme = '{theme}'").df()

    st.write(exercise)
st.header("Enter your code:")
# query = st.text_area(label="votre code SQL ici", key="user_input")
# if query:
#     result = db.sql(query).df()
#     st.dataframe(result)
#
#     if len(result.columns) != len(solution_df.columns):
#         st.write("Some columns are missing")
#
#     try:
#         result = result[solution_df.columns]
#         result.compare(solution_df)
#     except KeyError as e:
#         st.write("some columns are missing")
#
#     n_lignes_difference = result.shape[0] - solution_df.shape[0]
#     if n_lignes_difference != 0:
#         st.write(
#             f"Result has a {n_lignes_difference} lines difference with the solution_df"
#         )
#
# tab1, tab2 = st.tabs(["Tables", "Solution"])
# data = {"a": [1, 2, 3]}
# df = pd.DataFrame(data)

# with tab1:
#     st.write("Table : salaries")
#     st.dataframe(salaries)
#     st.write("Table : seniorities")
#     st.dataframe(seniorities)
#     st.write("Expected :")
#     st.dataframe(solution_df)
#
# with tab2:
#     st.write(ANSWER_STR)
