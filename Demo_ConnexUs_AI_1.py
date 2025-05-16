import streamlit as st
import streamlit.components.v1 as components
import base64

# ✅ Config with native favicon
st.set_page_config(
    page_title="ConnexUs.AI Widget Demo",
    page_icon="favicon-32x32.png",  # You can also use "favicon.ico" here
    layout="wide"
)

# ✅ Custom favicon (PNG version)
with open("favicon-32x32.png", "rb") as f:
    favicon_base64 = base64.b64encode(f.read()).decode("utf-8")

components.html(f"""
    <link rel="icon" type="image/png" href="data:image/png;base64,{favicon_base64}">
""", height=0)

# ✅ Load watermark and top logo
with open("connexus_logo_watermark.png", "rb") as f:
    watermark_base64 = base64.b64encode(f.read()).decode("utf-8")

with open("connexus_logo.png", "rb") as f:
    logo_topright_base64 = base64.b64encode(f.read()).decode("utf-8")
    
# ✅ Inject global styles + watermark
st.markdown(f"""
<style>
.block-container {{
    padding-top: 1rem !important;
    position: relative;
}}

.watermark {{
    position: fixed;
    top: 100px;
    left: 50%;
    transform: translateX(-50%);
    height: 600px;
    width: 600px;
    z-index: 0;
    pointer-events: none;
    background-image: url("data:image/png;base64,{watermark_base64}");
    background-repeat: no-repeat;
    background-position: center center;
    background-size: contain;
    opacity: 0.13;
}}

.top-logo {{
    position: absolute;
    top: 40px;
    right: 20px;
    max-height: 60px;
    width: auto;
    z-index: 999;
}}

.responsive-title {{
    font-size: clamp(26px, 3.5vw, 48px);
    font-weight: 700;
    margin-top: 120px;
    margin-bottom: 16px;
    color: inherit;
}}

.agent-header {{
    font-size: 32px;
    font-weight: 600;
    margin-top: 10px;
    margin-bottom: 10px;
    color: inherit;
}}

.stTabs [data-baseweb="tab"] {{
    font-size: 36px !important;
    font-weight: 600 !important;
    padding: 12px 24px !important;
}}
</style>

<!-- ✅ Inject watermark and logo -->
<div class="watermark"></div>
<img src="data:image/png;base64,{logo_topright_base64}" class="top-logo" />
""", unsafe_allow_html=True)

# ✅ Title
st.markdown("""
<h1 class="responsive-title">Pick the V-Rep you would like to speak with</h1>
""", unsafe_allow_html=True)

# ✅ Tabs - this section is now clean
tabs = st.tabs(["🧠 Vernon","🤖 Peggy","🧠 Veronica", "🤖 Noah"])

# === Vernon ===
with tabs[0]:
    st.markdown(
    f"""
    <h2 class="agent-header">
        Vernon - ACA
    </h2>
    """,
    unsafe_allow_html=True
)
    components.html("""
        <div style="background-color: transparent;">
        <script src="https://connexusai.pages.dev/chat-widget.js"
          integrity="vC9YPpJCP1QqkOQ9kePoXmywFRS4mksl4NjUesvWKelztotJiBII+WJuR6TYolgu%"
          data-source-id="Ai-001-Vernon-ACA"
          data-agent-id="agent_b1ecd31e4cdca318b4224881bb"
          data-agent-name="Vernon"
          data-div-id="Vernon-connexUS">
        </script>
        <script>
          window.onload = () => {{
            ChatWidget.initializeChatWidget();
            document.body.style.background = "transparent";
          }};
        </script>
        </div>
    """, height=400)
    
# === Peggy ===
with tabs[1]:
    st.markdown(
    f"""
    <h2 class="agent-header">
        Peggy – ACA
    </h2>
    """,
    unsafe_allow_html=True
)
    components.html("""
        <div style="background-color: transparent;">
        <script src="https://connexusai.pages.dev/chat-widget.js"
          integrity="vC9YPpJCP1QqkOQ9kePoXmywFRS4mksl4NjUesvWKelztotJiBII+WJuR6TYolgu%"
          data-source-id="Ai-001-Peggy"
          data-agent-id="agent_49bb00f8bf9e6390138405580d"
          data-agent-name="Peggy"
          data-div-id="Peggy-connexUS">
        </script>
        <script>
          window.onload = () => {{
            ChatWidget.initializeChatWidget();
            document.body.style.background = "transparent";
          }};
        </script>
        </div>
    """, height=400)

# === Veronica ===
with tabs[2]:
    st.markdown(
    f"""
    <h2 class="agent-header">
        Veronica – Home Life Shield Fronter
    </h2>
    """,
    unsafe_allow_html=True
)
    components.html("""
    <div style="background-color: transparent;">
    <script src="https://connexusai.pages.dev/chat-widget.js"
      integrity="vC9YPpJCP1QqkOQ9kePoXmywFRS4mksl4NjUesvWKelztotJiBII+WJuR6TYolgu%"
      data-source-id="Ai-001-HomeLifeShield-Fronter"
      data-agent-id="agent_262c145e728ec06e0916eb0d2d"
      data-agent-name="Veronica"
      data-div-id="Veronica-connexUS">
    </script>
    <script>
      window.onload = () => {{
        ChatWidget.initializeChatWidget();
        document.body.style.background = "transparent";
      }};
    </script>
    </div>
    """, height=400)

# === Noah ===
with tabs[3]:
    st.markdown(
    f"""
    <h2 class="agent-header">
        Noah - Home Life Shield
    </h2>
    """,
    unsafe_allow_html=True
)
    components.html("""
    <div style="background-color: transparent;">
    <script src="https://connexusai.pages.dev/chat-widget.js"
      integrity="vC9YPpJCP1QqkOQ9kePoXmywFRS4mksl4NjUesvWKelztotJiBII+WJuR6TYolgu%"
      data-source-id="Ai-001-Noah_HomeLifeShield"
      data-agent-id="agent_3db37228c59d76eef1f88f501e"
      data-agent-name="Noah"
      data-div-id="Noah-connexUS">
    </script>
    <script>
      window.onload = () => {{
        ChatWidget.initializeChatWidget();
        document.body.style.background = "transparent";
      }};
    </script>
    </div>
    """, height=400)
