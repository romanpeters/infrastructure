import re

ANSIBLE_INVENTORY_PATH = "inventory.ini"
SSH_CONFIG_FILE_PATH = "roles/base/files/ssh/config"

def generate_ssh_config(inventory_path, output_path):
    with open(inventory_path, 'r') as inventory_file:
        inventory_content = inventory_file.read()

    pattern = re.compile(r'(\S+)\s+ansible_host=(\S+)(?:\s+ansible_user=(\S+))?')

    ssh_config_entries = []
    for match in sorted(pattern.finditer(inventory_content), key=lambda m: m.group(2)):
        host_name = match.group(1)
        host_address = match.group(2)
        ansible_user = match.group(3) if match.group(3) else ""
        ssh_config_entries.append(f"Host {host_name}\n    Hostname {host_address}\n    User {ansible_user}")

    with open(output_path, 'w') as output_file:
        output_file.write('\n\n'.join(ssh_config_entries))

if __name__ == "__main__":
    generate_ssh_config(ANSIBLE_INVENTORY_PATH, SSH_CONFIG_FILE_PATH)
    print(f"SSH config file generated at {SSH_CONFIG_FILE_PATH}")

