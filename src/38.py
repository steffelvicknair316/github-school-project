import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Assuming 'features' and 'labels' are already defined and have the appropriate shapes.
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2)

model = LogisticRegression()
model.fit(X_train, y_train)
