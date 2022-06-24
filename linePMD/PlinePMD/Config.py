import enum
class config(object):

    Hosts = ''
    url = '/api/v4/TalkService.do'
    login = '/api/v4p/rs'
    api = '/S4'
    poll = '/P4'
    qr = '/Q'
    appList = ''
    accessLocation = '1.1.1.1'
    systemName = ''

    def __init__(self,Mhost=None,MappType=None,SystemName=None):
        if isinstance(Mhost,str):
            for names in host:
                if Mhost.casefold() == names.value:Mhost = names.value
        if isinstance(Mhost,int):
            if Mhost not in [i.value for i in host]:Mhost = host.ga2.value
        if isinstance(MappType,str):
            for names in AppType:
                if MappType.casefold() == names.value:MappType = names.value
        if isinstance(MappType,int):
            if MappType not in [i.value for i in AppType]:MappType = AppType.DESKTOPWIN.value
        if not Mhost:Mhost = host.ga2.value
        if not MappType:MappType = AppType.DESKTOPWIN.value
        if not SystemName:self.systemName = 'Miya'
        if host.ga.value == Mhost:self.Hosts = f'https://{host.ga.name}.line.naver.jp'
        elif host.gb.value == Mhost:self.Hosts = f'https://{host.gb.name}.line.naver.jp'
        elif host.gd.value == Mhost:self.Hosts = f'https://{host.gd.name}.line.naver.jp'
        elif host.gm.value == Mhost:self.Hosts = f'https://{host.gm.name}.line.naver.jp'
        elif host.ga2.value == Mhost:self.Hosts = f'https://{host.ga2.name}.line.naver.jp'
        elif host.gb2.value == Mhost:self.Hosts = f'https://{host.gb2.name}.line.naver.jp'
        elif host.gd2.value == Mhost:self.Hosts = f'https://{host.gd2.name}.line.naver.jp'
        elif host.gm2.value == Mhost:self.Hosts = f'https://{host.gm2.name}.line.naver.jp'
        elif host.legy.value == Mhost:self.Hosts = f'https://{host.legy.name}-jp.line.naver.jp'
        else:raise Exception('Host Error!')
        if MappType > 0x0004 & MappType <= 0x0000:MappType = 0x0001
        if AppType.DESKTOPWIN.value == MappType:self.appList = f'DESKTOPWIN\t5.9.2\t{self.systemName}\t11.4.1\t5.9.2\tMSI\t11.10.2'
        elif AppType.DESKTOPMAC.value == MappType:self.appList = f'DESKTOPMAC\t5.9.2\t{self.systemName}\t11.4.1\t5.9.2\tMSI\t11.10.2'
        elif AppType.WIN10.value == MappType:self.appList = f'WIN10\t5.5.5\t{self.systemName}\t11.4.1\t5.5.5\tMSI\t11.10.2'
        elif AppType.CHANNELGW.value == MappType:self.appList = f'CHANNELCP\t2.9.1\t{self.systemName}\t11.4.1\t2.9.1\tSM-J320G\t10.1.1'
        else:raise Exception('APP_LIST Error!')

@enum.unique
class host(enum.Enum):
    ga = 0x0001
    gb = 0x0002
    gd= 0x0003
    gm = 0x0004
    ga2 = 0x0011
    gb2 = 0x0012
    gd2 = 0x0013
    gm2 = 0x0014
    legy = 0x0100

@enum.unique
class AppType(enum.Enum):
    DESKTOPWIN = 0x0001
    DESKTOPMAC = 0x0002
    WIN10 = 0x0003
    CHANNELGW = 0x0004