import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Amber Widget", layout="wide")
st.title("🧠 Chat with Amber – Connexus AI")

components.html("""
<script src="https://connexusai.pages.dev/chat-widget.js"
  integrity="vC9YPpJCP1QqkOQ9kePoXmywFRS4mksl4NjUesvWKelztotJiBII+WJuR6TYolgu%"
  data-source-id="Ai-001-Ecampus_Protoype"
  data-agent-id="agent_d8a88fd3d28d15594dbdc0320b"
  data-agent-name="Amber"
  data-div-id="Amber-connexUS">
</script>
<script>
  window.onload = () => {
    ChatWidget.initializeChatWidget();
  };
</script>
""", height=400)

