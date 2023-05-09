# This is a sample receiver and returner for the ScaPy IPv6 Packet creation script.
# Created by Mate Vagner

# Imports
import scapy.all as sp
import time

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Sniff for packets
    s = sp.sniff(filter="ip6 and tcp dst port 9090", count=1)
    s[0].show()
    orig_src = s[0].getlayer(sp.IPv6).src
    print(orig_src)
    a = sp.Ether()/sp.IPv6(dst=orig_src)/sp.TCP(sport=9000, dport=9090)
    print(a)
    time.sleep(1)
    p = sp.sendp(a, iface="enp0s3")
    print("Answer send")
