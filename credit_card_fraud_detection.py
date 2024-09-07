import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Load the data
data = pd.read_csv("C:/Users/prata/OneDrive/Documents/fraudTrain.csv")

# Display basic info
print(data.info())

# Check for null values
print(data.isnull().sum())

# Check for class distribution
print(data['is_fraud'].value_counts())

# Separate data for analysis
normal = data[data.is_fraud == 0]
fraud = data[data.is_fraud == 1]
print("Normal transactions shape:", normal.shape)
print("Fraud transactions shape:", fraud.shape)

# Statistical analysis
print("Normal transactions amount statistics:")
print(normal.amt.describe())
print("Fraud transactions amount statistics:")
print(fraud.amt.describe())

# Create a new sample containing both normal and fraud transactions
normal_sample = normal.sample(n=7506, random_state=1)
new_data = pd.concat([normal_sample, fraud], axis=0)
print("New data shape:", new_data.shape)

# Check class distribution in new data
print(new_data['is_fraud'].value_counts())

# Drop non-numeric columns that are not useful for the model
new_data = new_data.drop(columns=['trans_date_trans_time'], axis=1)

# Convert date columns to datetime and then extract features
new_data['dob'] = pd.to_datetime(new_data['dob'], errors='coerce')
new_data['dob_year'] = new_data['dob'].dt.year
new_data['dob_month'] = new_data['dob'].dt.month
new_data['dob_day'] = new_data['dob'].dt.day
new_data = new_data.drop(columns=['dob'], axis=1)
new_data = new_data.drop(columns=['trans_num'], axis=1)

# Convert categorical columns to numeric using Label Encoding
categorical_columns = ['merchant', 'category', 'first', 'last', 'gender','street', 'city', 'state', 'job']
for col in categorical_columns:
    le = LabelEncoder()
    new_data[col] = le.fit_transform(new_data[col])

# Define feature matrix X and target vector y
X = new_data.drop(columns=['is_fraud'])
y = new_data['is_fraud']

# Check data types and contents
print(X.info())

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, stratify=y, random_state=3)
print("Training set shape:", X_train.shape)
print("Testing set shape:", X_test.shape)

# Standardize the feature matrix
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Model training (Logistic Regression)
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions and evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Model accuracy:", accuracy)
