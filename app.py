import csv
import hmac
import io
import zipfile
from datetime import date

import streamlit as st

# ------------------------------------------------------------------
# KeepRest dashboard
# Secrets (set these in Streamlit > Manage app > Settings > Secrets,
# NOT in this file):
#   ACCESS_CODE   = "your-new-passcode"
#   STRIPE_LINK   = "https://buy.stripe.com/xxxx"      (optional)
#   PAYPAL_LINK   = "https://www.paypal.com/xxxx"      (optional)
# ------------------------------------------------------------------


def get_secret(name, default=""):
    """Read a Streamlit secret without crashing if none are set."""
    try:
        return str(st.secrets.get(name, default))
    except Exception:
        return default


ACCESS_CODE = get_secret("ACCESS_CODE")
STRIPE_SUBSCRIPTION_URL = get_secret("STRIPE_LINK")
PAYPAL_SUBSCRIPTION_URL = get_secret("PAYPAL_LINK")

# --- 1. SESSION STATE ---
if "is_subscribed" not in st.session_state:
    st.session_state.is_subscribed = False
if "receipts" not in st.session_state:
    st.session_state.receipts = []
if "widget_round" not in st.session_state:
    st.session_state.widget_round = 0

# --- 2. TEXT ---
t = {
    "app_title": "KeepRest App Dashboard",
    "tax_reminder": "📢 FRIENDLY TAX SEASON REMINDER: Tax time is around the corner. Organize your receipts so you are prepared.",
    "settings_header": "⚙️ Settings",
    "state_label": "Select Your US State",
    "calculator_header": "💰 1099 Income Tax Estimator",
    "income_input_label": "Enter Your 1099 Income Amount ($)",
    "savings_label": "Rough Amount To Set Aside For Taxes",
    "estimate_note": "This is a rough estimate using a flat rate. It is not tax advice. Your actual taxes depend on your expenses, filing status and state. Please check with a tax professional.",
    "receipt_header": "📂 Receipt Log",
    "receipt_subtext": "Add each receipt with its amount, date and category, plus a photo if you have one. Download your list when you are done.",
    "privacy_note": "Your receipts are kept only while this page is open. They are not saved permanently, so download your list before you close the page.",
    "paywall_title": "💳 Subscription Required ($12.99/mo)",
    "paywall_text": "Unlock your personal KeepRest tax workspace.",
    "activation_label": "Have an access code? Enter it to unlock:",
    "btn_activate": "Unlock App Dashboard",
    "preview_banner": "👀 PREVIEW MODE: Below is a read-only preview of what you get when you subscribe.",
    "demo_title": "📱 How KeepRest Works (Quick Tour):",
    "step_1": "1️⃣ **Choose your State** - Get a rough set-aside estimate for your area.",
    "step_2": "2️⃣ **Enter 1099 Income** - See about how much to put aside for taxes.",
    "step_3": "3️⃣ **Log Receipts** - Record expenses with photos, then download the list for your accountant.",
}

CATEGORIES = [
    "Supplies",
    "Mileage / Gas",
    "Meals",
    "Software / Subscriptions",
    "Phone / Internet",
    "Home office",
    "Other",
]

US_STATES = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado",
    "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho",
    "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana",
    "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota",
    "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada",
    "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina",
    "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania",
    "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas",
    "Utah", "Vermont", "Virginia", "Washington", "West Virginia",
    "Wisconsin", "Wyoming", "Other",
]

NO_STATE_TAX = [
    "Alaska", "Florida", "Nevada", "New Hampshire", "South Dakota",
    "Tennessee", "Texas", "Washington", "Wyoming",
]


# --- 3. HELPERS ---
def receipts_csv(receipts):
    buf = io.StringIO()
    writer = csv.writer(buf)
    writer.writerow(["Date", "Category", "Amount", "Note", "Photo file"])
    for r in receipts:
        writer.writerow([r["date"], r["category"], f"{r['amount']:.2f}", r["note"], r["photo_name"]])
    return buf.getvalue().encode("utf-8")


def receipts_zip(receipts):
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
        for i, r in enumerate(receipts, start=1):
            if r["photo_bytes"]:
                zf.writestr(f"{i:03d}_{r['photo_name']}", r["photo_bytes"])
    return buf.getvalue()


def add_receipt(receipt_date, amount, category, note, photo):
    photo_bytes = photo.getvalue() if photo is not None else b""
    photo_name = getattr(photo, "name", "") if photo is not None else ""
    if photo is not None and not photo_name:
        photo_name = "camera_photo.jpg"
    st.session_state.receipts.append(
        {
            "date": receipt_date.isoformat(),
            "amount": float(amount),
            "category":
