# Healthify App - A Health and Wellness Application

import google.generativeai as genai
import streamlit as st
import os   
import pandas as pd

api = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=api)
model = genai.GenerativeModel('gemini-2.5-flash-lite')


#Lets create the UI for the app
st.title(":orange[HEALTHIFY] - :blue[Your Personal Health and Wellness Assistant at service]" )


st.header(''' "***This app is designed to provide personalized health and wellness advice using AI.You can ask questions about nutrition, exercise, mental health, and more.***" ''')
tips = ''' Follow the steps 
* Enter your details in the sidebar.
* Enter your gender , age, height(cms), weight(kgs), and any specific health concerns you have.
* Select the number on the fitness scale(0-5) , 5 - Fittest , 0 - No fitness at all.
* After filling the details , write your health-related question with the help of prompt and get your customised response .'''
st.write(tips)

#Lets Configure sidebar
st.sidebar.image('bmi_image.jpg', width=500)
st.sidebar.header('***:red[ENTER YOUR DETAILS:]***')
name = st.sidebar.text_input('Enter your name')
gender = st.sidebar.selectbox('Select your gender',['Male','Female','Other'])
age = st.sidebar.text_input('Enter your age in years')
weight = st.sidebar.text_input('Enter your weight in kgs')
height = st.sidebar.text_input('Enter your height in cms')
bmi =pd.to_numeric(weight) / (pd.to_numeric(height)/100)**2
fitness_scale = st.sidebar.slider('Select your fitness level between (0-5)', 0, 5, step = 1)
st.sidebar.write(f'{name} your BMI is : {round(bmi,2)}Kg/m^2')

# Lets use genai model to generate response
user_query = st.text_area('Enter your health-related question below:')

prompt = f''' Assume you are a health and wellness expert. Provide personalized advice 
based on the following user details , Use the details provided by the user.
name of user is {name},
gender is {gender},age is {age}, 
weight is {weight} kgs, 
height is {height} cms, 
BMI is {round(bmi,2)}Kg/m^2  and user fitness level is {fitness_scale} on a scale of 0-5. 
user rates his fitness level as {fitness_scale} on a scale of 0-5.
Answer the question asked by the user in a professional manner and in bullet points and in the following below given format.
*It should start by greeting the user with his name.
*It should start by giving one or two line comment on the query asked by the user.
*What could be the possible reason for the problem.
*What are the possible solutions to the problem.
*You can also mention what doctor to see(specialization) if needed.
*Strictly avoid any kind of medical jargons and terminologies.
*Make sure the response is easy to understand by a layman.
*Make a diet chart in the tabular format.
*In the end give a positive note to the user.
* In the end give summary of the response.
here is the question asked by the user {user_query}

'''


if user_query:
    response = model.generate_content(prompt)
    st.write(response.text)


