import math

# Display possible calculations
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan  " "\n")

# Prompt user for selection
choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

if choice == "investment":
    # Prompt user for inputs
    deposit = float(input("Enter the amount of money that you are depositing: "))
    interest_rate = float(input("Enter the interest rate (as a percentage): ")) / 100
    years = int(input("Enter the number of years you plan on investing: "))
    interest_type = input("Do you want 'simple' or 'compound' interest: ")
    
    # Calculate interest
    if interest_type.lower() == "simple":
        amount = deposit * (1 + interest_rate * years)
    elif interest_type.lower() == "compound":
        amount = deposit * math.pow((1 + interest_rate), years)
    else:
        print("Invalid interest type selected")
        exit()
    
    # Display result
    print("Your investment will be worth £" + str(round(amount, 2)))

elif choice == "bond":
    # Prompt user for inputs
    present_value = float(input("Enter the present value of the house: "))
    interest_rate = float(input("Enter the interest rate: ")) / 100
    months = int(input("Enter the number of months for repayment: "))

    # Calculate bond repayment
    monthly_interest_rate = interest_rate / 12
    repayment = (monthly_interest_rate * present_value) / (1 - math.pow((1 + monthly_interest_rate), -months))
    
    # Display result
    print("Your monthly bond repayment will be £" + str(round(repayment, 2)))

else:
    print("Invalid choice")
