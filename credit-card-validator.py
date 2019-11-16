'''
CHECKS IF A CREDIT CARD NUMBER IS VALID USING THE LUHN ALGORITHM
'''
def cc_checker():
    # Input a credit card number
    cc = input("Enter your credit card number: ")
    # Begin with a total of zero
    total = 0
    # Get every second digit starting from the right-most digit and double the value
    def double_digit():
        for i in cc[-2::-2]:
            yield int(i)*2
    # Check if number is double-digit number, if yes, add individual digits to total, otherwise add to total
    for x in double_digit():
        if len(str(x)) > 1:
            for i in str(x):
                total += int(i)
        else:
            total += int(x)
    # Get every other second digit and add to the total
    for i in cc[-1::-2]:
        total += int(i)
    # Checks if total is valid using module 10
    if total%10 == 0:
        print("VALID")
    else:
        print("NOT VALID")
            
cc_checker()

input("Press ENTER to exit")