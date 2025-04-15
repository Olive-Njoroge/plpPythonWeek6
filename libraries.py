#Create a NumPy array of numbers from 1 to 10 and calculate the mean.
import numpy as np

my_array = np.array([1,2,3,4,5,6,7,8,9,10])
mean = np.mean(my_array)
print(f"Mean: {mean}")

#Load a small dataset into a pandas DataFrame and display summary statistics.
imprt pandas as pd
data = {
    'Name': ["Olive", "Waigumo", "Njoroge", "Jane"],
    'Age': [1,2,3,4],
    'Height': [120,110,125,130]
}

person = pd.DataFrame(data)
print(person)
#summary statistics
print(person.describe())

#Fetch data from a public API using requests and print a key piece of information.
import requests

# API URL
url = "https://catfact.ninja/fact"

# Make the request
response = requests.get(url)

# Convert response to JSON
data = response.json()

# Print a key piece of information
print("Random Cat Fact:", data['fact'])
