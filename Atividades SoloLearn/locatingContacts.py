import pandas as pd

data = {
   'name': ['James', 'Billy', 'Bob', 'Amy', 'Tom'],
   'number': ['1234', '5678', '2222', '1111', '0909']
}
nome = input()
data = pd.DataFrame(data, index=['James', 'Billy', 'Bob', 'Amy', 'Tom'])

print(data)
print(data.loc[nome])
