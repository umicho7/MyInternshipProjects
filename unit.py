def meters_to_feet(meters):
    return meters * 3.28084

def feet_to_meters(feet):
    return feet / 3.28084

def km_to_meters(km):
    return km*1000

def meters_to_km(meters):
    return meters/1000

def km_to_feet(km):
    return km*3280.84

def feet_to_km(feet):
    return feet/3280.84

def main():
    while True:
        try:
            value = float(input("Enter a value: "))
            source_unit = input("Enter source unit (meters or feet or kilometers): ").strip().lower()
            target_unit = input("Enter target unit (meters or feet or kilometers): ").strip().lower()

            if source_unit == target_unit:
                print("Source and target units are the same. No conversion needed.")
            elif (source_unit == "meters" or "m") and (target_unit == "feet" or "ft"):
                result = meters_to_feet(value)
                print(f"{value} meters is equal to {result} feet.")
            elif (source_unit == "feet" or "ft") and (target_unit == "meters" or "m"):
                result = feet_to_meters(value)
                print(f"{value} feet is equal to {result} meters.")
            elif (source_unit == "kilometers" or "km") and (target_unit == "meters" or "m"):
                result = km_to_meters(value)
                print(f"{value} km is equal to {result} meters.")
            elif (source_unit == "meters" or "m") and (target_unit == "kilometers" or "km"):
                result = meters_to_km(value)
                print(f"{value} meters is equal to {result} km.")
            elif (source_unit == "kilometers" or "km") and (target_unit == "feet" or "ft"):
                result = km_to_feet(value)
                print(f"{value} km is equal to {result} feet.")
            elif (source_unit == "feet" or "ft") and (target_unit == "kilometers" or "km"):
                result = feet_to_km(value)
                print(f"{value} feet is equal to {result} km.")
            else:
                print("Unsupported units. Please enter 'meters' or 'feet'.")

        except ValueError:
            print("Invalid input. Please enter a valid numeric value.")
        except KeyboardInterrupt:
            print("\nProgram terminated.")
            break

if __name__ == "__main__":
    main()
