# Wine Classification with XGBoost - Docker Lab

## Overview
This project demonstrates containerized machine learning using Docker. It trains an XGBoost classifier on the Wine dataset to predict wine types based on chemical features.

## Modifications from Original Lab
- **Dataset**: Changed from Iris to Wine dataset (3 wine types, 13 features)
- **Model**: Upgraded from Random Forest to XGBoost classifier
- **Evaluation**: Added detailed metrics including classification report and confusion matrix
- **Python Version**: Updated to Python 3.11

## Project Structure
```
.
├── src/
│   ├── main.py
│   └── requirements.txt
├── Dockerfile
└── README.md
```

## How to Run

### Build the Docker image:
```bash
docker build -t wine-classifier:v1 .
```

### Run the container:
```bash
docker run wine-classifier:v1
```

### (Optional) Save the image:
```bash
docker save wine-classifier:v1 > wine_classifier_image.tar
```

## Expected Output
The container will train the model and display:
- Model accuracy score
- Classification report with precision, recall, F1-score
- Confusion matrix
- Success message

## Author
Swetha - Northeastern University MLOps Course
```

---

### **Step 4: Your Final Structure Should Look Like:**
```
mlops-docker-wine-classifier/
├── src/
│   ├── main.py
│   └── requirements.txt
├── Dockerfile
└── README.md