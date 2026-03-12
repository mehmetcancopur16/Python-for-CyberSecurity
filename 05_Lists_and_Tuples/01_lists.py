# --- LISTS (Mutable) ---
# Let's say we are writing a port scanner and we found some open ports.

open_ports = [21, 22, 80, 443]
print(f"Initially discovered ports: {open_ports}")

# We found another one! Let's append it to the end of the list.
open_ports.append(8080)
print(f"Ports after finding 8080: {open_ports}")

# Oh wait, port 21 is a honeypot, let's remove it.
open_ports.remove(21)
print(f"Ports after removing 21: {open_ports}")

# Accessing elements via Index (Python is 0-indexed!)
first_port = open_ports[0]
print(f"The first port in our list is: {first_port}")

# Slicing a list (getting a subset)
web_ports = open_ports[1:3] # Gets index 1 and 2 (stops before 3)
print(f"Web ports extracted: {web_ports}")
