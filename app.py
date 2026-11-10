import streamlit as st
import streamlit.components.v1 as components

# --- 1. INITIALIZE GLOBAL SECURITY STATE ---
if "is_subscribed" not in st.session_state:
    st.session_state.is_subscribed = False

if "estimated_savings" not in st.session_state:
    st.session_state.estimated_savings = 0.0

# --- 2. CONFIGURABLE CHECKOUT PORTAL URLS ---
# Paste your Stripe payment link right here inside the quotes:
STRIPE_SUBSCRIPTION_URL = "https://stripe.com"  

# 🖼️ YOUR APP DEMO ANIMATION LINK:
# Replace this with a link to an animated GIF demonstrating your app in motion!
# Right now, it points to a premium financial dashboard layout placeholder animation loop.
APP_DEMO_GIF_URL = "https://giphy.com"

# Your real embedded PayPal Subscription Button script
PAYPAL_BUTTON_HTML = """
<div style="text-align: center;">
    <div id="paypal-button-container-P-0CH31499JV265374YNLZJYJI"></div>
</div>
<script src="https://paypal.com" data-sdk-integration-source="button-factory"></script>
<script>
  paypal.Buttons({
      style: {
          shape: 'rect',
          color: 'gold',
          layout: 'vertical',
          label: 'subscribe'
      },
      createSubscription: function(data, actions) {
        return actions.subscription.create({
          plan_id: 'P-0CH31499JV265374YNLZJYJI'
        });
      },
      onApprove: function(data, actions) {
        alert("Subscription Approved! ID: " + data.subscriptionID); 
      }
  }).render('#paypal-button-container-P-0CH31499JV265374YNLZJYJI');
</script>
"""

# --- 3. TRANSLATION MAP ---
translations = {
    "English": {
        "app_title": "KeepRest App Dashboard",
        "tax_reminder": "📢 FRIENDLY TAX SEASON REMINDER: Tax time is around the corner. Organize your receipts so you are 100% prepared.",
        "settings_header": "⚙️ Settings",
        "state_label": "Select Your US State",
        "calculator_header": "💰 Income Calculator",
        "income_input_label": "Enter Your New Income Amount ($)",
        "savings_label": "Estimated Tax Savings Progress",
        "peace_of_mind": "✨ Your financial data is securely tracked for absolute peace of mind.",
        "receipt_header": "📂 Receipt Vault & Tax Saver Engine",
        "receipt_subtext": "Lose your receipts easily? Type the amount OR snap a picture below.",
        "upload_label": "Snap / Upload Receipt Pic",
        "paywall_title": "💳 Subscription Required ($12.99/mo)",
        "paywall_text": "Unlock complete interactive access to your KeepRest platform. Watch the interactive dashboard workflow preview below:",
        "stripe_button_text": "💳 Subscribe via Stripe",
        "activation_label": "Owner Bypass or Paid Account? Enter passcode to unlock:",
        "btn_activate": "Unlock App Dashboard",
        "preview_banner": "👀 PREVIEW MODE: Below is a read-only preview of what you get when you subscribe."
    }
}

t = translations["English"]

# --- 4. THE CONTENT RENDERING ENGINE ---
def render_dashboard(disabled_mode=False):
    st.header(t["settings_header"])
    us_states = ["California", "Texas", "Florida", "New York", "Other"]
    st.selectbox(t["state_label"], options=us_states, disabled=disabled_mode, key="state_box")

    st.header(t["calculator_header"])
    st.number_input(t["income_input_label"], min_value=0.0, step=1000.0, disabled=disabled_mode, key="income_box")
    st.metric(label=t["savings_label"], value=f"${st.session_state.estimated_savings:,.2f}")
    st.caption(t["peace_of_mind"])

    st.header(t["receipt_header"])
    st.write(t["receipt_subtext"])
    st.file_uploader(t["upload_label"], type=["png", "jpg", "jpeg"], disabled=disabled_mode, key="vault_box")


# --- 5. CONDITIONAL PAYWALL ROUTING ---
st.title(t["app_title"])

if not st.session_state.is_subscribed:
    # --- SHOW PAYWALL AND MOVING PREVIEW DIRECTLY ON FRONT PAGE ---
    with st.container(border=True):
        st.subheader(t["paywall_title"])
        st.write(t["paywall_text"])
        
        # 🎬 The moving walkthrough showcase loop
        st.image(APP_DEMO_GIF_URL, caption="KeepRest Platform Functionality Demo Walkthrough", use_container_width=True)
        st.divider()
        
        # Checkout Option Gateways
        st.markdown("### 🔒 Select a Gateway to Subscribe:")
        c1, c2 = st.columns(2)
        with c1:
            components.html(PAYPAL_BUTTON_HTML, height=180, scrolling=False)
        with c2:
            st.write("")  # layout cushion
            st.write("")
            st.link_button(t["stripe_button_text"], STRIPE_SUBSCRIPTION_URL, use_container_width=True)
            
        st.divider()
        
        # OWNER / BUYER UNLOCK BOX
        code = st.text_input(t["activation_label"], placeholder="Type 'test' to unlock immediately as owner")
        if st.button(t["btn_activate"], type="primary"):
            if code.strip() != "":
                st.session_state.is_subscribed = True
                st.rerun()
            else:
                st.error("Please enter a valid passcode to unlock.")
                
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
