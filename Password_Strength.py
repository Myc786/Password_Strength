import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker", page_icon="🔐")
st.title("🔐 Password Strength Checker")

st.markdown("""
            ## Welcome to the ultimate password strength checker! 🔐
            Use this simple tool to check your password strength and get suggestions to make it stronger.
            We will give you helpful tips to create a **strong password** 🔐.
            """)

password = st.text_input("Enter your password", type="password")  

feedback = []
score = 0

if password:
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❎ Your password should be at least 8 characters long.") 

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❎ Your password should contain both uppercase and lowercase letters.")  

    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("❎ Your password should contain at least one number.")  

    if re.search(r'[!@#$%^&*]', password):
        score += 1
    else:
        feedback.append("❎ Your password should contain at least one special character (!@#$%^&*).")                       

    if score == 4:
        feedback.append("💚 Your password is strong.") 
    elif score == 3:
        feedback.append("💛 Your password is medium strength. It could be stronger.") 
    else:
        feedback.append("🧡 Your password is weak, please make it stronger.")   

    if feedback: 
        st.markdown("## Improvement Suggestions ##")
        for tip in feedback:
            st.write(tip)
else:
    st.info("Please enter your password to get started.")
