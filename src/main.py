# Import necessary libraries
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib
import numpy as np

if __name__ == '__main__':
    # Load the Wine dataset
    wine = load_wine()
    X, y = wine.data, wine.target
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Train an XGBoost classifier
    model = XGBClassifier(
        n_estimators=100, 
        random_state=42,
        learning_rate=0.1,
        max_depth=5
    )
    model.fit(X_train, y_train)
    
    # Make predictions and evaluate
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"Model Accuracy: {accuracy:.4f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, target_names=wine.target_names))
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    
    # Save the model to a file
    joblib.dump(model, 'wine_classifier_model.pkl')
    
    print("\nThe model training was successful!")
