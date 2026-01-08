import numpy as np  # Import numpy package

# Raw Data of Employee Salaries in IS Department
employee_names = ["Latrece", "Payton", "Alice", "Bob", "Eva"]
salaries = [85, 92, 78, 450, 88]    # Includes data entry error

# Data Cleaning
# Fixing incorrect salary for Bob
salaries[3] = 95

# List Manipulation
# New Sr. analyst joined
np_salaries = np.array(salaries)    # Convert to numpy array for statistical calculations

# Calculate 5% performance bonus for all employees
bonuses = np_salaries * 0.05
total_compensation = np_salaries + bonuses

# Descriptive Statistics
# Using functions to summarize data
avg_salary = np.mean(np_salaries)   # Average salaries
max_comp = max(total_compensation) # Maximum compensation

# Output
print("---" + "IS Department Salary Report" + "---")
print("Processed " + str(len(employee_names)) + " employees.")  # Calculate amount of employees
print("Average Base Salary: $" + str(round(max_comp, 2)) + "k")
print("\nFull Compensation List (Base + Bonus): ")  # Create a new line \n
print(total_compensation)