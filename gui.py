from appJar import gui
import IP_scanner
import port_scanner

app = gui("Port Scanner", "600x400")
app.addLabel("title", "CNPS")
              
def startGui():
    app.addLabelEntry("Target IP")
    app.addButton("Scan Manual IP", press)
    app.addListBox("list", [])
    app.addButtons(["Get Network IPs", "Scan Selected IP", "Port Scan all IPs", "Cancel Scan"], press)
    app.go()
    globals()['app'] = app
    return app

def press(button):
    if button == "Get Network IPs":
        networkIPs = IP_scanner.getNetworkIPs()
        app.addListItems("list", networkIPs)
        app.deselectAllListItems("list", callFunction = False)
        
    elif button == "Scan Selected IP":
        print(app.getListBox('list'))
        selectedIP = app.getListBox('list')
        selectedIP = ' '.join(map(str, selectedIP))
        print(str(selectedIP))
        port_scanner.startScanningTarget(str(selectedIP))
        
    elif button == "Port Scan all IPs":
        print("Scanning Ports for all IPs\n") 
    elif button == "Cancel":
        quit()
        