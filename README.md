# StockPriceTrendPrediction

# StockTrend AI: Time Series Forecasting with LSTM

An end-to-end Machine Learning project that leverages **Deep Learning** to predict stock price trends. This project focuses on using **Long Short-Term Memory (LSTM)** networks to analyze historical stock data and forecast future movements.

---

## Overview
Predicting the stock market is a complex task influenced by numerous factors. This project demonstrates the application of **Recurrent Neural Networks (RNN)** to capture patterns in sequential financial data.

### Key Features:
* **Live Data Fetching:** Uses `yfinance` to retrieve up-to-date market data.
* **Technical Indicators:** Incorporates Moving Averages (SMA/EMA) to enhance feature depth.
* **Data Scaling:** Implements Robust Scaling to handle financial outliers.
* **Visualization:** Interactive charts comparing predicted vs. actual prices.

---

## Tech Stack
* **Language:** Python 3.x
* **Deep Learning:** TensorFlow / Keras
* **Data Analysis:** Pandas, NumPy
* **Visualization:** Matplotlib, Plotly
* **Data Source:** Yahoo Finance API

---

## How It Works

The project follows a rigorous data science pipeline:

1.  **Data Ingestion:** Downloading historical OHLC (Open, High, Low, Close) data.
2.  **Feature Engineering:** Creating a 60-day sliding window of historical prices to predict the 61st day.
3.  **Model Architecture:** * Multiple **LSTM** layers to capture long-term dependencies.
    * **Dropout** layers to prevent overfitting.
    * **Dense** output layer for price regression.
4.  **Backtesting:** Evaluating performance on a separate "unseen" test set.

---

## Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/stock-trend-prediction.git](https://github.com/yourusername/stock-trend-prediction.git)
