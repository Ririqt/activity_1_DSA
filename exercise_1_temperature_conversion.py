# Exercise 1: Converting Temperatures
while True:
    # Creating the Conversion
    try:
        # Prompt the User to Input
        temperature = float(input("What is your Temperature? "))
        conversion = int(input("Type '1' for (Celsius to Fahrenheit), Type '2' for (Fahrenheit to Celsius): "))
        # Creating the Conditions per Conversion
        if conversion == 1:
            fahrenheit_temperature = (temperature * 9/5) + 32
            print(f"Fahrenheit: {round(fahrenheit_temperature, 2)}°F")
            
        elif conversion == 2:
            celsius_temperature = (temperature - 32) * 5/9
            print(f"Celsius: {round(celsius_temperature, 2)}°C")
        # Getting other Possible Options
        else:
            print("Sorry, Please Enter '1' or '2' ")
            continue
        break
    # Handling Exceptions possibly made by the User
    except ValueError:
        print("You have made an Invalid Input, Please Enter a valid number for temperature and '1' (Celsius to Fahrenheit) or '2' (Fahrenheit to Celsius)!")
