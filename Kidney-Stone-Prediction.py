#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pickle
import streamlit as st

#Loading the saved model
loaded_model = pickle.load(open('C:/Users/Aniekan/Desktop/kidney stone/Train_model.sav', 'rb'))



#creating a function for prediction
def kidney_stone_pred(input_data):
    
    #Change the input data into array
    input_data_as_numpy_array = np.asarray(input_data)
    #Reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0]==0):
        return 'This person does not have Kidney Stone'
    else:
        return'This person have Kidney Stone'
        
        
        
        
def main():
    
    #Giving a title
    st.title('Kidney Stone Prediction Based on Urine Analysis')
    
    #Getting the imput data from user
    
    gravity = st.text_input('value of  the density of the urine relative to water')
    ph = st.text_input('value of the negative logarithm of the hydrogen ion')
    osmo = st.text_input('values of concentration of molecules in solution')
    cond = st.text_input('concentration of charged ions in solution')
    urea = st.text_input('concentration in millimoles per litre')
    calc = st.text_input('calcium concentration (CALC) in millimolesllitre.')
    
    
    #code for prediction
    diagnosis = ''
    
    #Creating a button for prediction
    if st.button('Kidney Stone Result'):
        diagnosis = kidney_stone_pred([gravity,ph,osmo,cond,urea,calc])
    
    st.success(diagnosis)
    
        
if __name__ == '__main__':
    main()
    
    


# In[ ]:




