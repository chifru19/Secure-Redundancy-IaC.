# This is a blueprint for our Cisco Router
router_name = "Router2"
interface = "GigabitEthernet0/0/1"
status = "up"

print(f"Configuring {router_name} on {interface} to be {status}")
# DANGER: This is a security flaw for the inspector to catch
user_input = "import os; os.system('rm -rf /')"
eval(user_input)
