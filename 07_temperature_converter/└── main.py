# ==========================================
# Day 7 - Temperature Converter
# ==========================================

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


print("======================================")
print("       TEMPERATURE CONVERTER")
print("======================================")

print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    celsius = float(input("Enter temperature in Celsius: "))

    fahrenheit = celsius_to_fahrenheit(celsius)

    print("\n----- Result -----")
    print(celsius, "°C =", round(fahrenheit, 2), "°F")

elif choice == "2":
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))

    celsius = fahrenheit_to_celsius(fahrenheit)

    print("\n----- Result -----")
    print(fahrenheit, "°F =", round(celsius, 2), "°C")

else:
    print("\nInvalid choice! Please select 1 or 2.")

print("======================================")
print("       Program Completed!")
print("======================================")
