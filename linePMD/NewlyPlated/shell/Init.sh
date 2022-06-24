chmod a+x Init.sh

echo "Please wait about 20 minutes ^^"

s="sudo"
sa="sudo apt"
s_a="sudo apt-get"
ag = "apt-get"
i="install"
PIP="pip3 install"
KeyIn="sudo su -c"
ExPort='export PATH="$PATH:/opt/mssql-tools/bin"'

$s timedatectl set-timezone Asia/Taipei
$sa update -y
$sa upgrade -y
$sa $i python3 -y 
$sa $i python3-pip -y
$sa $i unzip -y
$sa $i htop -y
$sa $i thrift-compiler -y
$sa $i gnupg2 -y
$s_a $i unixodbc-dev -y
$s_a $i screen -y
$s_a $i automake bison flex g++ git libboost-all-dev libevent-dev libssl-dev libtool make pkg-config -y

git remote add origin https://github.com/TaiwanMiya/linePMD.git
git branch -M main
git push -u origin main

$KeyIn "curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -"
$KeyIn "curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list > /etc/apt/sources.list.d/mssql-release.list"
$KeyIn "$s_a update"
$KeyIn "sudo ACCEPT_EULA=Y $ag $i -y msodbcsql17"
$KeyIn "sudo ACCEPT_EULA=Y $ag $i -y mssql-tools"
$KeyIn "echo $ExPort >> ~/.bashrc"
$KeyIn "source ~/.bashrc"
$KeyIn "$s_a $i -y unixodbc-dev"

$PIP six numpy cython requests pyodbc

echo "Installation is complete ^^"