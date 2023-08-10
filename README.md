# Predicting Water Quality: A Machine Learning Approach

### Introduction
Water is a fundamental necessity of life. However, the quality of water we consume can significantly impact our health. This project uses machine learning to predict whether water is drinkable based on various quality parameters.

SOURCE: https://www.kaggle.com/datasets/adityakadiwal/water-potability

### Dataset 
Feature Descrription:

1. ph: pH of 1. water (0 to 14).
2. Hardness: Capacity of water to precipitate soap in mg/L.
3. Solids: Total dissolved solids in ppm.
4. Chloramines: Amount of Chloramines in ppm.
5. Sulfate: Amount of Sulfates dissolved in mg/L.
6. Conductivity: Electrical conductivity of water in μS/cm.
7. Organic_carbon: Amount of organic carbon in ppm.
8. Trihalomethanes: Amount of Trihalomethanes in μg/L.
9. Turbidity: Measure of light emiting property of water in NTU.

Target Variable:

10. Potability: Indicates if water is safe for human consumption. Potable - 1 and Not potable - 0

# Project Structure

# 1.Exploratory Data Analysis (EDA)
- No significant outliers
- Feature distribution: There is no significant difference between means.
- The correlation between all features is small.

# 2. Preprocessing
Handling Missing Values:
1. Dropped missing value (39% of the dataset)
2. KNNImputer

Feature scaling and transformation:
1. StandardScaler
2. MinMaxScaler
3. PCA
4. TSNE

Adressing class imbalance:
1. Upsampling
2. Upsampling + SMOTE (Best Method for my dataset)

# 3. Model Building:
6 different models were applied
Model Selection --> Random Forest Classifier was the best performing model
('Logistic Regression': 0.5292899408284024, 
 'Random Forest Classifier': 0.9674556213017752,
 'KNN': 0.7775147928994084, 
 'AdaBoostClassifier': 0.6434911242603552, 
 'GradientBoostingClassifier': 0.7739644970414201)
Model Training --> Tuned the parameters for Random Forest Classifier and found the best parameters.

# 4. Model Evaluation
Evaluation Metrics:
- Accuracy
- Precision
- Recall
- Fi-Score
- Kappa

# 5. Feature Importance Analysis
Found which features were more important for different models.
Feature Importance Rank for the best performing model:
[(0.17106501462431903, 'ph'),
 (0.1455160095185526, 'Sulfate'),
 (0.12089342693258448, 'Chloramines'),
 (0.12070560045156185, 'Solids'),
 (0.11051370215344977, 'Hardness'),
 (0.09453636263914919, 'Turbidity'),
 (0.08501361575277308, 'Trihalomethanes'),
 (0.07657834747858894, 'Organic_carbon'),
 (0.07517792044902104, 'Conductivity')]
 
# Conclusions
The best performing model:
Upsampling + SMOTE --> StandardScaler --> Random Forest Classifier --> Kappa = 0.87
