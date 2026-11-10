import streamlit as st
import streamlit.components.v1 as components

# --- 1. INITIALIZE GLOBAL SECURITY STATE ---
if "user_account" not in st.session_state:
    st.session_state.user_account = None  

if "is_subscribed" not in st.session_state:
    st.session_state.is_subscribed = False

if "estimated_savings" not in st.session_state:
    st.session_state.estimated_savings = 0.0

if "mock_db" not in st.session_state:
    st.session_state.mock_db = {
        "admin": {"password": "test", "subscribed": True}  
    }

# --- 2. CONFIGURABLE CHECKOUT PORTAL URLS ---
# Keep your Stripe link ready here:
STRIPE_SUBSCRIPTION_URL = "https://stripe.com"  

# Raw embedded HTML/JS script block directly from your PayPal account setup
PAYPAL_BUTTON_HTML = """
<div style="text-align: center;">
    <div id="paypal-button-container-P-0CH31499JV265374YNLZJYJI"></div>
</div>
<script src="https://www.paypal.com/sdk/js?client-id=BAAml6BpucJg0E0-58er11J8OgtxjV6rsvnvNF9931T_kJB58I72D3-mLzUiiTeBlaaI0bxbMndV832MQc&vault=true&intent=subscription" data-sdk-integration-source="button-factory"></script>
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
        
        "auth_header": "🔐 KeepRest Secure Portal",
        "login_tab": "Sign In",
        "signup_tab": "Create Account",
        "username_label": "Email or Username",
        "password_label": "Password",
        "btn_login": "Log In",
        "btn_signup": "Register & Setup Billing",
        
        "paywall_title": "💳 Subscription Required ($12.99/mo)",
        "paywall_text": "Account created! To activate your interactive Income Calculator & Receipt Vault, complete payment below:",
        "stripe_button_text": "💳 Subscribe via Stripe",
        "activation_label": "Once paid, enter your Subscription ID or Receipt Code to activate:",
        "btn_activate": "Activate Account & Unlock App",
        "welcome_user": "Welcome back",
        "logout_label": "Secure Log Out"
    },
    "Spanish": {
        "app_title": "Panel de Control KeepRest",
        "tax_reminder": "📢 RECORDATORIO DE TEMPORADA DE IMPUESTOS...",
        "settings_header": "⚙️ Configuración",
        "state_label": "Seleccione su Estado de EE. UU.",
        "calculator_header": "💰 Calculadora de Ingresos",
        "income_input_label": "Ingrese su Nuevo Monto de Ingresos ($)",
        "savings_label": "Progreso Estimado de Ahorro de Impuestos",
        "peace_of_mind": "✨ Sus datos financieros se rastrean de forma segura para su absoluta tranquilidad.",
        "receipt_header": "📂 Bóveda de Recibos y Motor de Ahorro Fiscal",
        "receipt_subtext": "¿Pierde sus recibos fácilmente?...",
        "upload_label": "Tomar / Subir Foto de Recibo",
        
        "auth_header": "🔐 Portal Seguro KeepRest",
        "login_tab": "Iniciar Sesión",
        "signup_tab": "Crear Cuenta",
        "username_label": "Correo o Usuario",
        "password_label": "Contraseña",
        "btn_login": "Iniciar Sesión",
        "btn_signup": "Registrarse y Configurar Facturación",
        
        "paywall_title": "💳 Suscripción Requerida ($12.99/mes)",
        "paywall_text": "¡Cuenta creada! Para activar su panel interactivo, complete su pago a continuación:",
        "stripe_button_text": "💳 Suscribirse con Stripe",
        "activation_label": "Una vez pagado, ingrese su ID de suscripción para activar:",
        "btn_activate": "Activar Cuenta y Desbloquear",
        "welcome_user": "Bienvenido",
        "logout_label": "Cerrar Sesión Seguro"
    }
}

# --- 4. LANGUAGE SELECTOR ---
if "language" not in st.session_state:
    st.session_state.language = "English"

st.sidebar.markdown("### 🌐 Language / Idioma")
selected_lang = st.sidebar.selectbox(
    "Choose Language", options=["English", "Spanish"],
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


# --- 6. USER INTERFACE USER ROUTING ---
st.title(t["app_title"])

if st.session_state.user_account is None:
    # --- FLOW A: NOT SIGNED IN ---
    with st.container(border=True):
        st.subheader(t["auth_header"])
        tab1, tab2 = st.tabs([t["login_tab"], t["signup_tab"]])
        
        with tab1:
            username = st.text_input(t["username_label"], key="login_user")
            password = st.text_input(t["password_label"], type="password", key="login_pass")
            if st.button(t["btn_login"], type="primary"):
                if username in st.session_state.mock_db and st.session_state.mock_db[username]["password"] == password:
                    st.session_state.user_account = username
                    st.session_state.is_subscribed = st.session_state.mock_db[username]["subscribed"]
                    st.success(f"Logged in as {username}!")
                    st.rerun()
                else:
                    st.error("Invalid username or password.")
        
        with tab2:
            new_user = st.text_input(t["username_label"], key="reg_user")
            new_pass = st.text_input(t["password_label"], type="password", key="reg_pass")
            if st.button(t["btn_signup"]):
                if new_user.strip() == "" or new_pass.strip() == "":
                    st.error("Fields cannot be empty.")
                elif new_user in st.session_state.mock_db:
                    st.error("Account already exists.")
                else:
                    st.session_state.mock_db[new_user] = {"password": new_pass, "subscribed": False}
                    st.session_state.user_account = new_user
                    st.session_state.is_subscribed = False
                    st.success("Account registered! Please complete payment status below.")
                    st.rerun()
                    
    st.divider()
    render_dashboard(disabled_mode=True)

elif st.session_state.user_account and not st.session_state.is_subscribed:
    # --- FLOW B: SIGNED IN BUT UNPAID ---
    with st.container(border=True):
        st.subheader(t["paywall_title"])
        st.write(t["paywall_text"])
        
        # Payment Gateway Columns
        c1, c2 = st.columns(2)
        with c1:
            # Renders your live PayPal Smart button script directly into the layout column
            components.html(PAYPAL_BUTTON_HTML, height=200, scrolling=False)
        with c2:
            # Direct Stripe Link Button
            st.write("")  # Alignment spacing cushion
            st.write("")
            st.link_button(t["stripe_button_text"], STRIPE_SUBSCRIPTION_URL, use_container_width=True)
            
        st.divider()
        
        code = st.text_input(t["activation_label"], placeholder="e.g., P-0CH31499...")
        if st.button(t["btn_activate"], type="primary"):
            if code.strip() != "":
                st.session_state.is_subscribed = True
                st.session_state.mock_db[st.session_state.user_account]["subscribed"] = True
                st.success("Subscription verified successfully!")
                st.rerun()
            else:
                st.error("Please provide your confirmation code.")
                
    if st.sidebar.button(t["logout_label"]):
        st.session_state.user_account = None
        st.session_state.is_subscribed = False
        st.rerun()
        
    st.divider()
    render_dashboard(disabled_mode=True)

else:
    # --- FLOW C: SIGNED IN & FULLY SUBSCRIBED ---
    st.sidebar.markdown(f"👤 **{t['welcome_user']}, {st.session_state.user_account}!**")
    st.info(t["tax_reminder"])
    
    if st.sidebar.button(t["logout_label"]):
        st.session_state.user_account = None
        st.session_state.is_subscribed = False
        st.rerun()
        
    render_dashboard(disabled_mode=False)
