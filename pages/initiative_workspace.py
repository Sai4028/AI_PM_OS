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

saved_competition = get_artifact(
    initiative_id,
    "competition"
)

saved_strategy = get_artifact(
    initiative_id,
    "strategy"
)

saved_roadmap = get_artifact(
    initiative_id,
    "roadmap"
)

saved_prototype = get_artifact(
    initiative_id,
    "prototype"
)

if not initiative:

    st.error(
        "Initiative not found."
    )

    st.stop()

st.header(initiative[1])

# Progress Section

st.divider()

st.subheader("📊 Project Progress")

completed = sum([
    bool(saved_discovery),
    bool(saved_market),
    bool(saved_competition),
    bool(saved_strategy),
    bool(saved_roadmap),
    bool(saved_prototype)
])

total = 6

st.progress(completed / total)

st.write(
    f"{completed}/{total} Modules Complete"
)

st.divider()

# Tabs

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "🏠 Overview",
    "🔍 Discovery",
    "📈 Market",
    "🏆 Competition",
    "🎯 Strategy",
    "🗺️ Roadmap",
    "🎨 Prototype"
])

# OVERVIEW

with tab1:

    st.caption(initiative[2])

    st.subheader("Problem Statement")
    st.write(initiative[3])

    st.subheader("Target Users")
    st.write(initiative[4])

    st.subheader("Business Goal")
    st.write(initiative[5])

# DISCOVERY

with tab2:

    st.subheader("🤖 AI PM Insights")

    if st.button("Analyze Initiative"):

        with st.spinner("Analyzing..."):

            output = generate_discovery(
                initiative[1],
                initiative[2],
                initiative[3],
                initiative[4],
                initiative[5]
            )

            save_artifact(
                initiative_id,
                "discovery",
                output
            )

            st.rerun()

    if saved_discovery:
        st.markdown(saved_discovery[0])

# MARKET

with tab3:

    st.subheader("📈 Market Analysis")

    if st.button("Generate Market Analysis"):

        if saved_discovery:

            with st.spinner("Analyzing Market..."):

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
        st.markdown(saved_market[0])

# COMPETITION

with tab4:

    st.subheader("🏆 Competition Analysis")

    if st.button("Generate Competition Analysis"):

        output = """
Competition Analysis Placeholder

Coming Soon
"""

        save_artifact(
            initiative_id,
            "competition",
            output
        )

        st.rerun()

    if saved_competition:
        st.markdown(saved_competition[0])

# STRATEGY

with tab5:

    st.subheader("🎯 Product Strategy")

    if st.button("Generate Strategy"):

        output = """
Product Strategy Placeholder

Coming Soon
"""

        save_artifact(
            initiative_id,
            "strategy",
            output
        )

        st.rerun()

    if saved_strategy:
        st.markdown(saved_strategy[0])

# ROADMAP

with tab6:

    st.subheader("🗺️ Roadmap")

    if st.button("Generate Roadmap"):

        output = """
Roadmap Placeholder

Coming Soon
"""

        save_artifact(
            initiative_id,
            "roadmap",
            output
        )

        st.rerun()

    if saved_roadmap:
        st.markdown(saved_roadmap[0])

# PROTOTYPE

with tab7:

    st.subheader("🎨 Prototype")

    if st.button("Generate Prototype"):

        output = """
Prototype Placeholder

Screen 1:
Dashboard

Screen 2:
Search

Screen 3:
Details

Screen 4:
Recommendations
"""

        save_artifact(
            initiative_id,
            "prototype",
            output
        )

        st.rerun()

    if saved_prototype:
        st.markdown(saved_prototype[0])
