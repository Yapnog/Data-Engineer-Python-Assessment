import pandas as pd
import numpy as np
from sqlalchemy import create_engine

#load dataset
file = r"skill_test_data.xlsx"
data = pd.read_excel(file, sheet_name = "data")

#create pivot
values = ['Spend', 'Attributed Rev (1d)', 'Imprs', 'Visits', 'New Visits', 'Transactions (1d)', 'Email Signups (1d)']
table = pd.pivot_table(data,
                    values=values,
                    index='Platform (Northbeam)',
                    aggfunc=np.sum,
                    )

#sort pivot to desired setup
table = table[values].sort_values(by='Attributed Rev (1d)', ascending=False)
table.sort_values(by='Attributed Rev (1d)', ascending=False)

#get grand total for all columns
table_sums = table.sum(axis=0)
table_sums = pd.DataFrame(table_sums).transpose().rename(index={0:'Grand Total'})

#insert grand total to pivot table and round all numbers
final = pd.concat([table, table_sums]).round(2)

#setup sqlite
engine = create_engine('sqlite:///skill_test_data.db', echo=False)
final.to_sql('pivot_table', con=engine, if_exists='append')

print('Added to database!')