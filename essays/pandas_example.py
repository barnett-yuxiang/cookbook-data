import pandas as pd

# print(pd.__version__) # 2.2.3

# Create a simple DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"],
}

df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame:")
print(df)

# Basic Operation: Select Column
selected_column = df["Age"]

# Basic Operation: Filter Rows
filtered_rows = df[df["Age"] > 28]

# Basic Operation: Add New Column
df["Salary"] = [70000, 80000, 90000]

# Output the Selected Column and Filtered Results
print("Selected Column:")
print(selected_column)

print("Filtered Rows (Age > 28):")
print(filtered_rows)

print("DataFrame with New Column (Salary):")
print(df)
