# Python3 Program to
# Write a program to accept minutes and convert it into hours and minute

#storing the number of minutes in the variable 'minutes'
minutes = int(input("Enter the total number of minutes: "))
#converting it to hours and minute
minute_left = minutes % 60
hours = minutes // 60
#final output
print(f"time converted is {hours} hours and {minute_left} minutes")
