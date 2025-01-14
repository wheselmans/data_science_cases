import os
import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi
import pandas as pd
import sqlite3

# Load environment variables from the .env file
# load_dotenv()
#%%
# Get your Kaggle API credentials and use them to retrieve the dataset.
# https://github.com/Kaggle/kaggle-api/
api = KaggleApi()
api.authenticate()
# Download the dataset from Kaggle
kaggle.api.dataset_download_files('usdot/flight-delays', path='.', unzip=True)


# Load the dataset into a pandas DataFrame
df = pd.read_csv('flights.csv')
# Load additional datasets into pandas DataFrames
df_airlines = pd.read_csv('airlines.csv')
df_airports = pd.read_csv('airports.csv')