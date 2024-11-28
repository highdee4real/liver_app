import numpy as np
import pickle
import streamlit as st


#loading the saved model 
model = pickle.load(open('./lmodel.sav','rb'))


    
def main():   
    
    #title 
    st.title("A Software for Liver Disease Prediction")
    st.markdown('Kindly provide the details below')
    
    #getting user inputs
    Age = st.text_input("Enter your age")
    Gender = st.text_input("Enter your gender - 0: Male, 1: Female")
    TotalBilirubin= st.text_input("Total Bilirubin")
    DirectBilirubin = st.text_input("Direct Bilirubin")
    AAP = st.text_input("Alkphos Alkaline Phosphotase")
    Sgpt = st.text_input("Sgpt Alamine Aminotransferase")
    Sgot = st.text_input("Sgot Aspartate Aminotransferase")
    TotalProteins = st.text_input("Total Protiens")
    ALB = st.text_input("ALB Albumin")
    AGRatio = st.text_input("Albumin and Globulin Ratio")
         
    output = ''

    #button for prediction
    if st.button('Classify'):
        data = np.array([Age, Gender, TotalBilirubin, DirectBilirubin, AAP, Sgpt, Sgot, TotalProteins, ALB, AGRatio], dtype=np.float64)
        
        data_reshape = data.reshape(1, -1)
        
        #make prediction with the data
        result = model.predict(data_reshape)
        #result = int(result)
        
        if result == 0:
            output = 'The user has liver disease'  
        else:
            output = 'The user does not have liver disease'
    
    st.info(output)
        
        
        
if __name__ == '__main__':
    main()
        