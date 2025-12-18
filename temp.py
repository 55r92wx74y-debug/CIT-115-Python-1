print("Kaeliah Temp Converter:")

temp = float(input("Enter a Temperature:"))

temp_type = input("Is the temp F for Fahrenheit or C for Celsius?:")


if temp_type == "F" or "f" and temp > 212:
    print("Temp can not be > 212")
else:
    celsius = (5.0/9) * (temp - 32)
    print(f"The Celsius equivalent is: {celsius:.1f}")


if temp_type == "C" or "c":
    if temp > 100:
        print("Temp can not be > 100")
    else:
        fahrenheit = ((9.0/5.0) * temp) + 32
        print(f" The Fahrenheit equivalent is: {fahrenheit:.1f}")




  
