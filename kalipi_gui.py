import subprocess
import tkinter as tk
import tkinter.font as tkFont
#author: insertuserIDhere
#gui for the kali pi written in python, still needs to be modified to be executable on kali linux

#define the commands for each button
button_commands = [    ["nmap", "gnome-terminal -- nmap"],
    ["metasploit", "gnome-terminal -- msfconsole"],
    ["hydra", "gnome-terminal -- hydra"],
    ["john the ripper", "gnome-terminal -- john"],
    ["aircrack-ng", "gnome-terminal -- aircrack-ng"],
    ["wireshark", "gnome-terminal -- wireshark"],
]

button_commands2 = [    ["nikto", "gnome-terminal -- nikto"],
    ["sqlmap", "gnome-terminal -- sqlmap"],
    ["netcat", "gnome-terminal -- nc"],
    ["nbtscan", "gnome-terminal -- nbtscan"],
    ["dirb", "gnome-terminal -- dirb"],
    ["gobuster", "gnome-terminal -- gobuster"],
]

#create a function to execute the command for the button
def run_command(command):
    if command == "page2":
        create_page2()
    elif command == "page1":
        create_page1()
    else:
        subprocess.Popen(command, shell=True)

#create a function to create the page
def create_page(buttons):
    #clear the window
    for widget in root.winfo_children():
        widget.destroy()

    #add the buttons
    for i in range(len(buttons)):
        button = tk.Button(root, text=buttons[i][0], font=("Arial", 14), fg="#00ffff", bg="#1c1c1c", bd=1, activebackground="#00ff00", activeforeground="#1c1c1c", command=lambda cmd=buttons[i][1]: run_command(cmd))
        button.place(x=20 + (i % 2) * 240, y=20 + (i // 2) * 50, width=200, height=30)

    #add the "back" button (on second page only)
    if buttons == button_commands2:
        back_button = tk.Button(root, text="back", font=("Arial", 14), fg="#00ffff", bg="#1c1c1c", bd=1, activebackground="#00ff00", activeforeground="#1c1c1c", command=create_page1)
        back_button.place(x=140, y=160, width=200, height=30)

    #add the "more tools" button (on first page only)
    if buttons == button_commands:
        more_tools_button = tk.Button(root, text="more tools", font=("Arial", 14), fg="#00ffff", bg="#1c1c1c", bd=1, activebackground="#00ff00", activeforeground="#1c1c1c", command=create_page2)
        more_tools_button.place(x=140, y=160, width=200, height=30)

#create the first page
def create_page1():
    create_page(button_commands)

#create the second page
def create_page2():
    create_page(button_commands2)

#create the main window
root = tk.Tk()
root.geometry("480x320")


root.configure(bg="#1c1c1c")


#create the buttons for the first page
create_page1()

#run the window
root.mainloop()
