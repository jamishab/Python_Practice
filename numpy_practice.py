import numpy as np

# Create company_computers list to track computers per building
company_computers = [47, 25, 90, 52, 33, 28]
company_buildings = 6
print(" Company Computers: " + str(company_computers))
print("Company Buildings: " + str(company_buildings))

# Create numpy array from company_computers
np_company_computers = np.array(company_computers)
print(np_company_computers)

# Print index 4 from np_company_computers
print(np_company_computers[4])  # Results in 33

# Print np_company_computer type
print(type(np_company_computers))   # Results in 'numpy.ndarray'

# Print computers of np_company_computers: index '25' to '28'
print(np_company_computers[1:])

# Create a numpy array for company desk per room
company_desks = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                          [10, 15, 36, 12, 28, 22, 18, 24, 20, 10]])

print("Company Desks by Room: " + str(company_desks))
print(type(company_desks))
print(company_desks.shape)  # Results in 2 rows and 10 columns

print(company_desks[1]) # Results in full second column in company_desks
print(company_desks[:, 3])  # Results in '4' and '12'
print(company_desks[1, 5])  # Returns single value '22'

# Print mean
print(np.mean(np_company_computers))
print(np.mean(company_desks))
# Print median of company computers
print(np.median(np_company_computers))