import streamlit as st

# --- 1. INITIALIZE GLOBAL APPS SESSION STATE ---
if "estimated_savings" not in st.session_state:
    st.session_state.estimated_savings = 0.0

if "is_subscribed" not in st.session_state:
    st.session_state.is_subscribed = False

# --- 2. CONFIGURABLE ECOSYSTEM GATEWAY URLS ---
# Replace these with your live recurring $12.99 monthly subscription platform links:
PAYPAL_SUBSCRIPTION_URL = "https://paypal.com"  
STRIPE_SUBSCRIPTION_URL = "https://stripe.com"  

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
        
        "paywall_title": "🔒 KeepRest Dashboard Locked",
        "paywall_text": "Get complete interactive access to your personal Income Calculator, secure Receipt Vault, and live State Tax Saver Engines.",
        "price_tag": "💳 Subscription: $12.99 / month",
        "paypal_button_text": "🟡 Subscribe via PayPal",
        "stripe_button_text": "💳 Subscribe via Stripe",
        "mock_verify_label": "Already subscribed? Paste your Activation Code or Subscription ID to unlock:",
        "verify_button": "Unlock Dashboard",
        "invalid_code": "❌ Please enter a valid activation code to access the app.",
        "preview_banner": "👀 PREVIEW MODE: Below is a read-only preview of what you get when you subscribe.",
        
        "feature_title": "🚀 What is included with your subscription:",
        "feat_1": "✅ **Real-Time Income Tax Estimator** - See your progress instantly.",
        "feat_2": "✅ **Secure Receipt Vault Engine** - Store and snap invoices seamlessly.",
        "feat_3": "✅ **State-Specific Deductions** - Customized rules for US territories."
    },
    "Spanish": {
        "app_title": "Panel de Control KeepRest",
        "tax_reminder": "📢 RECORDATORIO AFABLE DE TEMPORADA DE IMPUESTOS: La temporada de impuestos está a la vuelta de la esquina. Organice sus recibos para estar 100% preparado.",
        "settings_header": "⚙️ Configuración",
        "state_label": "Seleccione su Estado de EE. UU.",
        "calculator_header": "💰 Calculadora de Ingresos",
        "income_input_label": "Ingrese su Nuevo Monto de Ingresos ($)",
        "savings_label": "Progreso Estimado de Ahorro de Impuestos",
        "peace_of_mind": "✨ Sus datos financieros se rastrean de forma segura para su absoluta tranquilidad.",
        "receipt_header": "📂 Bóveda de Recibos y Motor de Ahorro Fiscal",
        "receipt_subtext": "¿Pierde sus recibos fácilmente? Escriba el monto o tome una foto a continuación.",
        "upload_label": "Tomar / Subir Foto de Recibo",
        
        "paywall_title": "🔒 Panel de KeepRest Bloqueado",
        "paywall_text": "Obtenga acceso interactivo completo a su calculadora de ingresos personal, bóveda de recibos segura y motores de ahorro de impuestos estatales en vivo.",
        "price_tag": "💳 Suscripción: $12.99 / mes",
        "paypal_button_text": "🟡 Suscribirse con PayPal",
        "stripe_button_text": "💳 Suscribirse con Stripe",
        "mock_verify_label": "¿Ya está suscrito? Pegue su ID de suscripción o código de activación para desbloquear:",
        "verify_button": "Desbloquear Panel",
        "invalid_code": "❌ Ingrese un código de activación válido para acceder a la aplicación.",
        "preview_banner": "👀 MODO DE VISTA PREVIA: A continuación se muestra una vista previa de solo lectura de lo que obtiene al suscribirse.",
        
        "feature_title": "🚀 Qué incluye tu suscripción:",
        "feat_1": "✅ **Estimador de impuestos en tiempo real** - Vea su progreso al instante.",
        "feat_2": "✅ **Motor de bóveda de recibos seguro** - Guarde facturas sin problemas.",
        "feat_3": "✅ **Deducciones específicas del estado** - Reglas personalizadas para EE. UU."
    }
}

# --- 4. LANGUAGE SELECTOR & LANGUAGE STATE ---
if "language" not in st.session_state:
    st.session_state.language = "English"

st.sidebar.markdown("### 🌐 Language / Idioma")
selected_lang = st.sidebar.selectbox(
    "Choose Language / Seleccione el idioma", 
    options=["English", "Spanish"],
    index=0 if st.session_state.language == "English" else 1
)
st.session_state.language = selected_lang
t = translations[st.session_state.language]


# --- 5. THE CONTENT RENDERING ENGINE ---
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


# --- 6. CONDITIONAL GATEWAY ROUTING ---
if not st.session_state.is_subscribed:
    # --- SCREEN A: PAYWALL CONTENT PAGE ---
    st.title(t["app_title"])
    
    with st.container(border=True):
        st.subheader(t["paywall_title"])
        st.write(t["paywall_text"])
        st.warning(t["price_tag"])
        
        # Payment Gateway Columns (Side-by-Side checkout buttons)
        col1, col2 = st.columns(2)
        with col1:
            st.link_button(t["paypal_button_text"], PAYPAL_SUBSCRIPTION_URL, use_container_width=True)
        with col2:
            st.link_button(t["stripe_button_text"], STRIPE_SUBSCRIPTION_URL, use_container_width=True)
            
        st.divider()
        
        # Clean alternative to the video block: Bulleted visual showcase
        st.markdown(f"### {t['feature_title']}")
        st.markdown(t["feat_1"])
        st.markdown(t["feat_2"])
        st.markdown(t["feat_3"])
        
        st.divider()
        
        # Unlock Panel Box
        activation_code = st.text_input(t["mock_verify_label"], placeholder="e.g., Sub-12345")
        if st.button(t["verify_button"], type="primary"):
            if activation_code.strip() != "":
                st.session_state.is_subscribed = True
                st.rerun()
            else:
                st.error(t["invalid_code"])
                
    st.divider()
    st.info(t["preview_banner"])
    render_dashboard(disabled_mode=True)

else:
    # --- SCREEN B: UNLOCKED INTERACTIVE DASHBOARD ---
    st.title(t["app_title"])
    st.info(t["tax_reminder"])
    
    if st.sidebar.button("Log Out / Lock App"):
        st.session_state.is_subscribed = False
        st.rerun()
        
    render_dashboard(disabled_mode=False)
