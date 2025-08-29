print("\tConversor de temperaturas")
print("\nCelsius  Fahrenheit")

for celsius in range (0, 101, 10):
    fahrenheit = celsius * (9/5) + 32
    print(f"{celsius:<9} {fahrenheit:<10.1f}") 