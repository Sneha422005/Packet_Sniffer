from scapy.all import sniff, IP, TCP, UDP, ICMP

def packet_callback(packet):
    print("\n--- Packet Captured ---")
    # Check if the packet has an IP layer
    if IP in packet:
        ip_layer = packet[IP]
        print(f"Source IP: {ip_layer.src}")
        print(f"Destination IP: {ip_layer.dst}")
        print(f"Protocol: {ip_layer.proto}")
        
        # Check for specific protocols and extract details
        if TCP in packet:
            tcp_layer = packet[TCP]
            print(f"TCP Source Port: {tcp_layer.sport}")
            print(f"TCP Destination Port: {tcp_layer.dport}")
        elif UDP in packet:
            udp_layer = packet[UDP]
            print(f"UDP Source Port: {udp_layer.sport}")
            print(f"UDP Destination Port: {udp_layer.dport}")
        elif ICMP in packet:
            print("ICMP Packet")
        
        # Display raw payload if available
        if packet.payload:
            print(f"Payload: {bytes(packet.payload).hex()[:50]}...")  # Limit display to 50 bytes
    
    else:
        print("Non-IP Packet")

# Start sniffing packets
print("Starting packet sniffing... Press Ctrl+C to stop.")
sniff(prn=packet_callback, store=False)
