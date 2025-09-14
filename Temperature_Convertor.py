import time   # Used for adding small delays to make menu printing smoother

# ---------------- Conversion Functions ---------------- #


def celsius_to_fahrenheit(c):     #Convert Celsius to Fahrenheit
    return (c * 9/5) + 32         

def fahrenheit_to_celsius(f):     #Convert Fahrenheit to Celsius
    return (f - 32) * 5/9

def celsius_to_kelvin(c):         #Convert Celsius to Kelvin
    return c + 273.15

def kelvin_to_celsius(k):         #Convert Kelvin to Celsius
    return k - 273.15

def fahrenheit_to_kelvin(f):      #Convert Fahrenheit to Kelvin
    return (f - 32) * 5/9 + 273.15

def kelvin_to_fahrenheit(k):      #Convert Kelvin to Fahrenheit
    return (k - 273.15) * 9/5 + 32


# ---------------- Main Program Loop ---------------- #

while True:
    # Display Menu with a delay effect
    print("\n" + "="*40)
    print("   🌡️  Temperature Converter  🌡️")
    print("="*40)
    time.sleep(0.5)
    print("1. Celsius to Fahrenheit")
    time.sleep(0.5)
    print("2. Fahrenheit to Celsius")
    time.sleep(0.5)
    print("3. Celsius to Kelvin")
    time.sleep(0.5)
    print("4. Kelvin to Celsius")
    time.sleep(0.5)
    print("5. Fahrenheit to Kelvin")
    time.sleep(0.5)
    print("6. Kelvin to Fahrenheit")
    time.sleep(0.5)
    print("="*40)
    time.sleep(0.1)
    
    # Take user input safely
    try:
        choice = int(input("Enter your choice (1-6): "))      # Menu choice
        temp = float(input("Enter the temperature value: "))  # Temperature to convert
    except ValueError:
        # If user enters something that's not a number
        print("⚠️ Invalid input! Please enter numbers only.")
        continue   # Restart loop

    # Perform conversion based on choice
    if choice == 1:
        print(f"{temp}°C = {celsius_to_fahrenheit(temp):.2f}°F")
    elif choice == 2:
        print(f"{temp}°F = {fahrenheit_to_celsius(temp):.2f}°C")
    elif choice == 3:
        print(f"{temp}°C = {celsius_to_kelvin(temp):.2f}K")
    elif choice == 4:
        print(f"{temp}K = {kelvin_to_celsius(temp):.2f}°C")
    elif choice == 5:
        print(f"{temp}°F = {fahrenheit_to_kelvin(temp):.2f}K")
    elif choice == 6:
        print(f"{temp}K = {kelvin_to_fahrenheit(temp):.2f}°F")
    else:
        print("⚠️ Invalid choice! Please select between 1-6.")

    # Ask user if they want to continue
    again = input("Do you want to continue (y/n): ").lower()
    if again == 'n':   # Exit loop if user says "no"
        print("✅ Thanks for using Temperature Converter! Goodbye 👋")
        break
