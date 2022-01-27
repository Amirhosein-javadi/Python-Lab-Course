# **IPtables**

# Ping google.com
```
ping google.com

Pinging google.com [142.250.185.174] with 32 bytes of data:
Reply from 142.250.185.174: bytes=32 time=229ms TTL=111
Reply from 142.250.185.174: bytes=32 time=136ms TTL=111
Reply from 142.250.185.174: bytes=32 time=134ms TTL=111
Reply from 142.250.185.174: bytes=32 time=144ms TTL=111

Ping statistics for 142.250.185.174:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 134ms, Maximum = 229ms, Average = 160ms
```

# Blocking the IP of google
```
sudo iptables -A OUTPUT -s 0/0 -d 142.250.185.174 -j DROP

PING google.com (1142.250.185.174) 56(84) bytes of data.
ping: sendmsg: Operation not permitted
ping: sendmsg: Operation not permitted
ping: sendmsg: Operation not permitted
ping: sendmsg: Operation not permitted
ping: sendmsg: Operation not permitted
```
# Removing the rules
```
sudo iptables -F
```
before the code:
```
sudo iptables -L

Chain INPUT (policy ACCEPT)
target     prot opt source               destination         

Chain FORWARD (policy ACCEPT)
target     prot opt source               destination         

Chain OUTPUT (policy ACCEPT)
target     prot opt source               destination         
DROP       all  --  anywhere             mct01s05-in-f78.1e100.net 
```
after the code:
```
sudo iptables -L

Chain INPUT (policy ACCEPT)
target     prot opt source               destination         

Chain FORWARD (policy ACCEPT)
target     prot opt source               destination         

Chain OUTPUT (policy ACCEPT)
target     prot opt source               destination
```

# Block the IP of google with Iptables -A
```
sudo iptables -A INPUT -s 142.250.185.174 -j DROP
ping google.com
PING google.com (142.250.185.174) 56(84) bytes of data.
```
We didn't get any response because we drop the packages from the source.

# Iptables -L
lists your current rules in iptables.
```
target     prot opt source               destination         
DROP       all  --  fra24s11-in-f14.1e100.net  anywhere            

Chain FORWARD (policy ACCEPT)
target     prot opt source               destination         

Chain OUTPUT (policy ACCEPT)
target     prot opt source               destination 
```
New rule added!

# Blocking 192.168.2.x
```
sudo iptables -A INPUT -s 192.168.2.0/24 -j DROP
```
# Rules
```
iptables -A INPUT -i lo -p all -j ACCEPT 
```
It is a rule so your computer to be able to access itself through the loopback interface.

```
iptables -A INPUT -p all -s localhost -i eth0 -j DROP
```
It is a rule so that drop alll the packages from localhost and eth0 interface and all protocols.

```
iptables -A INPUT -s 0/0 -i eth0 -d 192.168.1.1 -p TCP -j ACCEPT
```
It is a rule that accept the packets using TCP protocols and are from localhost and interface eth0.

```
iptables -A FORWARD -s 0/0 -i eth0 -d 192.168.1.58 -o eth1 -p TCP --sprt 1024:65535 --dport:80 -j ACCEPT:
```
It forward all the packets from the port 1024-65535 and the interface eth0 and source localhost to the destination of 192.168.1.58 and port 80 and the Tcp protocol.

# Block http and https
```
iptables -I OUTPUT -m tcp -p tcp --dport 443 -j DROP
iptables -I OUTPUT -m tcp -p tcp --dport 80 -j DROP
```
# Limit ping packages to 5/min
```
iptables -A INPUT -p icmp -m icmp --icmp-type address-mask-request -j DROP
iptables -A INPUT -p icmp -m icmp --icmp-type timestamp-request -j DROP
iptables -A INPUT -p icmp -m icmp --icmp-type 8 -m limit --limit 5/second -j ACCEPT
```
# Only enable Input ssh
```
sudo iptables -I OUTPUT -m tcp -p tcp --dport 22 -j DROP
```

# Stop TCP/UDP traffic
```
sudo iptables -A INPUT -p tcp -j DROP
sudo iptables -A INPUT -p udp -j DROP
```
# Protecting a server
1) firewall 
2) locking down everything other than SSH
3) limit the maxmimum number of packages/min.
