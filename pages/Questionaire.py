import streamlit as st
import pandas as pd
pic1 = "Images/ice_cream.jpg"
pic2 = "Images/cookies.jpg"
pic3 = "Images/dining_hall.jpg"
def introduction():
    st.subheader("Welcome to the Questionaire! We'd just like to ask you a couple questions quickly about the dining halls, it won't take too much of your time.")
    st.write('---')
    st.image((pic3), width = 200)
    
introduction()

def question1():
    st.subheader("Question 1")
    #new
    dining_hall = st.radio("Which is your prefered dining hall?",("North Avenue", "West Village"))
question1()

def question2():
    st.subheader("Question 2")
    #new
    p_dining_hall = st.multiselect("What days do you eat at the dining hall?", ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"))
question2()

def question3():
        st.subheader("Question 3")
        dessert = 0
        #new
        dessert = st.number_input("How many days do you get dessert?")
question3()             

def question4():
    st.subheader("Question 4")
    st.image(pic2, width = 150)
    #new
    which_desserts = st.selectbox("Which dessert do you get the most frequently from the dining halls?", ("None", "Cake", "Cookies", "Brownies", "Cupcakes", "Ice Cream"))
question4()

def question5():
    st.subheader("Question 5")
    st.image(pic1, width = 150)
    #new
    no_ice = st.slider("How upset are you by the absence of ice cream at Willage?")
question5()
submit = st.button(label = 'Submit')

if submit:
    st.write("Thank you for your input!")



