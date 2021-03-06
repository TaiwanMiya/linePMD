from PlinePMD.Tools import ProcessServerPMD
from PlinePMD.SmsActivateType import (
    GetStatusString,
    SetStatusString,
    RentString,
    ErrorString,
    ActionString,
    StatusCode,
    SuccessString,
    RentStatusCode
    )

class Activate(object):

    def __init__(self) -> None:
        self.apiurl = 'https://api.sms-activate.org/stubs/handler_api.php'
        self.req = ProcessServerPMD(self.apiurl)
        self.countrys : dict = {}
        self.services : dict = {}
        self.apikey : str = ''
        self.action : str = ''
        self.statusGet = GetStatusString
        self.statusSet = SetStatusString
        self.rent = RentString
        self.error = ErrorString
        self.motion = ActionString
        self.success = SuccessString
        self.code = StatusCode
        self.rentcode = RentStatusCode
        self.debug : bool = False
        self.result : dict = {}

    @property
    def Debug(self) -> str:
        print(f'[DEBUG]\n{self.req.GetResponse.text}')

    def ErrorResult(self,values):
        for i in self.error:
            if i.name == values:
                self.result = {'ERROR':i.name,'MESSAGE':i.value}
                return self.result
        return False

    @property
    def ResetPayload(self):
        self.req.payload = {
            'api_key': self.apikey,
            'action': self.action
        }

    @property
    def GetResult(self):
        if self.debug:
            return self.Debug

        if self.action == self.motion.GET_NUMBER.value:
            values = self.req.GetResponse.text.split(':')
            if values[0] == self.success.ACCESS_NUMBER.name:
                self.result = {'ID': values[1],'NUMBER': values[2],'MESSAGE':self.success.ACCESS_NUMBER.value}
                return self.result
            else:
                return self.ErrorResult(values[0])

        if self.action == self.motion.GET_MULTI_SERVICE_NUMBER.value:
            values = self.req.GetResponse
            log = self.ErrorResult(values.text)
            if not log:
                self.result.clear()
                count = 0
                for i in values.json():
                    count += 1
                    self.result.update({str(count):{'ID':i['activation'],'NUMBER':i['phone'],'SERVICE':i['service'],'MESSAGE':self.success.ACCESS_NUMBER.value}})
                return self.result
            else:
                return log

        if self.action == self.motion.GET_BALANCE.value:
            values = self.req.GetResponse.text.split(':')
            if values[0] == self.success.ACCESS_BALANCE.name:
                self.result = {'BALANCE': values[1],'MESSAGE':self.success.ACCESS_BALANCE.value}
                return self.result
            else:
                return self.ErrorResult(values[0])

        if self.action == self.motion.GET_STATUS.value:
            values = self.req.GetResponse.text.split(':')
            for i in self.statusGet:
                if values[0] == i.name:
                    self.result = {'STATUS': i.name,'MESSAGE': i.value}
                    return self.result
            return self.ErrorResult(values[0])

        if self.action == self.motion.SET_STATUS.value:
            values = self.req.GetResponse.text.split(':')
            for i in self.statusSet:
                if values[0] == i.name:
                    self.result = {'STATUS': i.name,'MESSAGE': i.value}
                    return self.result
            return self.ErrorResult(values[0])

        if self.action == self.motion.GET_COUNTRIES.value:
            self.result = self.req.GetResponse.json()
            return self.result

        if self.action == self.motion.GET_PRICES.value:
            self.result = self.req.GetResponse.json()
            return self.result

        if self.action == self.motion.GET_RENT_NUMBER.value:
            values = self.req.GetResponse.json()
            if values['status'] == 'error':
                error = self.ErrorResult(values['message'])
                if error:return error
                else:
                    for i in self.rent:
                        if i.name == values['message']:
                            self.result = {'ERROR':i.name,'MESSAGE':i.value}
                            return self.result
            else:
                values = values['phone']
                self.result = {'STATUS': 'success','ID':values['id'],'END_DATE': values['endDate'],'NUMBER': values['number']}
                return self.result

        if self.action == self.motion.GET_RENT_STATUS.value:
            values = self.req.GetResponse.json()
            if values['status'] == 'error':
                if 'msg' in values:
                    return self.ErrorResult(values['msg'])
                else:
                    for i in self.rent:
                        if i.name == values['message']:
                            self.result = {'ERROR':i.name,'MESSAGE':i.value}
                            return self.result
            else:
                values = values['values']
                self.result.clear()
                for i in values:
                    self.result.update(
                        {
                            i:
                            {
                                'NUMBER':values[i]['phoneFrom'],
                                'TEXT':values[i]['text'],
                                'SERVICE':values[i]['service'],
                                'DATE':values[i]['date']
                            }
                        }
                    )
                return self.result

        if self.action == self.motion.SET_RENT_STATUS.value:
            values = self.req.GetResponse.json()
            if values['status'] == 'error':
                error = self.ErrorResult(values['message'])
                if error:return error
                else:
                    for i in self.rent:
                        if i.name == values['message']:
                            self.result = {'ERROR':i.name,'MESSAGE':i.value}
                            return self.result
            else:
                self.result = {'SUCCESS': 'success'}
                return self.result

        if self.action == self.motion.GET_RENT_LIST.value:
            values = self.req.GetResponse.json()
            if values['status'] == 'error':
                error = self.ErrorResult(values['message'])
                if error:return error
                else:
                    for i in self.rent:
                        if i.name == values['message']:
                            self.result = {'ERROR':i.name,'MESSAGE':i.value}
                            return self.result
            else:
                values = values['values']
                self.result.clear()
                for i in values:
                    self.result.update(
                        {
                            i:
                            {
                                'ID': values[i]['id'],
                                'NUMBER': values[i]['phone']
                            }
                        }
                    )
                return self.result
    
    '''
    [????????????]
    - statusset , setstatus -> ????????????
    - statusget , getstatus -> ????????????
    - rent -> ????????????
    - error -> ????????????
    - action , motion -> ???????????????
    - success -> ??????????????????
    - code , statuscode , codestatus -> ??????????????????
    - rentcode , coderent -> ????????????????????????
    '''
    def Help(self,method:str):
        method= method.casefold()
        self.result.clear()
        if method in ['statusset','setstatus']:
            for i in self.statusSet:
                self.result.update({i.name:i.value})
        elif method in ['statusget','getstatus']:
            for i in self.statusGet:
                self.result.update({i.name:i.value})
        elif method == 'rent':
            for i in self.rent:
                self.result.update({i.name:i.value})
        elif method == 'error':
            for i in self.error:
                self.result.update({i.name:i.value})
        elif method in ['motion','action']:
            for i in self.motion:
                self.result.update({i.name:i.value})
        elif method == 'success':
            for i in self.success:
                self.result.update({i.name:i.value})
        elif method in ['code','statuscode','codestatus']:
            for i in self.code:
                self.result.update({i.name:i.value})
        elif method in ['rentcode','coderent']:
            for i in self.rentcode:
                self.result.update({i.name:i.value})
        else:
            self.result = {'ERROR_HELP':'No help'}
        return self.result

    '''
    [??????????????????]
    - country -> ????????????(??????:?????????)
    - service -> ????????????
    - forward -> ????????????????????????
    - freePrice -> ????????????????????????
    - maxPrice -> ???????????????????????????????????????
    - phoneException -> ??????????????????????????????,???????????????,????????????:????????????????????????3???6?????????(??????7918,7900111),???????????????????????????????????????
    - operator -> ?????????????????????????????????????????????????????????????????????
    - ref -> ????????????ID
    - verification -> ????????????True,??????????????????????????????????????? , verification ??? multiService, freePrice ????????????
    '''
    def GetNumber(self,country=None,service=None,forward=None,freePrice=None,maxPrice=None,phoneException=None,operator=None,ref=None,verification=None):
        self.action = self.motion.GET_NUMBER.value
        self.ResetPayload
        if country:
            self.req.payload['country'] = country
        if service:
            self.req.payload['service'] = service
        if forward:
            self.req.payload['forward'] = forward
        if freePrice:
            self.req.payload['freePrice'] = freePrice
        if maxPrice:
            self.req.payload['maxPrice'] = maxPrice
        if phoneException:
            self.req.payload['phoneException'] = phoneException
        if operator:
            self.req.payload['operator'] = operator
        if ref:
            self.req.payload['ref'] = ref
        if verification:
            self.req.payload['verification'] = verification
        return self.GetResult

    '''
    [?????????????????????????????????]
    - country -> ????????????(??????:?????????)
    - service -> ??????????????????(????????????)
    - forward -> ??????????????????????????????(????????????)
    - operator -> ?????????????????????????????????????????????????????????????????????
    - ref -> ????????????ID
    '''
    def GetMultiServiceNumber(self,country=None,service=None,forward=None,operator=None,ref=None):
        self.action = self.motion.GET_MULTI_SERVICE_NUMBER.value
        self.ResetPayload
        if country:
            self.req.payload['country'] = country
        if service:
            self.req.payload['multiService'] = service
        if forward:
            self.req.payload['multiForward'] = forward
        if operator:
            self.req.payload['operator'] = operator
        if ref:
            self.req.payload['ref'] = ref
        return self.GetResult

    '''
    [????????????]
    - id -> ??????ID
    '''
    def GetStatus(self,id=None):
        self.action = self.motion.GET_STATUS.value
        self.ResetPayload
        if id:
            self.req.payload['id'] = id
        return self.GetResult

    '''
    [????????????]
    - id -> ??????ID
    - status -> ????????????(?????? help -> statuscode)
    - forward -> ????????????????????????
    '''
    def SetStatus(self,id=None,status=None,forward=None):
        self.action = self.motion.SET_STATUS.value
        self.ResetPayload
        if id:
            self.req.payload['id'] = id
        if status:
            self.req.payload['status'] = status
        if forward:
            self.req.payload['forward'] = forward
        return self.GetResult

    '''
    [??????????????????]
    '''
    def GetCountries(self):
        self.action = self.motion.GET_COUNTRIES.value
        self.ResetPayload
        return self.GetResult

    '''
    [??????????????????(??????apikey)]
    '''
    def GetCountriesList(self):
        newurl = 'https://sms-activate.org/api/api.php'
        new = ProcessServerPMD(newurl)
        new.payload = {
            'act': 'getCountriesList'
        }
        self.result = new.PostResponse.json()
        return self.result

    '''
    [??????????????????(??????apikey)]
    '''
    def GetServicesList(self):
        newurl = 'https://sms-activate.org/api/api.php'
        new = ProcessServerPMD(newurl)
        new.payload = {
            'act': 'getServicesList'
        }
        self.result = new.PostResponse.json()
        return self.result

    '''
    [??????(??????/??????)???(??????/??????)????????????????????????]
    - country -> ????????????(??????:?????????)
    - service -> ????????????
    '''
    def GetPrices(self,country=None,service=None):
        self.action = self.motion.GET_PRICES.value
        self.ResetPayload
        if country:
            self.req.payload['country'] = country
        if service:
            self.req.payload['service'] = service
        return self.GetResult

    '''
    [??????????????????]
    '''
    def GetBalance(self):
        self.action = self.motion.GET_BALANCE.value
        self.ResetPayload
        return self.GetResult

    '''
    [??????????????????]
    - country -> ????????????(??????:?????????)
    - service -> ????????????
    - operator -> ?????????????????????????????????????????????????????????????????????
    - time -> ?????????????????????????????????(??????4??????),????????????????????????12??????,?????????24??????,?????????????????????????????????,?????????(24,48,72)???...
    - url -> WebHook??????????????????(?????????????????????)
    '''
    def GetRentNumber(self,country=None,service=None,operator=None,time=None,url=None):
        self.action = self.motion.GET_RENT_NUMBER.value
        self.ResetPayload
        if country:
            self.req.payload['country'] = country
        if service:
            self.req.payload['service'] = service
        if operator:
            self.req.payload['operator'] = operator
        if time:
            self.req.payload['time'] = time
        if url:
            self.req.payload['url'] = url
        return self.GetResult

    '''
    [????????????????????????]
    - id -> ??????ID
    '''
    def GetRentStatus(self,id=None):
        self.action = self.motion.GET_RENT_STATUS.value
        self.ResetPayload
        if id:
            self.req.payload['id'] = id
        return self.GetResult

    '''
    [????????????????????????]
    - id -> ??????id
    - status -> ????????????(?????? help -> rentcode)
    '''
    def SetRentStatus(self,id=None,status=None):
        self.action = self.motion.SET_RENT_STATUS.value
        self.ResetPayload
        if id:
            self.req.payload['id'] = id
        if status:
            self.req.payload['status'] = status
        return self.GetResult

    '''
    [??????????????????????????????]
    '''
    def GetRentList(self):
        self.action = self.motion.GET_RENT_LIST.value
        self.ResetPayload
        return self.GetResult