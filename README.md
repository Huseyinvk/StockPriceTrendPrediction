# Stock Price Trend Prediction

A machine learning project that predicts whether a stock’s closing price will go **up or down the next trading day** using historical market data and technical indicators.

This project focuses on **classification**, not price forecasting.

---

## Overview

Financial markets are noisy and difficult to predict.  
This project explores whether simple, well-known technical indicators combined with classical machine learning models can capture short-term price direction signals.

The goal is to classify:
- **1** → next-day return > 0  
- **0** → otherwise

---

## Key Features

- **Live Data Fetching:** Historical stock data via `yfinance`
- **Feature Engineering:**
  - Daily returns
  - Price relative to moving averages (MA10, MA50)
  - Rolling volatility (10-day, 20-day)
  - Volume ratio
- **Time-Series Aware Split:** 80% train / 20% test (no data leakage)
- **Model Persistence:** Trained model saved using `joblib`

---

## Tech Stack

- **Language:** Python
- **Data Analysis:** Pandas, NumPy
- **Machine Learning:** Scikit-learn
- **Model:** Logistic Regression
- **Preprocessing:** StandardScaler
- **Data Source:** Yahoo Finance (yfinance)

---

## Methodology

1. **Data Collection**
   - Download historical OHLCV data from Yahoo Finance

2. **Feature Engineering**
   - Compute technical indicators from historical prices
   - Remove look-ahead bias using forward returns only for labels

3. **Target Construction**
   - Binary label based on next-day return direction

4. **Model Training**
   - Pipeline: StandardScaler → Logistic Regression
   - Time-based train/test split

5. **Evaluation**
   - ROC-AUC
   - Precision / Recall / F1-score

---

## Results

- **ROC-AUC:** ~0.45  
- **Accuracy:** ~0.54  

Performance is close to a random baseline, which is expected in short-term financial prediction tasks due to market efficiency.

---

## Disclaimer

This project is for **educational purposes only**.  
It is **not financial advice** and should not be used for real trading decisions.
