# Author: Makarius Epps
# Simple Interest Calculator: prompts for principal, rate, and time,
# validates each input, and prints the simple interest.

def get_float(prompt):
    while True:
        try: 
            value = float(input(prompt))
            if value < 0:
                print("Please enter a number that isn't negative.")
                continue
            return value
        except ValueError:
            print("That wasn't a number. Please try again.")

principal = get_float("Enter the principal amount: ")
rate = get_float("Enter the rate of interest (as a percentage): ")
time = get_float("Enter the time in years: ")

interest = (principal * rate * time) / 100
print(f"Simple interest: ${interest:.2f}")