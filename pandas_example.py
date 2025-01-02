import pandas as pd

data = {'Name':['Suleman','Hammad','Basit','Sayyam'],
        'Age':[19,20,23,21],
        'City':['Karachi','Lahore','Rawalpindi','Sukkar']}

df = pd.DataFrame(data)

print(df)

# OUTPUT:
#       Name  Age        City
# 0  Suleman   19     Karachi
# 1   Hammad   20      Lahore
# 2    Basit   23  Rawalpindi
# 3   Sayyam   21      Sukkar
