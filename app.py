import streamlit as st

# --- 1. INITIALIZE GLOBAL APPS SESSION STATE ---
if "estimated_savings" not in st.session_state:
    st.session_state.estimated_savings = 0.0

# --- 2. CONFIGURABLE ECOSYSTEM GATEWAY URLS ---
# Replace this with your direct PayPal payment link or your paypal.me address:
PAYPAL_PAYMENT_URL = "https://paypal.com"  

# Leave this as None for now. Once you want to add Stripe later, just paste your ://stripe.com link here:
STRIPE_PAYMENT_URL = None  

# --- 3. MULTILINGUAL TRANSLATION DICTIONARY MAP ---
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
        "premium_sidebar_title": "💳 KeepRest Premium Account Portal",
        "premium_sidebar_text": "Unlock automated matching receipt algorithms and live regional tax advisor tracking panels.",
        "upgrade_button_label": "Upgrade to Premium Plans",
        "premium_features_promo": "Get full corporate-grade automated tax deduction tracking for less than $10 a month.",
        "paypal_button_text": "🟡 Complete Upgrade via PayPal",
        "stripe_button_text": "💳 Complete Upgrade via Stripe"
    },
    "Spanish": {
        "app_title": "Panel de Control KeepRest",
        "tax_reminder": "📢 RECORDATORIO AFABLE DE LA TEMPORADA DE IMPUESTOS: La época de impuestos está a la vuelta de la esquina. Organiza tus recibos.",
        "settings_header": "⚙️ Configuración",
        "state_label": "Seleccione su Estado de EE.UU.",
        "calculator_header": "💰 Calculadora de Ingresos",
        "income_input_label": "Ingrese su Nuevo Monto de Ingresos ($)",
        "savings_label": "Progreso de Ahorros Fiscales Estimados",
        "peace_of_mind": "✨ Tus datos financieros están rastreados de forma segura para tu tranquilidad.",
        "receipt_header": "📂 Bóveda de Recibos y Motor de Ahorro",
        "receipt_subtext": "¿Pierdes tus recibos fácilmente? Escribe el monto O toma una foto abajo.",
        "upload_label": "Tomar / Subir Foto de Recibo",
        "premium_sidebar_title": "💳 Portal de Cuenta Premium KeepRest",
        "premium_sidebar_text": "Desbloquea algoritmos automáticos de emparejamiento de recibos y paneles de asesores fiscales.",
        "upgrade_button_label": "Actualizar a Planes Premium",
        "premium_features_promo": "Obtén seguimiento fiscal corporativo automatizado por menos de $10 al mes.",
        "paypal_button_text": "🟡 Completar Pago con PayPal",
        "stripe_button_text": "💳 Completar Pago con Stripe"
    }
}

# --- 4. LANGUAGE PICKER DROPDOWN CONFIGURATION ---
selected_language = st.selectbox("Choose Language / Idioma / 语言 /  भाषा", list(translations.keys()))
lang = translations[selected_language]

st.title(lang["app_title"])

# --- 5. APP REMINDER BANNER ---
st.info(lang["tax_reminder"])

# --- 6. MAIN MAIN INTERFACE SETTINGS SECTION ---
st.subheader(lang["settings_header"])
selected_state = st.selectbox(lang["state_label"], ["California", "New York", "Texas", "Florida", "North Carolina"])

# --- 7. TAX ENGINE INCOME CALCULATOR SECTION ---
st.subheader(lang["calculator_header"])
income_amount = st.number_input(lang["income_input_label"], min_value=0.0, step=100.0, value=0.0)

if income_amount > 0:
    st.session_state.estimated_savings = income_amount * 0.15
else:
    st.session_state.estimated_savings = 0.0

st.metric(label=lang["savings_label"], value=f"${st.session_state.estimated_savings:,.2f}")
st.markdown(lang["peace_of_mind"])

# --- 8. FILE MANAGEMENT RECEIPT VAULT LOADING BLOCKS ---
st.subheader(lang["receipt_header"])
st.write(lang["receipt_subtext"])
uploaded_pic = st.file_uploader(lang["upload_label"], type=["jpg", "jpeg", "png"])

if uploaded_pic is not None:
    st.success("File uploaded successfully!")

# --- 9. GLOBAL CONVERSION PREMIUM SIDEBAR SUBSCRIPTION DRAWER ---
with st.sidebar:
    st.header(lang["premium_sidebar_title"])
    st.write(lang["premium_sidebar_text"])
    st.divider()
    
    with st.expander(f"⚙️ {lang['upgrade_button_label']}", expanded=True):
        st.warning(lang["premium_features_promo"])
        
        # Primary Action Option 1: Live PayPal Checkout Gateway
        st.link_button(
            label=lang["paypal_button_text"],
            url=PAYPAL_PAYMENT_URL,
            type="primary",
            use_container_width=True
        )
        
        # Primary Action Option 2: Stripe Checkout Gateway (Loads only when link is provided above)
        if STRIPE_PAYMENT_URL:
            st.divider()
            st.link_button(
                label=lang["stripe_button_text"],
                url=STRIPE_PAYMENT_URL,
                type="secondary",
                use_container_width=True
            )
