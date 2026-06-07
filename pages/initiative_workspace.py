import streamlit as st
import streamlit.components.v1 as components
from services.gemini_service import (
    generate_discovery,
    generate_market_analysis,
    generate_competition_analysis,
    generate_strategy,
    generate_roadmap,
    generate_prototype,
    generate_prd,
    generate_fsd,
    generate_user_stories
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

saved_prd = get_artifact(
    initiative_id,
    "prd"
)

saved_fsd = get_artifact(
    initiative_id,
    "fsd"
)

saved_stories = get_artifact(
    initiative_id,
    "stories"
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

artifact_status = {
    "Discovery": saved_discovery,
    "Market": saved_market,
    "Competition": saved_competition,
    "Strategy": saved_strategy,
    "Roadmap": saved_roadmap,
    "Prototype": saved_prototype,
    "PRD": saved_prd,
    "FSD": saved_fsd,
    "Stories": saved_stories
}

completed = sum(
    bool(v) for v in artifact_status.values()
)

total = len(artifact_status)

st.progress(completed / total)

st.write(
    f"{completed}/{total} Modules Complete"
)

st.divider()

# Tabs

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs([
    "🏠 Overview",
    "🔍 Discovery",
    "📈 Market",
    "🏆 Competition",
    "🎯 Strategy",
    "🗺️ Roadmap",
    "🎨 Prototype",
    "📄 PRD",
    "📑 FSD",
    "📋 User Stories"
])

# OVERVIEW

with tab1:

    st.subheader("📋 Project Summary")

    st.write(f"**Project Name:** {initiative[1]}")
    st.write(f"**Industry:** {initiative[2]}")

    st.divider()

    st.subheader("📊 Project Status")

    if not saved_discovery:
        next_step = "Generate Discovery"

    elif not saved_market:
        next_step = "Generate Market Analysis"

    elif not saved_competition:
        next_step = "Generate Competition Analysis"

    elif not saved_strategy:
        next_step = "Generate Product Strategy"

    elif not saved_roadmap:
        next_step = "Generate Roadmap"

    elif not saved_prototype:
        next_step = "Generate Prototype"

    elif not saved_prd:
        next_step = "Generate PRD"

    elif not saved_fsd:
        next_step = "Generate FSD"

    elif not saved_stories:
        next_step = "Generate User Stories"

    else:
        next_step = "Workflow Complete"

    st.info(
        f"Recommended Next Action: {next_step}"
    )

    st.divider()

    st.subheader("🎯 Problem Statement")
    st.write(initiative[3])

    st.subheader("👥 Target Users")
    st.write(initiative[4])

    st.subheader("🚀 Business Goal")
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

# COMPETITION

with tab4:

    st.subheader("🏆 Competition Analysis")

    if st.button("Generate Competition Analysis"):

        if saved_market:

            output = generate_competition_analysis(
                initiative[1],
                initiative[2],
                initiative[3],
                saved_market[0]
            )

            save_artifact(
                initiative_id,
                "competition",
                output
            )

            st.rerun()

        else:

            st.warning(
                "Generate Market Analysis first."
            )

    if saved_competition:

        st.markdown(
            saved_competition[0]
        )

# STRATEGY

# STRATEGY

with tab5:

    st.subheader("🎯 Product Strategy")

    if st.button("Generate Strategy"):

        if saved_competition:

            output = generate_strategy(
                initiative[1],
                saved_competition[0]
            )

            save_artifact(
                initiative_id,
                "strategy",
                output
            )

            st.rerun()

        else:

            st.warning(
                "Generate Competition Analysis first."
            )

    if saved_strategy:

        st.markdown(
            saved_strategy[0]
        )

# ROADMAP

with tab6:

    st.subheader("🗺️ Roadmap")

    if st.button("Generate Roadmap"):

        if saved_strategy:

            output = generate_roadmap(
                initiative[1],
                saved_strategy[0]
            )

            save_artifact(
                initiative_id,
                "roadmap",
                output
            )

            st.rerun()

        else:

            st.warning(
                "Generate Strategy first."
            )

    if saved_roadmap:

        st.markdown(
            saved_roadmap[0]
        )

# PROTOTYPE

with tab7:

    st.subheader("🎨 Prototype")

    if st.button("Generate Prototype"):

        if saved_roadmap:

            output = generate_prototype(
                initiative[1],
                saved_roadmap[0]
            )

            save_artifact(
                initiative_id,
                "prototype",
                output
            )

            st.rerun()

        else:

            st.warning(
                "Generate Roadmap first."
            )

    if saved_prototype:

    preview_tab, code_tab = st.tabs(
        ["Preview", "HTML Code"]
    )

    with preview_tab:

        components.html(
            saved_prototype[0],
            height=800,
            scrolling=True
        )

    with code_tab:

        st.code(
            saved_prototype[0],
            language="html"
        )
# PRD

with tab8:

    st.subheader("📄 PRD")

    if st.button("Generate PRD"):

        if saved_prototype:

            output = generate_prd(
                initiative[1],
                saved_prototype[0]
            )

            save_artifact(
                initiative_id,
                "prd",
                output
            )

            st.rerun()

        else:

            st.warning(
                "Generate Prototype first."
            )

    if saved_prd:

        st.markdown(
            saved_prd[0]
        )
# FSD

with tab9:

    st.subheader("📑 FSD")

    if st.button("Generate FSD"):

        if saved_prd:

            output = generate_fsd(
                initiative[1],
                saved_prd[0]
            )

            save_artifact(
                initiative_id,
                "fsd",
                output
            )

            st.rerun()

        else:

            st.warning(
                "Generate PRD first."
            )

    if saved_fsd:

        st.markdown(
            saved_fsd[0]
        )
# USER STORIES

with tab10:

    st.subheader("📋 User Stories")

    if st.button("Generate User Stories"):

        if saved_fsd:

            output = generate_user_stories(
                initiative[1],
                saved_fsd[0]
            )

            save_artifact(
                initiative_id,
                "stories",
                output
            )

            st.rerun()

        else:

            st.warning(
                "Generate FSD first."
            )

    if saved_stories:

        st.markdown(
            saved_stories[0]
        )
