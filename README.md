# ARP Spoofer

This is a simple ARP spoofing tool written in Python using the Scapy library. It allows you to perform a man-in-the-middle attack by spoofing ARP packets.

## Requirements

- Python 3.x
- Scapy library

## Installation

1. Install Python 3.x from [python.org](https://www.python.org/).
2. Install Scapy using pip:
   ```sh
   pip install scapy
   ```

## Usage

1. Clone the repository or download the script.
2. Open a terminal and navigate to the directory containing the script.
3. Run the script with root privileges:
   ```sh
   sudo python3 ARPSpoofer.py
   ```

## Configuration

- Modify the `target_ip` and `gateway_ip` variables in the script to match the IP addresses of the target machine and the gateway (router).

## Enabling IP Forwarding

To enable IP forwarding on Linux, run the following command:

```sh
   echo 1 > /proc/sys/net/ipv4/ip_forward
```
