import socket

print("Simple Network Port Scanner")
print("----------------------------")

target = input("Enter target IP address: ")

ports = [21,22,23,25,53,80,110,139,143,443,445,3389]

print(f"\nScanning {target}...\n")

for port in ports:
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)

    result = scanner.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} is OPEN")
    else:
        print(f"Port {port} is CLOSED")

    scanner.close()

print("\nScan completed.")