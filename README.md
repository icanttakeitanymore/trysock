# trysock
Использование как nmap.

boris@SL06002508013:~/git/tcpchecker$ for i in $(seq 1 1000); do ./tcpchecker.py -a 192.168.1.1 -p $i; done | grep 
succes
Connection to 192.168.1.1:21 succesfully!
Connection to 192.168.1.1:80 succesfully!
Connection to 192.168.1.1:111 succesfully!
Connection to 192.168.1.1:222 succesfully!
Connection to 192.168.1.1:443 succesfully!
