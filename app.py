# POLYNOMIAL DIVIDER v3 #
# ANTIMONYXD #
# Last Edit: Sep. 27, 2025 #
# https://github.com/antimonyXD #

from os import name, system


def clear() -> None:
    # Clears the screen based on operating system
    if name == 'nt':

        # For Windows
        _ = system('cls')
    else:
        
        # For macOS and Linux
        _ = system('clear')


def polynomial_to_string(coeffs:list) -> str:

    # String representation of the polynomial
    p_string = " "

    # Loops through every coefficient
    for d in range(len(coeffs)):
    
        # Calculates the power of x
        power = len(coeffs) - d - 1
        
        # If this is the leading term
        if d == 0:
            
            # Adds ax^n to the polynomial string
            p_string += f"{coeffs[d]}x^{power}"

        else:
            
            # Ignores the term if its coefficient is 0
            if coeffs[d] == 0:
                continue

            # If the given coefficient > 0
            elif coeffs[d] > 0:

                # Adds plus sign and coefficient
                p_string += f" + {coeffs[d]}"

            else:
                # Adds negative sign and absolute value of coefficient
                p_string += f" - {abs(coeffs[d])}"

            # If this isn't the final constant term
            if d != len(coeffs) - 1:

                # Adds x^p to polynomial string
                p_string += f"x^{power}"
    
    # Removes "1x" and "x^1"
    p_string = p_string.replace(" 1x", " x").replace("x^1 ", "x ").strip()

    return p_string


def zero_float_cast(fl : float):

    # If the input is a float ending in ".0"
    if str(fl).endswith(".0"):

        # Converts the input to an int
        fl = int(fl)
    
    return fl


def polynomial_division(divis, dividend) -> list:

    # creates a copy of dividend with the same length as the divisor
    sub_dividend = dividend[:len(divis)]

    # temporary list to hold the results of subtraction
    temp = []

    # quotient
    quot = []
    new_quot_coeff = 0

    for n in range(len(dividend) - len(divis) + 1):

        # calculates new coefficient to add to the quotient list
        new_quot_coeff = zero_float_cast(sub_dividend[0] / divis[0])
        
        # adds said coefficient
        quot.append(new_quot_coeff)

        # loops through every number from 0 to length of divisor
        for k in range(1, len(divis)):

            # calculates number to get subtracted (known in fancy terms as the subtrahend)
            subtrahend = new_quot_coeff * divis[k]

            # subtracts subtrahend from the dividend copy, to determine the next term of the difference
            temp.append(sub_dividend[k] - subtrahend)
        
        # if there are any more terms to be brought down
        if n < (len(dividend) - len(divis)):

            # brings the next number down from the dividend
            temp.append(dividend[n+len(divis)])

        # updates dividend_copy
        sub_dividend = temp

        # clears temp list
        temp = []

    # grabs the remainder
    rem = zero_float_cast(sub_dividend[0])
    
    return [quot, rem]


def get_ordinal(n:int) -> str:
    
    n=str(n)

    if n[-1] == "1":
        n+="st"
    elif n[-1] == "2":
        n+="nd"
    elif n[-1] == "3":
        n+="rd"
    else:
        n+="th"
    return n


divisor_coeffs = []
dividend_coeffs = []


for n in range(2):

    # clears the screen
    clear()

    # input string
    ik=""

    if n == 0:
        print("--DIVIDEND (number you wanted to GET divided)--\n")
    else:
        print("--DIVISOR (number you wanted to DIVIDE by)--\n")

    cnt=1
    while ik == "":
        # asks for user input
        ik = input(f"Please insert the {get_ordinal(cnt)} coefficient (type EXIT if you want to leave): ") 

        # if the user inputs exit
        if ik.upper().strip() == "EXIT":

            # exits the while loop
            break

        else:
            try:
                # converts input to integer
                ik = int(ik)

                # adds input to coefficient list
                if n==0:
                    dividend_coeffs.append(ik)
                else:
                    divisor_coeffs.append(ik)

                cnt += 1

            except Exception:

                # prints message to let user know their input is void
                print("INVALID INPUT VOIDED\n")
            
            # sets input to empty string to restart the while loop
            ik = ""

# Calculates quotient and remainder 
quotient, remainder = polynomial_division(divisor_coeffs, dividend_coeffs)

# Clears screen
clear()

# Displays results
print(f"""--RESULTS--
Dividend: {polynomial_to_string(dividend_coeffs)}
Divisor: {polynomial_to_string(divisor_coeffs)}

---------------------------

Quotient: {polynomial_to_string(quotient)}
Remainder: {remainder}

--POLYNOMIAL DIVIDER--
2025 ANTIMONYXD
https://github.com/antimonyXD
""")
