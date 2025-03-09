# ARP Spoofer

This is a simple ARP spoofing tool written in Python using the Scapy library. It allows you to perform a man-in-the-middle attack by spoofing ARP packets.

## Requirements

- Python 3.x
- Scapy library

## Installation
To install NetworkScanner, follow these steps:

1. Clone the repository:
   ```sh
   git clone https://github.com/andymartinez1/ARP-Spoofer.git
   ```
2. Navigate to the project directory:
   ```sh
   cd ARP-Spoofer
   ```
3. Install the required dependencies:
   ```sh
   pip install scapy
   ```

## Usage

1. Run the script with root privileges:
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
 ## Contributing

   I am open to contributions! Please follow these steps to contribute:

   1. Fork the repository.
   2. Create a new branch:
      ```sh
      git checkout -b feature-branch
      ```
   3. Make your changes and commit them:
      ```sh
      git commit -m "Description of your changes"
      ```
   4. Push to the branch:
      ```sh
      git push origin feature-branch
      ```
   5. Create a pull request.
