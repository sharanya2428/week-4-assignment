import pandas as pd

data = {
    "Name": ["Ravi", "Sita", "Arun", "Priya"],
    "Department": ["IT", "HR", "IT", "Sales"],
    "Salary": [40000, 30000, 50000, 35000]
}

df = pd.DataFrame(data)

print("Employee Dataset:")
print(df)

print("\nAverage Salary:")
print(df["Salary"].mean())

print("\nDepartment Count:")
print(df["Department"].value_counts())

print("\nEmployees earning above 35000:")
print(df[df["Salary"] > 35000])

df.to_csv("employee_results.csv", index=False)
print("\nResults saved to employee_results.csv")
