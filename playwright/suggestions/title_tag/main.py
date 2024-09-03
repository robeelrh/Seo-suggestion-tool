import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import warnings
import os

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

def main(title_length,is_satisfied):

    train_df = load_data(os.getcwd() + '/..' + '/playwright'+ '/suggestions'+'/title_tag'+ '/data.csv')
 
    
    X_train = train_df[['title_length']]
    y_train = train_df['is_satisfied']
    
    X_train_split, X_test_split, y_train_split, y_test_split = train_test_split(X_train, y_train, test_size=0.2, random_state=42)
    
    model = train_model(X_train_split, y_train_split)
    
    #Evaluate the model on the testing set
    # print("Evaluation on testing set:")
    # evaluate_model(model, X_test_split, y_test_split)
    
    test_df = pd.DataFrame({
        "title_length": [title_length],
        "is_satisfied":[is_satisfied]
    })
    
    X_new = test_df[['title_length']]
    y_new = test_df['is_satisfied']
    
    # Make predictions on the new data
    #print("\nPredictions on new data:")
    predicted_is_satisfied = predict_new_data(model, X_new)
    
    for pred, title_len, actual in zip(predicted_is_satisfied, X_new['title_length'], y_new):
        if predicted_is_satisfied == 0:
            response = "The title tag length is not satisfactory."
            if title_length < 50:
                response += " Increase the title length to atleast 50 characters to improve satisfaction."
            elif title_length > 70:
                response += " Decrease the title length to 70 characters to improve satisfaction."
            else:
                response += "Try adjusting the title length to improve satisfaction within the range of 50 to 70 characters."
            return response
        else:
            return  "The title tag length is satisfactory."


if __name__ == "__main__":
    print(main(51,1))