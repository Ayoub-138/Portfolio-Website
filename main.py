import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Ayoub Ayadi")
    content = """Hi, I am Ayoub! I am a currently an Electro- and IT Bachelor of Engineering Student in the Applied 
    Science University of Düsseldorf in Germany with a focus on IT. I have had multiple projects including Neural 
    networking for Artificial Intelligence, Web and App development, Embedded Systems Programming, Network Security 
    and Data transmission."""

    st.info(content)

content2 = """
Below you can find some of my programming projects that i have made using Python and C#. Feel free to contact me !
"""

st.write(content2)