#This program will read the USB logs from Windows and Linux System
import os
import _winreg

#Detecting System type first

if (os.name=='nt'):
    print "===Dumping Information of USB connected to this Devices==="
    #Getting details of USB from registry
    query = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, r'SYSTEM\CurrentControlSet\Enum\USBSTOR', 0)
    i = 0
    try:
        while True:
            print _winreg.EnumKey(query, i)
            i += 1

    except WindowsError:
        print("\n\n")
        pass

elif(os.name=='posix'):
    usb_logs = open("/var/log/messages", "r")
    for line in usb_logs.readlines():
        if ("usb" or "USB") in line:
            print line,
    usb_logs.close()
