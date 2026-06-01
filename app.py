import streamlit as st

from database.db import (
    init_db,
    get_initiatives
)

st.set_page_config(
    page_title="AI PM OS",
    page_icon="🚀",
    layout="wide"
)

init_db()

st.title("🚀 AI PM OS")

st.subheader("My Initiatives")

initiatives = get_initiatives()

if initiatives:

    for initiative in initiatives:

        col1, col2 = st.columns([4, 1])

        with col1:
            st.write(
                f"### {initiative[1]}"
            )
            st.caption(
                initiative[2]
            )

        with col2:

            if st.button(
                "Open",
                key=f"open_{initiative[0]}"
            ):
                st.session_state["initiative_id"] = initiative[0]
                st.switch_page(
                    "pages/initiative_workspace.py"
                )

        st.divider()

else:
    st.info(
        "No initiatives found."
    )

st.page_link(
    "pages/create_initiative.py",
    label="➕ Create New Initiative"
)
