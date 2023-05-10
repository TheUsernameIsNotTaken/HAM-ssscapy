# This is a sample ScaPy IPv6 Packet creation script.
# Created by Mate Vagner
"""
IPv6 Header:
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|Version| Traffic Class |               Flow Label              |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|        Payload Length         |   Next Header |   Hop Limit   |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                                                               |
+                                                               +
|                                                               |
+                         Source Address                        +
|                                                               |
+                                                               +
|                                                               |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                                                               |
+                                                               +
|                                                               |
+                       Destination Address                     +
|                                                               |
+                                                               +
|                                                               |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
Represented in ScaPy:
use: ls(IPv6)
version : BitField = (6)
tc : BitField = (0)
fl : BitField = (0)
plen : ShortField = (None)
nh : ByteEnumField = (59)
hlim : ByteField = (64)
src : SourceIP6Field = (None)
dst : IP6Field = (’::1’)

For Header Extensions and more please read: 'IPv6 Packet Creation With Scapy' at https://www.idsv6.de/Downloads/IPv6PacketCreationWithScapy.pdf
"""

# Imports
import scapy.all as sp

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Scapy basic routing.
    print(" --- Interfaces: \n" + str(sp.get_if_list()))
    print(" --- IPv6 Route table: \n" + str(sp.conf.route6))
    print(" --- Router address: \n" + str(sp.conf.route6.route("fe80::/64")[2]))

    # Special IPv6 address
    my_add = '::abcd'

    # Generate a packet
    a = sp.Ether()/sp.IPv6(src=my_add, dst='::1')/sp.TCP(sport=9000, dport=9090)
    print(" --- Base packet send: \n" + str(a))

    # Generate payload
    data = "Hello RSU!\n\tFrom: ITU"

    # Send packet and receive answer
    p = sp.sendp(a/sp.Raw(load=data), iface="enp0s3", count=1, inter=1)

    # Receive return packet
    print("Waiting for answer")
    # INSERT_IP = REDACTED
    # s = sp.sniff(filter="ip6 host " + INSERT_IP + " and tcp dst port 9090", count=1)
    s = sp.sniff(filter="ip6 and tcp dst port 9090", count=1)   # dst host " + my_add + "
    s_p = s[0]

    # Write out the answer payload
    rec_tcp = [sp.TCP]
    rec_pl = rec_tcp.payload.load.decode('ascii')
    print(rec_pl)
