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

def append_to_csv(file_path, no_of_links, size, is_satisfied):
    """Append new data to the CSV file."""
    is_satisfied =  1 if is_satisfied else 0
    
    new_row = {
        "no_of_links": no_of_links,
        "size":size,
        "is_satisfied": is_satisfied,
    }
    df = pd.DataFrame([new_row])
    df.to_csv(file_path, mode='a', header=False, index=False)



def main(no_of_links,size, is_satisfied):
    warnings.filterwarnings("ignore", message="X does not have valid feature names, but LinearRegression was fitted with feature names")
    
    file_path = os.getcwd() + '/..' + '/playwright'+ '/suggestions'+'/site_map_size'+ '/data.csv'
    train_df = load_data(file_path)

    
    X_train = train_df[['no_of_links', 'size']]
    y_train = train_df['is_satisfied']
    
    X_train_split, X_test_split, y_train_split, y_test_split = train_test_split(X_train, y_train, test_size=0.2, random_state=42)
    
    model = train_model(X_train_split, y_train_split)
    
    # Evaluate the model on the testing set
    # print("Evaluation on testing set:")
    # evaluate_model(model, X_test_split, y_test_split)
    
    test_df = pd.DataFrame({
        "no_of_links": [no_of_links],
        "size":[size],
        "is_satisfied":[is_satisfied]
    })
    
    X_new = test_df[['no_of_links','size']]
    y_new = test_df['is_satisfied']
    
    # Make predictions on the new data
    # print("\nPredictions on new data:")
    predicted_is_satisfied = predict_new_data(model, X_new)
    
    for pred, actual, fields in zip(predicted_is_satisfied, y_new, X_new.itertuples()):
        # print(f"Predicted is_satisfied: {pred}, Actual is_satisfied: {actual}")
        if not pred:
            response = "The content of the webpage is not satisfactory."
            if fields.no_of_links > 40000:
                response += " Number of links should be less then 40000."
            if fields.size > 40000000:
                response += " The size of content should be less then 40000000."
            result = response
        else:
            result = "The content on webpage is satisfied."
    
        append_to_csv(file_path, no_of_links, size, is_satisfied)

        return result
        
if __name__ == "__main__":
    print(main(39912,40000090,0))
