import pandas as pd
from sklearn.model_selection import train_test_split

csv_path = 'clean_data.csv'
data = pd.read_csv(csv_path)
print(data.shape)

# Split data into training and testing sets
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)
print(train_data.shape)
print(test_data.shape)

# Save the training and testing data to CSV
train_data.to_csv('train_clean_data.csv', index=False)
test_data.to_csv('test_clean_data.csv', index=False)
