# --- SETS (Unique Items Only) ---

# Scenario 1: Deduplication (Removing duplicate IPs from a log)
log_ips = ["192.168.1.5", "10.0.0.1", "192.168.1.5", "10.0.0.1", "172.16.0.2"]
print(f"Total IPs extracted: {len(log_ips)}")

# Convert list to a set to remove duplicates instantly
unique_ips = set(log_ips)
print(f"Unique IPs to investigate: {unique_ips}")
print(f"Total Unique IPs: {len(unique_ips)}")

# Scenario 2: Set Operations (Intersection, Union, Difference)
server1_ports = {22, 80, 443}
server2_ports = {80, 443, 3306, 8080}

# What ports do BOTH servers have open? (Intersection)
common_ports = server1_ports.intersection(server2_ports)
print(f"\nCommon Open Ports: {common_ports}")

# What ports are open on Server 1 but NOT on Server 2? (Difference)
unique_to_server1 = server1_ports.difference(server2_ports)
print(f"Ports only on Server 1: {unique_to_server1}")

# Combine all unique open ports from both servers (Union)
all_open_ports = server1_ports.union(server2_ports)
print(f"All distinct open ports across infrastructure: {all_open_ports}")
