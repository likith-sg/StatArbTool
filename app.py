import streamlit as st
from data.fetch_data import get_historical_data
from strategies.stat_arb import compute_spread, generate_signals
from utils.cointegration import check_cointegration
from utils.copula_analysis import fit_copula, plot_copula_density
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("📈 Crypto Statistical Arbitrage Tool with Copulas")

symbol1 = st.sidebar.text_input("First Symbol (e.g., BTCUSDT)", "BTCUSDT")
symbol2 = st.sidebar.text_input("Second Symbol (e.g., ETHUSDT)", "ETHUSDT")
copula_type = st.sidebar.selectbox("Copula Type", ['Gaussian', 'Clayton', 'Frank', 'Gumbel'])

if st.sidebar.button("Run Analysis"):
    df1 = get_historical_data(symbol1)
    df2 = get_historical_data(symbol2)

    min_len = min(len(df1), len(df2))
    df1, df2 = df1[-min_len:], df2[-min_len:]

    st.subheader("Cointegration Test")
    cointegrated, pval = check_cointegration(df1['close'], df2['close'])
    st.write(f"p-value: {pval:.4f} | Cointegrated: {'✅ Yes' if cointegrated else '❌ No'}")

    st.subheader("Z-Score & Signal Plot")
    spread = compute_spread(df1['close'], df2['close'])
    long, short, exit = generate_signals(spread)

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(spread, label='Spread')
    ax.axhline(spread.mean(), color='black', linestyle='--')
    ax.plot(spread[long], 'g^', label='Long')
    ax.plot(spread[short], 'rv', label='Short')
    ax.set_title("Spread & Signals")
    ax.legend()
    st.pyplot(fig)

    st.subheader("Copula Density Plot")
    copula, u1, u2 = fit_copula(df1['close'].pct_change().dropna(), df2['close'].pct_change().dropna(), copula_type)
    fig = plot_copula_density(copula, u1, u2, title=f"{copula_type} Copula Density")
    st.pyplot(fig)
 
