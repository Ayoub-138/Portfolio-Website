import streamlit as st
import pandas

st.set_page_config(layout="wide")


col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Ayoub Ayadi")
    content = """
Greetings,

I am Ayoub, a student currently pursuing a Bachelor's degree in Electro- and IT Engineering at the Applied 
Science University of Düsseldorf in Germany, with a focus on Information Technology. Throughout my academic 
journey, I've actively engaged in diverse projects, specializing in Neural Networking for Artificial 
Intelligence, Web and App Development, Embedded Systems Programming, Network Security, and Data Transmission. 
This multifaceted experience has broadened my skills and adaptability, emphasizing my commitment to 
contributing meaningfully to the advancements in Information Technology."""

    st.info(content)

content2 = """
Below you can find some of my programming projects that i have made using Python and C#. 
Feel free to contact me !
"""

st.write(content2)

col3, empty_col, col4 = st.columns([1.5,0.5,1.5])
df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")