def convertSalary(salary, to_country):
    # Define the conversion rates
    EUR_to_CAD = 1.47
    EUR_to_USD = 1.10
    EUR_to_PoundSterling = 0.88
    EUR_to_CambodianRiel = 4847.38

    # Define the average salaries of the specified countries
    avg_salaries = {"Canada": 64000, "USA": 56516, "Cambodia": 5649856, "United Kingdom": 35423}

    # Convert the salary to the specified country's currency
    if to_country == "Canada":
        converted_salary = salary * EUR_to_CAD
        currency_name = "CAD"
    elif to_country == "USA":
        converted_salary = salary * EUR_to_USD
        currency_name = "USD"
    elif to_country == "Cambodia":
        converted_salary = salary * EUR_to_CambodianRiel
        currency_name = "Cambodian Riel"
    elif to_country == "United Kingdom":
        converted_salary = salary * EUR_to_PoundSterling
        currency_name = "Pound Sterling"
    else:
        print("Invalid country name")
        return

    # Compare the converted salary with the average salary of the specified country
    if converted_salary > avg_salaries[to_country]:
        print("You will be rich in {} with a salary of {:.2f} {}".format(to_country, converted_salary, currency_name))
    else:
        print("You will be poor in {} with a salary of {:.2f} {}".format(to_country, converted_salary, currency_name))
    return converted_salary

# Prompt the user to enter their salary in Euros and the country they want to migrate to
salary = float(input("Please enter your salary in Germany: "))
to_country = input("Enter the country you want to migrate to (Canada, USA, Cambodia, United Kingdom): ")

# Call the convertSalary function with the user's input and print the result
convertSalary(salary, to_country)
