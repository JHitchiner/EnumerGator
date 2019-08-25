#!/usr/bin/python

from subprocess import call
import sys
import os
import datetime
from argparse import ArgumentParser
from nmapModule import *

targetIP = "0.0.0.0" #Make global
outputFile = "" #Make global

def main():
    #Parse arguments
    parser = ArgumentParser(description="Enumerator 1.0")
    parser.add_argument("-nS", "--nmapStd", help="Standard nmap scan (sV sC)",
                        action="store_true")
    parser.add_argument("-nQ", "--nmapQuick", help="Fast nmap scan",
                        action="store_true")
    parser.add_argument("-nF", "--nmapFull", help="Nmap scan all ports",
                        action="store_true")
    parser.add_argument("-g", "--gobuster", help="Gobuster scan",
                        action="store_true")
    parser.add_argument("-s", "--smbmap", help="SMBMap scan",
                        action="store_true")

    parser.add_argument("-t", "--target", help="Host target IP", required=True)

    args = parser.parse_args()

    # Save targetIP for most function calls as commands will need it
    targetIP = args.target

    #Print Args List for debugging
    #print(args)

    #Test if host is up
    print("Testing if target is alive...")
    r = os.system("ping -c 1 "+targetIP+" > /dev/null")
    if r == 0:
        print(targetIP+" is alive!")
    else:
        print(targetIP+" is down...")
        sys.exit(0)

    #Start Enumeration with given flags
    print("Starting Enumeration...")

    #Create folder for output to end up in, name it Scan-(Time)
    dirName = "/Scan-" + datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    path = os.getcwd() + dirName
    try:
        os.mkdir(path)
    except OSError:
        print("Creation of %s failed" % dirName)
        path = "FALSE" # Set to false so can check if it failed later on aswell
    else:
        print("Created %s directory" % dirName)

    # nmap flags should be checked and run first, then move on to secondary flags
    # Only 1 nmap flag should be activated, if multiple have been default to std
    if(args.nmapStd == True):
        nmapScan("Standard", targetIP, path)
    elif(args.nmapQuick == True):
        nmapScan("Quick", targetIP, path)
    elif(args.nmapFull == True):
        nmapScan("Full", targetIP, path)

    # Check rest of flags
    if(args.gobuster == True):
        print("gobuster")

    if(args.smbmap == True):
        print("smbmap")

if __name__ == "__main__":
    main()
