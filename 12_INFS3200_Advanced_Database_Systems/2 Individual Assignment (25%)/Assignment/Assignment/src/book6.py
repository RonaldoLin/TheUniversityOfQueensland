#Import pandas
import pandas as pd

#Read the "Book3.csv" file into a DataFrame
df = pd.read_csv("../data/Book3.csv")

#Sample the records whose id is the multiple of 100
sample_set = df[df['1'] % 100 == 0]

#Get the number of records in the sample set
num_records = len(sample_set)

#Print the number of records in the sample set
print("Number of records in the sample set:", num_records)

#Count the number of fields containing NULL values in the sample set
null_fields = sample_set.isnull().sum().sum()

#Print the number of fields in the sample set
print("Number of fields containing NULL values:", null_fields)


#Calculate the total number of opportunities
total_opportunities = sample_set.shape[0] * sample_set.shape[1]

#Calculate the Empo
empo = (null_fields / total_opportunities) * 10**6

#Print the Empo
print("Empo:", empo)
