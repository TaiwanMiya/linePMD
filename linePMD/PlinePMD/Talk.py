from thrift.Thrift import TApplicationException
from PlinePMD.Core import *
class Talk(object):

    def __init__(self,ip,op=None) -> None:
        self.ip = self.op = ip
        if op is not None:
            self.op = op
    
    def sendGetRSAKey(self, provider):
        self.op.writeMessageBegin('getRSAKeyInfo', 0x01, 0x00)
        args = getRSAKeyArgs()
        args.provider = provider
        args.write(self.op)
        self.op.writeMessageEnd()
        self.op.trans.flush()

    def recvGetRSAKey(self):
        ip = self.ip
        (_, mtype, _) = ip.readMessageBegin()
        if mtype == 0x03:
            x = TApplicationException()
            x.read(ip)
            ip.readMessageEnd()
            raise x
        result = getRSAKeyResult()
        result.read(ip)
        ip.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(0x05, "GetRSAKey failed")

    def sendGetProfile(self):
        self.op.writeMessageBegin('getProfile', 0x01, 0x00)
        args = GetProfileArgs()
        args.write(self.op)
        self.op.writeMessageEnd()
        self.op.trans.flush()

    def recvGetProfile(self):
        ip = self.ip
        (_, mtype, _) = ip.readMessageBegin()
        if mtype == 0x03:
            x = TApplicationException()
            x.read(ip)
            ip.readMessageEnd()
            raise x
        result = GetProfileResult()
        result.read(ip)
        ip.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(0x05, "GetProfile failed")

    def sendGetContact(self, contactid):
        self.op.writeMessageBegin('getContact', 0x01, 0x00)
        args = GetContactArgs()
        args.id = contactid
        args.write(self.op)
        self.op.writeMessageEnd()
        self.op.trans.flush()

    def recvGetContact(self):
        ip = self.ip
        (_, mtype, _) = ip.readMessageBegin()
        if mtype == 0x03:
            x = TApplicationException()
            x.read(ip)
            ip.readMessageEnd()
            raise x
        result = GetContactResult()
        result.read(ip)
        ip.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(0x05, "GetContact failed")

    def sendGetContacts(self, midlist):
        self.op.writeMessageBegin('getContacts', 0x01, 0x00)
        args = GetContactsArgs()
        args.ids = midlist
        args.write(self.op)
        self.op.writeMessageEnd()
        self.op.trans.flush()

    def recvGetContacts(self):
        ip = self.ip
        (_, mtype, _) = ip.readMessageBegin()
        if mtype == 0x03:
            x = TApplicationException()
            x.read(ip)
            ip.readMessageEnd()
            raise x
        result = GetContactsResult()
        result.read(ip)
        ip.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(0x05, "GetContacts failed")

    def sendAddFriend(self, mid):
        self.op.writeMessageBegin('findAndAddContactsByMid', 0x01, 0x00)
        args = AddFriendArgs()
        args.reqSeq = 0x00
        args.mid = mid
        args.type = 0x00
        args.reference = ''
        args.write(self.op)
        self.op.writeMessageEnd()
        self.op.trans.flush()

    def recvAddFriend(self):
        ip = self.ip
        (_, mtype, _) = ip.readMessageBegin()
        if mtype == 0x03:
            x = TApplicationException()
            x.read(ip)
            ip.readMessageEnd()
            raise x
        result = AddFriendResult()
        result.read(ip)
        ip.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(0x05, "AddFriend failed")

    def sendGetAllFriends(self):
        self.op.writeMessageBegin('getAllContactIds', 0x01, 0x00)
        args = GetAllFriendsArgs()
        args.write(self.op)
        self.op.writeMessageEnd()
        self.op.trans.flush()

    def recvGetAllFriends(self):
        ip = self.ip
        (_, mtype, _) = ip.readMessageBegin()
        if mtype == 0x03:
            x = TApplicationException()
            x.read(ip)
            ip.readMessageEnd()
            raise x
        result = GetAllFriendsResult()
        result.read(ip)
        ip.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(0x05, "GetAllFriend failed")

    def sendGetGroup(self, groupId):
        self.op.writeMessageBegin('getGroup', 0x01, 0x00)
        args = GetGroupArgs()
        args.groupId = groupId
        args.write(self.op)
        self.op.writeMessageEnd()
        self.op.trans.flush()

    def recvGetGroup(self):
        ip = self.ip
        (_, mtype, _) = ip.readMessageBegin()
        if mtype == 0x03:
            x = TApplicationException()
            x.read(ip)
            ip.readMessageEnd()
            raise x
        result = GetGroupResult()
        result.read(ip)
        ip.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(0x05, "GetGroup failed")

    def sendGetGroups(self, gidlist):
        self.op.writeMessageBegin('getGroups', 0x01, 0x00)
        args = GetGroupsArgs()
        args.groupIds = gidlist
        args.write(self.op)
        self.op.writeMessageEnd()
        self.op.trans.flush()

    def recvGetGroups(self):
        ip = self.ip
        (_, mtype, _) = ip.readMessageBegin()
        if mtype == 0x03:
            x = TApplicationException()
            x.read(ip)
            ip.readMessageEnd()
            raise x
        result = GetGroupsResult()
        result.read(ip)
        ip.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(0x05, "GetGroups failed")

    def sendGetGroupids(self):
        self.op.writeMessageBegin('getGroupIdsJoined', 0x01, 0x00)
        args = GetGroupidsArgs()
        args.write(self.op)
        self.op.writeMessageEnd()
        self.op.trans.flush()

    def recvGetGroupids(self):
        ip = self.ip
        (_, mtype, _) = ip.readMessageBegin()
        if mtype == 0x03:
            x = TApplicationException()
            x.read(ip)
            ip.readMessageEnd()
            raise x
        result = GetGroupidsResult()
        result.read(ip)
        ip.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(0x05, "GetGroupids failed")

    def sendInvitation(self, groupId, contactIds):
        self.op.writeMessageBegin('inviteIntoGroup', 0x01, 0x00)
        args = InvitationArgs()
        args.reqSeq = 0x00
        args.groupId = groupId
        args.contactIds = contactIds
        args.write(self.op)
        self.op.writeMessageEnd()
        self.op.trans.flush()

    def recvInvitation(self):
        ip = self.ip
        (_, mtype, _) = ip.readMessageBegin()
        if mtype == 0x03:
            x = TApplicationException()
            x.read(ip)
            ip.readMessageEnd()
            raise x
        result = InvitationResult()
        result.read(ip)
        ip.readMessageEnd()
        if result.e is not None:
            raise result.e
        return

    def sendKickout(self, groupId, contactIds):
        self.op.writeMessageBegin('kickoutFromGroup', 0x01, 0x00)
        args = KickoutArgs()
        args.reqSeq = 0x00
        args.groupId = groupId
        args.contactIds = contactIds
        args.write(self.op)
        self.op.writeMessageEnd()
        self.op.trans.flush()

    def recvKickout(self):
        ip = self.ip
        (_, mtype, _) = ip.readMessageBegin()
        if mtype == 0x03:
            x = TApplicationException()
            x.read(ip)
            ip.readMessageEnd()
            raise x
        result = KickoutResult()
        result.read(ip)
        ip.readMessageEnd()
        if result.e is not None:
            raise result.e
        return

    def sendCancelInvitation(self, groupId, contactIds):
        self.op.writeMessageBegin('cancelGroupInvitation', 0x01, 0x00)
        args = CancelInvitationArgs()
        args.reqSeq = 0x00
        args.groupId = groupId
        args.contactIds = contactIds
        args.write(self.op)
        self.op.writeMessageEnd()
        self.op.trans.flush()

    def recvCancelInvitation(self):
        ip = self.ip
        (_, mtype, _) = ip.readMessageBegin()
        if mtype == 0x03:
            x = TApplicationException()
            x.read(ip)
            ip.readMessageEnd()
            raise x
        result = CancelInvitationResult()
        result.read(ip)
        ip.readMessageEnd()
        if result.e is not None:
            raise result.e
        return

    def sendSendMessage(self, seq, message):
        self.op.writeMessageBegin('sendMessage', 0x01, 0x00)
        args = SendMessageArgs()
        args.seq = seq
        args.message = message
        args.write(self.op)
        self.op.writeMessageEnd()
        self.op.trans.flush()

    def recvSendMessage(self):
        ip = self.ip
        (_, mtype, _) = ip.readMessageBegin()
        if mtype == 0x03:
            x = TApplicationException()
            x.read(ip)
            ip.readMessageEnd()
            raise x
        result = SendMessageResult()
        result.read(ip)
        ip.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(0x05, "SendMessage failed")

    def sendRetractMessage(self, seq, messageId):
        self.op.writeMessageBegin('unsendMessage', 0x01, 0x00)
        args = RetractMessageArgs()
        args.seq = seq
        args.messageId = messageId
        args.write(self.op)
        self.op.writeMessageEnd()
        self.op.trans.flush()

    def recvRetractMessage(self):
        ip = self.ip
        (_, mtype, _) = ip.readMessageBegin()
        if mtype == 0x03:
            x = TApplicationException()
            x.read(ip)
            ip.readMessageEnd()
            raise x
        result = RetractMessageResult()
        result.read(ip)
        ip.readMessageEnd()
        if result.e is not None:
            raise result.e
        return

    def sendGetRecentMessages(self, groupid, counter):
        self.op.writeMessageBegin('getRecentMessagesV2', 0x01, 0x00)
        args = GetRecentMessagesArgs()
        args.groupid = groupid
        args.counter = counter
        args.write(self.op)
        self.op.writeMessageEnd()
        self.op.trans.flush()

    def recvGetRecentMessages(self):
        ip = self.ip
        (_, mtype, _) = ip.readMessageBegin()
        if mtype == 0x03:
            x = TApplicationException()
            x.read(ip)
            ip.readMessageEnd()
            raise x
        result = GetRecentMessagesResult()
        result.read(ip)
        ip.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(0x05, "GetRecentMessages failed")

    def sendIntoGroup(self,groupid):
        self.op.writeMessageBegin('acceptGroupInvitation', 0x01, 0x00)
        args = IntoGroupArgs()
        args.reqSeq = 0x00
        args.groupId = groupid
        args.write(self.op)
        self.op.writeMessageEnd()
        self.op.trans.flush()

    def recvIntoGroup(self):
        ip = self.ip
        (_, mtype, _) = ip.readMessageBegin()
        if mtype == 0x03:
            x = TApplicationException()
            x.read(ip)
            ip.readMessageEnd()
            raise x
        result = IntoGroupResult()
        result.read(ip)
        ip.readMessageEnd()
        if result.e is not None:
            raise result.e
        return

    def sendFindGroupByUrl(self, ticketId):
        self.op.writeMessageBegin('findGroupByTicketV2', 0x01, 0x00)
        args = FindGroupByUrlArgs()
        args.ticketId = ticketId
        args.write(self.op)
        self.op.writeMessageEnd()
        self.op.trans.flush()

    def recvFindGroupByUrl(self):
        ip = self.ip
        (_, mtype, _) = ip.readMessageBegin()
        if mtype == 0x03:
            x = TApplicationException()
            x.read(ip)
            ip.readMessageEnd()
            raise x
        result = FindGroupByUrlResult()
        result.read(ip)
        ip.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(0x05, "FindGroupByUrl failed")

    def sendCreateGroup(self, name, contactIds):
        self.op.writeMessageBegin('createGroup', 0x01, 0x00)
        args = CreateGroupArgs()
        args.seq = 0x00
        args.name = name
        args.contactIds = contactIds
        args.write(self.op)
        self.op.writeMessageEnd()
        self.op.trans.flush()

    def recvCreateGroup(self):
        ip = self.ip
        (_, mtype, _) = ip.readMessageBegin()
        if mtype == 0x03:
            x = TApplicationException()
            x.read(ip)
            ip.readMessageEnd()
            raise x
        result = CreateGroupResult()
        result.read(ip)
        ip.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(0x05, "CreateGroup failed")

    def sendUpdateGroupUrl(self, groupMid):
        self.op.writeMessageBegin('reissueGroupTicket', 0x01, 0x00)
        args = UpdateGroupUrlArgs()
        args.groupMid = groupMid
        args.write(self.op)
        self.op.writeMessageEnd()
        self.op.trans.flush()

    def recvUpdateGroupUrl(self):
        ip = self.ip
        (_, mtype, _) = ip.readMessageBegin()
        if mtype == 0x03:
            x = TApplicationException()
            x.read(ip)
            ip.readMessageEnd()
            raise x
        result = UpdateGroupUrlResult()
        result.read(ip)
        ip.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(0x05, "UpdateGroupUrl failed")

    def sendUrlIntoGroup(self,groupid,route):
        self.op.writeMessageBegin('acceptGroupInvitationByTicket', 0x01, 0x00)
        args = UrlIntoGroupArgs()
        args.reqSeq = 0x00
        args.GroupMid = groupid
        args.ticketId = route
        args.write(self.op)
        self.op.writeMessageEnd()
        self.op.trans.flush()

    def recvUrlIntoGroup(self):
        ip = self.ip
        (_, mtype, _) = ip.readMessageBegin()
        if mtype == 0x03:
            x = TApplicationException()
            x.read(ip)
            ip.readMessageEnd()
            raise x
        result = UrlIntoGroupResult()
        result.read(ip)
        ip.readMessageEnd()
        if result.e is not None:
            raise result.e
        return

    def sendOutGroup(self, groupId):
        self.op.writeMessageBegin('leaveGroup', 0x01, 0x00)
        args = OutGroupArgs()
        args.reqSeq = 0x00
        args.groupId = groupId
        args.write(self.op)
        self.op.writeMessageEnd()
        self.op.trans.flush()

    def recvOutGroup(self):
        ip = self.ip
        (_, mtype, _) = ip.readMessageBegin()
        if mtype == 0x03:
            x = TApplicationException()
            x.read(ip)
            ip.readMessageEnd()
            raise x
        result = OutGroupResult()
        result.read(ip)
        ip.readMessageEnd()
        if result.e is not None:
            raise result.e
        return

    def sendUpdateGroup(self, group):
        self.op.writeMessageBegin('updateGroup', 0x01, 0x00)
        args = UpdateGroupArgs()
        args.reqSeq = 0x00
        args.group = group
        args.write(self.op)
        self.op.writeMessageEnd()
        self.op.trans.flush()

    def recvUpdateGroup(self):
        ip = self.ip
        (_, mtype, _) = ip.readMessageBegin()
        if mtype == 0x03:
            x = TApplicationException()
            x.read(ip)
            ip.readMessageEnd()
            raise x
        result = UpdateGroupResult()
        result.read(ip)
        ip.readMessageEnd()
        if result.e is not None:
            raise result.e
        return

    def sendCreateRoom(self, contactIds):
        self.op.writeMessageBegin('createRoomV2', 0x01, 0x00)
        args = CreateRoomArgs()
        args.reqSeq = 0x00
        args.contactIds = contactIds
        args.write(self.op)
        self.op.writeMessageEnd()
        self.op.trans.flush()

    def recvCreateRoom(self):
        ip = self.ip
        (_, mtype, _) = ip.readMessageBegin()
        if mtype == 0x03:
            x = TApplicationException()
            x.read(ip)
            ip.readMessageEnd()
            raise x
        result = CreateRoomResult()
        result.read(ip)
        ip.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(0x05, "CreateRoom failed")

    def sendOutRoom(self, roomId):
        self.op.writeMessageBegin('leaveRoom', 0x01, 0x00)
        args = OutRoomArgs()
        args.reqSeq = 0x00
        args.roomId = roomId
        args.write(self.op)
        self.op.writeMessageEnd()
        self.op.trans.flush()

    def recvOutRoom(self):
        ip = self.ip
        (_, mtype, _) = ip.readMessageBegin()
        if mtype == 0x03:
            x = TApplicationException()
            x.read(ip)
            ip.readMessageEnd()
            raise x
        result = OutRoomResult()
        result.read(ip)
        ip.readMessageEnd()
        if result.e is not None:
            raise result.e
        return