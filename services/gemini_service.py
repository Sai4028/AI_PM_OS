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

def generate_market_analysis(
    project_name,
    industry,
    problem_statement,
    discovery_output
):

    import streamlit as st
    import google.generativeai as genai

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

    return response.text
