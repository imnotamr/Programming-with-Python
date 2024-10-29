api = 'AIzaSyAJIGZjlt79fVaU_vnstZWBJiVU-E75yww'
import streamlit as st
import google.generativeai as genai
import os 

st.title('Google API Text Generator')

if api:
    genai.configure(api_key = api)
else:
    st.error('Your API Key is Not Found')


def Generate_Text(text):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(text)
    return response.text

if 'messages' not in st.session_state:
    st.session_state.messages = []
    
for message in st.session_state.messages:
    with st.chat_message(message['role']): #role ----> user / assistant
        st.markdown(message['content']) #content ----> user_input / response
        
if user_input := st.chat_input("Please Enter the Text...."):
        
        with st.chat_message("user"):
            st.markdown(user_input)
            
        st.session_state.messages.append({'role':'user', 'content' :user_input})
        
        with st.chat_message('assistant'):
            message_placeholder = st.empty()
            with st.spinner('Generating Response....'):
                response_text = Generate_Text(user_input)
                message_placeholder.markdown(f'{response_text}')
                
        st.session_state.messages.append({'role':'assistant', 'content' :response_text})
