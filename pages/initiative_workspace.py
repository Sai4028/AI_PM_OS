import streamlit as st
from services.gemini_service import (
    generate_discovery,
    generate_market_analysis
)
from database.db import (
    get_initiative_by_id,
    save_artifact,
    get_artifact
)

st.title("📁 Initiative Workspace")

if "initiative_id" not in st.session_state:

    st.warning(
        "Please select an initiative first."
    )

    st.stop()

initiative_id = st.session_state[
    "initiative_id"
]

initiative = get_initiative_by_id(
    initiative_id
)

saved_discovery = get_artifact(
    initiative_id,
    "discovery"
)
saved_market = get_artifact(
    initiative_id,
    "market"
)

if not initiative:

    st.error(
        "Initiative not found."
    )

    st.stop()

st.header(
    initiative[1]
)

st.caption(
    initiative[2]
)

st.subheader(
    "Problem Statement"
)

st.write(
    initiative[3]
)

st.subheader(
    "Target Users"
)

st.write(
    initiative[4]
)

st.subheader(
    "Business Goal"
)

st.write(
    initiative[5]
)

st.divider()

st.subheader(
    "Project Modules"
)

modules = [
    "Discovery",
    "Market Analysis",
    "Competition",
    "Strategy",
    "Roadmap",
    "Prototype",
    "PRD",
    "FSD",
    "Release Notes",
    "Sales Deck"
]

for module in modules:

    st.write(
        f"○ {module}"
    )

st.divider()

st.info(
    "Discovery Module Coming Soon"
)

st.divider()

st.subheader(
    "🤖 AI PM Insights"
)

if st.button(
    "Analyze Initiative"
):

    with st.spinner(
        "Analyzing..."
    ):

        output = generate_discovery(
            initiative[1],
            initiative[2],
            initiative[3],
            initiative[4],
            initiative[5]
        )

        st.session_state[
            "discovery_output"
        ] = output
        save_artifact(
            initiative_id,
            "discovery",
            output
        )

if saved_discovery:
    st.markdown(
        
        saved_discovery[0]
    )
st.divider()

st.subheader("📈 Market Analysis")
if st.button(
    "Generate Market Analysis"
):

    if saved_discovery:

        with st.spinner(
            "Analyzing Market..."
        ):

            output = generate_market_analysis(
                initiative[1],
                initiative[2],
                initiative[3],
                saved_discovery[0]
            )

            save_artifact(
                initiative_id,
                "market",
                output
            )

            st.rerun()
    if saved_market:

        st.markdown(
            saved_market[0]
        )
