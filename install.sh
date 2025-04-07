#Requirements
# -Nmap,whois,host,Dnsenum,Gobuster,Python


apt install python3 -y 
apt install nmap -y 
apt install whois -y 
apt install git -y

apt-get update && apt-get upgrade -y 
git clone https://github.com/OJ/gobuster.git
apt install golang -y 
cd gobuster
go build
chmod +x gobuster
cp gobuster $PATH
cd ..

cpan install Net::DNs
cpan install Net::CIDR
cpan install JSON
cpan install Net::IP
cpan install Net::Netmask
cpan install XML::Writer
cpan install String::Random

apt install perl -y
git clone https://github.com/fwaeytens/dnsenum.git
cd dnsenum
chmod +x dnsenum.pl
