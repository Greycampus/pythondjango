# Python program to check if the input year is a leap year or not

year = int(input('Enter year:'))

if (year % 4) == 0:#first condtion /4
   if (year % 100) == 0:#second condtion /100
       if (year % 400) == 0:#third condition /400
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))
