# EnumerGator
Little side project automating some basic pen testing enumeration :)

## Dependancies
nmap, python, gobuster

Basically just run this on kali linux and it should be sweet

## Usage
Running python enum.py -h will bring up an arguments list.
All arugments optional except -t (target IP address)

Output of scans will be saved as logs in a directory created where the script is run called "Scan-(Time of scan initiation)"

Note: Some arugments such as a full nmap scan will require the script to be run with root permissions
