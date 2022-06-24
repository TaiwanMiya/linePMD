from PlinePMD.Initial import smsPMD
import json
import codecs

class TestSMS(object):

    def __init__(self) -> None:
        self.sms = smsPMD('') # 輸入你的 api key
        # self.sms.debug = True
        self.Country = json.load(codecs.open('GetCountrys.json','r','utf-8'))
        self.CountriesList = json.load(codecs.open('GetCountries.json','r','utf-8'))
        self.ServiceList = json.load(codecs.open('GetServices.json','r','utf-8'))
        self.Prices = json.load(codecs.open('GetPrices.json','r','utf-8'))

    def save(self):
        json.dump(self.Country,codecs.open('GetCountrys.json','w','utf-8'),sort_keys=True,indent=4,ensure_ascii=False)
        json.dump(self.CountriesList,codecs.open('GetCountries.json','w','utf-8'),sort_keys=False,indent=4,ensure_ascii=False)
        json.dump(self.ServiceList,codecs.open('GetServices.json','w','utf-8'),sort_keys=True,indent=4,ensure_ascii=False)
        json.dump(self.Prices,codecs.open('GetPrices.json','w','utf-8'),sort_keys=True,indent=4,ensure_ascii=False)

    def help(self,where:str):
        if where.casefold() == 'setstatus':
            self.sms.HelpSetStatus()
        elif where.casefold() == 'getstatus':
            self.sms.HelpGetStatus()
        for i,x in self.sms.result.items():
            print(f'[{i}]\n{x}')

    def getCountry(self):
        self.Country = self.sms.GetCountries()
        self.save()
        for i,x in self.sms.result.items():
            print(f'{i}:{x}')

    def getCountries(self):
        self.CountriesList = self.sms.GetCountriesList()['data']
        self.save()
        for i,x in self.sms.result.items():
            print(f'{i}:{x}')

    def getService(self):
        self.ServiceList = self.sms.GetServicesList()['data']
        self.save()
        for i,x in self.sms.result.items():
            print(f'{i}:{x}')

    def getPrices(self):
        self.Prices = self.sms.GetPrices()
        self.save()
        for i,x in self.sms.result.items():
            print(f'{i}:{x}')

    def getPhone(self,country=None,service=None):
        self.sms.GetNumber(country,service)
        for i,x in self.sms.result.items():
            print(f'{i}:{x}')
        return self.sms.result['ID']

    def getBalance(self):
        self.sms.GetBalance()
        for i,x in self.sms.result.items():
            print(f'{i}:{x}')

    def getStatus(self,id=None):
        self.sms.GetStatus(id)
        for i,x in self.sms.result.items():
            print(f'{i} ->\n{x}')

    def setStatus(self,id,status):
        self.sms.SetStatus(id,status)
        for i,x in self.sms.result.items():
            print(f'{i} ->\n{x}')

    def getMultiServiceNumber(self,country=None,service=None):
        self.sms.GetMultiServiceNumber(country,service)
        for i,x in self.sms.result.items():
            print(f'{i} ->\n{x}')

    def getRentNumber(self,country=None,service=None):
        self.sms.GetRentNumber(country,service)
        for i,x in self.sms.result.items():
            print(f'{i} ->\n{x}')

    def getRentStatus(self,id=None):
        self.sms.GetRentStatus(id)
        for i,x in self.sms.result.items():
            print(f'{i} ->\n{x}')

    def setRentStatus(self,id=None,status=None):
        self.sms.SetRentStatus(id,status)
        for i,x in self.sms.result.items():
            print(f'{i} ->\n{x}')

    def getRentList(self):
        self.sms.GetRentList()
        for i,x in self.sms.result.items():
            print(f'{i} ->\n{x}')

if __name__ and '__main__':
    test = TestSMS()
    # test.getMultiServiceNumber(6,'me,me')
    # numberid = test.getPhone(6,'me')
    # test.getStatus(901468358)
    # test.setStatus(901624888,-1)
    # test.getPrices()
    # test.help('getstatus')
    # test.getRentNumber(6,'me')
    # test.getRentStatus(5688963)
    # test.setRentStatus(5688963,1)
    # test.getRentList()