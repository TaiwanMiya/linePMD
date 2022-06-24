do_you_have_domain(){
    while true
    do
        _read "你拥有自己的域名吗? (默认: n) [y/n]:"
        local yn="${inputInfo}"
        [ -z "${yn}" ] && yn="N"
        case "${yn:0:1}" in
            y|Y)
                doYouHaveDomian=Yes
                ;;
            n|N)
                doYouHaveDomian=No
                _echo -e "妈的穷鬼"
                ;;
            *)
                _echo -e "输入有误,重新输入."
                continue
                ;;
        esac
        _echo -r "  selected = ${doYouHaveDomian}"
        break
    done
}

_get_input_domain(){
    local domainTypeTip=$1

    while true
    do
        _read "输入一个域名(${domainTypeTip}):"
        domain="${inputInfo}"
        if ! judge_is_domain "${domain}"; then
            _echo -e "输入一个格式正确的域名."
            continue
        fi
        if ! judge_is_valid_domain "${domain}"; then
            _echo -e "无法解析到IP,输入一个正确有效的域名."
            continue
        fi
        break
   done
}

get_specified_type_domain(){
    # typeTip value：CDN，DNS-Only，Other
    local typeTip=$1

    while true
        do
        _get_input_domain "${typeTip}"
        domainType=$(judge_domain_type "${domain_ip}")
        if [ "${domainType}" = "${typeTip}" ]; then
            _echo -r "  domain = ${domain} (${domainType})"
            break
        else
            _echo -e "输入一个${typeTip}类型的域名."
            continue
        fi
    done
}

get_cdn_or_dnsonly_type_domain(){
    local typeTip="CDN 或 DNS-Only"

    while true
        do
        _get_input_domain "${typeTip}"
        domainType=$(judge_domain_type "${domain_ip}")
        if [ "${domainType}" = "Other" ]; then
            _echo -e "输入一个${typeTip}类型的域名."
            continue
        fi
        _echo -r "  domain = ${domain} (${domainType})"
        break
    done
}

get_all_type_domain(){
    while true
    do
        _read "任意输入一个域名 (默认: cloudfront.com):"
        domain="${inputInfo}"
        [ -z "${domain}" ] && domain="cloudfront.com"
        if ! judge_is_domain "${domain}"; then
            _echo -e "输入一个格式正确的域名."
            continue
        fi
        if ! judge_is_valid_domain "${domain}"; then
            _echo -e "无法解析到IP,输入一个正确有效的域名."
            continue
        fi
        unset domainType
        _echo -r "  domain = ${domain}"
        break
   done
}

get_input_ws_path(){
    gen_random_str
    while true
    do
        _read "输入你的WebSocket分流路径(默认：/${ran_str5}):"
        path="${inputInfo}"
        [ -z "${path}" ] && path="/${ran_str5}"
        if ! judge_is_path "${path}"; then
            _echo -e "输入以 / 开头的路径."
            continue
        fi
        _echo -r "  path = ${path}"
        break
    done
}

_get_input_mux_max_stream() {
    while true
    do
        _read "输入一个实际TCP连接中的最大复用流数 (默认: 8):"
        mux="${inputInfo}"
        [ -z "${mux}" ] && mux=8
        expr "${mux}" + 1 &>/dev/null
        if ! judge_is_num "${mux}"; then
            _echo -e "输入一个有效数字."
            continue
        fi
        if judge_is_zero_begin_num "${mux}"; then
            _echo -e "输入一个非0开头的数字."
            continue
        fi
        if ! judge_num_in_range "${mux}" "1024"; then
            _echo -e "输入一个在1-65535之间的数字."
            continue
        fi
        echo
        echo -e "${Red}  mux = ${mux}${suffix}"
        echo
        break
    done
}

_is_disable_mux(){
    while true
    do
        _read "是否禁用 mux (默认: n) [y/n]:"
        local yn="${inputInfo}"
        [ -z "${yn}" ] && yn="N"
        case "${yn:0:1}" in
            y|Y)
                isDisableMux=disable
                ;;
            n|N)
                isDisableMux=enable
                ;;
            *)
                _echo -e "输入有误重新输入!"
                continue
                ;;
        esac
        _echo -r "  mux = ${isDisableMux}"
        break
    done
}

is_disable_mux_logic(){
    _is_disable_mux
    if [ "${isDisableMux}" = "enable" ]; then
        _get_input_mux_max_stream
        clientMux=";mux=${mux}"
    fi
}

get_input_mirror_site(){
    while true
    do
        _echo -u "${Tip} 该站点建议满足(位于海外、支持HTTPS协议、会用来传输大流量... )的条件，默认值不建议使用."
        _read -d "输入你需要镜像到的站点(默认:https://www.bing.com):"
        mirror_site="${inputInfo}"
        [ -z "${mirror_site}" ] && mirror_site="https://www.bing.com"
        if ! judge_is_https_begin_site "${mirror_site}"; then
            _echo -e "输入以${Red} https:// ${suffix}开头，以${Red} 域名 ${suffix}结尾的URL."
            continue
        fi
        if ! judge_is_valid_domain "${mirror_site}"; then
            _echo -e "无法解析到IP,输入一个正确有效的域名."
            continue
        fi
        _echo -r "  mirror_site = ${mirror_site}"
        break
    done
}