cd 
sleep 0.5

# Colors
r='\e[91m'
g='\e[92m'
y='\e[93m'
b='\e[94m'
p='\e[95m'
c='\e[96m'
w='\e[97m'
n='\e[0m'
# effect colors
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

colors=( "${bd}${r}" "${bd}${g}" "${bd}${y}" "${bd}${b}" "${bd}${p}" "${bd}${c}")

thread=12
count=1

ping -c 1 google.com > /dev/null 2>&1
if [[ "$?" == 0 ]]; then
echo -e "$green[INFO]——[Internet Connection is Available] ^^"
sleep 1.5
else
echo -e "$red[ERROR]——[No Internet Connection] ^^"
sleep 5
echo -e "$red[HELP]——[Press: 'CTRL + C' To Exit] ^^"
exit
sleep 999999
sleep 999999
sleep 999999
exit
exit
fi

exits() {
	checkphp=$(ps aux | grep -o "curl" | head -n1)

	if [[ $checkphp == *'curl'* ]]; then
		pkill -f -2 curl > /dev/null 2>&1
	 	killall -2 curl > /dev/null 2>&1
	fi
}
trap 'printf "\n";exits;exit 0' INT
banner() {
	rand1=$( shuf -i 0-${#colors[@]} -n 1 )
	rand2=$( shuf -i 0-${#colors[@]} -n 1 )
	sss=''
	start=1
	end=50
	for (( mo=${start}; mo <= ${end}; mo++)); do
		if [[ $mo == ${start} ]]; then
			sss+="${bd}${w}+"
		elif [[ $mo == $end ]]; then
			sss+="${bd}${w}+"
		elif [[ $mo == $(( (end / 2 ) + 1)) ]]; then
			sss+="${bd}${g}+"
		elif [[ $mo > 1 ]]; then
			sss+="${bd}${r}-"
		fi
	done
echo -e "\t${colors[rand1]} ██      ██ ███    ██ ███████ ██████  ███    ███ ██████  "
echo -e "\t${colors[rand1]} ██      ██ ████   ██ ██      ██   ██ ████  ████ ██   ██ "
echo -e "\t${colors[rand1]} ██      ██ ██ ██  ██ █████   ██████  ██ ████ ██ ██   ██ "
echo -e "\t${colors[rand1]} ██      ██ ██  ██ ██ ██      ██      ██  ██  ██ ██   ██ "
echo -e "\t${colors[rand1]} ███████ ██ ██   ████ ███████ ██      ██      ██ ██████  "
	echo -e "                 \t${bd}${g}╭${w} Author  ${b}:${c} ${ul}Pea${n}                   ${g}${n}"
	echo -e "                 \t${bd}${g}│${w} Version ${b}:${w} 1.0.0                          ${g}${n}"
	echo -e "                 \t${bd}${g}│${w} Code    ${b}:${w} Bash, python                   ${g}${n}"
	echo -e "     \t${bd}${g} ╭──────────────┴${w} Date    ${b}:${w} 16 05 2021                 ${g}${n}"
}

scan() {
	web=${1}
	path="${2}"
	scan_web=$( curl -s -o /dev/null ${web}/${path} -w %{http_code} )
	if [[ $scan_web == 200 ]] || [[ $scan_web == 201 ]]; then
		printf "\n"
		echo -e "      \t${g}[${w}+${g}] ${w}${web}/${path} ${y}~> ${g}${scan_web}${n}"
		printf "\n"
	else
		echo -e "      \t${g}[${r}-${g}] ${w}${web}/${path} ${b}~> ${r}${scan_web}${n}"
	fi
}

# start
echo ""
python3 src/CheckVersion.py
sleep 1.5
clear
banner
echo -ne "      \t${c}[${w}>${c}] ${w}Enter your website ${g}:${n} "
read web
if [[ -z $web ]]; then
	printf "\n"
	echo -e "${b}[${r}!${b}]${w} Error! Invalid web site ^^"
	exit 0
fi
echo -ne "      \t${c}[${w}>${c}] ${w}Enter your wordlist ${g}(${w}Default${g}:${w} wordlist.txt${g}) ${g}:${n} "
read wordlist
web=$( echo ${web} | cut -d '/' -f 3 )
wordlist=${wordlist:-wordlist.txt}
if ! [[ -e $wordlist ]]; then
	printf "\n"
	echo -e "${b}[${r}!${b}]${w} List not found ^^"
	exit 0
fi
echo -ne "      \t${c}[${w}>${c}] ${w}Enter thread ${g}(${w}Default${g}:${w} 12${g}) ${g}:${n}  ~"
read thrd
thread=${thrd:-${thread}}
printf "\n"
echo -e "      \t${g}[${w}+${g}]${w} Total Wordlist ${g}:${w} $( wc -l $wordlist | cut -d ' ' -f 1 ) ~"
echo -ne "      \t${g}[${w}+${g}]${w} Start Scanning${n}"
for((;T++<=10;)) { printf '.'; sleep 1.5; }
printf "\n\n"
for list in $( < $wordlist ); do
	if [[ $(( $thread % $count )) = 0 && $count > 0 ]]; then
		sleep 2
	fi
	scan "${web}" "${list}" &
	(( count++ ))
done
wait
