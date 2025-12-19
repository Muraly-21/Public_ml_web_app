# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 22:22:31 2025

@author: 91888
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


#loading the saved models

diabetes_model = pickle.load(open("diabetes_trained_model.sav",'rb'))

heart_disease_model = pickle.load(open("heart_disease_prediction_model.sav",'rb'))

breast_cancer_model = pickle.load(open("breast_cancer_prediction_model.sav",'rb'))

#sidebar for navigation

with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System Using ML',
                           ['Diabetes Prediction',
                            'Heart Disease Prediciton',
                            'Breast Cancer Prediction'],
                           
                           icons = ['activity', 'heart-pulse' , 'clipboard2-pulse'],
                           
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
    
    
    
if(selected == 'Breast Cancer Prediction'):
    
    #title of the page
    st.title("Breast Cancer Prediction System")
    
    
    #getting input fields from the user
    
    #creating columns for the user
    col1,col2,col3 = st.columns(3)

    with col1:
        mean_radius = st.text_input("Mean Radius")
    with col2:
        mean_texture = st.text_input("Mean Texture")
    with col3:
        mean_perimeter = st.text_input("Mean Perimeter")
    
    with col1:
        mean_area = st.text_input("Mean Area")
    with col2:
        mean_smoothness = st.text_input("Mean Smoothness")
    with col3:
        mean_compactness = st.text_input("Mean Compactness")
    
    with col1:
        mean_concavity = st.text_input("Mean Concavity")
    with col2:
        mean_concave_points = st.text_input("Mean Concave Points")
    with col3:
        mean_symmetry = st.text_input("Mean Symmetry")
    
    with col1:
        mean_fractal_dimension = st.text_input("Mean Fractal Dimension")
    with col2:
        radius_error = st.text_input("Radius Error")
    with col3:
        texture_error = st.text_input("Texture Error")
    
    with col1:
        perimeter_error = st.text_input("Perimeter Error")
    with col2:
        area_error = st.text_input("Area Error")
    with col3:
        smoothness_error = st.text_input("Smoothness Error")
    
    with col1:
        compactness_error = st.text_input("Compactness Error")
    with col2:
        concavity_error = st.text_input("Concavity Error")
    with col3:
        concave_points_error = st.text_input("Concave Points Error")
    
    with col1:
        symmetry_error = st.text_input("Symmetry Error")
    with col2:
        fractal_dimension_error = st.text_input("Fractal Dimension Error")
    with col3:
        worst_radius = st.text_input("Worst Radius")  
        
    with col1:
        worst_texture = st.text_input("Worst Texture")
    with col2:
        worst_perimeter = st.text_input("Worst Perimeter")
    with col3:
        worst_area = st.text_input("Worst Area")
        
    with col1:
        worst_smoothness = st.text_input("Worst Smoothness")
    with col2:
        worst_compactness = st.text_input("Worst Compactness")
    with col3:
        worst_concavity = st.text_input("Worst Concavity")
        
    with col1:
        worst_concave_points = st.text_input("Worst Concave Points")
    with col2:
        worst_symmetry = st.text_input("Worst Symmetry")
    with col3:
        worst_fractal_dimension = st.text_input("Worst Fractal Dimension")
        
    
    #code for prediction
    breast_cancer_diagnosis = ''
    
    #button for prediction
    if st.button('Breast_Cancer_Result'):
        
        breast_cancer_result = breast_cancer_model.predict([[
            float(mean_radius), float(mean_texture), float(mean_perimeter),
            float(mean_area), float(mean_smoothness), float(mean_compactness),
            float(mean_concavity), float(mean_concave_points), float(mean_symmetry),
            float(mean_fractal_dimension), float(radius_error), float(texture_error),
            float(perimeter_error), float(area_error), float(smoothness_error),
            float(compactness_error), float(concavity_error),
            float(concave_points_error), float(symmetry_error),
            float(fractal_dimension_error), float(worst_radius),
            float(worst_texture), float(worst_perimeter), float(worst_area),
            float(worst_smoothness), float(worst_compactness),
            float(worst_concavity), float(worst_concave_points),
            float(worst_symmetry), float(worst_fractal_dimension)
        ]])
        
        if(breast_cancer_result[0] == 1):
            breast_cancer_diagnosis = "It is a Benign Cell"
            
        else:
            breast_cancer_diagnosis = "It is a  Malignant Cell"
            
        
    #displaying the result to the user
    st.success(breast_cancer_diagnosis)



        
            
    
    
    

