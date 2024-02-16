import random
import time

# Function to simulate motion detection
def simulate_motion_detection():
    return random.choice([True, False])

# Function to simulate ambient light intensity
def simulate_ambient_light():
    return random.uniform(0, 100)

# Function to simulate temperature changes
def simulate_temperature_change(current_temperature):
    temperature_change = random.uniform(-2, 2)
    return current_temperature + temperature_change

# Smart Home Automation Program

# User preferences
user_name = input("Enter your name: ")
light_preference = input("Enter your light preference (on/off): ").lower()
temperature_preference = input("Enter your temperature preference (warm/cool): ").lower()
security_preference = input("Enter your security preference (armed/disarmed): ").lower()

# Initial environmental conditions
ambient_light = simulate_ambient_light()
current_temperature = 22  # Initial temperature
security_system_status = "disarmed"

# Smart Home Automation Logic
print("\nSmart Home Automation System:")

# Simulating time passing and environmental changes
for _ in range(5):
    time.sleep(1)
    ambient_light = simulate_ambient_light()
    current_temperature = simulate_temperature_change(current_temperature)

    # Light Control
    if light_preference == "on" and ambient_light < 50:
        print("Turning on lights due to low ambient light ({} lux).".format(round(ambient_light, 2)))
    elif light_preference == "off":
        print("Turning off lights as per user preference.")
    else:
        print("Lights remain off.")

    # Temperature Control
    if temperature_preference == "warm" and current_temperature < 20:
        print("Increasing temperature for a warm environment ({}°C).".format(round(current_temperature, 2)))
    elif temperature_preference == "cool" and current_temperature > 25:
        print("Decreasing temperature for a cool environment ({}°C).".format(round(current_temperature, 2)))
    else:
        print("Temperature remains unchanged ({}°C).".format(round(current_temperature, 2)))

    # Security Control
    if security_preference == "armed" and simulate_motion_detection():
        print("Security alarm triggered due to motion detection.")
    elif security_preference == "disarmed":
        print("Security system disarmed as per user preference.")
    else:
        print("Security system remains unchanged.")

# End of Program
print("\nThank you, {}! Smart home automation completed.".format(user_name))
