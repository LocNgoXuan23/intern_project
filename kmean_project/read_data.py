import numpy as np
import pandas as pd

csv_path = 'train_clean_data.csv'
data = pd.read_csv(csv_path)

# filter cols = [toán, vật lí]
data = data[['toán', 'vật lí']]

# convert to numpy 
data = data.to_numpy()

# convert to list 2D
data = data.tolist()
print(data)