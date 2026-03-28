import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

# Page config
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

# working dir
working_dir = os.path.dirname(os.path.abspath(__file__))

# Load models
diabetes_model = pickle.load(open(f'{working_dir}/saved_models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open(f'{working_dir}/saved_models/heart_disease_model.sav', 'rb'))
liver_model = pickle.load(open(f'{working_dir}/saved_models/liver_model.pkl', 'rb'))

# Sidebar
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Liver Disease Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person'],
                           default_index=0)

# 🔥 Tabs (GLOBAL)
tab1, tab2 = st.tabs(["📝 Manual Input", "📂 Upload Report"])


# ================== UPLOAD TAB ==================
with tab2:

    st.title("📂 Upload Health Report")

    uploaded_file = st.file_uploader(
        "Upload CSV or Excel file",
        type=["csv", "xlsx"]
    )

    if uploaded_file is not None:

        if uploaded_file.name.endswith('.csv'):
            data = pd.read_csv(uploaded_file)
        else:
            data = pd.read_excel(uploaded_file)

        st.success("File uploaded successfully ✅")
        st.dataframe(data.head())

        row = data.iloc[0]

        st.subheader("🤖 AI Prediction Results")

        # Diabetes
        try:
            diabetes_input = [
                row['Pregnancies'], row['Glucose'], row['BloodPressure'],
                row['SkinThickness'], row['Insulin'], row['BMI'],
                row['DiabetesPedigreeFunction'], row['Age']
            ]
            pred = diabetes_model.predict([diabetes_input])[0]
            if pred == 1:
                st.error("🧠 Diabetes Risk: HIGH")
            else:
                st.success("🧠 Diabetes Risk: LOW")
        except:
            st.warning("Diabetes data not found")

        # Heart
        try:
            heart_input = [
                row['age'], row['sex'], row['cp'], row['trestbps'],
                row['chol'], row['fbs'], row['restecg'],
                row['thalach'], row['exang'], row['oldpeak'],
                row['slope'], row['ca'], row['thal']
            ]
            pred = heart_disease_model.predict([heart_input])[0]
            if pred == 1:
                st.error("❤️ Heart Disease Risk: HIGH")
            else:
                st.success("❤️ Heart Disease Risk: LOW")
        except:
            st.warning("Heart data not found")

        # Liver
        try:
            liver_input = [
                row['Age'], row['Gender'], row['Total_Bilirubin'],
                row['Direct_Bilirubin'], row['Alkaline_Phosphotase'],
                row['Alamine_Aminotransferase'],
                row['Aspartate_Aminotransferase'],
                row['Total_Protiens'], row['Albumin'],
                row['Albumin_and_Globulin_Ratio']
            ]
            pred = liver_model.predict([liver_input])[0]
            if pred == 1:
                st.error("🧪 Liver Disease Risk: HIGH")
            else:
                st.success("🧪 Liver Disease Risk: LOW")
        except:
            st.warning("Liver data not found")


# ================== MANUAL TAB ==================
with tab1:

    # Diabetes
    if selected == 'Diabetes Prediction':

        st.title('Diabetes Prediction using ML')

        col1, col2, col3 = st.columns(3)

        with col1:
            Pregnancies = st.text_input('Number of Pregnancies')

        with col2:
            Glucose = st.text_input('Glucose Level')

        with col3:
            BloodPressure = st.text_input('Blood Pressure value')

        with col1:
            SkinThickness = st.text_input('Skin Thickness value')

        with col2:
            Insulin = st.text_input('Insulin Level')

        with col3:
            BMI = st.text_input('BMI value')

        with col1:
            DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function')

        with col2:
            Age = st.text_input('Age')

        if st.button('Diabetes Test Result'):
            user_input = [float(Pregnancies), float(Glucose), float(BloodPressure),
                          float(SkinThickness), float(Insulin), float(BMI),
                          float(DiabetesPedigreeFunction), float(Age)]

            prediction = diabetes_model.predict([user_input])[0]

            if prediction == 1:
                st.error("🧠 Diabetes Risk: HIGH")
            else:
                st.success("🧠 Diabetes Risk: LOW")

    # Heart
    if selected == 'Heart Disease Prediction':

        st.title('Heart Disease Prediction using ML')

        col1, col2, col3 = st.columns(3)

        with col1:
            age = st.text_input('Age')

        with col2:
            sex = st.text_input('Sex')

        with col3:
            cp = st.text_input('Chest Pain types')

        with col1:
            trestbps = st.text_input('Resting Blood Pressure')

        with col2:
            chol = st.text_input('Cholesterol')

        with col3:
            fbs = st.text_input('Fasting Blood Sugar')

        with col1:
            restecg = st.text_input('Rest ECG')

        with col2:
            thalach = st.text_input('Max Heart Rate')

        with col3:
            exang = st.text_input('Exercise Angina')

        with col1:
            oldpeak = st.text_input('Oldpeak')

        with col2:
            slope = st.text_input('Slope')

        with col3:
            ca = st.text_input('CA')

        with col1:
            thal = st.text_input('Thal')

        if st.button('Heart Test Result'):
            user_input = [float(age), float(sex), float(cp), float(trestbps),
                          float(chol), float(fbs), float(restecg),
                          float(thalach), float(exang), float(oldpeak),
                          float(slope), float(ca), float(thal)]

            prediction = heart_disease_model.predict([user_input])[0]

            if prediction == 1:
                st.error("❤️ Heart Disease Risk: HIGH")
            else:
                st.success("❤️ Heart Disease Risk: LOW")

    # Liver
    if selected == 'Liver Disease Prediction':

        st.title('Liver Disease Prediction using ML')

        age = st.text_input('Age')
        gender = st.text_input('Gender (Male=1, Female=0)')
        total_bilirubin = st.text_input('Total Bilirubin')
        direct_bilirubin = st.text_input('Direct Bilirubin')
        alkaline_phosphotase = st.text_input('Alkaline Phosphotase')
        alt = st.text_input('ALT')
        ast = st.text_input('AST')
        total_proteins = st.text_input('Total Proteins')
        albumin = st.text_input('Albumin')
        ratio = st.text_input('A/G Ratio')

        if st.button('Liver Test Result'):

            input_data = [float(age), float(gender), float(total_bilirubin),
                          float(direct_bilirubin), float(alkaline_phosphotase),
                          float(alt), float(ast), float(total_proteins),
                          float(albumin), float(ratio)]

            prediction = liver_model.predict([input_data])[0]

            if prediction == 1:
                st.error("🧪 Liver Disease Risk: HIGH")
            else:
                st.success("🧪 Liver Disease Risk: LOW")