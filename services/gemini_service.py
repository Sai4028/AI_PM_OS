import streamlit as st
import google.generativeai as genai

def generate_discovery(
    project_name,
    industry,
    problem_statement,
    target_users,
    business_goal
):

    genai.configure(
        api_key=st.secrets["GEMINI_API_KEY"]
    )

    model = genai.GenerativeModel(
        "gemini-2.5-flash"
    )

    prompt = f"""
You are a Senior Product Manager.

Analyze this initiative.

Project:
{project_name}

Industry:
{industry}

Problem:
{problem_statement}

Users:
{target_users}

Goal:
{business_goal}

Generate:

1. Problem Summary

2. Key Pain Points

3. Business Impact

4. Assumptions

5. Success Metrics

Keep response practical.
"""

    response = model.generate_content(
        prompt
    )

    return response.text


def generate_market_analysis(
    project_name,
    industry,
    problem_statement,
    discovery_output
):

    genai.configure(
        api_key=st.secrets["GEMINI_API_KEY"]
    )

    model = genai.GenerativeModel(
        "gemini-2.5-flash"
    )

    prompt = f"""
You are a Product Strategy Consultant.

Project:
{project_name}

Industry:
{industry}

Problem:
{problem_statement}

Discovery Insights:
{discovery_output}

Generate:

1. Market Trends

2. Market Opportunities

3. Industry Challenges

4. Competitive Landscape

5. Strategic Recommendations

Keep it concise and practical.
"""

    response = model.generate_content(
        prompt
    )

    return response.text
def generate_competition_analysis(
    project_name,
    industry,
    problem_statement,
    market_analysis
):

    genai.configure(
        api_key=st.secrets["GEMINI_API_KEY"]
    )

    model = genai.GenerativeModel(
        "gemini-2.5-flash"
    )

    prompt = f"""
You are a Product Strategy Consultant.

Project:
{project_name}

Industry:
{industry}

Problem:
{problem_statement}

Market Analysis:
{market_analysis}

Generate:

1. Top Competitors

2. Competitor Strengths

3. Competitor Weaknesses

4. Market Gaps

5. Differentiation Opportunities

Keep response practical.
"""

    response = model.generate_content(
        prompt
    )

    return response.text
def generate_strategy(
    project_name,
    competition_analysis
):

    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

    model = genai.GenerativeModel("gemini-2.5-flash")

    prompt = f"""
Project:
{project_name}

Competition Analysis:
{competition_analysis}

Generate:

1. Product Vision
2. Strategic Objectives
3. Differentiators
4. Success Metrics
5. Risks
"""

    response = model.generate_content(prompt)

    return response.text

def generate_roadmap(
    project_name,
    strategy_output
):

    genai.configure(
        api_key=st.secrets["GEMINI_API_KEY"]
    )

    model = genai.GenerativeModel(
        "gemini-2.5-flash"
    )

    prompt = f"""
You are a Senior Product Manager.

Project:
{project_name}

Strategy:
{strategy_output}

Create a product roadmap.

Generate:

Phase 1 (0-3 Months)
- Key Features
- Expected Outcomes

Phase 2 (3-6 Months)
- Key Features
- Expected Outcomes

Phase 3 (6-12 Months)
- Key Features
- Expected Outcomes

Dependencies

Risks

Success Metrics
"""

    response = model.generate_content(
        prompt
    )

    return response.text

def generate_prototype(
    project_name,
    roadmap_output
):

    genai.configure(
        api_key=st.secrets["GEMINI_API_KEY"]
    )

    model = genai.GenerativeModel(
        "gemini-2.5-flash"
    )

    prompt = f"""
You are a Senior Product Designer.

Project:
{project_name}

Roadmap:
{roadmap_output}

Generate a low-fidelity product prototype.

Provide:

1. Screen Name

2. Purpose

3. Key Components

4. User Actions

Generate at least 5 screens.

Format clearly.
"""

    response = model.generate_content(
        prompt
    )

    return response.text

def generate_prd(
    project_name,
    strategy_output
):

    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

    model = genai.GenerativeModel("gemini-2.5-flash")

    prompt = f"""
Project:
{project_name}

Strategy:
{strategy_output}

Generate a Product Requirements Document with:

1. Objective
2. Scope
3. User Personas
4. Functional Requirements
5. Success Metrics
"""

    response = model.generate_content(prompt)

    return response.text
def generate_fsd(
    project_name,
    prd_output
):

    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

    model = genai.GenerativeModel("gemini-2.5-flash")

    prompt = f"""
Project:
{project_name}

PRD:
{prd_output}

Generate a Functional Specification Document including:

1. Features
2. Process Flow
3. Business Rules
4. Validations
5. Data Requirements
"""

    response = model.generate_content(prompt)

    return response.text
def generate_user_stories(
    project_name,
    fsd_output
):

    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

    model = genai.GenerativeModel("gemini-2.5-flash")

    prompt = f"""
Project:
{project_name}

FSD:
{fsd_output}

Generate:

10 User Stories

For each story provide:

- Story Title
- User Story
- Acceptance Criteria
- Priority
"""

    response = model.generate_content(prompt)

    return response.text
