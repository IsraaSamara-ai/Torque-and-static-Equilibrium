# -*- coding: utf-8 -*-
"""
تطبيق فيزياء تفاعلي — العزم والاتزان السكوني
نسخة Streamlit للنشر على Streamlit Cloud أو تشغيلها محليًا

التشغيل المحلي:
    pip install -r requirements.txt
    streamlit run app.py

النشر على Streamlit Cloud:
    1) أنشئي مستودعًا على GitHub وضعي فيه: app.py + requirements.txt + index.html
    2) ادخلي إلى share.streamlit.io واربطي المستودع
    3) الملف الرئيسي: app.py
"""

from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="العزم والاتّزان السكونيّ | فيزياء تفاعلية",
    page_icon="⚛",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# إخفاء عناصر Streamlit الافتراضية للحصول على تجربة تطبيق كاملة
st.markdown(
    """
    <style>
      #MainMenu {visibility: hidden;}
      header {visibility: hidden;}
      footer {visibility: hidden;}
      .block-container {padding: 0 !important; max-width: 100% !important;}
      .stApp {background: #faf9fc;}
    </style>
    """,
    unsafe_allow_html=True,
)

HTML_PATH = Path(__file__).parent / "index.html"

if not HTML_PATH.exists():
    st.error("⚠️ الملف index.html غير موجود بجانب app.py — ضعيه في المجلد نفسه.")
    st.stop()

html = HTML_PATH.read_text(encoding="utf-8")

# حقن التطبيق بإطار كامل الطول والعرض
components.html(
    html,
    height=1050,
    scrolling=True,
)
