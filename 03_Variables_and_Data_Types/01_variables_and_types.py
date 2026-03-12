# --- VARIABLES & NAMING CONVENTIONS ---
# In Python, we use snake_case for variable names (words separated by underscores).

target_ip = "10.10.10.5"       # String (str)
target_port = 22               # Integer (int)
timeout_seconds = 1.5          # Float (float)
is_admin_access = False        # Boolean (bool)

# Let's print them and check their types using the built-in type() function.
print("Target IP:", target_ip, "| Type:", type(target_ip))
print("Target Port:", target_port, "| Type:", type(target_port))
print("Timeout:", timeout_seconds, "| Type:", type(timeout_seconds))
print("Has Admin Access?", is_admin_access, "| Type:", type(is_admin_access))

print("-" * 30) # Prints 30 dashes for a clean output

# --- TYPE CASTING (Changing Data Types) ---
# Sometimes, you receive a port number as a string from user input, 
# but you need it as an integer to make a connection.

user_input_port = "8080" # This is a string!
print("Original input type:", type(user_input_port))

# Convert string to integer
usable_port = int(user_input_port)
print("Usable port type after casting:", type(usable_port))

# Convert integer to string (useful for concatenating with other text)
log_message = "Scan completed on port " + str(usable_port)
print(log_message)
