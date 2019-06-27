#!/usr/bin/python

from subprocess import call
import sys
import os
from argparse import ArgumentParser

targetIP = "0.0.0.0" #Make global
outputFile = "" #Make global

def main():
    #Parse arguments
    parser = ArgumentParser(description="Enumerator 1.0")
    parser.add_argument("-nS", "--nmapStd", help="Standard nmap scan (sV sC)",
                        action="store_true")
    parser.add_argument("-nQ", "--nmapQuick", help="Fast nmap scan",
                        action="store_true")
    parser.add_argument("-nA", "--nmapAll", help="Nmap scan all ports",
                        action="store_true")
    parser.add_argument("-g", "--gobuster", help="Gobuster scan",
                        action="store_true")
    parser.add_argument("-s", "--smbmap", help="SMBMap scan",
                        action="store_true")

    parser.add_argument("-o", "--output", help="Output file path")
    parser.add_argument("-t", "--target", help="Host target IP", required=True)

    args = parser.parse_args()

    targetIP = args.target
    if(args.output != None):
        outputFile = args.output

    #Print Args List for debugging
    #print(args)

    #Test if host is up
    print("Testing if target is alive...")
    r = os.system("ping -c 1 "+targetIP+" > /dev/null")
    if r == 0:
        print(targetIP+" is alive!")
    else:
        print(targetIP+" is down...")
        sys.exit()

    #Start Enumeration with given flags
    print("Starting Enumeration...")

if __name__ == "__main__":
    main()
