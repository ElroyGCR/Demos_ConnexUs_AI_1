import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from PIL import Image
from io import BytesIO
import base64

# --- Page Setup ---
st.set_page_config(page_title="ConnexUS AI ROI Calculator", layout="wide")

# --- Favicon Injection (Base64 Embedded) ---
def load_favicon_base64(path="favicon-32x32.png"):
    try:
        img = Image.open(path)
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        return base64.b64encode(buffer.getvalue()).decode("utf-8")
    except Exception as e:
        return None

favicon_b64 = load_favicon_base64()
if favicon_b64:
    st.markdown(
        f"""
        <link rel="icon" type="image/png" sizes="32x32" href="data:image/png;base64,{favicon_b64}">
        """,
        unsafe_allow_html=True
    )

# --- Theme-safe Global Styling ---
st.markdown(
    """
    <style>
    .block-container {
        padding-top: 1rem !important;
    }
    @media (max-width: 768px) {
        .block-container {
            padding-left: 0.5rem !important;
            padding-right: 0.5rem !important;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Watermark Setup ---
def load_watermark_base64(path="connexus_logo_watermark.png"):
    try:
        with open(path, "rb") as f:
            img = Image.open(f)
            buffer = BytesIO()
            img.save(buffer, format="PNG")
            return base64.b64encode(buffer.getvalue()).decode("utf-8")
    except:
        return None

watermark_b64 = load_watermark_base64()
if watermark_b64:
    st.markdown(
        f"""
        <style>
        .watermark {{
            position: fixed;
            top: 80px;
            left: calc(540px + 30%);
            transform: translateX(-50%);
            height: 800px;
            width: 850px;
            z-index: 0;
            pointer-events: none;
            background-image: url("data:image/png;base64,{watermark_b64}");
            background-repeat: no-repeat;
            background-position: center center;
            background-size: contain;
            opacity: 0.15;
        }}
        </style>
        <div class="watermark"></div>
        """,
        unsafe_allow_html=True
    )

# --- Placeholder UI Test ---
st.title("✅ ConnexUS ROI Calculator (Theme-Safe Build)")
st.write("This is a stable base build with favicon, watermark, and layout enhancements applied.")
'''
