import pandas as pd
import numpy as np

s = pd.Series([1, 3, 5, np.nan, 6, 8])

dates = pd.date_range("20220101", periods=2)

df = pd.DataFrame(np.random.randn(2, 3), index=dates, columns=list("ABA"))

df2 = pd.DataFrame(
    {
        'A': 1.0,
        'B': pd.Timestamp('20220101'),
        'C': pd.Series(1, index=list(range(4)), dtype='float')

    }
)

print(df2)
print(df2.dtypes)



# Ref : https://pandas.pydata.org/docs/user_guide/10min.html