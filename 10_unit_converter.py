'''This program will allow users to convert between different units, such as:

    Length: Meters to Kilometers, Miles to Kilometers, etc.
    Weight: Kilograms to Pounds, Grams to Ounces, etc.
    Temperature: Celsius to Fahrenheit, Fahrenheit to Celsius.'''
def unit_converter():
    while True:
        conversion = int(input("Enter \"1\" for Length conversion\n Enter \"2\" for Weight conversion\nEnter \"3\" for Temperature conversion\nEnter \"4\" for Miles to KM conversion\nEnter \"5\" to exit\nEnter your choice:"))
        if conversion == 1: 
            length = float(input("Enter the length (just the number, not the unit): "))
            unit = int(input("Enter the unit of the given length:\n1. Kilometer\n2. Meter\n3. Centimeter\nEnter your choice: "))
            conversion_unit_length = int(input("Enter the unit you want to convert the length to:\n1. Kilometer\n2. Meter\n3. Centimeter\n4. Miles\n5. Cancel the conversion\nEnter your choice: "))
            if unit == 1:  
                if conversion_unit_length == 1:
                    print(f"{length} KM")
                elif conversion_unit_length == 2:
                    print(f"{length * 1000} m")
                elif conversion_unit_length == 3:
                    print(f"{length * 100000} cm")
                elif conversion_unit_length == 4:
                    print(f"{length / 1.60934} miles")
                else:
                    print("Conversion canceled.")
            elif unit == 2: 
                if conversion_unit_length == 1:
                    print(f"{length / 1000} km")
                elif conversion_unit_length == 2:
                    print(f"{length} m")
                elif conversion_unit_length == 3:
                    print(f"{length * 100} cm")
                elif conversion_unit_length == 4:
                    print(f"{length / 1609.34} miles")
                else:
                    print("Conversion canceled.")
            elif unit == 3: 
                if conversion_unit_length == 1:
                    print(f"{length / 100000} km")
                elif conversion_unit_length == 2:
                    print(f"{length / 100} m")
                elif conversion_unit_length == 3:
                    print(f"{length} cm")
                elif conversion_unit_length == 4:
                    print(f"{length / 160934} miles")
                else:
                    print("Conversion canceled.")
            else:
                print("Invalid unit choice for length conversion.")
        elif conversion == 2:
            weight = float(input("Enter the weight (just the number,t the unit): "))
            unit = int(input("Enter the unit of the given weight:\n1. Kilogram\n2. Gam\n3. Pound\nEnter your choice: "))
            conversion_unit_weight = int(input("Enter the unit you want o convert the weight to:\n1. Kilgram\n2. Gram\n3. Pound\n4. Cancel the conversion\nEnter your choice: "))
            if unit == 1:
                if conversion_unit_weight == 1:
                    print(f"{weight} kg")
                elif conversion_unit_weight == 2:
                    print(f"{weight * 1000} g")
                elif conversion_unit_weight == 3:
                    print(f"{weight * 2.20462} lbs")
                else:
                    print("Conversion cceled.")
            elif unit == 2:
                if conversion_unit_weight == 1:
                    print(f"{weight / 1000} kg")
                elif conversion_unit_weight == 2:
                    print(f"{weight} g")
                elif conversion_unit_weight == 3:
                    print(f"{weight / 453.592} lbs")
                else:
                    print("Conversion canceled.")
            elif unit == 3:  
                if conversion_unit_weight == 1:
                    print(f"{weight / 2.20462} kg")
                elif conversion_unit_weight == 2:
                    print(f"{weight * 453.592} g")
                elif conversion_unit_weight == 3:
                    print(f"{weight} lbs")
                else:
                    print("Conversion cancled.")
            else:
                print("Invalid unit choice fo weight conversion.")

        elif conversion == 3:
            # Temperature Conversion
            temperature = float(input("Enter the temprature (just the number, not the unit): "))
            unit = int(input("Enter the unit of the given temperture:\n1. Celsius\n2. Fahrenheit\n 3. Kelvin\n Enter your choice: "))
            conversion_unit_temp = int(input("Enter the unit you want to convert the temperature to:\n1. Celsius\n2. Fahrenheit\n3. Kelvin\n4. Cancel the conversion\nEnter your choice: "))
            if unit == 1:
                if conversion_unit_temp == 1:
                    print(f"{temperature} °C")
                elif conversion_unit_temp == 2:
                    print(f"{(temperature * 9/5) + 32} °F")
                elif conversion_unit_temp == 3:
                    print(f"{temperature + 273.15} K")
                else:
                    print("Conversion canceled.")
            elif unit == 2:  
                if conversion_unit_temp == 1:
                    print(f"{(temperature - 32) * 5/9} °C")
                elif conversion_unit_temp == 2:
                    print(f"{temperature} °F")
                elif conversion_unit_temp == 3:
                    print(f"{(temperature - 32) * 5/9 + 273.15} K")
                else:
                    print("Conversion canceled.")
            elif unit == 3: 
                if conversion_unit_temp == 1:
                    print(f"{temperature - 273.15} °C")
                elif conversion_unit_temp == 2:
                    print(f"{(temperature - 273.15) * 9/5 + 32} °F")
                elif conversion_unit_temp == 3:
                    print(f"{temperature} K")
                else:
                    print("Conversion canceled.")
            else:
                print("Invalid unit choice for temperature conversion.")
        elif conversion == 4:
            miles = float(input("Enter the distance in miles: "))
            print(f"{miles * 1.60934} km")
        elif conversion == 5:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
unit_converter()

                
            
            
            