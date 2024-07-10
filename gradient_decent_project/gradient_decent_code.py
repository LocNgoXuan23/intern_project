import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load train data
train_csv_path = 'train_clean_data_filter.csv'
data = pd.read_csv(train_csv_path)

# Filter columns
data = data[['toán', 'vật lí', 'hóa học']]

# Separate features and target variable
X = data[['toán', 'hóa học']].values  # Features: toán (math), hóa học (chemistry)
y = data['vật lí'].values  # Target: vật lí (physics)

# Create and train the model
model = LinearRegression()
model.fit(X, y)

# Predict
y_hat = model.predict(X)

# Evaluate the model
mse = mean_squared_error(y, y_hat)
print(f'Mean Squared Error: {mse}')
print(f'Coefficients: {model.coef_}')
print(f'Intercept: {model.intercept_}')

# ////////////////////////////////////////////////////////////////////
# Load Test data
test_csv_path = 'test_clean_data_filter.csv'
test_data = pd.read_csv(test_csv_path)

# Filter columns
test_data = test_data[['toán', 'vật lí', 'hóa học']]

# Separate features and target variable
X_test = test_data[['toán', 'hóa học']].values  # Features: toán (math), hóa học (chemistry)
y_test = test_data['vật lí'].values  # Target: vật lí (physics)

# Predict
y_hat_test = model.predict(X_test)

# Evaluate the model
mse_test = mean_squared_error(y_test, y_hat_test)
print(f'Mean Squared Error (Test): {mse_test}')
print(f'Coefficients: {model.coef_}')
print(f'Intercept: {model.intercept_}')
