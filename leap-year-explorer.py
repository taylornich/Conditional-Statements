#question 3 task 1

year = int(input("Enter year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 ==0):
    print("True - this is a leap year")
else:
    print("False")


