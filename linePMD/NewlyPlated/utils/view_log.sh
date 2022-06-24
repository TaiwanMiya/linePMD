dynamic_display_log(){
    local args=$*
    echo -e "${Separator_1}${Separator_1}"
    echo -e "${Green}结束访问：${suffix}按Ctrl + C"
    echo -e "${Green}日志路径：${suffix}${args}"
    echo -e "${Separator_1}${Separator_1}"
    tail -f ${args}
}

show_log(){
    local ssLibevLog="/var/log/shadowsocks-libev.log"
    local ssRustLog="/var/log/shadowsocks-rust.log"
    local goSs2Log="/var/log/go-shadowsocks2.log"
    local kcptunLog="/var/log/kcptun.log"
    local cloakLog="/var/log/cloak.log"
    local rabbitLog="/var/log/rabbit-tcp.log"
    local caddyErrorLog="/var/log/caddy-error.log"
    local caddyAccessLog="/var/log/caddy-access.log"
    local nginxErrorLog="/var/log/nginx-error.log"
    local nginxAccessLog="/var/log/nginx-access.log"

    if [[ -e ${ssLibevLog} ]]; then
        local ssLog=${ssLibevLog}
    elif [[ -e ${ssRustLog} ]]; then
        local ssLog=${ssRustLog}
    elif [[ -e ${goSs2Log} ]]; then
        local ssLog=${goSs2Log}
    fi
    
    if [[ -e ${ssLog} ]] && [[ -e ${kcptunLog} ]]; then
        dynamic_display_log "${ssLog}" "${kcptunLog}"
    elif [[ -e ${ssLog} ]] && [[ -e ${cloakLog} ]]; then
        dynamic_display_log "${ssLog}" "${cloakLog}"
    elif [[ -e ${ssLog} ]] && [[ -e ${rabbitLog} ]]; then
        dynamic_display_log "${ssLog}" "${rabbitLog}"
    elif [[ -e ${ssLog} ]] && [[ -e ${caddyErrorLog} ]] && [[ -e ${caddyAccessLog} ]]; then
        dynamic_display_log "${ssLog}" "${caddyErrorLog}" "${caddyAccessLog}"
    elif [[ -e ${ssLog} ]] && [[ -e ${caddyErrorLog} ]]; then
        dynamic_display_log "${ssLog}" "${caddyErrorLog}"
    elif [[ -e ${ssLog} ]] && [[ -e ${caddyAccessLog} ]]; then
        dynamic_display_log "${ssLog}" "${caddyAccessLog}"
    elif [[ -e ${ssLog} ]] && [[ -e ${nginxErrorLog} ]] && [[ -e ${nginxAccessLog} ]]; then
        dynamic_display_log "${ssLog}" "${nginxErrorLog}" "${nginxAccessLog}"
    elif [[ -e ${ssLog} ]] && [[ -e ${nginxErrorLog} ]]; then
        dynamic_display_log "${ssLog}" "${nginxErrorLog}"
    elif [[ -e ${ssLog} ]] && [[ -e ${nginxAccessLog} ]]; then
        dynamic_display_log "${ssLog}" "${nginxAccessLog}"
    else
        if [[ -e ${ssLog} ]]; then
            dynamic_display_log "${ssLog}"
        else
            echo && echo -e "${Point} 当前没有生成日志文件,在日志文件生成后再试" && echo
        fi
    fi
}
