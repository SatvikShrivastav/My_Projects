# Loan Status Prediction using Machine Learning

## Overview

This project implements a machine learning classification system to predict whether a loan application is likely to be approved or rejected.

The project was developed in **Google Colab** using Python and the Scikit-learn ecosystem. It uses applicant demographic, financial, credit-history, and property-related information to predict the `Loan_Status` target.

The model used in the notebook is a **Support Vector Machine (SVM)** classifier with a **linear kernel**.

## Problem Statement

Loan approval decisions depend on several applicant characteristics such as income, credit history, education, marital status, loan amount, loan term, and property area. The objective of this project is to use historical loan application data to build a classification model that predicts the loan status of an applicant.

## Objectives

- Load and inspect the loan application dataset.
- Identify and handle missing values.
- Convert categorical variables into numerical representations.
- Perform basic exploratory data visualization.
- Separate input features and the target variable.
- Split the dataset into training and testing sets.
- Train a linear Support Vector Machine classifier.
- Evaluate the model using accuracy score.

## Dataset

The supplied dataset contains **614 records and 13 columns**.

### Columns

| Column | Description |
|---|---|
| `Loan_ID` | Unique loan application identifier |
| `Gender` | Applicant gender |
| `Married` | Marital status |
| `Dependents` | Number of dependents |
| `Education` | Graduate / Not Graduate |
| `Self_Employed` | Self-employment status |
| `ApplicantIncome` | Applicant income |
| `CoapplicantIncome` | Co-applicant income |
| `LoanAmount` | Loan amount |
| `Loan_Amount_Term` | Loan repayment term |
| `Credit_History` | Credit history indicator |
| `Property_Area` | Rural / Semiurban / Urban |
| `Loan_Status` | Target: `Y` = approved, `N` = not approved |

## Data Preprocessing

The notebook follows these preprocessing steps:

1. Load the CSV dataset with Pandas.
2. Inspect the dataset shape and statistical measures.
3. Check missing values in every column.
4. Remove rows containing missing values using `dropna()`.
5. Convert `Loan_Status` from `N/Y` to `0/1`.
6. Convert the `Dependents` value `3+` to `4`.
7. Encode categorical variables numerically:
   - `Married`: No = 0, Yes = 1
   - `Gender`: Female = 0, Male = 1
   - `Self_Employed`: No = 0, Yes = 1
   - `Property_Area`: Rural = 0, Semiurban = 1, Urban = 2
   - `Education`: Not Graduate = 0, Graduate = 1
8. Remove `Loan_ID` because it is an identifier rather than a predictive feature.
9. Separate the features (`X`) and target (`Y`).

After removing rows with missing values, the notebook uses **480 records** for model development.

## Exploratory Data Visualization

The notebook includes count plots to examine the relationship between:

- Education and Loan Status
- Marital Status and Loan Status

These visualizations provide a basic view of the distribution of loan outcomes across categorical applicant characteristics.

## Machine Learning Model

### Support Vector Machine

A **Support Vector Classifier (SVC)** is used:

```python
classifier = svm.SVC(kernel='linear')
```

The classifier uses a **linear kernel**.

## Train-Test Split

The cleaned dataset is divided using:

```python
train_test_split(
    X, Y,
    test_size=0.1,
    stratify=Y,
    random_state=2
)
```

This produces:

- Training set: **432 records**
- Testing set: **48 records**
- Number of input features: **11**

Stratification is used so that the target-class distribution is maintained between the training and testing sets.

## Model Training

The SVM model is trained with:

```python
classifier.fit(X_train, Y_train)
```

## Model Evaluation

The notebook evaluates the classifier using `accuracy_score`.

### Results

| Dataset | Accuracy |
|---|---:|
| Training data | **79.86%** |
| Test data | **83.33%** |

The test accuracy reported by the notebook is **83.33%**.

## Project Workflow

```text
Loan Dataset
     |
     v
Data Loading
     |
     v
Data Inspection
     |
     v
Missing-Value Check
     |
     v
Remove Missing Rows
     |
     v
Categorical Encoding
     |
     v
Feature / Target Separation
     |
     v
Train-Test Split
     |
     v
Linear SVM Training
     |
     v
Prediction
     |
     v
Accuracy Evaluation
```

## Technologies Used

- Python
- Google Colab
- NumPy
- Pandas
- Seaborn
- Scikit-learn
- Support Vector Machine (SVM)

## Libraries Used

```python
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
```

## Project Structure

```text
Project_1_Loan_Prediction/
│
├── Loan_Status_Prediction.ipynb
├── loan.csv
└── README.md
```

## How to Run

### Google Colab

1. Open `Loan_Status_Prediction.ipynb` in Google Colab.
2. Upload the dataset CSV.
3. Make sure the CSV filename/path matches the path used by the notebook.
4. Run the notebook cells from top to bottom.

The original notebook loads the dataset using:

```python
pd.read_csv('/content/dataset.csv')
```

If the uploaded file is named `loan.csv`, either rename it to `dataset.csv` in Colab or update the path in the notebook.

## Limitations

- Missing values are handled by removing incomplete rows, which reduces the available data from 614 records to 480 records.
- The categorical variables are manually label-encoded.
- Only a linear SVM model is trained in the supplied notebook.
- Evaluation is based primarily on accuracy; other classification metrics such as precision, recall, F1-score, ROC-AUC, and a confusion matrix are not included in the supplied notebook.
- The project does not include a deployed web or API interface.

## Future Improvements

Potential extensions include:

- Imputing missing values instead of dropping rows.
- Using a preprocessing pipeline.
- Comparing multiple classification algorithms.
- Performing hyperparameter tuning.
- Adding confusion matrix, precision, recall, F1-score, and ROC-AUC.
- Applying cross-validation.
- Building an interactive prediction interface.
- Deploying the trained model as a web application or API.

## Conclusion

This project demonstrates an end-to-end introductory machine learning workflow for loan status classification. The supplied implementation performs data cleaning, categorical encoding, feature-target separation, train-test splitting, linear SVM training, and accuracy-based evaluation. The trained model achieved **83.33% accuracy on the test set** in the notebook.

## Author

**Satvik Shrivastav**

GitHub: https://github.com/SatvikShrivastav
