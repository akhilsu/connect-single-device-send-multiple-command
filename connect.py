from netmiko import ConnectHandler

commands = ["show version","show platform","show processes cpu","show memory summary","show bgp scale"]

device = {
    "device_type" : "cisco_ios",
    "ip" : "10.10.10.10",
    "username" : "root",
    "password" : "root@123",
    "port" : 22
}

connectdevice = ConnectHandler(**device)
for j in commands:
    fetch = connectdevice.send_command(j)
    print(fetch)
connectdevice.disconnect()
