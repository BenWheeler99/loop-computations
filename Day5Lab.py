# Program to do loop computations
#
# Written by Ben Wheeler
# Culver-Stockton College    12/5/2018
#
# Set large to smallest real number available in Python
large = -1.797e+308
# Set small to largest real number available in Python
small = 1.797e+308
# Initialize count
count = 0.0
# Initialize sum
nsum = 0.0
num = 1.0

while num > 0:
    num = int(input("Enter an integer greater than 0 "))
    nsum = nsum + num
    if num != 0 and num > large:
        large = num
    if num != 0 and num < small:
        small = num
    if num != 0:
        count = count + 1
    
ave = nsum/count

print ("Count is " + str(count))
print ("Sum is " + str(nsum))
print ("Average is " + str(ave))
print ("Largest number entered " + str(large))
print ("Smallest number entered " + str(small))
