# For a year to be a leap year, it has to be divisible by 4, if by 100, then must also by 400 as well.

def check_year(year):

    leap = False  # By default, Setting it False.

    if year % 400 == 0:  # This means year is divisible by both 4 and 400
        leap = True
        print("\n\t",year, " is a leap year.")
        tryagain()

    elif year % 100 == 0:  # This means year is divisible by only 100
        leap = False
        print("\n\t",year, " is not a leap year.")
        tryagain()

    elif year % 4 == 0:  # This means year is divisible by 4.
        leap = True
        print("\n\t",year, " is a leap year.")
        tryagain()

    else:
        leap = False
        print("\n\t",year, " is not a leap year.")
        tryagain()

    #return leap


def is_leap():

    year = input("Enter a valid 4-digits year : ")

    while True:

        try:
            year = int(year)
            if year <= 9999 and year >= 1000:

                check_year(year)

            elif year > 9999:
                print("The entered year is greater than 4-digits")
                try:
                    year =  int(input("Try Entering a valid year :"))
                    if year > 9999:
                        print(" >> Not a valid year")
                        tryagain()
                    elif year < 1000:
                        print(" >> Not a valid year")
                        tryagain()
                    else:
                        check_year(year)
                except ValueError as e:
                    print(e)
                    exit(" >>> This is not a valid input")
                    tryagain()

            elif year < 1000:
                print("The entered year is lesser than 4-digits")
                try:
                    year = int(input("Try Entering a valid year : "))
                    if year > 9999:
                        print(" >> Not a valid year")
                        tryagain()
                    elif year < 1000:
                        print(" >> Not a valid year")
                        tryagain()
                    else:
                        check_year(year)


                except ValueError as e:
                    print(e)
                    exit(" >>> This is not a valid input")
                    tryagain()

        except ValueError as e:
            print(e)
            exit(" >>> This is not a valid input")
            tryagain()

def tryagain():
    print(" \n Want to try again ??")
    again = input("Enter 'Y' to continue and 'N' to exit : ")

    if (again == 'Y' or again == 'y'):
        is_leap()

    elif (again == 'N' or again == 'n'):
        exit("Exiting... \t Thank you !")

    else:
        print("Invalid Input")
        tryagain()


is_leap()  # Function Calling


