import math

#create menu "interface"
menu = {}
menu['1'] = "Adding"
menu['2'] = "Multiplying"
menu['3'] = "Division"
menu['4'] = "Square root of an equation"
menu['5'] = "Palindrome"
menu['6'] = "under construction"
menu['7'] = "under construction"
menu['8'] = "under construction"
menu['9'] = "Exit"

while True:
    options = menu.keys()
    options.sort()
    for entry in options:
        print entry, menu[entry]

    selection = raw_input("Please select: ")

    if selection == '1':
        adding_one = input("first number to add: \n")
        adding_two = input("second number to add : \n")

        sum_of_two = adding_one + adding_two
        print (sum_of_two)
    elif selection == '2':
        multi_one = input("first num to multiply: \n")
        multi_two = input("second num to multiply: \n")

        multi_of_two = multi_one * multi_two
        print (multi_of_two)
    elif selection == '3':
        division_one = input("first number to divide: ")
        division_two = input("second number to divide: ")

        division_of_two = division_one / division_two
        print(division_of_two)

    elif selection == '4':
        squareRootOfEq = input("equation or number to calc square root: \n")

        sqrtEq = math.sqrt(squareRootOfEq)
        print(sqrtEq)
    elif selection == '5':
        string = raw_input(("input a string to check if palindrome \n"))
        #raw_input is used because python 2.7 thrown an error if input is used to show strings
        
        #checks if string is the same in reverse
        if (string == string[:: -1]):
            print("string is palindrome")
        else:
            print("string is not palindrome")

    elif selection == '9':
        break
    else:
        print "unknown choice"