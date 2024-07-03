#Header Comments.

#Name: Rwebyogo24
#Course ID & Section: COP2002.0M1
#Date created: July 2, 2024
#Program title: Functions Part 2
#Brief description: Project 5 - Using the functions for output


import random

def numToName(portNumArray, portNameArray, portNumber):
    """Given a port number, identify the corresponding protocol (abbreviation). Using 3 arguments: a list of port numbers (portNumArray), a list of corresponding protocol names (portNameArray), and a string of port numbers to identify the portNumber."""
    
    for x in range(len(portNumArray)):
        if portNumber == portNumArray[x]:
            #portNameArray.append(portNameArray[x])
            return portNameArray[x]


def nameToNum(portNumArray, portNameArray, portName):
    """Given a port protocol, identify the corresponding port number. Using 3 arguments: a List of port numbers (portNumArray), a list of corresponding protocol names (portNameArray), and a string of Protocol names to identify the portName."""
    array = []
    for x in range(len(portNameArray)):
        if portName == portNameArray[x]:
            array.append(portNumArray[x])
    print(array)   
    return array
           


def getInput():
    """Gets users input for menu choice and returns a string for users input choice."""
    choice = ""
    while choice not in {"1", "2", "3"}:
        choice = input("Choice:  ").rstrip().lower()
        
    return choice
       
def main():
    """The main function to run the program"""

    
    portNumArray = ["20", "21", "22", "23", "25", "53", "67", "68", "80", "110", "137", "139", "143", "161", "162", "389", "443", "445", "3389"]                #Array containing the port numbers that will be used.

    
    portNameArray = ["FTP", "FTP", "SSH", "Telnet", "SMTP", "DNS", "DHCP", "DHCP", "HTTP", "POP3", "NetBIOS", "NetBIOS", "IMAP", "SNMP", "SNMP", "LDAP", "HTTPS", "SMB", "RDP"]             # Array containing the port names that will be used.    
    
    
    while True:
       # Choices given to the user.
        print("\nMain Menu:")
        print("1.  Given a port number, identify the PROTOCOL (use abbreviation).")
        print("2.  Given a port protocol, identify a port NUMBER.")
        print("3.  Exit\n")
        choice = getInput()
       
        # First option. Num ----> Name
        if choice == "1":
            print("Option 1:  Identify the port's PROTOCOL.")
            print("----------------------------------------\n")
            
            while True:  
                portNumber = random.choice(portNumArray)
                
                portName = numToName(portNumArray, portNameArray, portNumber)
                user_answer = ""

                user_answer = input(f"What is the protocol for port {portNumber} (m=Main Menu)?  ").rstrip().upper()
                
                if user_answer.lower() == "m":
                    break

                elif user_answer in portNameArray:
                    print("Correct answer!\n")

                else:
                    print(f"Incorrect.  The correct answer is {portName}.\n")

                    

        # Second option. Name ----> Num
        elif choice == "2":
            print("Option 2:  Identify the port's NUMBER.")
            print("----------------------------------------\n")

            
            while True:                    
                portName = random.choice(portNameArray)
                
                portNumber = nameToNum(portNumArray, portNameArray, portName)
                
                user_answer = input(f"What is the number for protocol {portName} (m=Main Menu)?  ").rstrip()
                
            
                if user_answer.lower() == "m":
                    break
                    
                elif user_answer in portNumArray:
                    print("Correct answer!\n")
                else:
                    print(f"Incorrect.  The correct answer is {portNumber}.\n")

                    
        # Third option.  Program complete
        elif choice == "3":
            print("\nProgram Complete.  I hope this has helped in studying for the CompTIA A+ certification.")
            break


        
        
            
if(__name__ == "__main__"):
    main()