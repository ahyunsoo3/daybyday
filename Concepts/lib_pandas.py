import pandas as pd
import numpy as np

s = pd.Series([1, 3, 5, np.nan, 6, 8])

dates = pd.date_range("20220101", periods=2)

df = pd.DataFrame(np.random.randn(2, 3), index=dates, columns=list("ABA"))

print(df)



# Ref : https://pandas.pydata.org/docs/user_guide/10min.html