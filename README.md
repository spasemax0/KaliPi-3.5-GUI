This project is a Python-based GUI for Kali Pi, designed to provide quick access to various tools and commands commonly used in Kali Linux. The GUI is implemented using the Tkinter library and allows users to execute commands through a graphical interface.

Features
Tool Execution: Provides buttons to run tools like nmap, metasploit, hydra, john the ripper, aircrack-ng, and wireshark.
Pagination: Includes a secondary page for additional tools such as nikto, sqlmap, netcat, nbtscan, dirb, and gobuster.
User-Friendly Interface: Simple and intuitive GUI designed with Tkinter.
Customizable: Easy to modify and extend with additional tools and commands.

Dependencies:
Python 3.x
Tkinter
Kali Linux with the following tools installed:
nmap
metasploit
hydra
john the ripper
aircrack-ng
wireshark
nikto
sqlmap
netcat
nbtscan
dirb
gobuster

Usage Options: 
Run using python - python3 kali_pi_gui.py

Make executable - 1. add shebang at top of script and save: #!/usr/bin/env python3 
2. change permissions: chmod +x kali_pi_gui.py

You can now run the script directly with ./kali_pi_gui.py
