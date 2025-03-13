import pandas as pd




df_match = pd.read_csv("match_data.csv")
print(df_match.head())

df_info = pd.read_csv("match_info_data.csv")
print(df_info.head())

# Missing values count for each column
print(df_match.isnull().sum())
print(df_info.isnull().sum())

# Fill missing value with 'unknown'
print(df_match.fillna('unknown',inplace=True))

# check for duplicate value
print(df_match.duplicated().sum())
print(df_info.duplicated().sum())

# Removing the duplicates value


df_match = df_match.drop_duplicates()  # ✅ Duplicate rows remove ho jayengi

# Check karne ke liye print karo

df_match = df_match.drop_duplicates()
print(f"Duplicates removed. New shape: {df_match.shape}")

df_info = df_info.drop_duplicates()
print(f"Duplicates removed. New shape: {df_info.shape}")





