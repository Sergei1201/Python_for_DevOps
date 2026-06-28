# Task 2. Script that output all configuration of a router/switch to a text file and onto the screen. Uses paramiko module to handle SSH connections

import paramiko # to handle SSH connections
import getpass # for securely getting passwords
import datetime # to handle date and time
import time # For using sleep method (delays)

# Input from the user
host: str = input("Enter device IP for connection: ")
user: str = input("Enter username: ")
passwd: str = getpass.getpass("Enter password: ") # get password securely with getpass() method

# Initialize SSH client according to the task instructions
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # Autoadd policy for unknown SSH host keys

# Try connecting to the device
try:
    print(f"Trying to connect to {host}")
    # Connection using the connect method of ssh client
    ssh_client.connect(host, user=user, passwd=passwd, look_for_keys=False) # look_for_keys defines if paramiko searches for a private key automatically

    # Start the shell after connection has been established by using invoke_shell() method
    shell = ssh_client.invoke_shell()

    # Send command to show configuration
    shell.send("Show running-config\n ")

    # Wait for the command to finish
    time.sleep(3) # Wait for 3 seconds

    # Output receiving
    output_receiving = shell.recv(65535).decode('utf-8')

    # Show config onto the screen
    print("=" * 40) # for better formatting
    print("Device configuration")
    print("=" * 40)
    print(output_receving)

    # Save the output to a file with timestamps
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    fname = f"{host}_config_{ts}.txt"

    
    # Write to file
    with open(fname, 'w') as file:
        file.write(output_receving)

    # Show the user that info has been written to a file
    print(f"The configuration has been written to {file}")

    # After we're done, close the connection
    ssh_client.close()

# Handle exceptions
except Exception as e:
    print("Error {e}")


