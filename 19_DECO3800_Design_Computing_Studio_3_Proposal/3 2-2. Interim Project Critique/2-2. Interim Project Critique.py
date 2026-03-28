# Import the pandas library and define an alias as pd.
import pandas as pd

# Load the data
data = pd.read_csv('/Users/xianglongronaldolin/Desktop/学习/2 The University of Queensland/2 Year/5/Semester/1/DECO3800/Assessment/2. Project/3 2-2. Interim Project Critique/data.csv')

# Display information about the data, including the count of non-null values and data types for each column
print(data.info())

# Display the first few rows of the data to get an overview of its structure
print(data.head())

# Check for and handle missing values
data = data.fillna('Unknown')  # Replace missing values with 'Unknown'

# Identify useful columns and rename them for ease of use
data.columns = [
    'Timestamp', 'Social_Media_Usage', 'Experienced_Trolling', 'Types_of_Trolling',
    'Example_of_Incident', 'Trolling_Frequency', 'Who_Trolls', 'Feelings_When_Trolled',
    'Response_to_Trolling', 'Activity_Changes_Due_to_Trolling', 'Real_Life_Impact',
    'Specific_Real_Life_Impact', 'Mental_Health_Impact', 'Most_Trolling_Platform',
    'Effective_Prevention', 'Platforms_Should_Do_More'
]

# Calculate the frequency of different types of online trolling behaviors
types_of_trolling = data['Types_of_Trolling'].value_counts()
print(types_of_trolling)

# Calculate the most common platforms for online trolling behavior
platform_trolling = data['Most_Trolling_Platform'].value_counts()
print(platform_trolling)

# The impact of online trolling behavior on mental health
mental_health_impact = data['Mental_Health_Impact'].value_counts()
print(mental_health_impact)

# Splitting the multiple-choice answers into separate columns and counting the frequency of each type's occurrence
trolling_types = data['Types_of_Trolling'].str.get_dummies(sep=';')
trolling_types_sum = trolling_types.sum().sort_values(ascending=False)
print(trolling_types_sum)

# Association between frequency and type
frequency_type_relation = data.groupby('Trolling_Frequency').agg(lambda x: x.str.get_dummies(sep=';').sum())
print(frequency_type_relation)

# Effectiveness of platform policies统计
policy_effectiveness = data['Effective_Prevention'].value_counts(normalize=True)
print(policy_effectiveness)

# Users' perspectives on the need for platform anti-trolling improvements
need_more_prevention = data['Platforms_Should_Do_More'].value_counts(normalize=True)
print(need_more_prevention)
