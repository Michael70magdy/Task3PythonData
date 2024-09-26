import pandas as pd

# Load the CSV file into a DataFrame
file_path = 'Employees.csv'  # Replace with your actual file path
df = pd.read_csv(file_path)

# Step 1: Remove any duplicates in the table
df.drop_duplicates(inplace=True)

# Step 2: Remove any decimal places in the Age column
df['Age'] = df['Age'].apply(lambda x: int(x))

# Step 3: Convert the USD salary to EGP (Assume 1 USD = 48.35 EGP)
conversion_rate = 48.35
df['Salary(EGP)'] = df['Salary(USD)'] * conversion_rate

# Step 4: Compute stats:
average_age = df['Age'].mean()
median_salary = df['Salary(EGP)'].median()
gender_counts = df['Gender'].value_counts()
male_female_ratio = gender_counts['M'] / gender_counts['F'] if 'F' in gender_counts else float('inf')

# Print the stats
print(f"Average age: {average_age:.2f}")
print(f"Median salary (in EGP): {median_salary:.2f}")
print(f"Male to Female ratio: {male_female_ratio:.2f}")

# Step 5: Save the updated dataframe to a new CSV file
new_file_path = 'Updated_Employees.csv'  # Change the file name or path if needed
df.to_csv(new_file_path, index=False)
