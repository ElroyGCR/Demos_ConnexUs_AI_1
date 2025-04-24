import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from PIL import Image
from io import BytesIO
import base64

def load_favicon_base64(path="favicon-32x32.png"):
    try:
        img = Image.open(path)
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        return base64.b64encode(buffer.getvalue()).decode("utf-8")
    except Exception as e:
        print("Favicon load error:", e)
        return None

favicon_b64 = load_favicon_base64("favicon-32x32.png")  # safer fallback than .ico

if favicon_b64:
    st.markdown(
        f"""
        <link rel="icon" type="image/png" sizes="32x32" href="data:image/png;base64,{favicon_b64}">
        <link rel="icon" type="image/png" sizes="16x16" href="data:image/png;base64,{favicon_b64}">
        """,
        unsafe_allow_html=True
    )
