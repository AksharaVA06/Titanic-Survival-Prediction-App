# Titanic-Survival-Prediction-App
Titanic survival prediction web app using Streamlit and Decision Tree
# Titanic Survival Prediction App

A machine learning web application built using **Python, Streamlit, and Decision Tree Classification** to predict the survival outcome of Titanic passengers based on their details.

## Project Overview

This project uses a Decision Tree Classifier trained on the Titanic dataset. Users can enter passenger information through an interactive web interface and receive a survival prediction with an estimated probability.

## Features

- Interactive Streamlit user interface
- Passenger class, age, fare, gender, and family information inputs
- Machine learning prediction using a trained Decision Tree model
- Estimated survival probability
- Input validation
- Model loading using Joblib

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Streamlit
- Joblib

## Project Files

| File | Description |
|---|---|
| `app.py` | Streamlit application |
| `titanic_model.joblib` | Trained Decision Tree model |
| `requirements.txt` | Required Python packages |
| `README.md` | Project documentation |

## How to Run Locally

1. Clone this repository:

```bash
git clone https://github.com/AksharaVA06/Titanic-Survival-Prediction-App.git
```

2. Open the project folder:

```bash
cd Titanic-Survival-Prediction-App
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
python -m streamlit run app.py
```

5. Open the local URL displayed in your terminal, usually `http://localhost:8501/`.

## Model Testing

The application was tested locally with sample passenger details and successfully generated a survival prediction and estimated probability.

## Deployment Status

The application currently runs locally. Public deployment was attempted but has not yet been completed.

## Disclaimer

This project is for educational purposes only. Predictions are based on a machine learning model and are not guarantees of actual survival outcomes.

