# Problem 3 — Medium

# Write a program that takes three numbers from the user and prints:

# The largest number
# The smallest number
# The average of the three numbers

# Do not use max() or min().


Fnum = int(input('Enter the first  number :'))
Snum =  int(input('Enter the second  number :'))
Tnum = int(input('Enter the third  number :'))

if Fnum > Snum and  Fnum >Tnum:
    print("Fnum is greatest number :",Fnum)
elif Snum>Fnum and Snum>Tnum:
    print('Snum is greatest number :',Snum)
else:
   print('Tnum is greates number :',Tnum)



total = Fnum+Snum+Tnum
avg = total/3   


print ("average of three number is :",avg)
if Fnum < Snum and Fnum < Tnum:
    print("Fnum is smallest:", Fnum)
elif Snum < Fnum and Snum < Tnum:
    print("Snum is smallest:", Snum)
else:
    print("Tnum is smallest:", Tnum)
 

