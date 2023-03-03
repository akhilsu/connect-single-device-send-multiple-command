from netmiko import ConnectHandler

commands = ["show version","show platform"]

device = {
    "device_type" : "cisco_ios",
    "ip" : "10.197.169.68",
    "username" : "cisco",
    "password" : "root@123",
    "port" : 22
}

connectdevice = ConnectHandler(**device)
for j in commands:
    fetch = connectdevice.send_command(j)
    print(fetch)
connectdevice.disconnect()
