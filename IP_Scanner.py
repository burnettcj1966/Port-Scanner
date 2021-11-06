from scapy.all import ARP, Ether, srp
import socket

#based on users internal IP, performs a scan of their network for all IPs using ARP
def IPscan(target_ip):

    #add subnet
    target_ip = target_ip + "/24"

    arp = ARP(pdst=target_ip)

    #create packet
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    result = srp(packet, timeout=3, verbose=0)[0]
    clients = []

    #add recieved IPs/MACs
    for sent, received in result:
        clients.append({'ip': received.psrc, 'mac': received.hwsrc})

    print("Available devices in the network:")
    print("IP" + " "*18+"MAC")
    for client in clients:
        print("{:16}    {}".format(client['ip'], client['mac']))


#gets the users internal networks IP
def get_internal_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

def printNetworkIPs():
    internalIP = get_internal_ip()
    IPscan(internalIP)

