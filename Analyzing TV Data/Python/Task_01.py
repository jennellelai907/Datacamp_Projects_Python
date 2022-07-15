import pandas as pd

super_bowls = pd.read_csv('datasets/super_bowls.csv')
tv = pd.read_csv('datasets/tv.csv')
halftime_musicians = pd.read_csv('datasets/halftime_musicians.csv')

display(super_bowls.head())
display(tv.head())
display(halftime_musicians.head())
