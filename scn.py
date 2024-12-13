import os
import platform
import requests
import subprocess
import shutil



class menu:
    def __init__(self):
        self.path = "Files/TOOL_LIST.md"
        self.red = "\033[91m"
        self.reset = "\033[0m"
        self.yellow = "\033[93m"
        self.urls = [
            f"https://www.facebook.com/{{nome}}",
            f"https://www.twitter.com/{{nome}}",
            f"https://www.instagram.com/{{nome}}",
            f"https://www.linkedin.com/in/{{nome}}",
            f"https://www.tiktok.com/@{{nome}}",
            f"https://www.reddit.com/user/{{nome}}",
            f"https://www.pinterest.com/{{nome}}",
            f"https://www.snapchat.com/add/{{nome}}",
            f"https://www.youtube.com/c/{{nome}}",
            f"https://www.whatsapp.com/{{nome}}",
            f"https://www.flickr.com/people/{{nome}}",
            f"https://www.vk.com/{{nome}}",

            f"https://www.google.com/search?q={{nome}}",
            f"https://www.bing.com/search?q={{nome}}",
            f"https://www.yahoo.com/search?q={{nome}}",
            f"https://www.yandex.com/search/?text={{nome}}",
            f"https://duckduckgo.com/?q={{nome}}",
            f"https://www.ask.com/web?q={{nome}}",
            f"https://www.startpage.com/sp/search?q={{nome}}",

            f"https://www.spokeo.com/{{nome}}",
            f"https://pipl.com/search/?q={{nome}}",
            f"https://www.whitepages.com/name/{{nome}}",
            f"https://www.beenverified.com/search/{{nome}}",
            f"https://www.intelius.com/results/{{nome}}",
            f"https://www.peoplefinders.com/people/{{nome}}",
            f"https://www.truthfinder.com/search/{{nome}}",
            f"https://www.zabasearch.com/{{nome}}",
            f"https://www.peekyou.com/{{nome}}",
            f"https://www.radaris.com/p/{{nome}}",

            f"https://www.social-searcher.com/social-media-search/{{nome}}",
            f"https://www.shodan.io/{{nome}}",
            f"https://www.censys.io/{{nome}}",
            f"https://www.robtex.com/{{nome}}",
            f"https://www.securitytrails.com/{{nome}}",

            f"https://www.twitch.tv/{{nome}}",
            f"https://www.dailymotion.com/{{nome}}",
            f"https://www.quora.com/search?q={{nome}}",
            f"https://www.vimeo.com/{{nome}}",
            f"https://www.meetup.com/{{nome}}",
            f"https://www.deviantart.com/{{nome}}",

            f"https://whois.domaintools.com/{{nome}}",
            f"https://www.namecheap.com/domains/whois/{{nome}}",
            f"https://www.godaddy.com/whois/results.aspx?domain={{nome}}",
            f"https://who.is/whois/{{nome}}",
            f"https://www.whois.net/whois/{{nome}}",

            f"https://scholar.google.com/scholar?q={{nome}}",
            f"https://www.researchgate.net/profile/{{nome}}",
            f"https://www.academia.edu/{{nome}}",
            f"https://www.orcid.org/{{nome}}",
            f"https://www.mendeley.com/profiles/{{nome}}",

            f"https://www.google.com/search?hl=en&tbm=isch&q={{nome}}",
            f"https://www.tineye.com/search/?url={{nome}}",
            f"https://www.pixsy.com/search/?q={{nome}}",
            f"https://www.flickr.com/search/?text={{nome}}",

            f"https://www.familysearch.org/search/{{nome}}",
            f"https://www.ancestry.com/search/{{nome}}",
            f"https://www.myheritage.com/research/{{nome}}",
            f"https://www.findmypast.co.uk/records/{{nome}}",

            f"https://www.backgroundchecks.org/{{nome}}",
            f"https://www.instantcheckmate.com/{{nome}}",
            f"https://www.checkpeople.com/{{nome}}",
            f"https://www.truthfinder.com/search/{{nome}}",

            f"https://www.govrecords.org/search/{{nome}}",
            f"https://www.archives.gov/research/genealogy/{{nome}}",
            f"https://www.ssa.gov/{{nome}}",

            f"https://www.altavista.com/search?q={{nome}}",
            f"https://www.excite.com/search?q={{nome}}",
            f"https://www.hotbot.com/search?q={{nome}}",
            f"https://www.lycos.com/search?q={{nome}}",

            f"https://www.nytimes.com/search?q={{nome}}",
            f"https://www.bbc.com/search?q={{nome}}",
            f"https://www.cnn.com/search?q={{nome}}",
            f"https://www.reuters.com/search/news/?blob={{nome}}",
            f"https://www.theguardian.com/search?q={{nome}}",

            f"https://www.medium.com/search?q={{nome}}",
            f"https://www.wordpress.com/search/{{nome}}",
            f"https://www.tumblr.com/search/{{nome}}",

            f"https://www.amazon.com/s?k={{nome}}",
            f"https://www.ebay.com/sch/i.html?_nkw={{nome}}",
            f"https://www.etsy.com/search?q={{nome}}",
            f"https://www.alibaba.com/countrysearch/{{nome}}",
            f"https://www.walmart.com/search/?query={{nome}}",

            f"https://www.google.com/maps?q={{nome}}",
            f"https://www.openstreetmap.org/search?q={{nome}}",
            f"https://www.bing.com/maps?q={{nome}}",

            f"https://www.crunchbase.com/person/{{nome}}",
            f"https://www.bloomberg.com/search?query={{nome}}",
            f"https://www.forbes.com/search/?q={{nome}}",
            f"https://www.manta.com/search?search={{nome}}",

            f"https://www.imdb.com/find?q={{nome}}",
            f"https://www.rottentomatoes.com/search?q={{nome}}",
            f"https://www.fandango.com/search?q={{nome}}",

            f"https://www.upwork.com/freelancers/~{{nome}}",
            f"https://www.fiverr.com/search/gigs?query={{nome}}",
            f"https://www.freelancer.com/search/projects?keywords={{nome}}",
        ]
        self.wordlists = [
            'wordlists/dirbuster/directory-list-1.0.txt',
            'wordlists/dirbuster/directory-list-2.3-medium.txt',
            'wordlists/dirbuster/directory-list-2.3-small.txt',
            'wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt',
            'wordlists/dirbuster/directory-list-lowercase-2.3-small.txt',
        ]
        self.files = ["username.txt"]

    def check_platform(self):
        system = platform.system()
        if system == "Linux" or system == "Darwin":
            print(f"System: {system}")
        elif system == "Windows":
            print(f"System: {system}")

    def clear_terminal(self):
        system = platform.system()
        if system == "Linux" or system == "Darwin":
            os.system('clear')  
        elif system == "Windows":
            os.system('cls') 

    def osint_search(self):
        nome = input("\n* Type username for search: ")

        dir = input("Dir_name: ")

        if not os.path.exists(dir):
            os.makedirs(dir)
        else:
            print("There is already a directory called {dir}.\n")

        if not os.path.exists(self.files[0]):
            with open(self.files[0], "w") as file:
                file.write("URLs pesquisadas para o nome: " + nome + "\n")

        with open(self.files[0], "a") as file:
            for url in self.urls:
                formatted_url = url.format(nome=nome)
                print(f"Buscando em: {formatted_url}")

                try:
                    response = requests.get(formatted_url)

                    if response.status_code == 200:
                        print(f"[OK] Página encontrada: {formatted_url}")
                        file.write(formatted_url + "\n")
                    elif response.status_code == 404:
                        print(f"[404] Página não encontrada: {formatted_url}")
                    else:
                        print(f"[{response.status_code}] Status retornado: {formatted_url}")

                except requests.exceptions.RequestException as e:
                    print(f"[Erro] Não foi possível acessar {formatted_url}: {e}")

            print("\n[+] Todas as URLs prováveis foram pesquisadas e os resultados foram registrados no arquivo usernames.txt.\n")


    def panel_gobuster(self):
        while True:
            try:
                pannel = int(input("""\n==============

------------ GOBUSTER PANEL -------------

0. EXIT;
1. PAGES ENUMERATION | DIRS;
2. SUBDOMAIN; 


=============

Number: """))

                if pannel == 0:
                    exit()

                url = input("url: ")
                dir = "results"

        
                if pannel == 1:
                    print("[+] PAGES ENUMERATION | DIRS SELECTED.")

                    self.gobuster_dirs(url, dir)

                elif pannel == 2:
                    self.gobuster_subdomains(url, dir)

                else:
                    print("\n[!] Invalid number or charater, try again!\n\n")


            except ValueError:
                print("\n[!] Invalid character, only numbers are allowed!\n\n")

    def gobuster_dirs(self, url, dir):

        if not os.path.exists(dir):
            os.makedirs(dir)
        else:
            print(f"There is already a directory called {dir}.\n")

        try:

            global wordlists
        
            wordlist_type = int(input("""
Which kind of wordlist is the best for you?\n\n
1. directory-list-1.0.txt\n
2. directory-list-2.3-medium.txt\n
3. directory-list-2.3-medium.txtdirectory-list-2.3-medium.txt\n
4. KaliLists/dirbuster/directory-list-lowercase-2.3-medium.txt\n
5. KaliLists/dirbuster/directory-list-lowercase-2.3-small.txt\n

Number: """
        ))

            if wordlist_type ==  1:
                subprocess.run(f'gobuster dir -u https://{url} -w {self.wordlists[0]} > results/pages.txt',shell=True,stdin=True,stderr=True,stdout=True)
            elif wordlist_type ==  2:
                subprocess.run(f'gobuster dir -u https://{url} -w {self.wordlists[1]} > results/pages.txt',shell=True,stdin=True,stderr=True,stdout=True)
            elif wordlist_type ==  3:
                subprocess.run(f'gobuster dir -u https://{url} -w {self.wordlists[2]} > results/pages.txt',shell=True,stdin=True,stderr=True,stdout=True)
            elif wordlist_type ==  4:
                subprocess.run(f'gobuster dir -u https://{url} -w {self.wordlists[3]} > results/pages.txt',shell=True,stdin=True,stderr=True,stdout=True)
            elif wordlist_type ==  5:
                subprocess.run(f'gobuster dir -u https://{url} -w {self.wordlists[4]} > results/pages.txt',shell=True,stdin=True,stderr=True,stdout=True)

        except KeyboardInterrupt:
            print("\n[!] Finishing program...")
        except Exception as e:
            print("\n[!] Failure to execute the program: ", e)

    def gobuster_subdomains(self,url,dir):

        if not os.path.exists(dir):
            os.makedirs(dir)
        else:
            print(f"There is already a directory called {dir}.\n")

        try:
            #gobuster dns -d example.com -w /caminho/para/wordlist.txt 
            print("\n[+] Finding domains...\n\n")
            subprocess.run(f"gobuster dns -d {url} -w wordlists/dns/subdomains-top1million-110000.txt > results/subdomains.txt",shell=True,check=True,stdin=True,stderr=True,stdout=True)
            print("\n[!] Subdomains registered on results/subdomains.txt, ending program.\n")
        except KeyboardInterrupt:
            print("\n[!] Finishing program...")
        except Exception as e:
            print("\n[!] Failure to execute the program: ", e)

    def list_tools(self):
        print("""\n########## Tools ##########\n""")
        tools = []
        try:
            with open(self.path, "r") as file:
                lines = file.readlines()
            
            if not lines:
                print("[WARNING] The file is empty.")
                return
            
            id_counter = 1
            tools_found = False
            
            for line in lines:
                line = line.strip()
                if line.startswith('- [') and '](' in line:
                    start_bracket = line.index('[') + 1
                    end_bracket = line.index(']')
                    tool_name = line[start_bracket:end_bracket]
                    
                    start_parenthesis = line.index('(') + 1
                    end_parenthesis = line.index(')')
                    tool_link = line[start_parenthesis:end_parenthesis]

                    description = line[end_parenthesis + 1:].strip().lstrip('- ')
                    tools.append((id_counter, tool_name, tool_link, description))


                    print(f'{self.yellow}[{id_counter}]{self.reset} {tool_name} ({tool_link}) - {description}')
                    tools_found = True
                    id_counter += 1
            
            if not tools_found:
                print("[WARNING] No tools found in the specified format.")
                return

            while True:
                install_tools = input("\nDo you wish to install some tool?\n1. Yes\n2. Search for a tool\n3. No\nAnswer (1, 2 or 3): ")
                if install_tools == "1":
                    tool_number = input("\nType number of the tool: ")
                    try:
                        tool_number = int(tool_number)
                        if 1 <= tool_number < id_counter:
                            selected_tool = tools[tool_number - 1]
                            github_link = selected_tool[2]
                            subprocess.run(f"cd $HOME && git clone {github_link}", shell=True)
                        else:
                            print(f"{self.red}[ERROR]{self.reset} Invalid tool number.")
                    except ValueError:
                        print(f"{self.red}[ERROR]{self.reset} Please enter a valid number.")

                elif install_tools == "2":
                    tool_name = input("Type your tool: ")
                    search_result = subprocess.run(f"cat TOOL_LIST.md | grep '{tool_name}'", shell=True, capture_output=True, text=True)

                    if search_result.stdout:
                        print("\nSearch results:\n")
                        for idx, line in enumerate(search_result.stdout.splitlines(), start=1):
                            print(f"{self.yellow}[{idx}]{self.reset} {line}")

                        selected_index = input("\nType the number of the tool you want to install or just press enter: ")
                        try:
                            selected_index = int(selected_index)
                            if 1 <= selected_index <= len(search_result.stdout.splitlines()):
                                chosen_tool = search_result.stdout.splitlines()[selected_index - 1]
                                tool_link = chosen_tool.split('(')[1].split(')')[0]
                                subprocess.run(f"git clone {tool_link}", shell=True)
                                

                            else:
                                print(f"{self.red}[ERROR]{self.reset} Invalid selection.")
                        except ValueError:
                            print(f"{self.red}[ERROR]{self.reset} Please enter a valid number.")

                elif install_tools == "3":
                    break
        
                else:
                    print(f"{self.red}[ERROR]{self.reset} Please choose 1, 2 or 3.")
                    
        except FileNotFoundError:
            print(f"{self.red}[ERROR]{self.reset} The specified file was not found.")
        except Exception as e:
            print(f"{self.red}[ERROR]{self.reset} An unexpected error occurred: {e}")
        except KeyboardInterrupt:
            print(f"{self.red}[End]{self.reset} Finishing all processes.")
            
    def panel(self):
        try:
            print("""
___________________________________________

███████╗ ██████╗ ███╗   ██╗
██╔════╝██╔═══   ████╗ ██╔╝
███████╗██║      ██╔████╔╝
╚════██║██║      ██║╚═██╔╝
███████║╚██████╔╝██║  ██ 
╚══════╝ ╚═════╝ ╚═╝     
                                  
.
░░░░░███████ ]▄▄▄▄▄▄ `~~~~~~ ~~~~ ~~~~ ~~~
▂▄▅████████▅▄▃ ...............
Il███████████████████]
◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤..

Autor: jhonnunes443  
Github: https://github.com/jhonnunes443/scn.git
                  

                  """)
            while True:

                panel_input = input("""\n=============== PANEL SCAN ============

Type one:
                                    
0 exit;
1 Scan with nmap;
2 Whois, Dns transfer zone and Dnsenum;
3 Check and install tools;
4 Install Kali-nethunter;
5 Username OSINT;
6 Gobuster Dirs | Subdomains.                        


==============================\n
* Type one number: """)


                if not panel_input.strip():
                    print(f"\n{self.red}[END]{self.reset} Invalid answer, please try again.\n")
                    continue

                try:
                    panel = int(panel_input)
                except ValueError:
                    print(f"\n{self.red}[ValueError]{self.reset} Invalid answer, please try again.\n")
                    self.clear_terminal()
                    continue

                if panel == 0:
                    print(f"{self.red}[!]{self.reset} Finishing program...\n")
                    break

                elif panel == 1:

                    print(f"\n{self.red}[+]{self.reset} Scan with nmap selected\n")
                    print(f"\n{self.red}[+]{self.reset} Choose a name for your nmap result dir.\n")
                    nmap_scan()

                elif panel == 2:

                    print(f"{self.red}[+]{self.reset} Dnsenum, Whois selected\n")

                    ip = input("Ip: ")
                    dir = input("Dir_name: ")

                    whois_dns(ip, dir)
                    zone_transfer(ip, dir)
                    enum = input(f"\nWould you like to try to enum dns servers {self.yellow}[y/n]{self.reset}?: ")

                    if enum.lower() in ["y", "yes"]:
                        dns_enum(ip, dir)
                        print(f"{self.red}[END]{self.reset} Finishing all the processes...")
                        break
                    elif enum.lower() in ["n", "no"]:
                        print(f"{self.red}[END]{self.reset} Finishing all the processes...")
                        break
                    else:
                        print(f"\n{self.red}[!]{self.reset} Resposta inválida\n")

                elif panel == 3:
                    print(f"\n{self.red}[+]{self.reset} List tools selected.\n")
                    self.list_tools()

                elif panel == 4:
                    print(f"\n{self.yellow}[+]{self.reset} Installing kali-nethunter...\n")
                    tool = "wget"
                    print(f"\n{self.yellow}[+]{self.reset} Installing {tool}\n")

                    try:
                        subprocess.run(f"apt install {tool} -y", shell=True, check=True)
                        print(f"\n{self.yellow}[+]{self.reset} WGET INSTALLED!\n")
                    except subprocess.CalledProcessError:
                        print(f"\n{self.yellow}[Failure]{self.reset} Tool {tool} not found. Attempting to install with sudo...")
                        try:
                            subprocess.run(f"sudo apt install {tool} -y", shell=True, check=True)
                            print(f"\n{self.yellow}[+]{self.reset} WGET INSTALLED!\n")
                        except subprocess.CalledProcessError:
                            print(f"Failed to install {tool}. Are you rooted?")

                    try:
                        subprocess.run("wget -O install-nethunter-termux https://offs.ec/2MceZWr", shell=True, check=True)
                        subprocess.run("chmod +x install-nethunter-termux", shell=True, check=True)
                        subprocess.run("./install-nethunter-termux", shell=True, check=True)
                    except Exception as e:
                        print(f"\n{self.red}[ERROR]{self.reset} Kali-nethunter is not supported on your device:", e)
                elif panel == 5:
                    self.osint_search()

                elif panel == 6:
                    self.panel_gobuster()


                else:
                    print(f"{self.red}[+]{self.reset} Invalid answer\n")
                    self.clear_terminal()

        except KeyboardInterrupt:
            print(f"\n{self.red}[END]{self.reset} Finishing all the processes...")

        except ValueError:
            print(f"\n{self.red}[END]{self.reset} Invalid answer\n")
            self.clear_terminal()


def nmap_installation():
    try:
        result = subprocess.run(["nmap"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        if result.returncode == 0:
            print(f"\n[+] Nmap is installed on the device\n")
        else:
            print(f"\n[+] Nmap is not installed on the device\n")
            try:
                install_result = subprocess.run("apt install nmap -y", shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                print(install_result.stdout.decode())
                print("[+] Nmap installed successfully.\n")
            except Exception as e:
                print("\n[!] Failure to install nmap, trying with sudo...\n")
                try:
                    install_result = subprocess.run("sudo apt install nmap -y", shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    print(install_result.stdout.decode())
                    print("[+] Nmap installed successfully with sudo.\n")
                except Exception as e:
                    print("\n[!] Unsupported device for nmap or installation failed.\n")
                    print(e)
    except FileNotFoundError:
        print("\n[!] Nmap command not found. Attempting to install...\n")
        try:
            install_result = subprocess.run("apt install nmap -y", shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(install_result.stdout.decode())
            print("[+] Nmap installed successfully.\n")
        except Exception as e:
            print("\n[!] Failure to install nmap, trying with sudo...\n")
            try:
                install_result = subprocess.run("sudo apt install nmap -y", shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                print(install_result.stdout.decode())
                print("[+] Nmap installed successfully with sudo.\n")
            except Exception as e:
                print("\n[!] Unsupported device for nmap or installation failed.\n")
                print(e)

def nmap_scan():
    if shutil.which("nmap") is None:
        print("[ERROR] nmap is not installed or not in PATH.")
        nmap_installation()

    dir = input("Dir_name: ")

    if not os.path.exists(dir):
        os.makedirs(dir)
    else:
        print("There is already a directory called {dir}.\n")
    
    ip = input("Ip: ")

    try:
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

def dns_enum_install():
    system = platform.system()

    if system == "Linux" or system == "Darwin":
        subprocess.run('sudo apt install dnsenum -y', shell=True, check=True, stderr=True, stdout=True, stdin=True)
        print(f"System: {system}")

    else:
        print(f"\n[!] Unsupported format.\n")


def dns_enum(ip, dir):
    try:
        if shutil.which("dnsenum") is None:
            print("[ERROR] dnsenum is not installed or not in PATH.")
            dns_enum_install()
        
        standart = "/usr/share/dnsenum/dns.txt"
        print("======== Type enter for default wordlist dnsenum on Linux. ==========")
        wordlist = str(input("[!] Type wordlist complete path (Standart dnsenum-wordlist = /usr/share/dnsenum/dns.txt): "))
        if wordlist == "":
            subprocess.run(f"dnsenum --enum {ip} -f {standart} > {dir}/dnsenum.txt ", shell=True)
        else:
            subprocess.run(f"dnsenum --enum {ip} -f {wordlist} > {dir}/dnsenum.txt ", shell=True)
            subprocess.run(f"cat {dir}/dnsenum.txt", shell=True)

        print("========== Dnsenum executed =========")

    except Exception as e:
        print("[!] Error: ", e)


def whois_dns(ip, dir):
    try:
        global dir_global
        dir_global = dir  

        if not os.path.exists(dir):
            os.makedirs(dir)
        else:
            print("There is already a directory called {dir}.\n")
    
        subprocess.run(f"whois {ip} | grep 'Name Server:' | cut -d ' ' -f 3 > {dir}/whois.txt", shell=True)
        subprocess.run(f"cat {dir}/whois.txt", shell=True)
        print("======== Getting information from the DNS server ========")

        with open(f'{dir}/whois.txt', 'r') as file:
            for line in file:
                domain = line.strip()
                if domain:
                    result = subprocess.run(['whois', domain], capture_output=True, text=True)
                    if result.returncode == 0:
                        with open(f"{dir}/whois_dns_connection_server.txt", "a") as file2:
                            file2.write(result.stdout.strip() + "\n\n") 
                        print(f"{result.stdout}\n\n[RESULT] Connection was successful.\n")
                    else:
                        print(f"{result.stderr}\n\n[RESULT] Unsuccessful connection.\n")

    except Exception as e:
        print("[!] ERROR: ", e)
    except KeyboardInterrupt as e:
        print("Finishing all processes: ", e)

def zone_transfer(ip, dir):
    print("========== ZONE TRANSFER ========")

    dnsfile = f"{dir}/whois.txt"
    
    with open(dnsfile, "r") as file3:
        dns_servers = file3.read().splitlines()
    
    for dns_server in dns_servers:
        dns_server = dns_server.strip()
        if not dns_server: 
            continue
        
        print(f"\n#Testing zone transfer with {dns_server} for domain {ip}...\n\n")
        
        result = subprocess.run(['host', '-l', ip, dns_server], capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"Zone transfer successful with {dns_server}:\n")
            print(result.stdout)
        else:
            print(f"Zone transfer failed with {dns_server}:\n")
            print(result.stderr)

# Example usage
# dir = '/path/to/your/directory'  # Set your directory here
# zone_transfer('globo.com')


system = menu()
system.panel()
system.check_platform()
