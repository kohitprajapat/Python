from datetime import date
name = input("Your name: ")

age = int(input("Enter Dob as YYYY: "))

today = date.today()

print("Dear",name,"your age is",(today.year)-age)