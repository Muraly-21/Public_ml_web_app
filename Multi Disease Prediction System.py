# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 22:22:31 2025

@author: 91888
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


#loading the saved models

diabetes_model = pickle.load(open("E:/ML_Models Deployment/Multiple Disease Predictive System/diabetes_trained_model.sav",'rb'))

heart_disease_model = pickle.load(open("E:/ML_Models Deployment/Multiple Disease Predictive System/heart_disease_prediction_model.sav",'rb'))


#sidebar for navigation

with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System Using ML',
                           ['Diabetes Prediction',
                            'Heart Disease Prediciton'],
                           
                           icons = ['activity', 'heart-pulse'],
                           
                           default_index=0)
    

#diabetes prediction page
if(selected == 'Diabetes Prediction'):
    
    #page title
    st.title("Diabetes Prediction System")
    
    
    #getting the inputs from the user
    
    #creating column for the input fields
    col1,col2,col3 = st.columns(3)
    
    with col1:
        pregnancies = st.text_input('Number of Pregnancies')
    
    with col2:
        Glucose = st.text_input("Glucose Level")
    
    with col3:
        BloodPressure = st.text_input("Blood Pressure Level")
    
    with col1:
        SkinThickness = st.text_input("Skin Thickness Level")
    
    with col2:
        Insulin = st.text_input("Insulin Level")
    
    with col3:
        BMI = st.text_input("BMI")
    
    with col1:
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function")
    
    with col2:
        Age = st.text_input("Age")
    
    
    #code for prediction
    diab_diagnosis = ''
    
    
    #creating a button for prediction
    if st.button("Diabetes Test Result"):
        
        diab_prediction = diabetes_model.predict([[pregnancies , Glucose , BloodPressure , SkinThickness , Insulin , BMI , DiabetesPedigreeFunction , Age]])
        
        if(diab_prediction[0] == 1):
            diab_diagnosis = "The Person is Diabetic"
        else:
            diab_diagnosis = "The Person is Not Diabetic"
            
    
    #displaying the result to the user
    st.success(diab_diagnosis)
    

#heart disease prediction page
if(selected == 'Heart Disease Prediciton'):  
    
    #page title
    st.title("Heart Disease Prediction System")
    
    
    #getting input fields from the user
    
    #creating column for the input fields
    col1,col2,col3 = st.columns(3)
    
    with col1:
        age = st.text_input("Age")
    
    with col2:
        sex = st.text_input("Sex")
    
    with col3:
        cp = st.text_input("Chest Pain Type")
    
    with col1:
        trestbps = st.text_input("Resting Blood Pressure")
    
    with col2:
        chol = st.text_input("Serum Cholestoral in mg/dl")
    
    with col3:
        fbs = st.text_input("fasting blood sugar > 120 mg/dl")
    
    with col1:
        restecg = st.text_input("resting electrocardiographic results (values 0,1,2)")
    
    with col2:
        thalach	= st.text_input("maximum heart rate achieved")
    
    with col3:
        exang = st.text_input("exercise induced angina")
    
    with col1:
        oldpeak	= st.text_input("oldpeak = ST depression induced by exercise relative to rest")
    
    with col2:
        slope = st.text_input("the slope of the peak exercise ST segment")
    
    with col3:
        ca = st.text_input("number of major vessels (0-3) colored by flourosopy")
    
    with col1:
        thal = st.text_input("thal: 0 = normal; 1 = fixed defect; 2 = reversable defect")
      
        
    #code for prediction
    heart_diagnosis = ''
    
    
    #button for prediction
    if st.button('Heart Test Prediction'):
        
        heart_prediction = heart_disease_model.predict([[
        float(age), float(sex), float(cp), float(trestbps),
        float(chol), float(fbs), float(restecg), float(thalach),
        float(exang), float(oldpeak), float(slope),
        float(ca), float(thal)
        ]])

        
        if(heart_prediction[0] == 1):
            heart_diagnosis= "The Person Has Heart Disease"
            
        else:
            heart_diagnosis = "The Person Does Not Have Heart Disease"
            
    
    #displaying the result to the users
    st.success(heart_diagnosis)
            
    
    
    
