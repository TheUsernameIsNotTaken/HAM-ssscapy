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
>>> ls(IPv6)
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

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    # Scapy basic routing.
    print(sp.get_if_list())
    print(sp.conf.ifaces)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
