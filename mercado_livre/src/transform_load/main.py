import pandas as pd
import sqlite3
from datetime import datetime
import os

path = "mercado_livre/data/data.json"
df = pd.read_json(path)

#setando pandas pra mostrar todas as colunas
pd.options.display.max_columns = None


df['_source'] = "https://lista.mercadolivre.com.br/notebook?sb=rb#D[A:notebook]"
df['_datetime'] = datetime.now()


print(df.head())
