import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('salarios.csv')

print('Dados do arquivo CSV: ')
print(df)

plt.figure(figsize=(8,5))
plt.bar(df['Nome'], df['Salario'], color='skyblue')  #se fosse grafico de pizza: pie/ rosca: donut, etc isso tem na literatura completa, assim como as cores tb
plt.title('Salario por pessoa')
plt.xlabel('Nome')
plt.ylabel('Salario')

plt.show() #EXIBIRRRRR!!!