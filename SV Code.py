import pandas as pd
import matplotlib.pyplot as plt

def calculate_kinematic_viscosity(time_seconds):
    # Saybolt viscosity formula: Viscosity (in centistokes) = (time in seconds) * 0.1
    return time_seconds * 0.1

def main():
    # Create an empty DataFrame to store the data
    data = pd.DataFrame(columns=['Serial Number', 'Temperature (°C)', 'Time (s)', 'Kinematic Viscosity (cSt)'])

    while True:
        # Input data from the user
        serial_number = input("Enter Serial Number (or type 'exit' to finish): ")
        if serial_number.lower() == 'exit':
            break
        temperature = float(input("Enter Temperature of Oil (°C): "))
        time_seconds = float(input("Enter Time to collect 60ml of oil (s): "))

        # Calculate kinematic viscosity
        kinematic_viscosity = calculate_kinematic_viscosity(time_seconds)

        # Create a new DataFrame for the new entry
        new_entry = pd.DataFrame({
            'Serial Number': [serial_number],
            'Temperature (°C)': [temperature],
            'Time (s)': [time_seconds],
            'Kinematic Viscosity (cSt)': [kinematic_viscosity]
        })

        # Concatenate the new entry with the existing DataFrame
        data = pd.concat([data, new_entry], ignore_index=True)

    # Display the collected data
    print("\nCollected Data:")
    print(data)

    # Plotting the graph
    plt.figure(figsize=(10, 6))
    plt.plot(data['Temperature (°C)'], data['Kinematic Viscosity (cSt)'], marker='o')
    plt.title('Temperature vs Kinematic Viscosity')
    plt.xlabel('Temperature (°C)')
    plt.ylabel('Kinematic Viscosity (cSt)')
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()
