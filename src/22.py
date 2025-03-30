import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load the dataset
data = pd.read_csv('path_to_your_dataset.csv')

# Split the data into features and target variable
X = data.drop('target_column', axis=1)
y = data['target_column']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a logistic regression model
model = LogisticRegression(max_iter=10000)

# Train the model on the training data
model.fit(X_train, y_train)

# Make predictions on the testing set
predictions = model.predict(X_test)
