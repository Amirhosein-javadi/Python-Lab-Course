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
after that code:
```
sudo iptables -L
Chain INPUT (policy ACCEPT)
target     prot opt source               destination         

Chain FORWARD (policy ACCEPT)
target     prot opt source               destination         

Chain OUTPUT (policy ACCEPT)
target     prot opt source               destination
```
