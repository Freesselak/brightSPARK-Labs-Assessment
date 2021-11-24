#1 Pull all data from dataset.xlsx
#2 Sort data by 'division' and 'points'
#3 Select top 3 results and output them to console
#       output example:
#       records:
#       - name: <firstname> <lastname>
#         details: In division <division> from <date> performing <summary>
#       - name: <firstname> <lastname>
#         details: In division <division> from <date> performing <summary>
#       - name: <firstname> <lastname>
#         details: In division <division> from <date> performing <summary>

import pandas as pd

df = pd.read_csv("dataset.csv")
print(df)

print()
test = df.sort_values(by=["division"])

print(test)