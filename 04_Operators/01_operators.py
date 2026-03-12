# --- 1. ARITHMETIC OPERATORS ---
total_ports = 65535
scanned_ports = 1024
remaining_ports = total_ports - scanned_ports
print(f"Remaining ports to scan: {remaining_ports}")

# --- 2. COMPARISON OPERATORS ---
target_port = 80
is_http = (target_port == 80)  # Returns True if it is 80
print(f"Is target port HTTP (80)? {is_http}")

# --- 3. LOGICAL OPERATORS ---
has_username = True
has_password = False
# Both must be True for 'and' to return True
is_authenticated = has_username and has_password 
print(f"Is user authenticated? {is_authenticated}")

# --- 4. BITWISE OPERATORS (CyberSec Special) ---
# Let's look at XOR (^). It compares bits. If they are different, it returns 1. If same, 0.
# It is symmetric: (A XOR B) XOR B = A
original_data = 65      # ASCII for 'A'
key = 42                # Secret key

# Encrypting
encrypted_data = original_data ^ key
print(f"Encrypted data: {encrypted_data}")

# Decrypting
decrypted_data = encrypted_data ^ key
print(f"Decrypted data: {decrypted_data} (Back to original!)")
