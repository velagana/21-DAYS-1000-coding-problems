def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Test the functions
celsius_temp = 30
fahrenheit_temp = 86

print(f"{celsius_temp} Celsius is equal to {celsius_to_fahrenheit(celsius_temp):.2f} Fahrenheit")
print(f"{fahrenheit_temp} Fahrenheit is equal to {fahrenheit_to_celsius(fahrenheit_temp):.2f} Celsius")

