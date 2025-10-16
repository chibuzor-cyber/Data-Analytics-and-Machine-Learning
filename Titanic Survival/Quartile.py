import pandas as pd

data = [10, 12, 15, 18, 20, 22, 25, 30, 50, 100]
df = pd.DataFrame(data, columns=['values'])

Q1 = df['values'].quantile(0.25)
Q3 = df['values'].quantile(0.75)
IQR = Q3 - Q1

print(f'Q1: {Q1}')
print(f'Q3: {Q3}')
print(IQR)