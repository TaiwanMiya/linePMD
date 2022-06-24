from enum import Enum

class GetStatusString(Enum):
    STATUS_WAIT_CODE = 'Waiting for sms\n正在等待短信'
    STATUS_WAIT_RETRY = 'Past Inappropriate Code - Waiting for Code Refinement\n正在等待準備完成'
    STATUS_WAIT_RESEND  = 'Waiting for re-sending SMS\n正在等待重新發送短信'
    STATUS_CANCEL = 'Activation canceled\n已取消的激活'
    STATUS_OK = 'Code received\n已收到短信'
    FULL_SMS = 'Full text received\n收到全文'

class SetStatusString(Enum):
    ACCESS_READY = 'Phone number ready\n號碼已準備成功'
    ACCESS_RETRY_GET  = 'Re-fetch new text messages\n已重新獲取新短信'
    ACCESS_ACTIVATION = 'Service successfully activated\n服務已成功激活'
    ACCESS_CANCEL = 'Activation canceled\n激活已取消'

class RentString(Enum):
    NO_ID_RENT  = 'Activation ID not specified\n未指定激活ID'
    INVALID_PHONE = 'You did not rent the number\n你沒有租用該號碼(租借ID錯誤)'
    STATUS_WAIT_CODE = 'Waiting for the first SMS\n等待第一條短信'
    STATUS_FINISH = 'Rent paid and completed\n租金已付並已完成'
    STATUS_CANCEL = 'Rent canceled with a refund\n租金取消並已退款'

class ErrorString(Enum):
    NO_NUMBERS = 'There are no free numbers for receiving SMS from the current service\n目前的國家與服務沒有號碼'
    NO_BALANCE = 'Not enough funds\n帳戶餘額不足'
    BAD_ACTION = 'Invalid action (action parameter)\n無效的動作,故無法作動(動作參數)'
    BAD_SERVICE = 'Incorrect service name (service parameter)\n服務名稱不正確(服務參數)'
    BAD_KEY = 'Invalid API access key\nAPI 訪問密鑰無效'
    ERROR_SQL = 'One of the parameters has an invalid value.\n參數之一具有無效值'
    SQL_ERROR = 'One of the parameters has an invalid value.\n參數之一具有無效值'
    NO_ACTIVATION = 'The specified activation id does not exist\n指定的激活 ID 不存在'
    BAD_STATUS = 'Attempt to establish a non-existent status\n不存在或無效的狀態'
    STATUS_CANCEL = 'Current activation canceled and no longer available\n當前激活已取消且不再可用'
    BANNED = 'Account is blocked\n帳戶已被凍結'
    NO_CONNECTION = 'No connection to servers sms-activate\n沒有連接到服務器 sms-activate'
    ACCOUNT_INACTIVE = 'No numbers available\n沒有可用的號碼'
    NO_ID_RENT = 'Rent id not specified\n未指定租用編號'
    INVALID_PHONE = 'The number was not rented by you (wrong rental id)\n該號碼不是您租用的(租用 ID 錯誤)'
    STATUS_FINISH = 'Rent paid and completed\n租金已付並已完成'
    INCORECT_STATUS = 'Missing or incorrect status\n狀態缺失或不正確'
    CANT_CANCEL = 'Unable to cancel the lease (more than 20 minutes have passed)\n無法取消(已超過 20 分鐘)'
    ALREADY_FINISH = 'The lease has already been completed\n租約已經完成'
    ALREADY_CANCEL = 'The lease has already been canceled\n租約已經取消'
    WRONG_OPERATOR = 'Lease Transfer Operator is not MTT\n租賃轉讓運營商不是 MTT'
    NO_YULA_MAIL = 'To buy a number from the mail group holding, you must have at least 500 rubles on your account\n要從郵件組控股購買號碼，您的帳戶必須至少有 500 盧布'
    WHATSAPP_NOT_AVAILABLE = 'No WhatsApp numbers available\n沒有可用的 WhatsApp 號碼'
    NOT_INCOMING = 'Activation is not call-verified activation\n激活不是呼叫驗證激活(沒有收到)'
    INVALID_ACTIVATION_ID = 'Invalid activation id\n無效的激活 ID'
    WRONG_ADDITIONAL_SERVICE = 'Invalid additional service (only services for forwarding are allowed)\n無效的附加服務(只允許轉發服務)'
    WRONG_ACTIVATION_ID = 'Invalid parental activation ID\n無效的家長激活 ID'
    WRONG_SECURITY = 'An error occurred when trying to transfer an activation ID without forwarding, or a completed / inactive activation\n嘗試在不轉發的情況下轉移激活 ID 或完成/非活動激活時發生錯誤'
    REPEAT_ADDITIONAL_SERVICE = 'The error occurs when you try to order the purchased service again'
    NO_KEY = 'API key missing\n缺少 API 密鑰'

class ActionString(Enum):
    GET_NUMBER = 'getNumber'
    GET_BALANCE = 'getBalance'
    GET_STATUS = 'getStatus'
    SET_STATUS = 'setStatus'
    GET_COUNTRIES = 'getCountries'
    GET_PRICES = 'getPrices'
    GET_MULTI_SERVICE_NUMBER = 'getMultiServiceNumber'
    GET_RENT_NUMBER = 'getRentNumber'
    GET_RENT_STATUS = 'getRentStatus'
    SET_RENT_STATUS = 'setRentStatus'
    GET_RENT_LIST = 'getRentList'

class SuccessString(Enum):
    ACCESS_NUMBER = 'Access to mobile phone number succeeded\n訪問手機號成功'
    ACCESS_BALANCE = 'Get account balance\n訪問帳戶餘額成功'
    ADDITIONAL = 0x04

class StatusCode(Enum):
    STOP = '-1'
    READY = '1'
    AGAIN = '3'
    DONE = '6'
    CANCEL = '8'

class RentStatusCode(Enum):
    FINISH = '1'
    CANCEL = '2'