# Monicah Wambugu <--- Your name
# user_input.py  <--- File Name
# 19th June 2017  <--- Date

"""
Prompt: Write a program that will ask the user for their first and last name, and date of 
birth, and print them out formatted.

"""

firstname = input("Enter your firstname: ");
lastname = input("Enter your last name: ")
dob_month = input("Enter your date of birth: \nMonth?")
dob_day = input("Day?")
year = input("Year")

print(firstname,lastname,' was born on ',dob_month,dob_day,',',year)
