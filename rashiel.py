import streamlit as st


# Find more emoji's here:https://www.webfx.com/tools/emoji_cheat_sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


# ---- Header ----
with st.container():
 st.title("Ramos Webpage :tada:")
 image_column, text_column=st.columns(2)

    #Image from a local file
with image_column:
        st.image("rashiel.jpg")

with text_column: 
        st.header("Hi I am Rashiel Jane Ramos")       
        st.write("AGE: 18 years old")
        st.write("BIRTHDATE: April 14, 2005")
        st.write("STATUS: Single")
        st.write("FROM: Municipality of Sison")
        st.write("I am currently studying at SNSU - Surigao Del Norte State University")   
        st.title("Hobbies")  
        st.write("A journalist in the past High School days. I also played volleyball. And also spent myself more on reading books. I am between my younger and eldest siblings. ")
        st.write("*If you want to ask more information about me or want to make a project connected with my hobbies just get intouch with my Facebook Account")       
            
        st.write("---") 
        st.header("👉 Get In Touch With Me! 👈") 
        st.markdown("[Learn More >](https://www.facebook.com/profile.php?id=100066155058574)")
        st.write("Instagram: FRELHIRT")
        st.write("##")
    