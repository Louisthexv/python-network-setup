import random

# Function to generate a random IP address in the specified class
def generate_random_ip(network_class):
    if network_class == 'A':
        ip = f"10.{random.randint(0, 255)}.{random.randint(0, 255)}.1/24"
    elif network_class == 'B':
        ip = f"172.{random.randint(16, 31)}.{random.randint(0, 255)}.1/24"
    elif network_class == 'C':
        ip = f"192.168.{random.randint(0, 255)}.1/24"
    else:
        return "Invalid network class"

# Prompt the user for the network class
network_class = input("Choose a network class (A, B, C): ").upper()

# Generate and print a random IP address
random_ip = generate_random_ip(network_class)
if random_ip != "Invalid network class":
    print(f"Random {network_class} IP Address: {random_ip}")
else:
    print("Invalid network class chosen.")

print("\nThis tool is currently developed for the Linux environment.")
print("macOS and Windows versions will be available in the future.")
print("Thank you for your understanding.")
