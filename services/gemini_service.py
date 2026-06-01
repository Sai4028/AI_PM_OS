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
        "gemini-2.5-pro"
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
