
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Titanic Survival Predictor",
    page_icon="🚢",
    layout="centered"
)

@st.cache_resource
def load_model():
    data = joblib.load("titanic_model.joblib")
    return data["model"], data["feature_columns"]

model, feature_columns = load_model()

st.title("🚢 Titanic Survival Predictor")
st.write("Enter passenger details to predict the likelihood of survival.")

st.subheader("Passenger Details")

pclass = st.selectbox("Passenger Class", [1, 2, 3])
age = st.slider("Age", 0, 80, 25)
sibsp = st.slider("Number of Siblings/Spouses", 0, 8, 0)
parch = st.slider("Number of Parents/Children", 0, 6, 0)
fare = st.slider("Ticket Fare", 0.0, 513.0, 32.0, 0.5)
sex = st.selectbox("Sex", ["Female", "Male"])
embarked = st.selectbox(
    "Port of Embarkation",
    ["C", "Q", "S"],
    format_func=lambda x: {
        "C": "Cherbourg",
        "Q": "Queenstown",
        "S": "Southampton"
    }[x]
)

if st.button("Predict Survival"):
    if age < 0 or fare < 0:
        st.error("Please enter valid passenger details.")
    else:
        passenger = pd.DataFrame([{
            "Pclass": pclass,
            "Age": age,
            "SibSp": sibsp,
            "Parch": parch,
            "Fare": fare,
            "Sex_male": 1 if sex == "Male" else 0,
            "Embarked_Q": 1 if embarked == "Q" else 0,
            "Embarked_S": 1 if embarked == "S" else 0
        }])

        passenger = passenger[feature_columns]

        prediction = model.predict(passenger)[0]

        st.subheader("Prediction Result")

        if prediction == 1:
            st.success("🎉 The model predicts that the passenger would survive!")
        else:
            st.error("The model predicts that the passenger would not survive.")

        if hasattr(model, "predict_proba"):
            probability = model.predict_proba(passenger)[0]
            st.write(f"Estimated survival probability: {probability[1] * 100:.2f}%")
            st.progress(float(probability[1]))

st.caption("Educational project only. Predictions are not guarantees.")
