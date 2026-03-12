"""
This is a Docstring.
It's a multi-line comment usually placed at the top of a script or function
to explain its overall purpose.
Example: "This script scans a target IP for open ports."
"""

# 1. Variables and Print statements
target_ip = "192.168.1.100"  # We will attack... I mean, 'test' this IP.
print("Target identified:", target_ip)

# 2. Indentation (The heart of Python's readability)
is_vulnerable = True

# Notice the 4 spaces before the print statement! This is required.
if is_vulnerable:
    print("Vulnerability found! Exploiting...")
    # print("This would cause an IndentationError if it wasn't aligned properly.")

# 3. Multiple Statements on a Single Line (Not recommended, but possible)
port_http = 80; port_https = 443; print(f"Checking ports {port_http} and {port_https}...")
