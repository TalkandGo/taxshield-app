import streamlit as st

# --- 1. INITIALIZE GLOBAL APPS SESSION STATE ---
if "estimated_savings" not in st.session_state:
    st.session_state.estimated_savings = 0.0

if "is_subscribed" not in st.session_state:
    st.session_state.is_subscribed = False

# --- 2. CONFIGURABLE ECOSYSTEM GATEWAY URLS ---
# Replace this with your recurring $12.99 PayPal subscription billing link:
PAYPAL_SUBSCRIPTION_URL = "https://paypal.com"  

# 🎥 STABLE PREVIEW VIDEO LINK
PREVIEW_VIDEO_URL = "https://w3schools.com"  

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
        "paywall_text": "Subscribe monthly to unlock complete interactive access to the Income Calculator, Receipt Vault, and State Tax Saver Engine.",
        "video_caption": "🎥 Take a look at the interactive engine features below:",
        "price_tag": "💳 Subscription: $12.99 / month",
        "paypal_button_text": "🟡 Subscribe Now via PayPal",
        "mock_verify_label": "Already subscribed? Paste your PayPal Subscription ID to unlock:",
        "verify_button": "Unlock Dashboard",
        "invalid_code": "❌ Please enter a valid activation code to access the app.",
        "preview_banner": "👀 PREVIEW MODE: Below is a read-only preview of what you get when you subscribe."
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
        "paywall_text": "Suscríbase mensualmente para desbloquear el acceso interactivo completo a la calculadora de ingresos, la bóveda de recibos y el motor de ahorro de impuestos estatales.",
        "video_caption": "🎥 Eche un vistazo a las características del motor interactivo a continuación:",
        "price_tag": "💳 Suscripción: $12.99 / mes",
        "paypal_button_text": "🟡 Suscríbase ahora a través de PayPal",
        "mock_verify_label": "¿Ya está suscrito? Pegue su ID de suscripción de PayPal o código de activación para desbloquear:",
        "verify_button": "Desbloquear Panel",
        "invalid_code": "❌ Ingrese un código de activación válido para acceder a la aplicación.",
        "preview_banner": "👀 MODO DE VISTA PREVIA: A continuación se muestra una vista previa de solo lectura de lo que obtiene al suscribirse."
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
    # --- SCREEN A: PAYWALL + VIDEO + APP PREVIEW ---
    st.title(t["app_title"])
    
    with st.container(border=True):
        st.subheader(t["paywall_title"])
        st.write(t["paywall_text"])
        st.warning(t["price_tag"])
        
        # PayPal Link
        st.link_button(t["paypal_button_text"], PAYPAL_SUBSCRIPTION_URL, use_container_width=True)
        
        st.divider()
        
        # Video Walkthrough Embed
        st.write(t["video_caption"])
        st.video(PREVIEW_VIDEO_URL)  
        
        st.divider()
        
        # Unlock Mechanism
        activation_code = st.text_input(t["mock_verify_label"], placeholder="e.g., I-XXXXXX")
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
    # --- SCREEN B: FULLY UNLOCKED INTERACTIVE APPLICATION ---
    st.title(t["app_title"])
    st.info(t["tax_reminder"])
    
    if st.sidebar.button("Log Out / Lock App"):
        st.session_state.is_subscribed = False
        st.rerun()
        
    render_dashboard(disabled_mode=False)
