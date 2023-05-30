#Send show commands to multiple devices

from netmiko import ConnectHandler

#Define the device parameters
devices = [
{
    'device_type': 'cisco_ios',
    'host':   '172.16.1.4',
    'username': 'cisco',
    'password': 'cisco',
    'port' : 22,          
    'secret': 'cisco',
},
{
    'device_type': 'cisco_ios',
    'host':   '172.16.1.7',
    'username': 'cisco',
    'password': 'cisco',
    'port' : 22,          
    'secret': 'cisco',
}
]

# Define the list of show commands
commands = ['show interfaces']

# Iterate over devices
for device in devices:
    # Establish an SSH connection to the device
    connection = ConnectHandler(**device)
    connection.enable()

    # Execute the show commands
    output = ""
    for command in commands:
        output += connection.send_command(command)

    # Print the output
    print(f"Device: {device['host']}")
    print(output)

    # Close the SSH connection
    connection.disconnect()