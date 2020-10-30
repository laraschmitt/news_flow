import pandas as pd

df_city = pd.read_csv(
    '../data/location_ref/city_multilingu_citycoord_countrycode_countrycoord.csv',
    index_col=0)

# check number of cities
print('unique citycoords: ', df_city['city_lat_long_3857'].nunique())

print(df_city.loc[df_city['CITY_NAME'] == 'berlin'])  # not listed in english

# get english citynames - citycoords df
df_city_en = df_city[df_city['language'] == 'en']
df_city_en = df_city_en[['CITY_NAME', 'city_lat_long_3857']]
df_city_en = df_city_en.reset_index(drop=True)

# test
print(df_city_en.loc[df_city_en['CITY_NAME'] == 'new york city']['CITY_NAME'].values[0])

# write to disk
df_city_en.to_csv('../data/location_ref/citycoords_citynames_en.csv')
