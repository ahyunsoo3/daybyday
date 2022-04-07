import pandas as pd

data = [[1,4], [2,5], [3,6]]

df = pd.DataFrame(data, index=['row1','row2','ro3'],
                  columns=['col1','col2'])

print(df)


# https://towardsdatascience.com/a-python-pandas-introduction-to-excel-users-1696d65604f6