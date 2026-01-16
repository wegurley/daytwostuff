# %%
#Path
print("/workspaces/daytwostuff")

#%% 
#Virtual environment
# You do not put the environment in the repo, you put the requirements.txt file in there "
# and then people can download them into their own environment.
# The path is still the same: /workspaces/daytwostuff

print("/workspaces/daytwostuff")

#%% 
# Load data
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

df.head()

# %%
# Extension Menu
# I notice that the extension menu has 3 sections:
# 1. Local Extensions
# 2. Codespace Extensions
# 3. Recommended Extensions

#%%
# Data Wrangler Capabilities
# Some capabilities of Data Wrangler include:
# 1. Visualize & filter large tabular datasets
# 2. One-click transforms (fill, drop, type-cast…)
# 3. Automatic Pandas code preview & export

#%%
# Plotly version: 6.5.1
# terminal command to add plotly to requirements.txt:
# echo plotly==6.5.1 >> requirements.txt
# We use a requirements.txt file to manage dependencies
# in our virtual environment. It makes it easy to 
# share the environment with others.

#%%
#update requirements.txt file
# pip freeze > requirements.txt
# This command will overwrite the existing requirements.txt file
# with the current list of installed packages in your environment.

#%%
# Git Terminal Commands:
# git add .
# git commit -m "add python file, update requirements.txt"
# git push origin main

#%% 
# Recipe
# # 1. Create a new GitHub repository or fork an existing one
# 2. Create a new GitHub Codespace from the repository
# 3. Open the Codespace in local VS Code using the Codespaces extension

# 4. Open a terminal in VS Code
# 5. Create a virtual environment
#    python -m venv venv

# 6. Activate the virtual environment
#    source venv/bin/activate

# 7. Verify the environment is active (venv should appear in terminal path)

# 8. Install project dependencies
#    pip install -r requirements.txt

# 9. Verify installations
#    pip list

# 10. Begin development by creating or editing Python scripts
