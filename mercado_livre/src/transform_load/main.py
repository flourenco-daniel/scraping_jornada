import pandas as pd
import sqlite3
from datetime import datetime
import os

path = "mercado_livre/data/data.json"
df = pd.read_json(path)

#setando pandas pra mostrar todas as colunas
pd.options.display.max_columns = None



df['old_value'] = df['old_value'].fillna('0')
df['new_value'] = df['new_value'].fillna('0')
df['rating'] = df['rating'].fillna('0')

df['old_value'] = df['old_value'].astype(str).str.replace('.', '', regex=False)
df['new_value'] = df['new_value'].astype(str).str.replace('.', '', regex=False)
df['rating'] = df['rating'].astype(str).str.replace('[\(\)]', '', regex=True)

df['_source'] = "https://lista.mercadolivre.com.br/notebook?sb=rb#D[A:notebook]"
df['_datetime'] = datetime.now()
df['old_value'] = df['old_value'].astype(float)
df['new_value'] = df['new_value'].astype(float)
df['rating'] = df['rating'].astype(float)


df = df[
    (df['old_value'] >=1000) & (df['old_value'] <= 10000) &
    (df['old_value'] >=1000) & (df['old_value'] <= 10000)
]

print(df)

#salvando no banco

conn = sqlite3.connect('mercado_livre/data/notebook.db')

df.to_sql('notebook_research', conn, if_exists='replace', index=False)

conn.close()