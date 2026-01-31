# Wine Classification with XGBoost - MLOps Docker Lab

## Project Overview
This project demonstrates containerized machine learning using Docker. It trains an XGBoost classifier to predict wine types based on chemical composition features from the UCI Wine dataset.

## Author
**Swetha Ganesh**  
Master's in Data Analytics Engineering  
Northeastern University

## Modifications from Original Lab

This project is a modified version of the original Docker Lab. The following changes were implemented:

### 1. Dataset Change
- **Original**: Iris flower dataset (150 samples, 4 features, 3 classes)
- **Modified**: Wine dataset (178 samples, 13 features, 3 wine types)
- **Reasoning**: Wine dataset provides more complex feature relationships and better demonstrates real-world classification tasks

### 2. Model Upgrade
- **Original**: Random Forest Classifier
- **Modified**: XGBoost Classifier with custom hyperparameters
  - `n_estimators=100`
  - `learning_rate=0.1`
  - `max_depth=5`
- **Reasoning**: XGBoost is an industry-standard gradient boosting algorithm that often outperforms traditional Random Forest models

### 3. Enhanced Evaluation Metrics
- **Original**: Simple print statement
- **Modified**: Comprehensive evaluation including:
  - Accuracy score
  - Classification report (precision, recall, F1-score for each class)
  - Confusion matrix
- **Reasoning**: Provides deeper insight into model performance across all wine classes

### 4. Python Version Update
- **Original**: Python 3.10
- **Modified**: Python 3.11
- **Reasoning**: Latest stable Python version with performance improvements

## Project Structure
```
mlops-docker-wine-classifier/
├── src/
│   ├── main.py              # Modified ML training script
│   └── requirements.txt     # Updated dependencies
├── Dockerfile               # Container configuration
├── .gitignore              # Ignore large files
└── README.md               # Project documentation
```

## Technologies Used
- **Docker**: Containerization platform
- **Python 3.11**: Programming language
- **XGBoost**: Gradient boosting framework
- **Scikit-learn**: Machine learning library
- **NumPy**: Numerical computing

## Dataset Information
The Wine dataset contains 13 chemical features:
- Alcohol, Malic acid, Ash, Alkalinity of ash
- Magnesium, Total phenols, Flavanoids, Nonflavanoid phenols
- Proanthocyanins, Color intensity, Hue, OD280/OD315, Proline

**Target**: 3 wine cultivars (class 0, 1, 2)

## How to Run

### Prerequisites
- Docker Desktop installed and running
- Terminal/Command Prompt access

### Step 1: Clone the Repository
```bash
git clone https://github.com/Swethaganesh10/mlops-docker-wine-classifier.git
cd mlops-docker-wine-classifier
```

### Step 2: Build the Docker Image
```bash
docker build -t wine-classifier:v1 .
```

### Step 3: Run the Container
```bash
docker run wine-classifier:v1
```

### Optional: Save the Docker Image
```bash
docker save wine-classifier:v1 > wine_classifier_image.tar
```

## Expected Output
```
Model Accuracy: 0.9722

Classification Report:
              precision    recall  f1-score   support

     class_0       1.00      1.00      1.00        14
     class_1       0.93      1.00      0.97        14
     class_2       1.00      0.88      0.93         8

    accuracy                           0.97        36
   macro avg       0.98      0.96      0.97        36
weighted avg       0.97      0.97      0.97        36

Confusion Matrix:
[[14  0  0]
 [ 0 14  0]
 [ 0  1  7]]

The model training was successful!
```

## Model Performance
- **Accuracy**: 97.22%
- **Precision**: 97-100% across all classes
- **Recall**: 88-100% across all classes

The model demonstrates excellent performance in classifying all three wine types with minimal misclassification.

## Key Learnings
1. **Docker containerization** ensures consistent execution across different environments
2. **XGBoost** provides robust performance for multi-class classification
3. **Comprehensive evaluation metrics** are essential for understanding model behavior
4. **Version control** and documentation are critical for reproducible ML workflows

## Future Enhancements
- Add cross-validation for more robust evaluation
- Implement hyperparameter tuning (GridSearchCV)
- Add model versioning and experiment tracking (MLflow)
- Deploy as REST API using Flask
- Add data visualization (feature importance plots)

## Course Information
**Course**: MLOps  
**Institution**: Northeastern University  
**Assignment**: Lab Assignment 1 - Docker Labs  


