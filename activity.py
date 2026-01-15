# %%
#Path
print("/workspaces/daytwostuff")

#%% 
#Virtual environment
"""" You do not put the environment in the repo, you put the requirements.txt file in there "
and then people can download them into their own environment.
The path is still the same: /workspaces/daytwostuff"""

print("/workspaces/daytwostuff")

# %%
import pandas as pd
# Install dependencies as needed:
# pip install kagglehub[pandas-datasets]
import kagglehub
from kagglehub import KaggleDatasetAdapter

# Set the path to the file you'd like to load
file_path = "Apple.csv"

# Load the latest version
df = kagglehub.load_dataset(
  KaggleDatasetAdapter.PANDAS,
  "harshgupta4444/15-multinational-companies-stock-data-2025",
  file_path,
  # Provide any additional arguments like 
  # sql_query or pandas_kwargs. See the 
  # documenation for more information:
  # https://github.com/Kaggle/kagglehub/blob/main/README.md#kaggledatasetadapterpandas
)

print("First 5 records:", df.head())
df.head()
# %%
df.head()

# %%
# Advantages of Data Wrangler:
# Visualize & filter large tabular datasets
# Automatic Pandas code preview & export
#  One-click transforms (fill, drop, type-cast…)
