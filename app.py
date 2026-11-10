import streamlit as st

# Page Configuration & Clean Aesthetic Styling
st.set_page_config(page_title="TaxShield", page_icon="🛡️", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    div[data-testid="stMetricValue"] { font-size: 38px !important; font-weight: bold; }
    .stNumberInput div div input { font-size: 18px !important; }
    .safe-text { color: #1565c0; font-weight: bold; font-size: 20px; }
    .expense-text { color: #d32f2f; font-weight: bold; font-size: 18px; }
    </style>
""", unsafe_allow_html=True)

# --- 5 LANGUAGES DICTIONARY WITH EXPENSE VAULT ---
translations = {
    "English": {
        "title": "TaxShield",
        "caption": "Relax. Your tax is handled. Focus on growing your business.",
        "settings_hdr": "⚙️ Settings",
        "state_lbl": "Select Your US State",
        "mode_lbl": "Tax Pull Preference",
        "mode_ask": "Ask me first before moving money",
        "mode_auto": "Automatically move it",
        "income_hdr": "💰 New Income Arrived",
        "income_lbl": "Enter Income Amount ($) or Upload Paycheck Image",
        "tax_aside": "Tax to set aside",
        "safe_spend": "Guilt-free money to spend:",
        "btn_auto": "✅ Process & Log Income",
        "btn_ask": "🛡️ Move money to Tax Vault Now",
        "success_auto": "Transferred money directly to your Tax Vault!",
        "success_ask": "Successfully protected money for tax time!",
        "vault_hdr": "🔒 Protected Tax Vault",
        "vault_metric": "Total Saved for Tax Time",
        "peace_of_mind": "🟢 **Your tax bills are covered.** Whatever is left in your main account is **100% yours to spend or reinvest.**",
        "expense_hdr": "📁 Receipt & Expense Vault (Tax Write-Offs)",
        "expense_lbl": "Snap or Upload Receipt to Lower Your Taxes",
        "expense_logged": "Logged Expense Amount ($)",
        "expense_success": "Receipt saved! This lowering your upcoming tax liability.",
        "total_writeoffs": "Total Tax Write-Offs Tracked"
    },
    "Español": {
        "title": "TaxShield",
        "caption": "Relájate. Tus impuestos están bajo control. Enfócate en tu negocio.",
        "settings_hdr": "⚙️ Configuración",
        "state_lbl": "Selecciona tu Estado de EE. UU.",
        "mode_lbl": "Preferencia de Retiro",
        "mode_ask": "Preguntarme antes de mover el dinero",
        "mode_auto": "Mover automáticamente",
        "income_hdr": "💰 Nuevos Ingresos Recibidos",
        "income_label": "Ingresa el Monto ($) o sube foto del cheque",
        "tax_aside": "Impuesto a reservar",
        "safe_spend": "Dinero libre de culpa para gastar:",
        "btn_auto": "✅ Procesar y Registrar Ingreso",
        "btn_ask": "🛡️ Mover dinero a la Bóveda de Impuestos",
        "success_auto": "¡Dinero transferido directamente a tu Bóveda de Impuestos!",
        "success_ask": "¡Dinero protegido con éxito para la temporada de impuestos!",
        "vault_hdr": "🔒 Bóveda de Impuestos Protegida",
        "vault_metric": "Total Ahorrado para Impuestos",
        "peace_of_mind": "🟢 **Tus impuestos están cubiertos.** Lo que quede en tu cuenta principal es **100% tuyo para gastar o reinvertir.**",
        "expense_hdr": "📁 Bóveda de Recibos y Gastos (Deducciones)",
        "expense_lbl": "Toma foto o sube un Recibo para bajar tus Impuestos",
        "expense_logged": "Monto del Gasto Registrado ($)",
        "expense_success": "¡Recibo guardado! Esto reduce lo que debes pagar en impuestos.",
        "total_writeoffs": "Total de Deducciones Registradas"
    },
    "简体中文": {
        "title": "TaxShield",
        "caption": "放轻松。税款已为您留存。专心发展您的业务即可。",
        "settings_hdr": "⚙️ 设置",
        "state_lbl": "选择您所在的美国联邦州",
        "mode_lbl": "税款提取偏好",
        "mode_ask": "转账前先询问我",
        "mode_auto": "自动直接转账",
        "income_hdr": "💰 新收入入账",
        "income_lbl": "输入收入金额 ($) 或上传支票照片",
        "tax_aside": "需留存的税款",
        "safe_spend": "您可以放心消费的金额：",
        "btn_auto": "✅ 处理并记录收入",
        "btn_ask": "🛡️ 立即将税款移至税务保险库",
        "success_auto": "已将税款直接转入您的税务保险库！",
        "success_ask": "已成功为您留存税期所需的资金！",
        "vault_header": "🔒 受保护的税务保险库",
        "vault_metric": "税务准备金总额",
        "peace_of_mind": "🟢 **您的税款已妥善留存。** 留在您主账户中的资金 **100% 属于您，可自由消费或再投资。**",
        "expense_hdr": "📁 收据与报销保险库（抵税项目）",
        "expense_lbl": "拍摄或上传收据以减少您的应纳税额",
        "expense_logged": "已记录的费用金额 ($)",
        "expense_success": "收据已保存！这将降低您接下来的预估税款。",
        "total_writeoffs": "已记录的抵税总额"
    },
    "Français": {
        "title": "TaxShield",
        "caption": "Détendez-vous. Vos impôts sont gérés. Concentrez-vous sur votre entreprise.",
        "settings_hdr": "⚙️ Paramètres",
        "state_lbl": "Sélectionnez votre État américain",
        "mode_lbl": "Préférence de Prélèvement",
        "mode_ask": "Me demander avant de déplacer l'argent",
        "mode_auto": "Déplacer automatiquement",
        "income_hdr": "💰 Nouveau Revenu Reçu",
        "income_lbl": "Entrez le Montant ($) ou photographiez le chèque",
        "tax_aside": "Impôt à mettre de côté",
        "safe_spend": "Argent que vous pouvez dépenser l'esprit tranquille :",
        "btn_auto": "✅ Traiter et Enregistrer le Revenu",
        "btn_ask": "🛡️ Déplacer l'argent vers le Coffre Fiscal maintenant",
        "success_auto": "Argent transféré directement dans votre Coffre Fiscal !",
        "success_ask": "Argent sécurisé avec succès pour la période des impôts !",
        "vault_hdr": "🔒 Coffre Fiscal Sécurisé",
        "vault_metric": "Total Économisé pour les Impôts",
        "peace_of_mind": "🟢 **Vos impôts sont couverts.** Ce qui reste sur votre compte principal est **100% à vous pour dépenser ou réinvestir.**",
        "expense_hdr": "📁 Coffre de Reçus & Dépenses (Déductions)",
        "expense_lbl": "Prenez ou importez un reçu pour réduire vos impôts",
        "expense_logged": "Montant de la dépense enregistrée ($)",
        "expense_success": "Reçu sauvegardé ! Cela réduit votre future dette fiscale.",
        "total_writeoffs": "Total des Déductions Suivies"
    },
    "Tiếng Việt": {
        "title": "TaxShield",
        "caption": "Thư giãn đi. Thuế của bạn đã được xử lý. Hãy tập trung phát triển kinh doanh.",
        "settings_hdr": "⚙️ Cài đặt",
        "state_lbl": "Chọn Bang tại Mỹ của Bạn",
        "mode_lbl": "Tùy chọn Trích thuế",
        "mode_ask": "Hỏi tôi trước khi chuyển tiền",
        "mode_auto": "Tự động trích tiền",
        "income_hdr": "💰 Doanh thu Mới Nhận",
        "income_lbl": "Nhập Số tiền Doanh thu ($) hoặc Chụp ảnh Phiếu lương",
        "tax_aside": "Tiền thuế cần trích ra",
        "safe_spend": "Số tiền bạn có thể thoải mái chi tiêu:",
        "btn_auto": "✅ Xử lý & Ghi nhận Doanh thu",
        "btn_ask": "🛡️ Chuyển tiền vào Két thuế Ngay",
        "success_auto": "Đã chuyển tiền trực tiếp vào Két thuế của bạn!",
        "success_ask": "Đã bảo vệ thành công số tiền cho mùa thuế sắp tới!",
        "vault_hdr": "🔒 Két Thuế Được Bảo Vệ",
        "vault_metric": "Tổng Tiền Tiết kiệm Cho Mùa Thuế",
        "peace_of_mind": "🟢 **Các hóa đơn thuế đã được lo liệu.** Số tiền còn lại trong tài khoản chính là **100% của bạn để chi tiêu hoặc tái đầu tư.**",
        "expense_hdr": "📁 Két Lưu Trữ Hóa Đơn & Chi Phí (Khấu Trừ Thuế)",
        "expense_lbl": "Chụp hình hoặc Tải lên Hóa đơn để Giảm Thuế Phải Trả",
        "expense_logged": "Số tiền Chi phí Đã Ghi Nhận ($)",
        "expense_success": "Đã lưu hóa đơn! Chi phí này sẽ giúp hạ thấp nghĩa vụ thuế của bạn.",
        "total_writeoffs": "Tổng Chi Phí Khấu Trừ Đã Theo Dõi"
    }
}

state_rates = {
    "California": 0.33, "New York": 0.32, "Texas": 0.25, "Florida": 0.25, 
    "North Carolina": 0.28, "Illinois": 0.29, "Ohio": 0.27, "Georgia": 0.28, 
    "Pennsylvania": 0.28, "Washington": 0.25, "Virginia": 0.28, "Massachusetts": 0.30
}

# --- INTERFACE LANGUAGE PICKER ---
selected_lang = st.selectbox("🌐 Language / Idioma / 语言 / Ngôn ngữ", list(translations.keys()))
lang = translations[selected_lang]

st.title(f"🛡️ {lang['title']}")
st.caption(lang["caption"])

# Initialize background balances
if 'tax_vault' not in st.session_state:
    st.session_state.tax_vault = 1250.00
if 'expense_vault' not in st.session_state:
    st.session_state.expense_vault = 340.00

st.markdown("---")

# --- STEP 1: SETTINGS ---
st.markdown(f"### {lang['settings_hdr']}")
col_state, col_mode = st.columns(2)
with col_state:
    chosen_state = st.selectbox(lang["state_lbl"], list(state_rates.keys()))
    tax_rate = state_rates[chosen_state]
with col_mode:
    mode = st.radio(lang["mode_lbl"], [lang["mode_ask"], lang["mode_auto"]], index=0)

st.markdown("---")

# --- STEP 2: INCOME INPUT & PAYCHECK PIC ---
st.markdown(f"### {lang['income_hdr']}")
income = st.number_input(lang["income_lbl"], min_value=0.0, value=0.0, step=100.0)

paycheck_file = st.file_uploader("📷 Optional: Scan / Upload Paycheck Image", type=["jpg", "jpeg", "png"])
if paycheck_file:
    st.info("✨ Paycheck Image recognized! Enter the total amount in the field above to lock in calculation.")

if income > 0:
    calculated_tax = income * tax_rate
    safe_spend = income - calculated_tax
    rate_pct = int(tax_rate * 100)
    
    st.markdown(f"**{lang['tax_aside']} ({rate_pct}%):** `${calculated_tax:,.2f}`")
    st.markdown(f"**{lang['safe_spend']}** <span class='safe-text'>${safe_spend:,.2f}</span>", unsafe_allow_html=True)
    st.write("")
    
    if mode == lang["mode_auto"]:
        if st.button(lang["btn_auto"]):
            st.session_state.tax_vault += calculated_tax
            st.success(f"{lang['success_auto']} (+${calculated_tax:,.2f})")
    else:
        if st.button(f"{lang['btn_ask']} (${calculated_tax:,.2f})"):
            st.session_state.tax_vault += calculated_tax
            st.success(f"{lang['success_ask']} (+${calculated_tax:,.2f})")

st.markdown("---")

# --- STEP 3: EXCLUSIVE RECEIPT & EXPENSE VAULT ---
st.markdown(f"### {lang['expense_hdr']}")
st.caption(lang["expense_lbl"])
col_exp_pic, col_exp_amt = st.columns(2)
with col_exp_pic:
receipt_file = st.file_uploader("📷 Snap / Upload Receipt Pic", type=["jpg", "jpeg", "png"])
with col_exp_amt:
expense_amt = st.number_input(lang["expense_logged"], min_value=0.0, value=0.0, step=10.0)
if expense_amt > 0 and receipt_file:
if st.button("📁 Log Receipt to Deductions"):
st.session_state.expense_vault += expense_amt
st.success(lang["expense_success"])
st.markdown("---")

--- STEP 4: BALANCES OVERVIEW ---

st.markdown(f"### {lang['vault_hdr']}")
col1, col2 = st.columns(2)
with col1:
st.metric(label=lang["vault_metric"], value=f"${st.session_state.tax_vault:,.2f}")
with col2:
st.metric(label=lang["total_writeoffs"], value=f"${st.session_state.expense_vault:,.2f}")
st.markdown(lang["peace_of_mind"])
