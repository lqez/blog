Title: Port forwarding on ‘modern’ OS X
Date: 2016-11-15
Lang: ko
Tags: os x, port, forwarding, pf
Status: draft

ipforwarding

```
# sysctl net.inet.ip.forwarding=1
# sysctl net.inet6.ip6.forwarding=1
# sysctl -a | grep forwarding
```

alias
# ifconfig lo0 172.16.6.225 alias


/etc/pf.anchors/com.forwarding
rdr pass inet proto tcp from any to 172.16.6.225 port 11211 -> 127.0.0.1 port 11211


scrub-anchor "com.apple/*"                                           
nat-anchor "com.apple/*"                                             
rdr-anchor "com.apple/*"                                             
rdr-anchor "forwarding"                                              
dummynet-anchor "com.apple/*"                                        
anchor "com.apple/*"                                                 
load anchor "com.apple" from "/etc/pf.anchors/com.apple"             
load anchor "forwarding" from "/etc/pf.anchors/com.forwarding"       



verification
$ pfctl -vnf /etc/pf.conf

reload
# pfctl -ef /etc/pf.conf 
