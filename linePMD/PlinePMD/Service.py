from PlinePMD.Core import Message,Group,Room,Contact,Profile,TalkException
from PlinePMD.Tools import FileTransfer
from random import randint
class service(object):
    message = {}
    retract = 0

    def __init__(self, sender=None):
        self.sender = sender

    # User

    def GetProfile(self) -> Profile:
        '''
        - Get self Profile
        - 獲取自身簡介
        - self.GetProfile()
        '''
        self.sender.talk.sendGetProfile()
        return self.sender.talk.recvGetProfile()

    # Contact

    def GetContact(self,mid:str) -> Contact:
        '''
        - Get single Contact
        - 獲取單個聯繫人
        - self.GetContact(self,mid)
        '''
        self.sender.talk.sendGetContact(mid)
        return self.sender.talk.recvGetContact()

    def GetContacts(self,midlist:list) -> Contact:
        '''
        - Get multiple Contacts
        - 獲取多個聯繫人
        - self.GetContacts(self,midlist)
        '''
        self.sender.talk.sendGetContacts(midlist)
        return self.sender.talk.recvGetContacts()

    def AddFriend(self,mid:str) -> Contact:
        '''
        - Add Friend
        - 加入好友
        - self.AddFriend(mid)
        '''
        self.sender.talk.sendAddFriend(mid)
        return self.sender.talk.recvAddFriend()

    def GetAllFriends(self):
        '''
        - Get self all friend
        - 獲取自身所有好友
        - self.GetAllFriends()
        '''
        self.sender.talk.sendGetAllFriends()
        return self.sender.talk.recvGetAllFriends()

    # Group
    
    def GetGroup(self,gid:str) -> Group:
        '''
        - Get single Group
        - 獲取單個群組信息
        - self.GetGroup(gid)
        '''
        self.sender.talk.sendGetGroup(gid)
        return self.sender.talk.recvGetGroup()

    def GetGroups(self, gidlist:list) -> Group:
        '''
        - Get multiple Groups
        - 獲取多個群組信息
        - self.GetGroups(gidlist)
        '''
        self.sender.talk.sendGetGroups(gidlist)
        return self.sender.talk.recvGetGroups()

    def GetGroupids(self) -> list:
        '''
        - Get all own groups id
        - 獲取自身所有群組
        - self.GetGroupids()
        '''
        self.sender.talk.sendGetGroupids()
        return self.sender.talk.recvGetGroupids()

    def Invitation(self,gid:str,midlist:list):
        '''
        - Invite to group
        - 邀請加入群組
        - self.Invitation(gid,midlist)
        '''
        self.sender.talk.sendInvitation(gid,midlist)
        return self.sender.talk.recvInvitation()

    def Kickout(self,gid:str,midlist:list):
        '''
        - kick out of group
        - 踢出群組
        - self.Kickout(gid,midlist)
        '''
        self.sender.talk.sendKickout(gid,midlist)
        return self.sender.talk.recvKickout()

    def CancelInvitation(self,gid:str,mid:str):
        '''
        - Cancel Group Invitation
        - 取消邀請
        - self.CancelInvitation(gid,mid)
        '''
        self.sender.talk.sendCancelInvitation(gid,mid)
        return self.sender.talk.recvCancelInvitation()

    def IntoGroup(self,gid:str):
        '''
        - Join the group yourself
        - 自身加入群組
        - self.IntoGroup(gid)
        '''
        self.sender.talk.sendIntoGroup(gid)
        return self.sender.talk.recvIntoGroup()

    def FindGroupByUrl(self, urlid:str) -> Group:
        '''
        - Find groups using URL
        - 依據網址找到群組
        - self.FindGroupByUrl(urlid)
        '''
        self.sender.talk.sendFindGroupByUrl(urlid)
        return self.sender.talk.recvFindGroupByUrl()

    def CreateGroup(self,groupname:str,midlist:list) -> Group:
        '''
        - Create new Group
        - 創建新群組
        - self.CreateGroup(groupname,midlist)
        '''
        self.sender.talk.sendCreateGroup(groupname,midlist)
        return self.sender.talk.recvCreateGroup()

    def UpdateGroupUrl(self,gid:str):
        '''
        - Update group URL
        - 更新群組網址
        - self.UpdateGroupUrl(gid)
        '''
        self.sender.talk.sendUpdateGroupUrl(gid)
        return self.sender.talk.recvUpdateGroupUrl()

    def UrlIntoGroup(self,gid:str,urlid:str):
        '''
        - URL to join group
        - 網址加入群組
        - self.UrlIntoGroup(gid,urlid)
        '''
        self.sender.talk.sendUrlIntoGroup(gid,urlid)
        return self.sender.talk.recvUrlIntoGroup()

    def LeaveGroup(self,gid):
        '''
        - Leave group
        - 退出群組
        - self.LeaveGroup(gid)
        '''
        self.sender.talk.sendOutGroup(gid)
        return self.sender.talk.recvOutGroup()

    def UpdateGroup(self,group:object):
        '''
        - Update group
        - 更新群組
        - self.UpdateGroup(group)
        '''
        self.sender.talk.sendUpdateGroup(group)
        return self.sender.talk.recvUpdateGroup()

    # Room

    def CreateRoom(self, midlist:list) -> Room:
        '''
        - Create new Room(copys)
        - 創建新房間(副本)
        - self.CreateRoom(midlist)
        '''
        self.sender.talk.sendCreateRoom(midlist)
        return self.sender.talk.recvCreateRoom()

    def LeaveRoom(self, rid:str):
        '''
        - Leave Room
        - 退出房間
        - self.LeaveRoom(rid)
        '''
        self.sender.talk.sendOutRoom(rid)
        return self.sender.talk.recvOutRoom()

    # Message

    def SendMessage(self,to:str,text:str,msgid:str=None,data:dict={},types:int=0) -> Message:
        '''
        - Send Message
        - 發送訊息
        - self.SendMessage(msgto,msgtext,msgid,msgdata,msgtype)
        '''
        msg = Message()
        msg.to, msg._from = to, self.sender.profile.mid
        msg.text = text
        msg.contentType, msg.contentMetadata = types, data
        if msgid != None:msg.relatedMessageId, msg.messageRelationType ,msg.relatedMessageServiceCode = msgid,0x03,0x01
        if to not in self.message:self.message[to] = -1
        self.message[to] += 1
        self.sender.talk.sendSendMessage(self.message[to], msg)
        return self.sender.talk.recvSendMessage()

    def RetractMessage(self,msgid:str):
        '''
        - Retract Message
        - 收回訊息
        - self.RetractMessage(msgid)
        '''
        self.retract += 1
        self.sender.talk.sendRetractMessage(self.retract, msgid)
        return self.sender.talk.recvRetractMessage()

    def GetRecentMessages(self,gid:str,counter:int=1000) -> Message:
        '''
        - Get Recent Messages
        - 獲取最近的訊息
        - self.GetRecentMessages(gid,counter)
        '''
        self.sender.talk.sendGetRecentMessages(gid,counter)
        return self.sender.talk.recvGetRecentMessages()

    def SendSticker(self,to:str,package:str,sticker:str,id=None) -> Message:
        '''
        - Send Sticker
        - 發送貼圖
        - self.SendSticker(msgto,package,sticker,msgid)
        '''
        if package.isdecimal() and sticker.isdecimal():
            data = {
                'STKTXT': '[Sticker]',
                'STKVER': '1',
                'STKPKGID': package,
                'STKID': sticker
            }
            return self.SendMessage(to,str(),id,data,7)

    def SendContact(self,to:str,mid:str,id:str=None) -> Message:
        '''
        - Send friend information
        - 發送好友資訊
        - self.SendContact(msgto,mid,msgid)
        '''
        if isinstance(mid,str):
            data = {'mid': mid}
            return self.SendMessage(to,str(),id,data,13)

    # Media

    def SendImage(self,to:str,path:str) -> Message:
        '''
        - Send local pictures
        - 發送本地圖片
        - self.SendImage(msgto,path)
        '''
        id = self.SendMessage(to,None,types=1).id
        return FileTransfer().UploadFile(path=path, type='image', returnAs='bool', id=id, to=to, revision=self.sender.revision, headers=self.sender.header)

    def SendGif(self,to:str,path:str) -> Message:
        '''
        - Send local gif file
        - 發送本地gif圖片
        - self.SendGif(msgto,path)
        '''
        return FileTransfer().UploadFile(path=path, type='gif', returnAs='bool', to=to, revision=self.sender.revision, headers=self.sender.header)

    def SendVideo(self,to:str,path:str) -> Message:
        '''
        - Send local video
        - 發送本地影片
        - self.SendVideo(msgto,path)
        '''
        id = self.SendMessage(to,None,types=2,data={'VIDLEN': '60000','DURATION': '60000'}).id
        return FileTransfer().UploadFile(path=path, type='video', returnAs='bool', id=id, to=to, revision=self.sender.revision, headers=self.sender.header)

    def SendAudio(self,to:str,path:str) -> Message:
        '''
        - Send local audio
        - 發送本地音檔
        - self.SendAudio(msgto,path)
        '''
        id = self.SendMessage(to,None,types=3).id
        return FileTransfer().UploadFile(path=path, type='audio', returnAs='bool', id=id, to=to, revision=self.sender.revision, headers=self.sender.header)

    def SendImageWithURL(self,to:str,url:str,path:str='') -> Message:
        '''
        - Send URL pictures
        - 發送網址圖片
        - self.SendImageWithURL(msgto,url)
        '''
        path = FileTransfer().DownloadFile(url,'path', saveAs=path,headers=self.sender.header)
        return self.SendImage(to, path)

    def SendGifWithURL(self,to:str,url:str,path:str='') -> Message:
        '''
        - Send URL gif file
        - 發送網址gif圖片
        - self.SendGifWithURL(msgto,url)
        '''
        path = FileTransfer().DownloadFile(url,'path', saveAs=path,headers=self.sender.header)
        return self.SendGif(to, path)

    def SendVideoWithURL(self,to:str,url:str,path:str='') -> Message:
        '''
        - Send URL video
        - 發送網址影片
        - self.SendVideoWithURL(msgto,url)
        '''
        path = FileTransfer().DownloadFile(url, 'path', saveAs=path,headers=self.sender.header)
        return self.SendVideo(to, path)

    def SendAudioWithURL(self,to:str,url:str,path:str='') -> Message:
        '''
        - Send URL audio
        - 發送網址音檔
        - self.SendAudioWithURL(msgto,url)
        '''
        path = FileTransfer().DownloadFile(url, 'path', saveAs=path,headers=self.sender.header)
        return self.SendAudio(to, path)