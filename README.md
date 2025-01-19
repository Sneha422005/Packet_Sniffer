# Packet_Sniffer
This Python-based packet sniffer tool captures and analyzes network packets. It displays relevant information such as source and destination IP addresses, protocols (TCP, UDP, ICMP), and payload data.

## **Table of Contents**
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)

---

## **Installation**

### **Step 1: Install Npcap (Required for Windows)**

**Npcap** is a necessary library for sniffing packets on Windows. It provides raw packet capture functionality for Scapy.

1. **Download Npcap**:
   - Go to the [Npcap Download Page](https://nmap.org/npcap/).
   - Download the latest stable version.

2. **Install Npcap**:
   - Run the installer.
   - Make sure to select the option **"Install Npcap in WinPcap API-compatible mode"** during installation.
   - Choose the option to **allow Npcap to run in Admin-only mode**.

### **Step 2: Install Python Dependencies**

1. Open **VS Code** or your terminal and create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv

 2. Activate the virtual environment
  - **On Windows**:
    ```bash
     .\venv\Scripts\activate
    ```
  - **On macOs/Linux**:
    ```bash 
      source venv/bin/activate
    ```
 3. Install the required Python libraries:
    ```bash
      pip install scapy
    ```
### **Step 3: Run the Script**

1. After completing the installation, run the Python script using:
   ```bash
     python packet_sniffer.py
   ```

## **Usage**
  Once the script is running, it will start capturing packets from your network. The script will display information for each packet, including:

 - Source IP address
 - Destination IP address
 - Protocol (TCP, UDP, ICMP)
 - Source and destination ports (for TCP/UDP packets)
 - Packet payload (in hexadecimal)

## **Dependencies**

  - **Python** (>=3.x)
  - **Scapy**:A Python library used for packet crafting and sniffing.
  - **Npcap**: A packet capture driver for Windows (required for raw packet sniffing).

To install the dependencies, use the following commands:
```bash
pip install scapy
```



     
