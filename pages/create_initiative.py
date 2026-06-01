import streamlit as st

from database.db import (
    create_initiative
)

st.title("➕ Create Initiative")

name = st.text_input(
    "Initiative Name"
)

industry = st.text_input(
    "Industry"
)

problem_statement = st.text_area(
    "Problem Statement"
)

target_users = st.text_area(
    "Target Users"
)

business_goal = st.text_area(
    "Business Goal"
)

if st.button(
    "Create Initiative"
):

    if not name:

        st.error(
            "Please enter Initiative Name"
        )

    else:

        create_initiative(
            name,
            industry,
            problem_statement,
            target_users,
            business_goal
        )

        st.success(
            "Initiative Created Successfully!"
        )

        st.page_link(
            "app.py",
            label="⬅ Back to Dashboard"
        )
