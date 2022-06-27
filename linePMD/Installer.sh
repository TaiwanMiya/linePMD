chmod a+x Installer.sh
r='\e[91m'
g='\e[92m'
y='\e[93m'
b='\e[94m'
p='\e[95m'
c='\e[96m'
w='\e[97m'
n='\e[0m'
bd='\e[1m'
dm='\e[2m'
it='\e[3m'
ul='\e[4m'
rv='\e[7m'
red='\e[1;31m'
default='\e[0m'
yellow='\e[0;33m'
orange='\e[38;5;166m'
green='\033[92m'
s="sudo"
sa="sudo apt"
s_a="sudo apt-get"
saroot="apt"
s_aroot="apt-get"
i="install"
PIP="pip3 install"
KeyIn="sudo su - -c"
ExPort='export PATH="$PATH:/opt/mssql-tools/bin"'

Do_Initial_Installation(){
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
    $PIP numpy
    $PIP requests
    $PIP pyodbc
    $PIP cython
    $PIP six
}

Do_Initial_Installation_Root(){
    $s timedatectl set-timezone Asia/Taipei
    $saroot update -y
    $saroot upgrade -y
    $saroot $i python3 -y 
    $saroot $i python3-pip -y
    $saroot $i unzip -y
    $saroot $i htop -y
    $saroot $i thrift-compiler -y
    $saroot $i gnupg2 -y
    $s_aroot $i unixodbc-dev -y
    $s_aroot $i screen -y
    $s_aroot $i automake bison flex g++ git libboost-all-dev libevent-dev libssl-dev libtool make pkg-config -y
    $PIP numpy
    $PIP requests
    $PIP pyodbc
    $PIP cython
    $PIP six
}

Do_Printf_Logo(){
    echo "\t${red} ██     ██ ███████ ██       ██████  ██████  ███    ███ ███████     ████████  ██████      ██      ██ ███    ██ ███████ ██████  ███    ███ ██████  "
    echo "\t${orange} ██     ██ ██      ██      ██      ██    ██ ████  ████ ██             ██    ██    ██     ██      ██ ████   ██ ██      ██   ██ ████  ████ ██   ██ "
    echo "\t${yellow} ██  █  ██ █████   ██      ██      ██    ██ ██ ████ ██ █████          ██    ██    ██     ██      ██ ██ ██  ██ █████   ██████  ██ ████ ██ ██   ██ "
    echo "\t${green} ██ ███ ██ ██      ██      ██      ██    ██ ██  ██  ██ ██             ██    ██    ██     ██      ██ ██  ██ ██ ██      ██      ██  ██  ██ ██   ██ "
    echo "\t${red}  ███ ███  ███████ ███████  ██████  ██████  ██      ██ ███████        ██     ██████      ███████ ██ ██   ████ ███████ ██      ██      ██ ██████  "
}

SuccessfulInstallation(){
    echo "${yellow}>< Installation is complete ^^"
    echo "${yellow}Please install LINQ.sh"
    echo "${yellow}The following command must be used ^^"
    echo "${yellow}必須使用以下命令 ^^"
    echo "${yellow}>>>sh LINQ.sh"
    echo "${default}"
}

SuccessfulInstallation_Root(){
    curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
    curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
    sudo apt-get update
    sudo ACCEPT_EULA=Y apt-get install -y msodbcsql17
    sudo ACCEPT_EULA=Y apt-get install -y mssql-tools
    echo 'export PATH=\"$PATH:/opt/mssql-tools/bin\"' >> ~/.bashrc
    source ~/.bashrc
    sudo apt-get install -y unixodbc-dev
    rm -f LINQ.sh &
}

GenerateLINQ(){
    local LINQ="LINQ.sh"
    touch $LINQ
    echo "curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
sudo apt-get update
sudo ACCEPT_EULA=Y apt-get install -y msodbcsql17
sudo ACCEPT_EULA=Y apt-get install -y mssql-tools
echo 'export PATH=\"$PATH:/opt/mssql-tools/bin\"' >> ~/.bashrc
source ~/.bashrc
sudo apt-get install -y unixodbc-dev
rm -f LINQ.sh &
echo \"\033[92m Please enter exit to exit by yourself ^^ \e[0m\"
echo \"\033[92m 请输入exit来结束root ^^ \e[0m\"" > $LINQ
    sudo su
}

Do_Printf_Logo
if [ `id -u` -eq 0 ];then
    Do_Initial_Installation_Root
    SuccessfulInstallation_Root
else
    Do_Initial_Installation
    SuccessfulInstallation
    GenerateLINQ
fi