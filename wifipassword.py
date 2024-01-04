import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')

# Now we will store the profiles by converting them to a list
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

# Using a for loop in Python, we are checking and printing Wi-Fi passwords
for i in profiles:
    try:
        result = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'keyMaterial=clear']).decode('utf-8').split('\n')

        # Storing password after converting them to a list
        result = [b.split(":")[1][1:-1] for b in result if "Key Content" in b]

        print("{:<30} | {:<}".format(i, result[0]))
    except subprocess.CalledProcessError as e:
        print(f"Error retrieving password for profile '{i}': {e}")
