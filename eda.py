import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#READ THE DATASET
credit_df = pd.read_csv("credit_prediction.csv")

# Info, shape, describe
print(f"Dataset informations:\n")
print(credit_df.info())
print(f"\nDataset shape:\n")
print(credit_df.shape) # We have 10^5 id
print(f"Dataset description:\n")
print(credit_df.describe())

# Verify we aren't aggregating duplicate rows
_ = credit_df.iloc[:,1:25].drop_duplicates()
print(_.shape)


print(f'Columns we are dealing with : \n {credit_df.columns}')

print(credit_df.isnull().sum()) # check for missing values


# Check for null values and replace them with 0
credit_df.isnull().sum()
for column in credit_df.columns:
    credit_df[column].fillna(credit_df[column].mode()[0], inplace=True)
credit_df.isnull().sum()

# Insight on Categorical variables
credit_df['Occupation'].value_counts()


