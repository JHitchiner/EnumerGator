#!/usr/bin/python

from subprocess import call
import sys
import os

def nmapScan(scanType, targetIP, path):

    if(scanType == "Standard"):
        print("Running standrd nmap scan...")
        command = "nmap -sV -sC " + targetIP + " -oN " + path + "/nmapStd.txt >/dev/null"
        r = os.system(command)
        print("Finished scan.")
        return

    elif(scanType == "Quick"):
        print("Running quick nmap scan...")
        command = "nmap " + targetIP + " -oN " + path + "/nmapQuick.txt >/dev/null"
        r = os.system(command)
        print("Finished scan.")
        return

    elif(scanType == "Full"):
        print("Running full nmap scan...")
        if(os.getuid() != 0):
            print("Root permissions required for full scan, re-run scirpt with sudo.")
            return
        else:
            command = "nmap -sSUV -sC -O -p- " + targetIP + " -oN " + path + "/nmapFull.txt >/dev/null"
            r = os.system(command)
            print("Finished scan.")
            return

    elif(scanType == "SMB"):
        print("Running SMB scan...")
        command = "nmap --script smb-enum-shares -p 139,445 " + targetIP + " -oN " + path + "/smbscan.txt >/dev/null"
        r = os.system(command)
        print("Finished scan.")
        return

    else:
        print("Error: Could not identify scan type.")
        return
