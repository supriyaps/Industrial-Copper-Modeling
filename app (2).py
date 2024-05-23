







import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
import pickle

# -------------------------------This is the configuration page for our Streamlit Application---------------------------
st.set_page_config(
    page_title="Industrial Copper Modeling",

    layout="wide"
)

# -------------------------------This is the sidebar in a Streamlit application, helps in navigation--------------------
with st.sidebar:
    selected = option_menu("Main Menu", ["About Project", "Selling Price Prediction", "Status (Win/Lost)"],
                           icons=["house", "gear", "gear"],
                           styles={"nav-link": {"font": "sans serif", "font-size": "20px", "text-align": "centre"},
                                   "nav-link-selected": {"font": "sans serif", "background-color": "#0072b1"},
                                   "icon": {"font-size": "20px"}
                                   }
                           )

# -----------------------------------------------About Project Section--------------------------------------------------
if selected == "About Project":
    st.markdown("# :blue[Industrial Copper Modeling]")
    st.markdown('<div style="height: 50px;"></div>', unsafe_allow_html=True)
    st.markdown("### :blue[Technologies :] Python, Pandas, Numpy, Scikit-Learn, Streamlit, Python scripting, "
                "Machine Learning, Data Preprocessing, Visualization, EDA, Model Building, Data Wrangling, "
                "Model Deployment")
    st.markdown("### :blue[Overview :] This project aims to construct a machine learning model and implement "
                "it as a user-friendly online application in order to provide accurate predictions about the "
                "Selling price and status of the copper model. This prediction model will be based on past transactions.")

    # ------------------------------------------------Predictions Section---------------------------------------------------
if selected == "Selling Price Prediction":
    st.markdown("# :blue[Predicting Results based on Trained Model]")
    # -----New Data inputs from the user for predicting the selling price-----
    a1 = st.text_input("Quantity")
    b1 = st.text_input("Status")
    c1 = st.text_input("Item Type")
    d1 = st.text_input("Application")
    e1 = st.text_input("Thickness")
    f1 = st.text_input("Width")
    g1 = st.text_input("Country")
    h1 = st.text_input("Customer")
    i1 = st.text_input("Product Reference")

    with open(r"/content/Reg_model.pkl", 'rb') as file_1:
        regression_model = pickle.load(file_1)

    # -----Submit Button for PREDICT RESALE PRICE-----
    predict_button_1 = st.button("Predict Selling Price")

    if predict_button_1:

        a1 = float(a1)
        b1 = float(b1)
        c1 = float(c1)
        d1 = float(d1)
        e1 = float(e1)
        f1 = float(f1)
        g1 = float(g1)
        h1 = float(h1)
        i1 = float(i1)

        # -----Sending the user enter values for prediction to our model-----
        new_sample_1 = np.array(
                [[np.log(a1), b1, c1, d1, np.log(e1), f1, g1, h1, i1]])
        new_pred_1 = regression_model.predict(new_sample_1)[0]

        st.write('## :green[Predicted resale price:] ', np.exp(new_pred_1))

if selected == "Status (Win/Lost)":
    st.markdown("# :blue[Predicting Results based on Trained Model]")
    # -----New Data inputs from the user for predicting the status-----
    a2 = st.text_input("Quantity")
    b2 = st.text_input("Selling Price")
    c2 = st.text_input("Item Type")
    d2 = st.text_input("Application")
    e2 = st.text_input("Thickness")
    f2 = st.text_input("Width")
    g2 = st.text_input("Country")
    h2 = st.text_input("Customer")
    i2 = st.text_input("Product Reference")

    with open(r"/content/classfier_model.pkl", 'rb') as file_2:
        classification_model = pickle.load(file_2)

    # -----Submit Button for PREDICT RESALE PRICE-----
    predict_button_2 = st.button("Predict Status")

    if predict_button_2:

        a2 = float(a2)
        b2 = float(b2)
        c2 = float(c2)
        d2 = float(d2)
        e2 = float(e2)
        f2 = float(f2)
        g2 = float(g2)
        h2 = float(h2)
        i2 = float(i2)
        # -----Sending the user enter values for prediction to our model-----
        new_sample_2 = np.array(
                [[np.log(a2), np.log(b2), c2, d2, np.log(e2), f2, g2, h2, i2]])
        new_pred_2 = classification_model.predict(new_sample_2)

        if new_pred_2 ==1:
            st.write('## :green[The Status is: Won]')
        else:
            st.write('## :green[The Status is: Lost]')
