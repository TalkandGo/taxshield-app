import streamlit as st

# --- 1. INITIALIZE GLOBAL SECURITY STATE ---
if "is_subscribed" not in st.session_state:
    st.session_state.is_subscribed = False

# --- 2. CONFIGURABLE CHECKOUT PORTAL URLS ---
# Paste your active PayPal Subscription Plan Link right here:
PAYPAL_SUBSCRIPTION_URL = "https://paypal.com"  
STRIPE_SUBSCRIPTION_URL = "https://stripe.com"  

# --- 3. TRANSLATION MAP ---
translations = {
    "English": {
        "app_title": "KeepRest App Dashboard",
        "tax_reminder": "📢 FRIENDLY TAX SEASON REMINDER: Tax time is around the corner. Organize your receipts so you are 100% prepared.",
        "settings_header": "⚙️ Settings",
        "state_label": "Select Your US State",
        "calculator_header": "💰 1099 Income Tax Estimator",
        "income_input_label": "Enter Your 1099 Income Amount ($)",
        "savings_label": "Amount To Set Aside For Upcoming Taxes",
        "peace_of_mind": "✨ Your financial data is securely tracked for absolute peace of mind.",
        "receipt_header": "📂 Receipt Vault & Tax Saver Engine",
        "receipt_subtext": "Lose your receipts easily? Type the amount OR snap a picture below to keep them safely organized for your tax accountant.",
        "upload_label": "Snap / Upload Receipt Pic",
        "paywall_title": "💳 Subscription Required ($12.99/mo)",
        "paywall_text": "Unlock complete interactive access to your personal KeepRest tax workspace instantly.",
        "paypal_button_text": "🟡 Subscribe via PayPal",
        "stripe_button_text": "💳 Subscribe via Stripe",
        "activation_label": "Owner Bypass or Paid Account? Enter passcode to unlock:",
        "btn_activate": "Unlock App Dashboard",
        "preview_banner": "👀 PREVIEW MODE: Below is a read-only preview of what you get when you subscribe.",
        
        "demo_title": "📱 How KeepRest Works (Quick Tour):",
        "step_1": "1️⃣ **Choose your State** - The dashboard instantly loads local rules.",
        "step_2": "2️⃣ **Input 1099 Revenue** - Know exactly how much to set aside for the IRS.",
        "step_3": "3️⃣ **Vault Receipts** - Snap and store photos so you never lose a tax deduction write-off."
    }
}

t = translations["English"]

# --- 4. THE CONTENT RENDERING ENGINE ---
def render_dashboard(disabled_mode=False):
    st.header(t["settings_header"])
    
    # 🇺🇸 COMPLETE 50 US STATES LIST
    us_states = [
        "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", 
        "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", 
        "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", 
        "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", 
        "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", 
        "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", 
        "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", 
        "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", 
        "Utah", "Vermont", "Virginia", "Washington", "West Virginia", 
        "Wisconsin", "Wyoming", "Other"
    ]
    
    selected_state = st.selectbox(t["state_label"], options=us_states, disabled=disabled_mode, key="state_box")

    st.header(t["calculator_header"])
    income = st.number_input(t["income_input_label"], min_value=0.0, step=1000.0, disabled=disabled_mode, key="income_box")
    
    # 🧮 SELF-EMPLOYED 1099 TAX BUFFER CALCULATION
    # Sets aside a 15% buffer for state-tax-free zones or 25% to safely cover combined Self-Employment + State tax cushions
    no_state_tax = ["Alaska", "Florida", "Nevada", "New Hampshire", "South Dakota", "Tennessee", "Texas", "Washington", "Wyoming"]
    
    if selected_state in no_state_tax:
        tax_rate = 0.15  
    else:
        tax_rate = 0.25  
        
    calculated_savings = income * tax_rate
    
    # Clear, direct financial guidance metric for 1099 workers
    st.metric(label=t["savings_label"], value=f"${calculated_savings:,.2f}")
    st.caption(t["peace_of_mind"])

    # Safe account keeper zone for receipt handoffs to CPA/tax pros
    st.header(t["receipt_header"])
    st.write(t["receipt_subtext"])
    st.file_uploader(t["upload_label"], type=["png", "jpg", "jpeg"], disabled=disabled_mode, key="vault_box")


# --- 5. CONDITIONAL PAYWALL ROUTING ---
st.title(t["app_title"])

if not st.session_state.is_subscribed:
    # --- SHOW PAYWALL DIRECTLY ON FRONT PAGE ---
    with st.container(border=True):
        st.subheader(t["paywall_title"])
        st.write(t["paywall_text"])
        st.divider()
        
        # Text Walkthrough Tour card
        st.markdown(f"### {t['demo_title']}")
        st.markdown(t["step_1"])
        st.markdown(t["step_2"])
        st.markdown(t["step_3"])
        st.divider()
        
        # Checkout Option Gateways
        st.markdown("### 🔒 Select a Gateway to Subscribe:")
        c1, c2 = st.columns(2)
        with c1:
            st.link_button(t["paypal_button_text"], PAYPAL_SUBSCRIPTION_URL, use_container_width=True)
        with c2:
            st.link_button(t["stripe_button_text"], STRIPE_SUBSCRIPTION_URL, use_container_width=True)
            
        st.divider()
        
        # OWNER / BUYER UNLOCK BOX
        code = st.text_input(t["activation_label"], placeholder="Type a passcode to unlock...")
        if st.button(t["btn_activate"], type="primary"):
            if code.strip() == "securepass123":
                st.session_state.is_subscribed = True
                st.rerun()
            else:
                st.error("Invalid passcode. Please try again.")
                
    st.divider()
    st.info(t["preview_banner"])
    render_dashboard(disabled_mode=True)

else:
    # --- DASHBOARD FULLY UNLOCKED ---
    st.info(t["tax_reminder"])
    if st.sidebar.button("Lock Dashboard / Log Out"):
        st.session_state.is_subscribed = False
        st.rerun()
        
    render_dashboard(disabled_mode=False)
