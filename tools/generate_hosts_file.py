#!/usr/bin/env python3

import os
import re

ANSIBLE_INVENTORY_PATH = "inventory.ini"
ANSIBLE_HOSTS_FILE_PATH = "roles/base/files/etc/hosts"


def generate_hosts_file(inventory_path, output_path):
    with open(inventory_path, "r") as inventory_file:
        inventory_content = inventory_file.read()

    pattern = re.compile(r"(\S+)\s+ansible_host=(\S+)")

    hosts = []
    for match in sorted(pattern.finditer(inventory_content), key=lambda m: m.group(2)):
        host_name = match.group(1)
        host_address = match.group(2)
        hosts.append(f"{host_address}\t{host_name}")

    directory_path = os.path.dirname(output_path)
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    with open(output_path, "w") as output_file:
        output_file.write("\n".join(hosts))


if __name__ == "__main__":
    generate_hosts_file(ANSIBLE_INVENTORY_PATH, ANSIBLE_HOSTS_FILE_PATH)
    print(f"Hosts file generated at {ANSIBLE_HOSTS_FILE_PATH}")
