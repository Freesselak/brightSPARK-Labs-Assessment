import pandas as pd

#Importing the dataset without the header row
dataFrame = pd.read_csv("dataset.csv", header=None)

#Sorting the data from the csv file by the 'division' and 'points' columns
#Ascending variable to sort them in the correct order
sortedData = dataFrame.sort_values([3, 4], ascending=(True, False))

#Setting variables for the for loop to print desired results
i = 0
numberOfResults = 3

#Prints the results to the console
#Prints the results selected from the sorted data, in the indexes that correspond to the desired output
print("records:")
while i < numberOfResults:
    print("- name: " + sortedData[0].values[i] + " " + sortedData[1].values[i])
    print("- details: In division " + sortedData[3].values[i] + " from " + sortedData[2].values[i] + " performing " + sortedData[5].values[i])
    i += 1