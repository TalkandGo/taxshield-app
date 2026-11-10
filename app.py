import streamlit as st

st.set_page_config(page_title="KeepRest", page_icon="🛡️", layout="centered")

# --- 5 COMPACT LANGUAGES DICTIONARY (CLEAN TRACKER ONLY) ---
translations = {
    "English": {
        "title": "KeepRest", 
        "caption": "Relax. Your tax is handled. Focus on growing your business.", 
        "settings_hdr": "⚙️ Settings", 
        "state_lbl": "Select Your US State", 
        "income_hdr": "💰 Income Calculator", 
        "income_lbl": "Enter Your New Income Amount ($)", 
        "tax_aside": "Tax to set aside in your private bank account", 
        "safe_spend": "Guilt-free money left over to spend:", 
        "expense_hdr": "📁 Receipt Vault & Tax Saver Estimator", 
        "expense_lbl": "💡 Lose your receipts easily? Type the amount OR snap a picture below to securely store it for tax time!", 
        "expense_logged": "Enter Receipt Total ($) - Optional if uploading image", 
        "btn_log": "📁 Save to Receipt Vault & Estimate Savings",
        "expense_success": "Receipt safely saved in your vault! Keeping records lowers your final tax bill.", 
        "reminder_banner": "⏰ **FRIENDLY TAX SEASON REMINDER:** Tax time is getting close! Keep saving and logging your write-offs so you are 100% prepared.",
        "vault_hdr": "🔒 Your Tax & Savings Ledger Balance", 
        "vault_metric": "Estimated Total Tax to Set Aside", 
        "total_writeoffs": "Estimated Tax Savings From Receipts", 
        "peace_of_mind": "🟢 Keep your tax money safe inside your main bank or PayPal account. What remains is **100% yours to spend without guilt.**"
    },
    "Español": {
        "title": "KeepRest", 
        "caption": "Relájate. Tus impuestos están bajo control. Enfócate en tu negocio.", 
        "settings_hdr": "⚙️ Configuración", 
        "state_lbl": "Selecciona tu Estado de EE. UU.", 
        "income_hdr": "💰 Calculadora de Ingresos", 
        "income_lbl": "Ingresa el Monto de tu Nuevo Ingreso ($)", 
        "tax_aside": "Impuesto a guardar en tu cuenta bancaria privada", 
        "safe_spend": "Dinero libre de culpa que te queda para gastar:", 
        "expense_hdr": "📁 Bóveda de Recibos y Estimador de Ahorros", 
        "expense_lbl": "💡 ¿Pierdes tus recibos fácilmente? ¡Ingresa el monto O toma una foto abajo para guardarlo de forma segura!", 
        "expense_logged": "Ingresa el Total del Recibo ($) - Opcional si subes imagen", 
        "btn_log": "📁 Guardar en la Bóveda de Recibos",
        "expense_success": "¡Recibo guardado con éxito! Conservar tus registros reduce tu factura fiscal final.", 
        "reminder_banner": "⏰ **RECORDATORIO AMISTOSO:** ¡La temporada de impuestos se acerca! Sigue guardando y registrando tus deducciones para estar 100% preparado.",
        "vault_hdr": "🔒 Balance de tu Libro de Impuestos y Ahorros", 
        "vault_metric": "Impuesto Total Estimado a Guardar", 
        "total_writeoffs": "Ahorro de Impuestos Estimado por Recibos", 
        "peace_of_mind": "🟢 Mantén tu dinero de impuestos seguro en tu banco o cuenta de PayPal. El resto es **100% tuyo para gastar sin culpa.**"
    },
    "简体中文": {
        "title": "KeepRest", 
        "caption": "放轻松。税款已为您留存。专心发展您的业务即可。", 
        "settings_hdr": "⚙️ 设置", 
        "state_lbl": "选择您所在的美国联邦州", 
        "income_hdr": "💰 收入计算器", 
        "income_lbl": "输入您的新收入金额 ($)", 
        "tax_aside": "需存入您个人银行账户的税款", 
        "safe_spend": "您可以放心消费的剩余金额：", 
        "expense_hdr": "📁 收据保险库与预计省税估算", 
        "expense_lbl": "💡 经常弄丢收据？在下方输入金额“或”拍照，即可安全储存以备税期使用！", 
        "expense_logged": "输入收据总额 ($) - 若上传图片则可选填", 
        "btn_log": "📁 保存至收据保险库并估算节省金额",
        "expense_success": "收据已安全保存！保留凭证可降低您最终的税单金额。", 
        "reminder_banner": "⏰ **温馨税务提示：** 纳税期快到了！请继续保存并记录您的抵税项目，做到100%从容应对。",
        "vault_hdr": "🔒 您的税务与储蓄账本余额", 
        "vault_metric": "预估需留存的税款总额", 
        "total_writeoffs": "收据带来的预估省税总额", 
        "peace_of_mind": "🟢 请将税款安全存放在您的主银行账户或 PayPal 中。其余资金 **100% 属于您。**"
    },
    "Français": {
        "title": "KeepRest", 
        "caption": "Détendez-vous. Vos impôts sont gérés. Concentrez-vous sur votre entreprise.", 
        "settings_hdr": "⚙️ Paramètres", 
        "state_lbl": "Sélectionnez votre État américain", 
        "income_hdr": "💰 Calculateur de Revenus", 
        "income_lbl": "Entrez le montant de votre nouveau revenu ($)", 
        "tax_aside": "Impôt à mettre de côté sur votre compte bancaire privé", 
        "safe_spend": "Argent que vous pouvez dépenser l'esprit tranquille :", 
        "expense_hdr": "📁 Coffre de Reçus & Dépenses (Déductions)", 
        "expense_lbl": "💡 Vous perdez souvent vos reçus ? Saisissez le montant OU prenez une photo ci-dessous pour les sécuriser !", 
        "expense_logged": "Entrez le total du reçu ($) - Optionnel si image fournie", 
        "btn_log": "📁 Enregistrer dans le coffre professionnel",
        "expense_success": "Reçu sauvegardé ! Conserver vos reçus réduit votre facture fiscale finale.", 
        "reminder_banner": "⏰ **RAPPEL FISCAL AMICAL :** La période des impôts approche ! Continuez à enregistrer vos déductions pour être prêt à 100%.",
        "vault_hdr": "🔒 Solde de votre Grand Livre Fiscal et d'Épargne", 
        "vault_metric": "Impôt total estimé à mettre de côté", 
        "total_writeoffs": "Économies d'impôt estimées grâce aux reçus", 
        "peace_of_mind": "🟢 Gardez votre argent pour les impôts en sécurité sur votre compte bancaire principal ou PayPal. Le reste est **100% à vous.**"
    },
    "Tiếng Việt": {
        "title": "KeepRest", 
        "caption": "Thư giãn đi. Thuế của bạn đã được xử lý. Hãy tập trung phát triển kinh doanh.", 
        "settings_hdr": "⚙️ Cài đặt", 
        "state_lbl": "Chọn Bang tại Mỹ của Bạn", 
        "income_hdr": "💰 Máy tính Doanh thu", 
        "income_lbl": "Nhập Số tiền Doanh thu Mới của Bạn ($)", 
        "tax_aside": "Tiền thuế cần trích ra và gửi vào tài khoản ngân hàng của bạn", 
        "safe_spend": "Số tiền bạn có thể thoải mái chi tiêu:", 
        "expense_hdr": "📁 Két Lưu Trữ Hóa Đơn & Chi Phí (Khấu Trừ Thuế)", 
        "expense_lbl": "💡 Bạn hay làm mất hóa đơn? Nhập số tiền HOẶC chụp hình bên dưới để lưu trữ an toàn cho mùa thuế!", 
        "expense_logged": "Nhập Tổng tiền Hóa đơn ($) - Không bắt buộc nếu có ảnh", 
        "btn_log": "📁 Lưu vào Két Hóa Đơn & Ước Tính Tiền Tiết Kiệm",
        "expense_success": "Đã lưu hóa đơn an toàn! Giữ lại hóa đơn sẽ giúp hạ thấp hóa đơn thuế cuối cùng của bạn.", 
        "reminder_banner": "⏰ **NHẮC NHỞ MÙA THUẾ:** Mùa thuế đang đến rất gần! Hãy tiếp tục tích lũy và ghi nhận chi phí để chuẩn bị sẵn sàng 100%.",
        "vault_hdr": "🔒 Số dư Sổ cái Thuế & Tiền Tiết kiệm của Bạn", 
        "vault_metric": "Tổng Tiền Thuế Ước Tính Cần Trích Ra", 
        "total_writeoffs": "Tiền Tiết Kiệm Thuế Ước Tính Từ Hóa Đơn", 
        "peace_of_mind": "🟢 Hãy giữ tiền thuế an toàn trong tài khoản ngân hàng chính hoặc ví PayPal của bạn. Số tiền còn lại là **100% của bạn để chi tiêu thoải mái.**"
    }
}

state_rates = {"California": 0.33, "New York": 0.32, "Texas": 0.25, "Florida": 0.25, "North Carolina": 0.28, "Illinois": 0.29, "Ohio": 0.27, "Georgia": 0.28, "Pennsylvania": 0.28, "Washington": 0.25, "Virginia": 0.28, "Massachusetts": 0.30}

selected_lang = st.selectbox("🌐 Language / Idioma / 语言 / Ngôn ngữ", list(translations.keys()))
lang = translations[selected_lang]

st.title(f"🛡️ {lang['title']}")
st.caption(lang["caption"])

# Initialize ledger values
if 'tax_vault' not in st.session_state: st.session_state.tax_vault = 0.00
if 'estimated_savings' not in st.session_state: st.session_state.estimated_savings = 0.00

st.warning(lang["reminder_banner"])

st.markdown("---")
st.markdown(f"### {lang['settings_hdr']}")
chosen_state = st.selectbox(lang["state_lbl"], list(state_rates.keys()))
tax_rate = state_rates[chosen_state]

st.markdown("---")
st.markdown(f"### {lang['income_hdr']}")
income = st.number_input(lang["income_lbl"], min_value=0.0, value=0.0, step=100.0)

if income > 0:
    calculated_tax = income * tax_rate
    safe_spend = income - calculated_tax
    st.markdown(f"**{lang['tax_aside']} ({int(tax_rate * 100)}%):** `${calculated_tax:,.2f}`")
    st.markdown(f"**{lang['safe_spend']}** <span style='color:#1565c0; font-weight:bold; font-size:22px;'>${safe_spend:,.2f}</span>", unsafe_allow_html=True)
    st.session_state.tax_vault = calculated_tax

st.markdown("---")
st.markdown(f"### {lang['expense_hdr']}")
st.caption(lang["expense_lbl"])

col_exp_pic, col_exp_amt = st.columns(2)
with col_exp_pic: 
    receipt_file = st.file_uploader("📷 Snap / Upload Receipt Pic", type=["jpg", "jpeg", "png"])
with col_exp_amt: 
    expense_amt = st.number_input(lang["expense_logged"], min_value=0.0, value=0.0, step=10.0)

if (expense_amt > 0 or receipt_file) and st.button(lang["btn_log"]):
    base_value = expense_amt if expense_amt > 0 else 50.00
    st.session_state.estimated_savings += (base_value * 0.15)
    st.success(lang["expense_success"])

st.markdown("---")
st.markdown(f"### {lang['vault_hdr']}")
col1, col2 = st.columns(2)
with col1: st.metric(label=lang["vault_metric"], value=f"${st.session_state.tax_vault:,.2f}")
with col2: st.metric(label=lang["total_writeoffs"], value=f"${st.session_state.estimated_savings:,.2f}")
st.markdown(lang["peace_of_mind"])
