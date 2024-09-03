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



def main(favicon, is_satisfied):
    warnings.filterwarnings("ignore", message="X does not have valid feature names, but LinearRegression was fitted with feature names")
    
    train_df = load_data(os.getcwd() + '/..' + '/playwright'+ '/suggestions'+'/favicon'+ '/data.csv')
    
    X_train = train_df[['favicon']]
    y_train = train_df['is_satisfied']
    
    X_train_split, X_test_split, y_train_split, y_test_split = train_test_split(X_train, y_train, test_size=0.2, random_state=42)
    
    model = train_model(X_train_split, y_train_split)
    
    # Evaluate the model on the testing set
    # print("Evaluation on testing set:")
    # evaluate_model(model, X_test_split, y_test_split)
    
    # Load new data for testing
    test_df = pd.DataFrame({
        "favicon":[favicon],
        "is_satisfied":[is_satisfied]
    })
    
    X_new = test_df[['favicon']]
    y_new = test_df['is_satisfied']
    
    # Make predictions on the new data
    # print("\nPredictions on new data:")
    predicted_is_satisfied = predict_new_data(model, X_new)
    
    for pred, actual in zip(predicted_is_satisfied, y_new):
        # print(f"Predicted is_satisfied: {pred}, Actual is_satisfied: {actual}")
        if not pred:
            return "The favicon should be present in web-page"
        else:
            return "The favicon is present in web-page"
        
if __name__ == "__main__":
    print(main(1, 1))
