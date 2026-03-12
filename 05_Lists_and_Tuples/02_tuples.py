# --- TUPLES (Immutable) ---
# We want to define our target server. We don't want any part of our script
# to accidentally change this IP or Port during execution.

target_server = ("192.168.1.10", 443)
print(f"Target Server Conf: {target_server}")

# Accessing is the same as lists
print(f"Target IP: {target_server[0]}")
print(f"Target Port: {target_server[1]}")

# UNPACKING A TUPLE
# We can extract values directly into variables
ip, port = target_server
print(f"Connecting to {ip} on port {port}...")

# If we try to change a tuple, Python will throw a TypeError.
# target_server[1] = 80  # Un-commenting this line will crash the script!
