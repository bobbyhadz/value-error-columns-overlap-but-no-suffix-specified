# ValueError: columns overlap but no suffix specified

import pandas as pd

df1 = pd.DataFrame({
    'name': ['Alice', 'Bobby', 'Carl', 'Dan'],
    'experience': [1, 3, 5, 7],
    'salary': [175.1, 180.2, 190.3, 205.4],
})

df2 = pd.DataFrame({
    'name': ['Alice', 'Bobby', 'Carl', 'Dan'],
    'age': [29, 30, 31, 32],
})

df3 = df1.join(df2, how='left', lsuffix='_left', rsuffix='_right')

#   name_left  experience  salary name_right  age
# 0     Alice           1   175.1      Alice   29
# 1     Bobby           3   180.2      Bobby   30
# 2      Carl           5   190.3       Carl   31
# 3       Dan           7   205.4        Dan   32
print(df3)