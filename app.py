import streamlit as st
from alerts.email_alert import send_email_alert  # ✅ Corrected import
from alerts.telegram_alert import send_telegram_alert
from auth.firebase_auth import login_user
from auth.postgres_auth import login_user_pg
from trading.simulator import simulate_trade
from utils.config import BINANCE_API_KEY

st.set_page_config(layout="wide")
st.title("📊 AI Trading Dashboard")
st.write("Welcome to the AI Trading Dashboard")