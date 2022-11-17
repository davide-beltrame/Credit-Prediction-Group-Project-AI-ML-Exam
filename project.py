import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns

# Explanatory data analysis
credit_df = pd.read_csv('credit_prediction.csv')
# Info, shape, describe
print(f"Dataset informations:\n")
print(credit_df.info())
print(f"\nDataset shape:\n")
print(credit_df.shape) # We have 10^5 id
print(f"Dataset description:\n")
print(credit_df.describe())
# We can see from the description that our customers have
# age between 10 and 40 yeas old and a salary
# contained in (303.000 and 15204.000 $) thus we have customers with very
# diverse portfolio
#Verify we aren't aggregating duplicate rows
_ = credit_df.iloc[:,1:25].drop_duplicates()
print(_.shape) # Every row (excluding id) of our dataset is different,
# thus no duplicate are present

print(f'Columns we are dealing with : \n {credit_df.columns}')

print(credit_df.isnull().sum()) # check for missing values

# DATA VISUALIZATION

sns.countplot(x = credit_df['Occupation'], palette="mako")
plt.xticks(rotation=90);
plt.show()

sns.countplot(x = credit_df['Credit_Score'],palette="mako")
plt.xticks(rotation=45)
plt.show() #Lots of customers have Standart Score

sns.histplot(x = credit_df['Annual_Income'])
plt.show()
