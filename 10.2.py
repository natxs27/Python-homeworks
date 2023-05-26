import pandas as pd
import numpy as np

# Get the current date
current_date = pd.Timestamp.now().floor('D')

# Create the index containing days of the current month
start_date = current_date.replace(day=1)
end_date = current_date.replace(day=pd.Timestamp(current_date.year, current_date.month + 1, 1).day) - pd.DateOffset(days=1)
index = pd.date_range(start_date, end_date, freq='D')

# Create some sample data (temperatures at noon)
data = np.random.randint(20, 30, size=len(index))

# Create the pandas Series
series = pd.Series(data, index)

# Print the series
print(series)
