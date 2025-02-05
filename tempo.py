import pandas as pd
import seaborn as srn
import statistics as est

dataset = pd.read_csv("tempo.csv", sep = ";")

# Aparencia fora do dominio
aparencia = dataset.groupby(dataset['Aparencia']).size()

# Descobrindo a moda
est.mode(dataset['Aparencia'])

# Atribuimos chuva (moda) aos de fora do dominio
dataset.loc[dataset['Aparencia'].isin(['menos']), 'Aparencia'] = "sol"

# Verificamos o resultado
aparencia = dataset.groupby(['Aparencia']).size()


# Temperatura fora do dominio
dataset.loc[(dataset['Temperatura'] < -135) | (dataset['Temperatura'] > 130)]

# Calcular a mediana das temperaturas
medianatemp = est.median(dataset.loc[(dataset['Temperatura'] >= -135) & (dataset['Temperatura'] <= 130), 'Temperatura'])

# Substituir os valores fora do domínio
dataset.loc[(dataset['Temperatura'] <= -135) | (dataset['Temperatura'] >= 130), 'Temperatura'] = int(medianatemp)


# Umidade fora do dominio
dataset.loc[(dataset['Umidade'] < 0) | (dataset['Umidade'] > 100) | (dataset['Umidade'].isna())]

# Calcular a mediana das umidades
medianaumi = est.median(dataset.loc[(dataset['Umidade'] >= 0) & (dataset['Umidade'] <= 100), 'Umidade'])

# Substituir os valores fora do domínio
dataset.loc[(dataset['Umidade'] < 0) | (dataset['Umidade'] > 100) | (dataset['Umidade'].isna()), 'Umidade'] = medianaumi


# Vento fora do dominio
vento = dataset.groupby(dataset['Vento']).size()

# Descobrindo a moda
est.mode(dataset['Vento'])

# Atribuimos FALSO (moda) aos de fora do dominio
dataset.loc[dataset['Vento'].isna(), 'Vento'] = "FALSO"

# Verificamos o resultado
vento = dataset.groupby(['Vento']).size()

print(dataset)