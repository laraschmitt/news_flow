import pandas as pd

# load lookup tables
df = pd.read_csv('../data/location_ref/IP2LOCATION-COUNTRY-MULTILINGUAL.csv')
df = df[df['LANG_NAME'] == 'ENGLISH']
df['COUNTRY_NAME'] = df['COUNTRY_NAME'].str.lower()

# add shortcut names for UK and US
df['COUNTRY_NAME'] = df['COUNTRY_NAME'].replace('united kingdom of great britain and northern ireland', 'united kingdom')
df['COUNTRY_NAME'] = df['COUNTRY_NAME'].replace('united states of america', 'united states')

UK_row = df[(df['COUNTRY_ALPHA2_CODE'] == 'GB') & (df['LANG'] == 'EN')]
UK_row['COUNTRY_NAME'] = UK_row['COUNTRY_NAME'].replace('united kingdom', 'UK')

US_row = df[(df['COUNTRY_ALPHA2_CODE'] == 'US') & (df['LANG'] == 'EN')]
US_row['COUNTRY_NAME'] = US_row['COUNTRY_NAME'].replace('united states', 'US')

US_row2 = df[(df['COUNTRY_ALPHA2_CODE'] == 'US') & (df['LANG'] == 'EN')]
US_row2['COUNTRY_NAME'] = US_row2['COUNTRY_NAME'].replace('united states', 'USA')

df2 = df.append([UK_row, US_row, US_row2])
df2.reset_index(inplace=True)

df2.to_csv('../data/location_ref/countrycode_countryname_en.csv')
