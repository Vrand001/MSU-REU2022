desired_pin = '1252'
max_tries = 3


def verify_pin(the_pin):
    return the_pin == desired_pin


def main():
    tries = 0

    while tries < max_tries:
        pin = input('please enter your pin code: ')
        if verify_pin(pin):
            print('Welcome how much money would you like to withdrawl')
            break
        else:
            print('Sorry you have entered the wrong pin please try again')
        tries += 1

    else:   # Else will run when no `break` statement is run in while loop.
        print("You are now currently locked out please come into the bank")


if __name__ == '__main__':
    main()
    
    
print('----------------------------------------------------------------------------------------')

num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))
   
print('----------------------------------------------------------------------------------------')

num = int(input("Enter a number: "))
if (num % 4) == 0:
   print("Hello")
else:
   print("BYE")

print('----------------------------------------------------------------------------------------')

marks = float(input("Enter your marks in the REU : "))

if marks > 90:
    print("Grade: A")
elif marks >= 80 and marks < 90:
    print("Grade: B")
elif marks >= 60 and marks < 80:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
    
print('----------------------------------------------------------------------------------------')

year = int(input('Enter year : '))

if (year%4 == 0 and year%100 != 0) or (year%400 == 0) :
    print(year, "is a leap year.")
else :
    print(year, "is not a leap year.")
    
print('----------------------------------------------------------------------------------------')

# assign list
l = [1, 2.0, 'mark', 'bin', 'trill', 'bop']
 
# assign string
s = 'bop' 
 
# check if string is present in the list
if s in l:
    print(f'{s} is present in the list')
else:
    print(f'{s} is not present in the list')