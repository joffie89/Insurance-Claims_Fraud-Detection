# Fraud Detection in Insurance Claims

## Project Description
This project aims to implement a machine learning model to detect fraudulent insurance claims. The dataset used for this project includes various features related to insurance claims, and the goal is to predict whether a claim is fraudulent.

## Key Contributions
- **Data Collection and Preprocessing**:
  - Loaded the dataset from a local CSV file.
  - Cleaned and preprocessed the data by handling missing values and encoding categorical variables.
  - Scaled numerical features to normalize the data.
- **Feature Engineering**:
  - Removed unnecessary features to reduce dimensionality and improve model performance.
- **Model Training and Evaluation**:
  - Trained multiple machine learning models, including Logistic Regression, Random Forest, and Isolation Forest.
  - Evaluated the models using accuracy, precision, recall, and F1 score metrics.
- **Hyperparameter Tuning**:
  - Performed hyperparameter tuning on the Random Forest model to optimize its performance.
- **Model Deployment**:
  - Saved the best-performing model for deployment.

## Files
- `Fraud_Detection_Insurance_Claims.ipynb`: Jupyter notebook containing the full analysis, data preprocessing, model training, evaluation, and hyperparameter tuning.
- `app.py`: Flask application for deploying the trained model and making predictions.

## Setup Instructions

### Prerequisites
Ensure you have the following packages installed:
- pandas
- numpy
- scikit-learn
- joblib
- Flask (for deployment)

You can install these packages using pip:
```bash
pip install pandas numpy scikit-learn joblib Flask
