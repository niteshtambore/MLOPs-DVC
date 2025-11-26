import os
import csv

import pandas as pd

# Folder and file path
data_folder = "data"
file_path = os.path.join(data_folder, "sample_data.csv")

# Create data folder if not exists
os.makedirs(data_folder, exist_ok=True)

# Sample employee data
employees = [
    ["emp_id", "name", "age", "department", "salary"],
    [1001, "Nitesh", 29, "Data Engineering", 1200000],
    [1002, "Yogesh", 31, "Backend", 900000],
    [1003, "Ravi", 26, "QA", 650000],
    [1004, "Sneha", 28, "MLOps", 1100000],
    [1005, "Priya", 24, "Analytics", 750000],
    [1006,"Nidhi",28, "Data Analysis",80000],
    [1007,"Ankit",29,"AI",80000],
    [1008,"Pallavi",27,"Data",80000]
]

# Write CSV file
with open(file_path, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(employees)

print(f"CSV file created at: {file_path}")
