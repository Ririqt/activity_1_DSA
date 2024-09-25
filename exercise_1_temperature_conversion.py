while True:
    try:
        temperature = float(input("What is your Temperature? "))
        conversion = int(input("Type '1' for (Celsius to Fahrenheit), Type '2' for (Fahrenheit to Celsius): "))
        if conversion == 1:
            fahrenheit_temperature = (temperature * 9/5) + 32
            print(f"Fahrenheit: {round(fahrenheit_temperature, 2)}°F")
            
        elif conversion == 2:
            celsius_temperature = (temperature - 32) * 5/9
            print(f"Celsius: {round(celsius_temperature, 2)}°C")
        
        else:
            print("Sorry, Please Enter '1' or '2' ")
            continue
        break

    except ValueError:
        