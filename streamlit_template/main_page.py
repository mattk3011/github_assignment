import streamlit as st

st.markdown("# Welcome to my Website!")
st.sidebar.markdown("# Main Page")

st.write("Click on a page to see racer stats")

link = '[To my Github Pages site](http://127.0.0.1:5500/)'
st.markdown(link, unsafe_allow_html=True)