import streamlit as st
import joblib
import pandas as pd
import yfinance as yf

# Başlık
st.title("📈 Stock Trend Prediction App")

# Modeli yükle
model = joblib.load("model.joblib")

# Kullanıcıdan hisse al
ticker = st.text_input("Hisse sembolü gir (örn: AAPL, THYAO.IS)", "AAPL")

if st.button("Tahmin Et"):
    data = yf.download(ticker, period="6mo")

    if data.empty:
        st.error("Veri çekilemedi")
    else:
        data["ret_1"] = data["Close"].pct_change()
        data["ma_10"] = data["Close"].rolling(10).mean()
        data["ma_50"] = data["Close"].rolling(50).mean()
        data["vol_10"] = data["ret_1"].rolling(10).std()
        data["vol_20"] = data["ret_1"].rolling(20).std()
        data["vol_ratio"] = data["Volume"] / data["Volume"].rolling(20).mean()

        data = data.dropna()

        X = data[[
            "ret_1",
            "ma_10",
            "ma_50",
            "vol_10",
            "vol_20",
            "vol_ratio"
        ]].iloc[-1:]

        pred = model.predict(X)[0]
        prob = model.predict_proba(X)[0][1]

        st.subheader("Sonuç")
        if pred == 1:
            st.success(f"📈 Yükseliş bekleniyor (olasılık: %{prob*100:.1f})")
        else:
            st.warning(f"📉 Düşüş bekleniyor (olasılık: %{(1-prob)*100:.1f})")
