from scapy.all import *

ports=[25,80,53,443,445,8080,8443]

def SynScan(host):
    ans,unans=sr(IP(dst=host)/TCP(sport=5555,dport=ports,flags="S"),timeout=2,verbose=0)
    print("Open ports at %s:" % host)
    for(s,r,)in ans:
        if s[TCP].dport== r[TCP].sport:
            print(s[TCP].dport)

def DNSScan(host):
    ans,unans=sr(IP(dst=host)/UDP(sport=5555,dport=53)/DNS(rd=1,qd=DNSQR(qname="google.com")),timeout=2,verbose=0)
    if ans:
        print("DNS server at %s"%host)

host ="8.8.8.8"
SynScan(host)
DNSScan(host)

def tcp_scan(dst_ip,dport):
    #to check if destination port is open by sending packets with syn flags.
    packet=IP(dst=dst_ip)/TCP(dport=dport)
    ans,unans=sr(pkt,timeout=2,verbose=0)
    if not ans:
        print(f"Host {dst_ip} is Offline")
    else:
        for sent,recv in ans:
            if recv[TCP].flags == "SA":
                print(f"Port {dport} on host {dst_ip} is open")
            else:
                print(f"Port {dport} on host {dst_ip} is closed but host is online")
        
tcp_scan(192.168.1.140,80)