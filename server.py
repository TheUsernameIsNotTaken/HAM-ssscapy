# This is a sample receiver and returner for the ScaPy IPv6 Packet creation script.
# Created by Mate Vagner

# Imports
import scapy.all as sp
import time

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Sniff for packets
    s = sp.sniff(filter="ip6 and tcp dst port 9090", count=1)
    s_p = s[0]
    print(" --- Received packet to send: \n")
    s_p.show()
    # Get the sender address
    orig_src = s[0].getlayer(sp.IPv6).src
    print(" --- Source IP6 address: \n\t" + orig_src)

    # Write out the payload
    rec_tcp = s_p[sp.TCP]
    rec_pl = rec_tcp.payload.load.decode('ascii')
    print(" --- Received payload: \n" + rec_pl)

    # Do something
    time.sleep(1)
    # Generate return header
    a = sp.Ether() / sp.IPv6(dst=orig_src) / sp.TCP(sport=9000, dport=9090)
    # Generate payload
    data = "ITU packet received.\n\tFrom: RSU"

    # Send answer
    p = sp.sendp(a/sp.Raw(load=data), iface="enp0s3")
    print("Answer send")
