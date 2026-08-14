# 🤖 AI Data Analyst Agent

An AI-powered data analysis application that allows users to upload CSV datasets, explore their data through interactive visualizations, and ask natural-language questions to receive AI-generated business insights.

The goal of this project is to combine **Data Analytics + Generative AI + Business Intelligence** into a single intelligent analyst assistant.

---

## 🚀 Features

- 📂 Upload CSV datasets
- 📊 Automatic dataset preview
- 📌 Dataset overview and statistics
- ⚠️ Missing-value detection
- 🔢 Statistical analysis
- 💰 Revenue analysis
- 📈 Profit analysis
- 🥧 Category-level analysis
- 📊 Interactive Plotly visualizations
- 🧠 AI-generated business insights
- 💬 Chat with your dataset using natural-language questions
- 🔍 Data-driven recommendations
- 🛡️ API key protection using environment variables

---

## 🧠 How It Works

```text
             CSV Dataset
                  │
                  ▼
        ┌───────────────────┐
        │   Pandas Engine   │
        │ Data Processing   │
        └─────────┬─────────┘
                  │
                  ▼
        ┌───────────────────┐
        │ Data Analysis     │
        │ Statistics        │
        │ Aggregations      │
        └─────────┬─────────┘
                  │
          ┌───────┴────────┐
          ▼                ▼
   Interactive Charts    AI Analyst
          │                │
          │                ▼
          │        Natural Language
          │             Q&A
          │                │
          └────────┬───────┘
                   ▼
          Business Insights
          & Recommendations
