import pandas as pd

df = pd.read_csv('gdp.csv', encoding='ISO-8859-1')

states = ["Cal",'Tex','Flo','New']
population = [396, 297, 219, 192]
dict_states = {'States':states, 'Population':population}

df = pd.DataFrame(dict_states)

df.to_csv('../df.csv')

print(df)


# Ref : https://towardsdatascience.com/a-python-pandas-introduction-to-excel-users-1696d65604f6
# Issue Ref : https://stackoverflow.com/questions/43283202/permission-denied-when-pandas-dataframe-to-tempfile-csv


