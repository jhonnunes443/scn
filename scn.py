import os
import subprocess



class menu:
    def __init__(self):
        self.path = "README.md"

    def list_tools(self):
        print("\n########## Tools ##########\n")
        tools = []  # Para armazenar as ferramentas e seus links
        try:
            with open(self.path, "r") as file:
                lines = file.readlines()
            
            if not lines:
                print("[WARNING] The file is empty.")
                return
            
            id_counter = 1  # Começa a contagem em 1
            tools_found = False  # Para rastrear se alguma ferramenta foi encontrada
            
            for line in lines:
                line = line.strip()
                if line.startswith('- [') and '](' in line:
                    # Extrai o nome e o link da ferramenta
                    start_bracket = line.index('[') + 1
                    end_bracket = line.index(']')
                    tool_name = line[start_bracket:end_bracket]
                    
                    start_parenthesis = line.index('(') + 1
                    end_parenthesis = line.index(')')
                    tool_link = line[start_parenthesis:end_parenthesis]

                    # Extrai a descrição
                    description = line[end_parenthesis + 1:].strip().lstrip('- ')

                    # Armazena a ferramenta e seu link
                    tools.append((id_counter, tool_name, tool_link, description))

                    # Códigos ANSI para cor amarela
                    yellow = "\033[93m"
                    reset = "\033[0m"
                    
                    print(f'{yellow}[{id_counter}]{reset} {tool_name} ({tool_link}) - {description}')  # Imprime ID, nome, link e descrição
                    tools_found = True
                    id_counter += 1
            
            if not tools_found:
                print("[WARNING] No tools found in the specified format.")
                return
            
            while True:
                install_tools = input("\nDo you wish to install some tool?\n1. Yes\n2. No\nAnswer (1 or 2): ")
                if install_tools == "1":  # Corrigido para comparar com string
                    tool_number = input("\nType number of the tool: ")
                    try:
                        tool_number = int(tool_number)
                        # Verifica se o número está na lista de ferramentas
                        if 1 <= tool_number < id_counter:
                            selected_tool = tools[tool_number - 1]  # Acessa a ferramenta selecionada
                            github_link = selected_tool[2]  # URL do GitHub
                            subprocess.run(f"git clone {github_link}", shell=True)  # Clona o repositório
                        else:
                            print("[ERROR] Invalid tool number.")
                    except ValueError:
                        print("[ERROR] Please enter a valid number.")
                elif install_tools == "2":
                    break
                else:
                    print("[ERROR] Please choose 1 or 2.")
                
        except FileNotFoundError:
            print("[ERROR] The specified file was not found.")
        except Exception as e:
            print(f"[ERROR] An unexpected error occurred: {e}")

    def panel(self):
        while True:
            panel = int(input("""\n=============== PANEL SCAN ============

Type one:

1 Scan with nmap;
2 Whois, Dns transfer zone and Dnsenum;
3 Check and install tools;
4 exit.


==============================\n
"""))

            if panel == 1:
                print("\n[+] Scan with nmap selected\n")
                nmap_scan()
                
            elif panel == 2:
                print("[+] Dnsenum, Whois selected\n")
                whois_dns()
                zone_transfer()
                enum = input("\nWould you like try to enum dns servers [y/n]?: ")
                if enum == "y" or "yes":
                    dns_enum()
                    print("Finishing all the processes...")
                    break
                elif enum == "n" or "no":
                    print("Finishing all the processes...")
                    break
                else: 
                    print("\n[!]Invalid answer\n")

            elif panel == 3:
                print("\n[+] List tools selected.\n")
                self.list_tools()

            elif panel == 4:
                print("Finishing program...")
                break
            else:
                print("Invalid answer")


def nmap_scan():

    try:
        #########      USE "#" TO COMENT SOME SCAN      ##########

        subprocess.run(f"nmap -sP {ip} | grep 'Nmap scan report for' | cut -d ' ' -f 5 > {dir}/ips.txt", shell=True)
        subprocess.run(f"cat {dir}/ips.txt", shell=True)
        print("\n========== Ip list result  ==========\n")


        subprocess.run(f"nmap -Pn --script=default -iL {dir}/ips.txt > {dir}/default.txt", shell=True) 
        subprocess.run(f"cat {dir}/default.txt", shell=True)
        print("\n========== default.txt created  ==========\n")

        subprocess.run(f"nmap -Pn --script vuln -iL {dir}/ips.txt > {dir}/vuln.txt", shell=True)
        subprocess.run(f"cat {dir}/vuln.txt", shell=True)
        print("\n========== vuln.txt created  ==========\n")

        subprocess.run(f"nmap -Pn --script smb-os-discovery -iL {dir}/ips.txt -p 445 > {dir}/smb-os-discovery.txt", shell=True)
        subprocess.run(f"cat {dir}/smb-os-discovery.txt", shell=True)
        print("\n========== smb-os-discovery.txt created  ==========\n")

        subprocess.run(f"nmap -Pn --script http-enum -iL {dir}/ips.txt > {dir}/http-enum.txt", shell=True)
        subprocess.run(f"cat {dir}/http-enum.txt", shell=True)
        print("\n========== http-enum.txt created  ==========\n")

        subprocess.run(f"nmap -Pn --script ftp-anon -iL {dir}/ips.txt -p 21 > {dir}/ftp-anon.txt", shell=True)
        subprocess.run(f"cat {dir}/ftp-anon.txt", shell=True)
        print("\n========== ftp-anon.txt created  ==========\n")

        subprocess.run(f"nmap -Pn --script banner -sV -iL {dir}/ips.txt > {dir}/banner.txt",shell=True)
        subprocess.run(f"cat {dir}/banner.txt", shell=True)
        print("\n========== banner.txt created  ==========\n")

        print("\n[!]  Nmap scan completed!!!\n ")


        while True:
            try:
                ask = int(input(""""###############

Do you want to exit?
1 yes
2 no

#############
"""))
                if ask == 1:
                    exit()
                elif ask == 2:
                    break
                else:
                    print("\nInvalid input! Try again.\n")

            except Exception as e:
                print("\n[ERROR] Failed to type answer from panel:  ", e)

    except FileNotFoundError as e:
        print("[ERROR!] Not found file ips.txt: ", e)


def dns_enum():
    try:
        ###### dnsenum #######
        standart = "/usr/share/dnsenum/dns.txt"
        print("======== Type enter for default wordlist dnsenum on Linux. ==========")
        wordlist = str(input("[!] Type wordlist complete path(Standart dnsenum-wordlist = /usr/share/dnsenum/dns.txt): "))
        if wordlist == "":
            subprocess.run(f"dnsenum --enum {ip} -f {standart} > {dir}/dnsenum.txt ", shell=True)
        else:
            subprocess.run(f"dnsenum --enum {ip} -f {wordlist} > {dir}/dnsenum.txt ", shell=True)
            subprocess.run(f"cat {dir}/dnsenum.txt", shell=True)

        print("========== Dnsenum executed =========")

    except Exception as e:
        print("[!] Error: ", e)

def whois_dns():
    try:
       subprocess.run(f"whois {ip} | grep 'Name Server:' | cut -d ' ' -f 3 > {dir}/whois.txt", shell=True)
       subprocess.run(f"cat {dir}/whois.txt", shell=True)
       # TRYING DNS CONNECTION
       print("======== Getting information from the dns server ========")
       with open(f'{dir}/whois.txt', 'r') as file:
            for line in file:
                domain = line.strip()
                if domain:
                    result = subprocess.run(['whois', domain], capture_output=True, text=True)
                    if result.returncode == 0:
                        with open(f"{dir}/whois_dns_connection_server.txt","a") as file2:
                            file2.write(str(result))
                        print(f"{result}\n\n[RESULT] Connection was sucessfuly.\n")
                    else: 
                        print(f"{result}\n\n[RESULT] Unsucessfull connection.\n")

    except Exception as e:
       print("[!] ERROR: ", e)
    except KeyboardInterrupt as e:
       print("Finishing all processes: " ,e)

def zone_transfer():
    print("========== ZONE TRANSFER ========")
    dnsfile = f"{dir}/whois.txt"
    with open(dnsfile, "r") as file3:
        dns_servers = file3.read().splitlines()
    for dns_server in dns_servers:
         print(f"\n#Testing zone transfer with {dns_server} for domain {ip}...\n\n")
         result = subprocess.run(['host', '-l', ip, dns_server], capture_output=True, text=True)
         if result.returncode == 0:
            print(f"Zone transfer successful with {dns_server}:\n")
            print(result.stdout)
         else:
            print(f"Zone transfer failed with {dns_server}:\n")
            print(result.stderr)



try:
    ip = input("Ip: ")
    dir = input("Dir_name: ")

    if not os.path.exists(dir):
        os.makedirs(dir)
    else:
        print("There is already a directory called {dir}.\n")

except Exception as e:
    print("Invalid ip address or failed to make directory: ", e)



system = menu()

system.panel()
