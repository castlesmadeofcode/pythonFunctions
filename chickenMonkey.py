# Write a program that prints the numbers from 1 to 100. 
# You can use Python's range() to quickly make a list of numbers.
# For multiples of five (5, 10, 15, etc.) print "Chicken" instead of the number.
# For the multiples of seven (7, 14, 21, etc.) print "Monkey".
# For numbers which are multiples of both five and seven print "ChickenMonkey".


x = range(101)
for n in x:
    if n%5 == 0 and n%7 == 0:
        print("chicken monkey")
    elif n%5 == 0:
        print("chicken")
    elif n%7 == 0:
        print("monkey")
    else:
        print(n)
        

