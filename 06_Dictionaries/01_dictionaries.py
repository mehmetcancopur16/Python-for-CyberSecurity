# --- DICTIONARIES (Key:Value mapping) ---
# Imagine we scanned a target and want to store its profile neatly.

target_host = {
    "ip": "10.10.10.5",
    "hostname": "WinServer01",
    "os": "Windows",
    "open_ports": [80, 445, 3389],
    "is_vulnerable": True
}

# 1. Accessing Data
print(f"Target IP: {target_host['ip']}")
print(f"Open Ports: {target_host['open_ports']}")

# 2. Modifying Data
# We found another open port during our scan!
target_host["open_ports"].append(21)
print(f"Updated Ports: {target_host['open_ports']}")

# 3. Adding New Key:Value pairs
# We discovered the admin username
target_host["admin_user"] = "Administrator"

# 4. Iterating through a Dictionary
print("\n--- Target Profile Summary ---")
for key, value in target_host.items():
    print(f"{key.capitalize()}: {value}")

# 5. Safe Access with .get()
# If you try to access a key that doesn't exist (e.g., target_host["mac_address"]), 
# your script will crash. Use .get() to return None or a default value instead.
mac = target_host.get("mac_address", "Not Found")
print(f"\nMAC Address: {mac}")
