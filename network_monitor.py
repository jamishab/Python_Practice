import numpy as np  # Import numpy package
import math # Import math package

# Variables and Data Types
company = "Tinkered Bell IS Solutions"  # Assigning str containing name for company tailored to programmer Bell
is_active = True    # Assigning bool value
num_devices = 5 # Assigning variable int value

# IS Inventory 
# Grouping Device Names with current Latency (ms) using list of lists
devices = [     
    ["Router-Main", 15.5],
    ["Switch-Floor1", 10.2],
    ["Server-DB", 8.9],
    ["AccessPoint-A", 25.4],
    ["Firewall-01", 12.1]
]

# Data Analysis
# Extract latency numbers for high-speed calculation
latency_list = [15.5, 10.2, 8.9, 25.4, 12.1]
np_latency = np.array(latency_list) # Convert list to numpy array

# Calculate average latency using numpy function
avg_latency = np.mean(np_latency)

# Using Math package for System Planning
# If expand data center, calculate area of circular cooling vent with radius 0.43 meters
vent_radius = 0.43
vent_area = math.pi * (vent_radius ** 2)    # Calculation for area of a circle

# Reporting Output
print("---" + company + " IS Status Report ---")
print("Total Devices Monitored: " + str(len(devices)))  # Count length of devices list of lists
print("Average Network Latency: " + str(round(avg_latency, 2)) + " ms")
print("Required Cooling Vent Area: " + str(round(vent_area, 4)) + " sq.m")