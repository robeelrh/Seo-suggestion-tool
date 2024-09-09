import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import warnings


def load_data(file_path):
    """Load data from a CSV file."""
    return pd.read_csv(file_path)

def train_model(X_train, y_train):
    """Train a Random Forest classifier."""
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    """Evaluate the trained model."""
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    cm = confusion_matrix(y_test, predictions)
    print(f"Accuracy: {accuracy}")
    print("Confusion Matrix:")
    print(cm)

def predict_new_data(model, new_data):
    """Predict is_satisfied for new data."""
    predicted_is_satisfied = model.predict(new_data)
    return predicted_is_satisfied

def append_to_csv(file_path, breadcrumb, is_satisfied):
    """Append new data to the CSV file."""
    breadcrumb = 1 if breadcrumb else 0
    is_satisfied = 1 if is_satisfied else 0
    new_row = {
        "breadcrumb": breadcrumb,
        "is_satisfied": is_satisfied,
    }
    df = pd.DataFrame([new_row])
    df.to_csv(file_path, mode='a', header=False, index=False)


def main(breadcrumb, is_satisfied):
    warnings.filterwarnings("ignore", message="X does not have valid feature names, but LinearRegression was fitted with feature names")
    
    file_path = os.getcwd() + '/../playwright/suggestions/breadcrumb/data.csv'
    train_df = load_data(file_path)
    
    X_train = train_df[['breadcrumb']]
    y_train = train_df['is_satisfied']
    
    X_train_split, X_test_split, y_train_split, y_test_split = train_test_split(X_train, y_train, test_size=0.2, random_state=42)
    
    model = train_model(X_train_split, y_train_split)
    
    test_df = pd.DataFrame({
        "breadcrumb": [breadcrumb],
        "is_satisfied": [is_satisfied]
    })
    
    X_new = test_df[['breadcrumb']]
    y_new = test_df['is_satisfied']
    
    predicted_is_satisfied = predict_new_data(model, X_new)
    
    for pred, actual in zip(predicted_is_satisfied, y_new):
        if not pred:
            result = "The HTML should contain breadcrumb structured data found in the HTML"
        else:
            result = "The HTML already contains breadcrumb structured data."
        
        append_to_csv(file_path, breadcrumb, is_satisfied)
        
        return result
        
if __name__ == "__main__":
    print(main(1, 1))
