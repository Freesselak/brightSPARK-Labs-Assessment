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

dataFrame = pd.read_csv("dataset.csv", header=None)
#print(dataFrame)

#print()
sortedData = dataFrame.sort_values([3, 4], ascending=(True, False))

#print(sortedData)

i = 0
numberOfResults = 3

print("records:")
while i < numberOfResults:
    print("- name: " + sortedData[0].values[i] + " " + sortedData[1].values[i])
    print("- details: In division " + sortedData[3].values[i] + " from " + sortedData[2].values[i] + " performing " + sortedData[5].values[i])
    i += 1
