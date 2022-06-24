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
    [查看幫助]
    - statusset , setstatus -> 設定狀態
    - statusget , getstatus -> 獲取狀態
    - rent -> 租用服務
    - error -> 錯誤訊息
    - action , motion -> 作動與命令
    - success -> 訪問成功訊息
    - code , statuscode , codestatus -> 狀態代碼訊息
    - rentcode , coderent -> 租用狀態代碼訊息
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
    [獲取手機號碼]
    - country -> 國家代碼(默認:俄羅斯)
    - service -> 服務代碼
    - forward -> 是否轉發請求號碼
    - freePrice -> 使用免費價格購買
    - maxPrice -> 免费價格購買房間的最高價格
    - phoneException -> 不包括俄语數字的前綴,用逗號指定,記錄格式:國家代碼和掩碼的3到6位數字(例如7918,7900111),默認值在左側菜單中設置的值
    - operator -> 號碼的移動供應商，可以指定多個以逗號分隔的號碼
    - ref -> 轉移推薦ID
    - verification -> 如果傳遞True,獲取一個能夠接收呼叫的號碼 , verification 與 multiService, freePrice 不起作用
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
    [獲取多個服務的手機號碼]
    - country -> 國家代碼(默認:俄羅斯)
    - service -> 多個服務代碼(逗號隔開)
    - forward -> 多個是否轉發請求號碼(逗號隔開)
    - operator -> 號碼的移動供應商，可以指定多個以逗號分隔的號碼
    - ref -> 轉移推薦ID
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
    [獲取狀態]
    - id -> 激活ID
    '''
    def GetStatus(self,id=None):
        self.action = self.motion.GET_STATUS.value
        self.ResetPayload
        if id:
            self.req.payload['id'] = id
        return self.GetResult

    '''
    [設定狀態]
    - id -> 激活ID
    - status -> 設置狀態(詳見 help -> statuscode)
    - forward -> 是否轉發請求號碼
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
    [獲取所有國家]
    '''
    def GetCountries(self):
        self.action = self.motion.GET_COUNTRIES.value
        self.ResetPayload
        return self.GetResult

    '''
    [獲取所有國家(無須apikey)]
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
    [獲取所有服務(無須apikey)]
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
    [獲取(指定/所有)的(國家/服務)的價格與剩餘數量]
    - country -> 國家代碼(默認:俄羅斯)
    - service -> 服務代碼
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
    [獲取帳戶餘額]
    '''
    def GetBalance(self):
        self.action = self.motion.GET_BALANCE.value
        self.ResetPayload
        return self.GetResult

    '''
    [獲取租用號碼]
    - country -> 國家代碼(默認:俄羅斯)
    - service -> 服務代碼
    - operator -> 號碼的移動供應商，可以指定多個以逗號分隔的號碼
    - time -> 已小時為單位的租聘時間(默認4小時),下一個可用時段是12小時,然後是24小時,申請一天或者更長的時間,需輸入(24,48,72)等...
    - url -> WebHook掛勾服務連接(默認情況不考慮)
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
    [獲取租用號碼狀態]
    - id -> 激活ID
    '''
    def GetRentStatus(self,id=None):
        self.action = self.motion.GET_RENT_STATUS.value
        self.ResetPayload
        if id:
            self.req.payload['id'] = id
        return self.GetResult

    '''
    [設定租用號碼狀態]
    - id -> 激活id
    - status -> 設置狀態(詳見 help -> rentcode)
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
    [獲取當前所有租用列表]
    '''
    def GetRentList(self):
        self.action = self.motion.GET_RENT_LIST.value
        self.ResetPayload
        return self.GetResult