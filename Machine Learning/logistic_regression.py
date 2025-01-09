import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Loan Approval Data (Income and Credit Score)

data = {
    'Income in $':[2000,2500,5000,3500,1800],
    'Credit Score':[750,650,800,700,600],
    'Loan Approval':[1,1,1,1,0]
}

# Convert a data into DataFrame
df = pd.DataFrame(data)

# Separate Features (Income and credit score) and Target(Loan Approval).
X=df[['Income in $','Credit Score']]
y=df[['Loan Approval']]

# Train-Test split (80% training and 20% testing data)
X_train , X_test , y_train , y_test = train_test_split(X,y,test_size=0.2,random_state=42)

# Logistic Regression Model
model = LogisticRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions using the model
y_pred = model.predict(X_test)


# Check the accuracy and confusion matrix of the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100} %')
