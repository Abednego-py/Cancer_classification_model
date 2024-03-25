import numpy as np
import pandas as pd
import joblib
import streamlit as st

model = joblib.load('cancer_model_revised.joblib')


def prediction(ucell_size, ucell_shape, bnuclei):
    y = model.predict(np.array([[ucell_size, ucell_shape, bnuclei]]))
    return y


def main():
    st.title('Cancer Classification Model')
    
    ucell_size = st.text_input('U cell size: ')
    ucell_shape = st.text_input('U cell shape: ')
    bnuclei = st.text_input('b nuclei : ')
    
    result = ''
    
    if st.button('Predict'):
        result = prediction(int(ucell_size), int(ucell_shape), int(bnuclei))
        if result[0] == 1:
            st.error('The cancer case is malignant')
        else:
            st.success('The cancer case is benign')
    
if __name__=='__main__':
    main()