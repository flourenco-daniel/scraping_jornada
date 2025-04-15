import pandas as pd
import sqlite3
from datetime import datetime
import os

path = "mercado_livre/data/data.json"
df = pd.read_json(path)

print(df.head())

