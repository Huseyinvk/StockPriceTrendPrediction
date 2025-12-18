# Stock Trend Prediction App

**Live Demo (Streamlit App):**  
👉 https://stockpricetrendprediction-lnmredthjfqeax6ugkucek.streamlit.app

An end-to-end **Machine Learning–powered web application** that predicts short-term stock price trends using historical market data and technical indicators.

This project covers the **full ML lifecycle** — from data ingestion and feature engineering to model inference and live deployment.


An end-to-end **Machine Learning & Data Science** project that predicts short-term stock price **trend direction** using historical market data.

The project includes:
- Feature engineering on financial time series
- A trained classification model
- An interactive **Streamlit web application**

---

## Problem Definition
Given historical stock data, the model predicts whether the **next trading day’s closing price** will increase or decrease compared to today.

This is framed as a **binary classification** problem:
- `0` → No increase / downward movement
- `1` → Upward movement

---

## Model Overview
- **Algorithm:** Logistic Regression
- **Validation:** TimeSeriesSplit (prevents data leakage)
- **Target:** Next-day price direction
- **Output:** Probability-based trend prediction

---

## Feature Engineering
Key features include:
- Daily returns
- Moving average ratios (MA10, MA50)
- Volatility measures
- Volume anomaly indicators

The model focuses on **price behavior**, not raw prices.

---

## Web Application
The Streamlit app allows users to:
- Enter a stock ticker (e.g. AAPL, THYAO.IS)
- Fetch live market data
- View predicted trend direction with probability

---

## Tech Stack
- Python
- Pandas, NumPy
- scikit-learn
- yfinance
- Streamlit

---

##  Disclaimer
This project is for educational purposes only and does **not** constitute financial advice.

---

## AI Assistance Notice

AI-based tools were used during the development of this project to accelerate experimentation, improve code quality, and assist with documentation.  
The overall system design, data pipeline, model selection, and evaluation were performed by the author.

