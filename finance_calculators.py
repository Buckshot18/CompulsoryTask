import math

# HEADLINE
print("Financial calculator\n")

# INFORMATION ABOUT INVESTMENT AND BOND
print("Investment - to calculate the amount of interest you'll earn on your investment")
print("Bond - to calculate the amount you'll have to pay on a home loan \n")

user_input = input(
    "Enter 'investment' or 'bond' from the menu above to proceed: "
).lower()


# Function to get a valid float input
def get_valid_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")


# Function to get a valid integer input
def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid integer.")


# Function to convert interest rate percentage to decimal
def convert_rate(rate):
    return rate / 100


# IF THE USER CHOOSES INVESTMENT
if user_input == "investment":
    deposit = get_valid_float("How much money are you depositing R ")
    rate = convert_rate(get_valid_float("Enter the interest rate (e.g., 8 for 8%): "))
    years = get_valid_int("How many years do you plan on investing: ")
    interest = input("Enter 'simple' or 'compound' interest: ").lower()

    # SIMPLE INTEREST CALCULATIONS AND OUTPUT
    if interest == "simple":
        total_amount = deposit * (1 + rate * years)
        print(
            f"The total amount after {years} years with simple interest is: R{round(total_amount, 2)}"
        )

    # COMPOUND INTEREST CALCULATIONS AND OUTPUT
    elif interest == "compound":
        total_amount = deposit * math.pow((1 + rate), years)
        print(
            f"The total amount after {years} years with compound interest is: R{round(total_amount, 2)}"
        )

    else:
        print("Invalid input! Please enter 'simple' or 'compound'.")

# IF THE USER CHOOSES BOND
elif user_input == "bond":
    house_value = get_valid_float("Please enter the value of the house: ")
    rate = convert_rate(get_valid_float("Enter the interest rate: "))
    months_amount = get_valid_int("Total months to repay: ")

    # CALCULATION OF BOND REPAYMENT
    monthly_rate = rate / 12
    repayment = (monthly_rate * house_value) / (
        1 - (1 + monthly_rate) ** (-months_amount)
    )

    print(f"You will have to repay R{round(repayment, 2)} each month.")

# INVALID INPUT HANDLING
else:
    print("Invalid input! Please enter 'investment' or 'bond'.")
