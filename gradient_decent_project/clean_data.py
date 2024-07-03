import numpy as np
import pandas as pd

train_csv_path = 'train_clean_data.csv'
test_csv_path = 'test_clean_data.csv'

train_data = pd.read_csv(train_csv_path)
test_data = pd.read_csv(test_csv_path)
print(len(train_data))
print(len(test_data))

# remove row with toán or vật lí is -1
train_data = train_data[(train_data['toán'] != -1) & (train_data['vật lí'] != -1) & (train_data['hóa học'] != -1)]
test_data = test_data[(test_data['toán'] != -1) & (test_data['vật lí'] != -1) & (test_data['hóa học'] != -1)]

print(len(train_data))
print(len(test_data))

# Save to csv
train_data.to_csv('train_clean_data_filter.csv', index=False)
test_data.to_csv('test_clean_data_filter.csv', index=False)
