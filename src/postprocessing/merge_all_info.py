import pandas as pd

df = pd.read_csv('../../data/Processed/joined_data/merged_table.csv')
df_cat = pd.read_csv('../../data/Processed/joined_data/labeled_cat.csv')

#rename columns in df_cat that has label in the name, add _cat at the end
df_cat = df_cat.rename(columns=lambda x: x + '_cat' if 'label' in x else x)


# merge the two dataframes on district_code and neighborhood_code
df_merged = pd.merge(df, df_cat, on=['district_code', 'neighbourhood_code'])

#drop the columns district_code, neighborhood_code, district_name_y, neighborhood_name_y
df_merged = df_merged.drop(['district_name_y', 'neighbourhood_name_y'], axis=1)

# save the merged dataframe
df_merged.to_csv('../../data/Processed/joined_data/final_table_all_info.csv', index=False)
