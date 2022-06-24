# 導入初始化類別
# import initialization class
from PlinePMD.Initial import linePMD

# 導入API
# import API
from PlinePMD.Service import service

# 導入回傳
# import postback
from PlinePMD.Replys import Reply
import sys
import os
import traceback
import time

# 輸入帳號密碼 或者token
# Enter account password or token
main = linePMD('')

# 調用API必需把linePMD加入至service內,否則無法使用
# Calling the API must add linePMD to the service, otherwise it cannot be used
svo = service(main)

# 調用回傳必須把linePMD加入至Reply內,否則無法使用,參數'50'則是每次回傳需求數量
# The call back must add linePMD to Reply, otherwise it cannot be used, 
# The parameter '50' is the number of requests returned each time
rep = Reply(main,50)

# 獲取自身所有狀態
# Get all state of self
profile = svo.GetProfile()

# 定義你的UI來做為運行時的判斷
# Define your UI for runtime judgment
def run(op):

    try:

        # op.type 13 124 是邀請時的偵測
        # op.type 13 124 is the detection when inviting
        if op.type in [13,124]:
            if op.param3 == profile.mid:
                svo.IntoGroup(op.param1)
                svo.SendMessage(op.param1,'成功入群\nsuccessfully joined the group')

        # op.type 25 26 是發送訊息與收到訊息的偵測
        # op.type 25 26 is the detection of sent and received messages
        if op.type in [25,26]:
            text : str = op.message.text
            to : str = op.message.to
            id : str = op.message.id
            be : str = op.message._from
            reid : str = op.message.relatedMessageId
            data : str = op.message.contentMetadata
            types : int = op.message.contentType
            if text != None:

                if types == 0:

                    if text.lower() == 'sp':
                        start = time.time()
                        svo.SendMessage(to,'Speed test')
                        end = time.time() - start
                        svo.SendMessage(to,str(end))

                    # 發送多個訊息
                    # send multiple message
                    elif text.lower().startswith('msg'):
                        message = text[3:]
                        if ' ' not in message:
                            raise Exception('需要空格分割次數與字串\n\
                            Need spaces to separate the number of times and strings')
                        else:
                            message = message.split(' ')
                            count = 1
                            msg = ''
                            for i in message:
                                if i.isdecimal():
                                    count = int(i)
                                else:
                                    msg += i
                            for i in range(count):
                                svo.SendMessage(to,msg)

                    # 收回訊息
                    # retract message
                    elif text.lower().startswith('un'):
                        unsend = text.rstrip('un')
                        retract = []
                        if unsend.isdecimal():
                            messages = svo.GetRecentMessages(to)
                            for message in messages:
                                if be == profile.mid:
                                    if len(retract) < int(unsend):
                                        retract.append(message.id)
                            for i in retract:
                                svo.RetractMessage(i)
                        else:
                            svo.SendMessage(to,'無效的收回\ninvalid retraction')

                    # 退出群組或房間
                    # leave a group or room
                    elif text.lower() == 'out':
                        try:
                            svo.LeaveGroup(to)
                        except:
                            svo.LeaveRoom(to)

                    # 重新登入
                    # log in again
                    elif text.lower() == 'reb':
                        sys.stdout.flush()
                        os.execv(sys.executable, [sys.executable] + sys.argv)

                    # 登出
                    # Signout
                    elif text.lower() == 'signout':
                        os._exit(0)

            if data != None:
                print(data)

    except:traceback.print_exc()

if __name__ == "__main__":

    # 主程式進入點,進行迴圈判斷
    # Main program entry point, make loop judgment
    while 1:
        try:
            
            # 定義回傳列表
            # Define the return list
            ops = rep.Trace
            if ops != None:
                for op in ops:

                    # 進入UI判斷定義
                    # Enter UI judgment definition
                    run(op)

                    # 必須調整你的回傳參數,否則會接收失敗
                    # You must adjust your return parameters, otherwise it will fail to receive
                    rep.SettingsRevision(op.revision)
        except:
            traceback.print_exc()