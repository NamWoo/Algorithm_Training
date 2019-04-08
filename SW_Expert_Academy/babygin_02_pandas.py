

import pandas as pd

inputt = 312231
input = list(str(inputt))

t1 = pd.Series(input).sort_values()

print(t1)

print(t1.value_counts())

print('')


if t1.value_counts().sum() >2:

    print(t1.value_counts().sum())


