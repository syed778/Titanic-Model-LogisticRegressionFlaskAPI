# Titanic Survival Prediction - Machine Learning Project

This project predicts whether a passenger survived the Titanic disaster using machine learning. It includes exploratory data analysis (EDA), model building, evaluation, and deployment using a Flask API.

---

## 📁 Project Structure

```
titanic-survival-prediction/
├── app.py                 # Flask API app
├── model.pkl              # (optional) Saved ML model (if applicable)
├── titanic_model.ipynb    # Jupyter Notebook for EDA, training, evaluation
├── requirements.txt       # Python dependencies
├── .gitignore             # Files to exclude from Git
└── README.md              # Project documentation
```

---

## ⚙️ Tech Stack

- **Python 3.8+**
- **Pandas, NumPy, Matplotlib, Seaborn**
- **scikit-learn**
- **Flask**
- **Postman** (for API testing)
- **Jupyter Notebook**

---

## 📊 Steps Covered

1. **Exploratory Data Analysis (EDA)**  
   - Missing values, distributions, correlation heatmaps, etc.

2. **Feature Engineering**  
   - One-hot encoding, handling missing values, feature selection.

3. **Model Building**  
   - Logistic Regression (can be replaced with Decision Tree, RandomForest, etc.)

4. **Model Evaluation**  
   - Accuracy, Confusion Matrix, Precision, Recall, F1 Score.

5. **Flask API Development**  
   - A simple `/predict` endpoint that accepts passenger data as JSON and returns survival prediction.

6. **Postman Testing**  
   - POST request to `/predict` with JSON payload.

---

## 🔧 How to Run

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Run Flask App

```bash
python app.py
```

By default, the app runs on: `http://127.0.0.1:5000/`

### Step 3: Test with Postman

- Method: `POST`
- URL: `http://127.0.0.1:5000/predict`
- Body (JSON):
```json
{
  "Pclass": 3,
  "Age": 22,
  "SibSp": 1,
  "Parch": 0,
  "Fare": 7.25,
  "Sex_male": 1,
  "Embarked_Q": 0,
  "Embarked_S": 1
}
```

---

## ✅ Output

```json
{
  "Survived": 0
}
```

---

## 📁 Dataset

- Source: [Kaggle - Titanic: Machine Learning from Disaster](https://www.kaggle.com/competitions/titanic)
- Data includes: Passenger demographics, ticket details, survival label.

---

## 🏁 Future Improvements

- Improve model accuracy with better features.
- Add input validation to the Flask API.
- Deploy model on cloud (Heroku, AWS, etc.)

---

## 📜 License

This project is open-source under the MIT License.
