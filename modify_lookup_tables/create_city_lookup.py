import pandas as pd

# load in cityname citycoord csv
df1 = pd.read_csv('../data/location_ref/citynamemulti_councode_cityco.csv')
df1 = df1.drop(columns=['city', 'country'])

print(df1.shape, df1['cityCoords'].nunique())

# load in city population csv
df2 = pd.read_csv('../data/location_ref/cityco_citypop.csv')
df2 = df2.drop(columns=['city', 'cityLabel'])
df2 = df2.drop_duplicates()  # remove duplicates

df_co = pd.DataFrame(df1['cityCoords'].unique())
df_co = df_co.rename(columns={0: 'cityCoords'})

# merge dfs t
df3 = df2.merge(df_co, how='inner', on='cityCoords', suffixes=(False, False))
ll = df3['cityCoords'].to_list()
print(len(ll))

# find cities
inverse_boolean_series = ~(df2.cityCoords).isin(df3.cityCoords)
inverse_filtered_df = df2.cityCoords[inverse_boolean_series]
inverse_filtered_df.shape

# remove all the city coordinates that do not appear in the other lis
df6 = df3[df3['cityCoords'].isin(ll)]

df1 = df1[df1['cityCoords'].isin(ll)]
print(df1['cityCoords'].nunique())  # left 28046 right 21859

# merge
df = df1.merge(df6, how='right', on='cityCoords', suffixes=(False, False))
print(df.shape)
print(df.head())

# final clean up steps
# remove duplicates cityLabel entries
df_dup_free = df[~df['cityLabel'].duplicated()]
print(df_dup_free.shape)

# pop column
# remove non numerical characters
df_dup_free['population'] = df_dup_free['population'].str.replace(r'[a-zA-Z]', '').astype('float')

# kick out small cities (pop size < 900000)
df_dup_free = df_dup_free[df_dup_free['population'] >= 900000]
print(df_dup_free.shape)

# reorder cols
# reame columns
df_d = df_dup_free.rename({'alpha2Code': 'COUNTRY_ALPHA2_CODE',
                           'cityLabel': 'CITY_NAME',
                           'cityCoords': 'city_long_lat_3857'}, axis='columns')


# create coordinates col
df_d['city_long_lat_3857'] = df_d['city_long_lat_3857'].replace("Point\(", "", regex=True).replace(" ", ", ", regex=True).replace("\)", "", regex=True)

#df_d['city_long_lat_3857'] = df_d['city_long_lat_3857'].apply(lambda x:pd.Series(x.split()[::-1]))


# converting to string series
df_d['city_long_lat_3857'] = df_d['city_long_lat_3857'].astype(str)

# splitting at occurrence of whitespace
df_d['city_long_lat_3857'] = df_d['city_long_lat_3857'].str.split(",", 1)

# displaying second element from list
df_d['city_lat_3857'] = df_d['city_long_lat_3857'].str.get(1)

# displaying first element from list
df_d['city_long_3857'] = df_d['city_long_lat_3857'].str.get(0)

df_d['city_lat_long_3857'] = df_d['city_lat_3857'] + ", " + df_d['city_long_3857']
df_d = df_d.drop(columns='city_long_lat_3857')

print(df_d.head())

# export to disk
df_d.to_csv('../data/location_ref/citynamemulti_councode_cityco_citypop.csv')
