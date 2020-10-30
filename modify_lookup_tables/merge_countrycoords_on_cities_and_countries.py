import pandas as pd

# load table countrycode - countrycoords and preprocess
df_co_from_cc = pd.read_csv('../data/location_ref/councode_councood.csv')

# reame columns
df_co_from_cc = df_co_from_cc.rename({'alpha2Code': 'COUNTRY_ALPHA2_CODE'}, axis='columns')
df_co_from_cc['countryCoords'] = df_co_from_cc['countryCoords'].replace("Point\(", "", regex=True).replace(" ", ", ", regex=True).replace("\)", "", regex=True)

# converting to string series
df_co_from_cc['countryCoords'] = df_co_from_cc['countryCoords'].astype(str)

# splitting at occurrence of whitespace
df_co_from_cc['countryCoords'] = df_co_from_cc['countryCoords'].str.split(",", 1)

# displaying second element from list
df_co_from_cc['country_lat_3857'] = df_co_from_cc['countryCoords'].str.get(1)

# displaying first element from list
df_co_from_cc['country_long_3857'] = df_co_from_cc['countryCoords'].str.get(0)


df_co_from_cc['country_lat_long_3857'] = df_co_from_cc['country_lat_3857'] + "," + df_co_from_cc['country_long_3857']

df_co_from_cc['country_lat_long_3857'] = df_co_from_cc['country_lat_long_3857'].replace(" ", "", regex=True)


df_co_from_cc = df_co_from_cc.drop(columns=['countryCoords', 'country'])

print(df_co_from_cc.head(), df_co_from_cc.shape)


# load table country names multilingual - country name - country code

df_c_multilingu = pd.read_csv('../data/location_ref/IP2LOCATION-COUNTRY-MULTILINGUAL.CSV')
df_c_multilingu = df_c_multilingu.drop(columns=['COUNTRY_ALPHA3_CODE', 'COUNTRY_NUMERIC_CODE'])
# make COUNTRY_NAME lowercase
df_c_multilingu['COUNTRY_NAME'] = df_c_multilingu['COUNTRY_NAME'].str.lower()
df_c_multilingu['LANG'] = df_c_multilingu['LANG'].str.lower()

print(df_c_multilingu.head())

# drop: re, man
print(df_c_multilingu[df_c_multilingu['COUNTRY_NAME'] == 'man'])
# yt, re, man, mf
# nga = russia
df_c_multilingu = df_c_multilingu.drop(index=[13051, 13798, 14047, 19609, 19667, 19562])

# merge these 2
df_c = df_c_multilingu.merge(df_co_from_cc, how='left', on='COUNTRY_ALPHA2_CODE', suffixes=(False, False))

# check number of countries
print(df_c['country_lat_long_3857'].nunique())
print('english country_names ', df_c.loc[df_c['LANG'] == 'en'].shape)

# df_c = df_c[~df_c['COUNTRY_NAME'].duplicated()] do not appy removal of duplicates!

# change some of the countrynames to the usually used abbrevations

df_country = df_c

df_country['COUNTRY_NAME'] = df_country['COUNTRY_NAME'].replace('united kingdom of great britain and northern ireland', 'united kingdom')
df_country['COUNTRY_NAME'] = df_country['COUNTRY_NAME'].replace('united states of america', 'united states')
df_country['COUNTRY_NAME'] = df_country['COUNTRY_NAME'].replace('vereinigte staaten von amerika', 'USA')
df_country['COUNTRY_NAME'] = df_country['COUNTRY_NAME'].replace('vereinigtes königreich großbritannien und nordirland', 'großbritannien')

UK_row = df_country[(df_country['COUNTRY_ALPHA2_CODE'] == 'GB') & (df_country['LANG'] == 'en')]
UK_row['COUNTRY_NAME'] = UK_row['COUNTRY_NAME'].replace('united kingdom', 'UK')

US_row = df_country[(df_country['COUNTRY_ALPHA2_CODE'] == 'US') & (df_country['LANG'] == 'en')]
US_row['COUNTRY_NAME'] = US_row['COUNTRY_NAME'].replace('united states', 'US')

US_row2 = df_country[(df_country['COUNTRY_ALPHA2_CODE'] == 'US') & (df_country['LANG'] == 'en')]
US_row2['COUNTRY_NAME'] = US_row2['COUNTRY_NAME'].replace('united states', 'USA')

df_country2 = df_country.append([UK_row, US_row, US_row2])
print(df_country2.head)
#df_country2 = df_country2.drop(columns='level_0')

print('test', df_country2[(df_country2['COUNTRY_ALPHA2_CODE'] == 'GB') & (df_country2['LANG'] == 'de')])

df_country2.to_csv('../data/location_ref/country_multilingu_countrycode_countrycoord.csv')


# import cityname multilingu
df_d = pd.read_csv('../data/location_ref/citynamemulti_councode_cityco_citypop.csv',
                   dtype={'cityCoords': str}, index_col=0)


print(df_d.head())
df_e = df_d.merge(df_co_from_cc, how='left', on='COUNTRY_ALPHA2_CODE', suffixes=(False, False))

# reorder cols
# cols = list(df_e.columns.values)
col_order = ['language',
             'CITY_NAME',
             'city_lat_3857',
             'city_long_3857',
             'city_lat_long_3857',
             'population',
             'COUNTRY_ALPHA2_CODE',
             'country_lat_3857',
             'country_long_3857',
             'country_lat_long_3857']

df_e = df_e[col_order]

# make city_name lowercase
df_e['CITY_NAME'] = df_e['CITY_NAME'].str.lower()

print(df_e.shape)
df_e.to_csv('../data/location_ref/city_multilingu_citycoord_countrycode_countrycoord.csv')
