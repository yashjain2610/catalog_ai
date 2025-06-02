import streamlit as st

st.set_page_config(page_title="Jewelry App Hub", page_icon="💎", layout="centered")

st.title("Welcome to the Jewelry Image Generator 💍")

st.markdown("Choose an app to get started:")

col1, col2 , col3 = st.columns(3)

with col1:
    if st.button("🔹 Open catalog ai"):
        st.switch_page("pages/catalog_ai.py")

with col2:
    if st.button("🔸 Open ai image gen"):
        st.switch_page("pages/img_gen.py")
with col3:
    if st.button("🔸 Open leads dashboard"):
        st.switch_page("pages/leads_gen.py")