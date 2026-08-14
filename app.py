import streamlit as st
import pandas as pd
import plotly.express as px

from ai_agent import generate_insights


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="AI Data Analyst",
    page_icon="🤖",
    layout="wide"
)


# ==================================================
# TITLE
# ==================================================

st.title("🤖 AI Data Analyst Agent")

st.write(
    "Upload your CSV file and get automated analysis, "
    "visualizations, and AI-powered business insights."
)


# ==================================================
# FILE UPLOAD
# ==================================================

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)


# ==================================================
# MAIN APP
# ==================================================

if uploaded_file:

    # ==================================================
    # READ DATASET
    # ==================================================

    df = pd.read_csv(uploaded_file)


    # ==================================================
    # CREATE AI DATASET CONTEXT
    # ==================================================

    context = f"""
DATASET INFORMATION

Number of rows:
{df.shape[0]}

Number of columns:
{df.shape[1]}

Column names:
{list(df.columns)}

STATISTICAL SUMMARY:

{df.describe(include="all").to_string()}
"""


    # ==================================================
    # REVENUE ANALYSIS
    # ==================================================

    if "Revenue" in df.columns:

        context += f"""

REVENUE INFORMATION:

Total Revenue:
{df["Revenue"].sum():,.2f}

Average Revenue:
{df["Revenue"].mean():,.2f}

Highest Revenue:
{df["Revenue"].max():,.2f}
"""


    # ==================================================
    # PROFIT ANALYSIS
    # ==================================================

    if "Profit" in df.columns:

        context += f"""

PROFIT INFORMATION:

Total Profit:
{df["Profit"].sum():,.2f}

Average Profit:
{df["Profit"].mean():,.2f}

Highest Profit:
{df["Profit"].max():,.2f}
"""


    # ==================================================
    # PRODUCT ANALYSIS
    # ==================================================

    if "Product" in df.columns and "Revenue" in df.columns:

        product_revenue = (
            df.groupby("Product")["Revenue"]
            .sum()
            .sort_values(ascending=False)
        )

        context += f"""

REVENUE BY PRODUCT:

{product_revenue.to_string()}
"""


    # ==================================================
    # PRODUCT PROFIT ANALYSIS
    # ==================================================

    if "Product" in df.columns and "Profit" in df.columns:

        product_profit = (
            df.groupby("Product")["Profit"]
            .sum()
            .sort_values(ascending=False)
        )

        context += f"""

PROFIT BY PRODUCT:

{product_profit.to_string()}
"""


    # ==================================================
    # REGION ANALYSIS
    # ==================================================

    if "Region" in df.columns and "Revenue" in df.columns:

        region_revenue = (
            df.groupby("Region")["Revenue"]
            .sum()
            .sort_values(ascending=False)
        )

        context += f"""

REVENUE BY REGION:

{region_revenue.to_string()}
"""


    # ==================================================
    # DATASET PREVIEW
    # ==================================================

    st.subheader("📊 Dataset Preview")

    st.dataframe(
        df,
        use_container_width=True
    )


    # ==================================================
    # DATASET OVERVIEW
    # ==================================================

    st.subheader("📌 Dataset Overview")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Rows",
            df.shape[0]
        )

    with col2:
        st.metric(
            "Total Columns",
            df.shape[1]
        )

    with col3:
        st.metric(
            "Duplicate Rows",
            df.duplicated().sum()
        )


    # ==================================================
    # MISSING VALUES
    # ==================================================

    st.subheader("⚠️ Missing Values")

    missing_data = df.isnull().sum()

    st.dataframe(
        missing_data,
        use_container_width=True
    )


    # ==================================================
    # STATISTICAL SUMMARY
    # ==================================================

    st.subheader("📈 Statistical Summary")

    st.dataframe(
        df.describe(),
        use_container_width=True
    )


    # ==================================================
    # REVENUE CHART
    # ==================================================

    if "Product" in df.columns and "Revenue" in df.columns:

        st.subheader("💰 Revenue by Product")

        revenue_data = (
            df.groupby("Product")["Revenue"]
            .sum()
            .reset_index()
            .sort_values(
                "Revenue",
                ascending=False
            )
        )

        fig = px.bar(
            revenue_data,
            x="Product",
            y="Revenue",
            title="Revenue Performance"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # ==================================================
    # PROFIT CHART
    # ==================================================

    if "Product" in df.columns and "Profit" in df.columns:

        st.subheader("📈 Profit by Product")

        profit_data = (
            df.groupby("Product")["Profit"]
            .sum()
            .reset_index()
            .sort_values(
                "Profit",
                ascending=False
            )
        )

        fig2 = px.bar(
            profit_data,
            x="Product",
            y="Profit",
            title="Profit Performance"
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )


    # ==================================================
    # CATEGORY CHART
    # ==================================================

    if "Category" in df.columns and "Revenue" in df.columns:

        st.subheader("🥧 Revenue by Category")

        category_data = (
            df.groupby("Category")["Revenue"]
            .sum()
            .reset_index()
        )

        fig3 = px.pie(
            category_data,
            names="Category",
            values="Revenue",
            title="Category Revenue Distribution"
        )

        st.plotly_chart(
            fig3,
            use_container_width=True
        )


    # ==================================================
    # AI GENERATED REPORT
    # ==================================================

    st.divider()

    st.subheader("🧠 AI Analyst")

    if st.button("Generate AI Insights"):

        report_prompt = f"""
You are analyzing this business dataset.

DATASET CONTEXT:

{context}

Generate a professional business analysis.

Include:

## Executive Summary

## Key Findings

## Data Evidence

## Business Recommendations

## Next Steps

Use only the information supported by the dataset.

Do not invent facts or numbers.
Clearly distinguish facts from recommendations.
"""

        with st.spinner(
            "🤖 AI is analyzing your dataset..."
        ):

            response = generate_insights(
                report_prompt
            )

        st.markdown(response)


    # ==================================================
    # CHAT WITH DATASET
    # ==================================================

    st.divider()

    st.subheader("💬 Chat With Your Dataset")

    question = st.text_input(
        "Ask a question about your data",
        placeholder="Example: Which product performs best?"
    )


    if question:

        chat_prompt = f"""
DATASET CONTEXT:

{context}

USER QUESTION:

{question}

Answer the user's question directly.

IMPORTANT:

- Use ONLY information supported by the dataset.
- Do not invent facts or numbers.
- Focus only on information relevant to the question.
- Do not discuss unrelated columns or metrics.
- Do not generate a long report unless the user asks for detailed analysis.
- If the question is simple, give a concise answer.
"""

        with st.spinner(
            "🤖 AI is analyzing your question..."
        ):

            answer = generate_insights(
                chat_prompt
            )

        st.markdown("### 🤖 AI Analyst")

        st.markdown(answer)