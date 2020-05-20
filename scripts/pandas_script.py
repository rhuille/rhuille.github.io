# This script prepare data for https://rhuille.github.io/posts/5-visualisations-to-compare-distributions.html
# `base-cc-dads-2016.xlsx` file come from https://www.insee.fr/fr/statistiques/2021266

import pandas as pd

columns = [
    'Salaire net horaire moyen F en 2016 (€)',
    'Salaire net horaire moyen H en 2016 (€)'
]
new_name_column = ['Femme', 'Homme']

data = pd.read_excel("base-cc-dads-2016.xlsx", header=4, usecols=columns, skiprows=[5])

(data
.sample(25).reset_index(drop=True)
.assign(**dict(zip(
    data.columns,
    map(lambda column: lambda df: df[column].sort_values().reset_index(drop=True), data.columns)
)))
.rename(columns = dict(zip(columns, new_name_column)))
.round(2)
.melt()
).to_csv('salaire_net_horaire_moyen_sample.csv', index=False)
