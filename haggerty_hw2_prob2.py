# Author: Parker Haggerty
# Date: 2/7/17
# Assignment 2, Problem 2

# Variables
a1=15.67
a2=17.23
a3=0.75
a4=93.2
A = int(input("Please enter a mass number: \n"))
Z = int(input("Please enter an atomic number: \n"))

# Conditions for a5...
if A%2==0:
    if Z%2==0:
        a5=12.0
    else:
        a5=-12.0
else:
    a5=0

# The Binding Energy
B = a1*A - a2*(A**(2.0/3)) - a3*((Z**2)/(A**(1.0/3))) - ((a4*(A-2*Z)**2)/A) - a5/(A**(1.0/2))
print("The Binding Energy is:", B)
print("\n")

# Binding Energy per nucleon
y = B/A
print("Binding Energy per nucleon:", y)



# Results
# For A=58, Z=28: The Binding Energy is: 490.78425241273493; Binding Energy per nucleon: 8.46179745539198
# For A=59, Z=28: The Binding Energy is: 498.144677545714; Binding Energy per nucleon: 8.443130127893458
# For A=58, Z=27: The Binding Energy is: 485.30934897614435; Binding Energy per nucleon: 8.367402568554214