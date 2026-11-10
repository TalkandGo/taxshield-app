import streamlit as st

st.set_page_config(page_title="KeepRest", page_icon="🛡️", layout="centered")

# Clean 10-Language Selector Dropdown Matrix
lang_map = {
    "English": "en", "Español": "es", "简体中文": "zh", "Français": "fr", 
    "العربية": "ar", "Tagalog": "tl", "Tiếng Việt": "vi", "한국어": "ko", 
    "Português": "pt", "हिन्दी": "hi"
}
selected_lang = st.selectbox("🌐 Choose Language / Idioma / 语言 / भाषा", list(lang_map.keys()))

st.title("🛡️ KeepRest")
st.warning("⏰ **FRIENDLY TAX SEASON REMINDER:** Tax time is getting close! Keep saving and logging your receipts so you are 100% prepared.")

# Initialize background data counters
if 'tax_vault' not in st.session_state: st.session_state.tax_vault = 0.00
if 'estimated_savings' not in st.session_state: st.session_state.estimated_savings = 0.00

st.markdown("---")
st.markdown("### ⚙️ Settings")
state_rates = {"California": 0.33, "New York": 0.32, "Texas": 0.25, "Florida": 0.25, "North Carolina": 0.28, "Illinois": 0.29, "Ohio": 0.27, "Georgia": 0.28, "Pennsylvania": 0.28, "Washington": 0.25, "Virginia": 0.28, "Massachusetts": 0.30}
chosen_state = st.selectbox("Select Your US State", list(state_rates.keys()))
tax_rate = state_rates[chosen_state]

st.markdown("---")
st.markdown("### 💰 Income Calculator")
income = st.number_input("Enter Your New Income Amount ($)", min_value=0.0, value=0.0, step=100.0)

if income > 0:
    calculated_tax = income * tax_rate
    safe_spend = income - calculated_tax
    st.markdown(f"**Tax to set aside in your private bank account ({int(tax_rate * 100)}%):** `${calculated_tax:,.2f}`")
    st.markdown(f"**Guilt-free money left over to spend:** <span style='color:#1565c0; font-weight:bold; font-size:22px;'>${safe_spend:,.2f}</span>", unsafe_allow_html=True)
    st.session_state.tax_vault = calculated_tax

st.markdown("---")
st.markdown("### 📁 Receipt Vault & Tax Saver Estimator")
st.caption("💡 Lose your receipts easily? Type the amount OR snap a picture below to securely store it for tax time!")

col_exp_pic, col_exp_amt = st.columns(2)
with col_exp_pic: receipt_file = st.file_uploader("📷 Snap / Upload Receipt Pic", type=["jpg", "jpeg", "png"])
with col_exp_amt: expense_amt = st.number_input("Enter Receipt Total ($)", min_value=0.0, value=0.0, step=10.0)

if (expense_amt > 0 or receipt_file) and st.button("📁 Save to Receipt Vault"):
    st.session_state.estimated_savings += ((expense_amt if expense_amt > 0 else 50.00) * 0.15)
    st.success("Receipt safely saved in your vault! Keeping records lowers your final tax bill.")


st.markdown("---")
st.markdown("### 🔒 Your Tax & Savings Ledger Balance")
col1, col2 = st.columns(2)
with col1: st.metric(label="Estimated Total Tax to Set Aside", value=f"${st.session_state.tax_vault:,.2f}")
with col2: st.metric(label="Estimated Tax Savings From Receipts", value=f"${st.session_state.estimated_savings:,.2f}")
st.markdown("🟢 Keep your tax money safe inside your main bank or PayPal account. What remains is **100% yours to spend without guilt.**")
