import sys
from thrift.Thrift import TException
from PlinePMD.Tools import ReprPMD

class Contact(object):

    def __init__(self, mid=None, createdTime=None, type=None, status=None, relation=None, displayName=None, phoneticName=None, pictureStatus=None, thumbnailUrl=None, statusMessage=None, displayNameOverridden=None, favoriteTime=None, capableVoiceCall=None, capableVideoCall=None, capableMyhome=None, capableBuddy=None, attributes=None, settings=None, picturePath=None, recommendParams=None, friendRequestStatus=None, musicProfile=None, videoProfile=None):
        self.mid = mid
        self.createdTime = createdTime
        self.type = type
        self.status = status
        self.relation = relation
        self.displayName = displayName
        self.phoneticName = phoneticName
        self.pictureStatus = pictureStatus
        self.thumbnailUrl = thumbnailUrl
        self.statusMessage = statusMessage
        self.displayNameOverridden = displayNameOverridden
        self.favoriteTime = favoriteTime
        self.capableVoiceCall = capableVoiceCall
        self.capableVideoCall = capableVideoCall
        self.capableMyhome = capableMyhome
        self.capableBuddy = capableBuddy
        self.attributes = attributes
        self.settings = settings
        self.picturePath = picturePath
        self.recommendParams = recommendParams
        self.friendRequestStatus = friendRequestStatus
        self.musicProfile = musicProfile
        self.videoProfile = videoProfile

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:break
            if D == 1:
                if M == 0x0b:
                    self.mid = ip.readString().decode('utf-8') if sys.version_info[0] == 2 else ip.readString()
                else:
                    ip.skip(M)
            elif D == 2:
                if M == 0x0a:
                    self.createdTime = ip.readI64()
                else:
                    ip.skip(M)
            elif D == 10:
                if M == 0x08:
                    self.type = ip.readI32()
                else:
                    ip.skip(M)
            elif D == 11:
                if M == 0x08:
                    self.status = ip.readI32()
                else:
                    ip.skip(M)
            elif D == 21:
                if M == 0x08:
                    self.relation = ip.readI32()
                else:
                    ip.skip(M)
            elif D == 22:
                if M == 0x0b:
                    self.displayName = ip.readString().decode('utf-8') if sys.version_info[0] == 2 else ip.readString()
                else:
                    ip.skip(M)
            elif D == 23:
                if M == 0x0b:
                    self.phoneticName = ip.readString().decode('utf-8') if sys.version_info[0] == 2 else ip.readString()
                else:
                    ip.skip(M)
            elif D == 24:
                if M == 0x0b:
                    self.pictureStatus = ip.readString().decode('utf-8') if sys.version_info[0] == 2 else ip.readString()
                else:
                    ip.skip(M)
            elif D == 25:
                if M == 0x0b:
                    self.thumbnailUrl = ip.readString().decode('utf-8') if sys.version_info[0] == 2 else ip.readString()
                else:
                    ip.skip(M)
            elif D == 26:
                if M == 0x0b:
                    self.statusMessage = ip.readString().decode('utf-8') if sys.version_info[0] == 2 else ip.readString()
                else:
                    ip.skip(M)
            elif D == 27:
                if M == 0x0b:
                    self.displayNameOverridden = ip.readString().decode('utf-8') if sys.version_info[0] == 2 else ip.readString()
                else:
                    ip.skip(M)
            elif D == 28:
                if M == 0x0a:
                    self.favoriteTime = ip.readI64()
                else:
                    ip.skip(M)
            elif D == 31:
                if M == 0x02:
                    self.capableVoiceCall = ip.readBool()
                else:
                    ip.skip(M)
            elif D == 32:
                if M == 0x02:
                    self.capableVideoCall = ip.readBool()
                else:
                    ip.skip(M)
            elif D == 33:
                if M == 0x02:
                    self.capableMyhome = ip.readBool()
                else:
                    ip.skip(M)
            elif D == 34:
                if M == 0x02:
                    self.capableBuddy = ip.readBool()
                else:
                    ip.skip(M)
            elif D == 35:
                if M == 0x08:
                    self.attributes = ip.readI32()
                else:
                    ip.skip(M)
            elif D == 36:
                if M == 0x0a:
                    self.settings = ip.readI64()
                else:
                    ip.skip(M)
            elif D == 37:
                if M == 0x0b:
                    self.picturePath = ip.readString().decode('utf-8') if sys.version_info[0] == 2 else ip.readString()
                else:
                    ip.skip(M)
            elif D == 38:
                if M == 0x0b:
                    self.recommendParams = ip.readString().decode('utf-8') if sys.version_info[0] == 2 else ip.readString()
                else:
                    ip.skip(M)
            elif D == 39:
                if M == 0x08:
                    self.friendRequestStatus = ip.readI32()
                else:
                    ip.skip(M)
            elif D == 40:
                if M == 0x0b:
                    self.musicProfile = ip.readString().decode('utf-8') if sys.version_info[0] == 2 else ip.readString()
                else:
                    ip.skip(M)
            elif D == 42:
                if M == 0x0b:
                    self.videoProfile = ip.readString().decode('utf-8') if sys.version_info[0] == 2 else ip.readString()
                else:
                    ip.skip(M)
            else:
                ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('Contact')
        if self.mid is not None:
            op.writeFieldBegin('mid', 0x0b, 1)
            op.writeString(self.mid.encode('utf-8') if sys.version_info[0] == 2 else self.mid)
            op.writeFieldEnd()
        if self.createdTime is not None:
            op.writeFieldBegin('createdTime', 0x0a, 2)
            op.writeI64(self.createdTime)
            op.writeFieldEnd()
        if self.type is not None:
            op.writeFieldBegin('type', 0x08, 10)
            op.writeI32(self.type)
            op.writeFieldEnd()
        if self.status is not None:
            op.writeFieldBegin('status', 0x08, 11)
            op.writeI32(self.status)
            op.writeFieldEnd()
        if self.relation is not None:
            op.writeFieldBegin('relation', 0x08, 21)
            op.writeI32(self.relation)
            op.writeFieldEnd()
        if self.displayName is not None:
            op.writeFieldBegin('displayName', 0x0b, 22)
            op.writeString(self.displayName.encode('utf-8') if sys.version_info[0] == 2 else self.displayName)
            op.writeFieldEnd()
        if self.phoneticName is not None:
            op.writeFieldBegin('phoneticName', 0x0b, 23)
            op.writeString(self.phoneticName.encode('utf-8') if sys.version_info[0] == 2 else self.phoneticName)
            op.writeFieldEnd()
        if self.pictureStatus is not None:
            op.writeFieldBegin('pictureStatus', 0x0b, 24)
            op.writeString(self.pictureStatus.encode('utf-8') if sys.version_info[0] == 2 else self.pictureStatus)
            op.writeFieldEnd()
        if self.thumbnailUrl is not None:
            op.writeFieldBegin('thumbnailUrl', 0x0b, 25)
            op.writeString(self.thumbnailUrl.encode('utf-8') if sys.version_info[0] == 2 else self.thumbnailUrl)
            op.writeFieldEnd()
        if self.statusMessage is not None:
            op.writeFieldBegin('statusMessage', 0x0b, 26)
            op.writeString(self.statusMessage.encode('utf-8') if sys.version_info[0] == 2 else self.statusMessage)
            op.writeFieldEnd()
        if self.displayNameOverridden is not None:
            op.writeFieldBegin('displayNameOverridden', 0x0b, 27)
            op.writeString(self.displayNameOverridden.encode('utf-8') if sys.version_info[0] == 2 else self.displayNameOverridden)
            op.writeFieldEnd()
        if self.favoriteTime is not None:
            op.writeFieldBegin('favoriteTime', 0x0a, 28)
            op.writeI64(self.favoriteTime)
            op.writeFieldEnd()
        if self.capableVoiceCall is not None:
            op.writeFieldBegin('capableVoiceCall', 0x02, 31)
            op.writeBool(self.capableVoiceCall)
            op.writeFieldEnd()
        if self.capableVideoCall is not None:
            op.writeFieldBegin('capableVideoCall', 0x02, 32)
            op.writeBool(self.capableVideoCall)
            op.writeFieldEnd()
        if self.capableMyhome is not None:
            op.writeFieldBegin('capableMyhome', 0x02, 33)
            op.writeBool(self.capableMyhome)
            op.writeFieldEnd()
        if self.capableBuddy is not None:
            op.writeFieldBegin('capableBuddy', 0x02, 34)
            op.writeBool(self.capableBuddy)
            op.writeFieldEnd()
        if self.attributes is not None:
            op.writeFieldBegin('attributes', 0x08, 35)
            op.writeI32(self.attributes)
            op.writeFieldEnd()
        if self.settings is not None:
            op.writeFieldBegin('settings', 0x0a, 36)
            op.writeI64(self.settings)
            op.writeFieldEnd()
        if self.picturePath is not None:
            op.writeFieldBegin('picturePath', 0x0b, 37)
            op.writeString(self.picturePath.encode('utf-8') if sys.version_info[0] == 2 else self.picturePath)
            op.writeFieldEnd()
        if self.recommendParams is not None:
            op.writeFieldBegin('recommendParams', 0x0b, 38)
            op.writeString(self.recommendParams.encode('utf-8') if sys.version_info[0] == 2 else self.recommendParams)
            op.writeFieldEnd()
        if self.friendRequestStatus is not None:
            op.writeFieldBegin('friendRequestStatus', 0x08, 39)
            op.writeI32(self.friendRequestStatus)
            op.writeFieldEnd()
        if self.musicProfile is not None:
            op.writeFieldBegin('musicProfile', 0x0b, 40)
            op.writeString(self.musicProfile.encode('utf-8') if sys.version_info[0] == 2 else self.musicProfile)
            op.writeFieldEnd()
        if self.videoProfile is not None:
            op.writeFieldBegin('videoProfile', 0x0b, 42)
            op.writeString(self.videoProfile.encode('utf-8') if sys.version_info[0] == 2 else self.videoProfile)
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)
    
    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class Group(object):

    def __init__(self, id=None, createdTime=None, name=None, pictureStatus=None, preventedJoinByTicket=None, groupPreference=None, members=None, creator=None, invitee=None, notificationDisabled=None):
        self.id = id
        self.createdTime = createdTime
        self.name = name
        self.pictureStatus = pictureStatus
        self.preventedJoinByTicket = preventedJoinByTicket
        self.groupPreference = groupPreference
        self.members = members
        self.creator = creator
        self.invitee = invitee
        self.notificationDisabled = notificationDisabled

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:break
            if D == 1:
                if M == 0x0b:
                    self.id = ip.readString().decode('utf-8') if sys.version_info[0] == 2 else ip.readString()
                else:
                    ip.skip(M)
            elif D == 2:
                if M == 0x0a:
                    self.createdTime = ip.readI64()
                else:
                    ip.skip(M)
            elif D == 10:
                if M == 0x0b:
                    self.name = ip.readString().decode('utf-8') if sys.version_info[0] == 2 else ip.readString()
                else:
                    ip.skip(M)
            elif D == 11:
                if M == 0x0b:
                    self.pictureStatus = ip.readString().decode('utf-8') if sys.version_info[0] == 2 else ip.readString()
                else:
                    ip.skip(M)
            elif D == 12:
                if M == 0x02:
                    self.preventedJoinByTicket = ip.readBool()
                else:
                    ip.skip(M)
            elif D == 13:
                if M == 0x0c:
                    self.groupPreference = GroupPreference()
                    self.groupPreference.read(ip)
                else:
                    ip.skip(M)
            elif D == 20:
                if M == 0x0f:
                    self.members = []
                    (_etype258, _size255) = ip.readListBegin()
                    for _i259 in range(_size255):
                        _elem260 = Contact()
                        _elem260.read(ip)
                        self.members.append(_elem260)
                    ip.readListEnd()
                else:
                    ip.skip(M)
            elif D == 21:
                if M == 0x0c:
                    self.creator = Contact()
                    self.creator.read(ip)
                else:
                    ip.skip(M)
            elif D == 22:
                if M == 0x0f:
                    self.invitee = []
                    (_etype264, _size261) = ip.readListBegin()
                    for _i265 in range(_size261):
                        _elem266 = Contact()
                        _elem266.read(ip)
                        self.invitee.append(_elem266)
                    ip.readListEnd()
                else:
                    ip.skip(M)
            elif D == 31:
                if M == 0x02:
                    self.notificationDisabled = ip.readBool()
                else:
                    ip.skip(M)
            else:
                ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('Group')
        if self.id is not None:
            op.writeFieldBegin('id', 0x0b, 1)
            op.writeString(self.id.encode('utf-8') if sys.version_info[0] == 2 else self.id)
            op.writeFieldEnd()
        if self.createdTime is not None:
            op.writeFieldBegin('createdTime', 0x0a, 2)
            op.writeI64(self.createdTime)
            op.writeFieldEnd()
        if self.name is not None:
            op.writeFieldBegin('name', 0x0b, 10)
            op.writeString(self.name.encode('utf-8') if sys.version_info[0] == 2 else self.name)
            op.writeFieldEnd()
        if self.pictureStatus is not None:
            op.writeFieldBegin('pictureStatus', 0x0b, 11)
            op.writeString(self.pictureStatus.encode('utf-8') if sys.version_info[0] == 2 else self.pictureStatus)
            op.writeFieldEnd()
        if self.preventedJoinByTicket is not None:
            op.writeFieldBegin('preventedJoinByTicket', 0x02, 12)
            op.writeBool(self.preventedJoinByTicket)
            op.writeFieldEnd()
        if self.groupPreference is not None:
            op.writeFieldBegin('groupPreference', 0x0c, 13)
            self.groupPreference.write(op)
            op.writeFieldEnd()
        if self.members is not None:
            op.writeFieldBegin('members', 0x0f, 20)
            op.writeListBegin(0x0c, len(self.members))
            for iter267 in self.members:
                iter267.write(op)
            op.writeListEnd()
            op.writeFieldEnd()
        if self.creator is not None:
            op.writeFieldBegin('creator', 0x0c, 21)
            self.creator.write(op)
            op.writeFieldEnd()
        if self.invitee is not None:
            op.writeFieldBegin('invitee', 0x0f, 22)
            op.writeListBegin(0x0c, len(self.invitee))
            for iter268 in self.invitee:
                iter268.write(op)
            op.writeListEnd()
            op.writeFieldEnd()
        if self.notificationDisabled is not None:
            op.writeFieldBegin('notificationDisabled', 0x02, 31)
            op.writeBool(self.notificationDisabled)
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)
    
    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class Profile(object):

    def __init__(self, mid=None, userid=None, phone=None, email=None, regionCode=None, displayName=None, phoneticName=None, pictureStatus=None, thumbnailUrl=None, statusMessage=None, allowSearchByUserid=None, allowSearchByEmail=None, picturePath=None, musicProfile=None, videoProfile=None):
        self.mid = mid
        self.userid = userid
        self.phone = phone
        self.email = email
        self.regionCode = regionCode
        self.displayName = displayName
        self.phoneticName = phoneticName
        self.pictureStatus = pictureStatus
        self.thumbnailUrl = thumbnailUrl
        self.statusMessage = statusMessage
        self.allowSearchByUserid = allowSearchByUserid
        self.allowSearchByEmail = allowSearchByEmail
        self.picturePath = picturePath
        self.musicProfile = musicProfile
        self.videoProfile = videoProfile

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:break
            if D == 1:
                if M == 0x0b:self.mid = ip.readString().decode('ascii') if sys.version_info[0] == 2 else ip.readString()
                else:ip.skip(M)
            elif D == 3:
                if M == 0x0b:self.userid = ip.readString().decode('ascii') if sys.version_info[0] == 2 else ip.readString()
                else:ip.skip(M)
            elif D == 10:
                if M == 0x0b:self.phone = ip.readString().decode('ascii') if sys.version_info[0] == 2 else ip.readString()
                else:ip.skip(M)
            elif D == 11:
                if M == 0x0b:self.email = ip.readString().decode('ascii') if sys.version_info[0] == 2 else ip.readString()
                else:ip.skip(M)
            elif D == 12:
                if M == 0x0b:self.regionCode = ip.readString().decode('ascii') if sys.version_info[0] == 2 else ip.readString()
                else:ip.skip(M)
            elif D == 20:
                if M == 0x0b:self.displayName = ip.readString().decode('ascii') if sys.version_info[0] == 2 else ip.readString()
                else:ip.skip(M)
            elif D == 21:
                if M == 0x0b:self.phoneticName = ip.readString().decode('ascii') if sys.version_info[0] == 2 else ip.readString()
                else:ip.skip(M)
            elif D == 22:
                if M == 0x0b:self.pictureStatus = ip.readString().decode('ascii') if sys.version_info[0] == 2 else ip.readString()
                else:ip.skip(M)
            elif D == 23:
                if M == 0x0b:self.thumbnailUrl = ip.readString().decode('ascii') if sys.version_info[0] == 2 else ip.readString()
                else:ip.skip(M)
            elif D == 24:
                if M == 0x0b:self.statusMessage = ip.readString().decode('ascii') if sys.version_info[0] == 2 else ip.readString()
                else:ip.skip(M)
            elif D == 31:
                if M == 0x02:self.allowSearchByUserid = ip.readBool()
                else:ip.skip(M)
            elif D == 32:
                if M == 0x02:self.allowSearchByEmail = ip.readBool()
                else:ip.skip(M)
            elif D == 33:
                if M == 0x0b:self.picturePath = ip.readString().decode('ascii') if sys.version_info[0] == 2 else ip.readString()
                else:ip.skip(M)
            elif D == 34:
                if M == 0x0b:self.musicProfile = ip.readString().decode('ascii') if sys.version_info[0] == 2 else ip.readString()
                else:ip.skip(M)
            elif D == 35:
                if M == 0x0b:self.videoProfile = ip.readString().decode('ascii') if sys.version_info[0] == 2 else ip.readString()
                else:ip.skip(M)
            else:ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('Profile')
        if self.mid is not None:
            op.writeFieldBegin('mid', 0x0b, 1)
            op.writeString(self.mid.encode('ascii') if sys.version_info[0] == 2 else self.mid)
            op.writeFieldEnd()
        if self.userid is not None:
            op.writeFieldBegin('userid', 0x0b, 3)
            op.writeString(self.userid.encode('ascii') if sys.version_info[0] == 2 else self.userid)
            op.writeFieldEnd()
        if self.phone is not None:
            op.writeFieldBegin('phone', 0x0b, 10)
            op.writeString(self.phone.encode('ascii') if sys.version_info[0] == 2 else self.phone)
            op.writeFieldEnd()
        if self.email is not None:
            op.writeFieldBegin('email', 0x0b, 11)
            op.writeString(self.email.encode('ascii') if sys.version_info[0] == 2 else self.email)
            op.writeFieldEnd()
        if self.regionCode is not None:
            op.writeFieldBegin('regionCode', 0x0b, 12)
            op.writeString(self.regionCode.encode('ascii') if sys.version_info[0] == 2 else self.regionCode)
            op.writeFieldEnd()
        if self.displayName is not None:
            op.writeFieldBegin('displayName', 0x0b, 20)
            op.writeString(self.displayName.encode('ascii') if sys.version_info[0] == 2 else self.displayName)
            op.writeFieldEnd()
        if self.phoneticName is not None:
            op.writeFieldBegin('phoneticName', 0x0b, 21)
            op.writeString(self.phoneticName.encode('ascii') if sys.version_info[0] == 2 else self.phoneticName)
            op.writeFieldEnd()
        if self.pictureStatus is not None:
            op.writeFieldBegin('pictureStatus', 0x0b, 22)
            op.writeString(self.pictureStatus.encode('ascii') if sys.version_info[0] == 2 else self.pictureStatus)
            op.writeFieldEnd()
        if self.thumbnailUrl is not None:
            op.writeFieldBegin('thumbnailUrl', 0x0b, 23)
            op.writeString(self.thumbnailUrl.encode('ascii') if sys.version_info[0] == 2 else self.thumbnailUrl)
            op.writeFieldEnd()
        if self.statusMessage is not None:
            op.writeFieldBegin('statusMessage', 0x0b, 24)
            op.writeString(self.statusMessage.encode('ascii') if sys.version_info[0] == 2 else self.statusMessage)
            op.writeFieldEnd()
        if self.allowSearchByUserid is not None:
            op.writeFieldBegin('allowSearchByUserid', 0x02, 31)
            op.writeBool(self.allowSearchByUserid)
            op.writeFieldEnd()
        if self.allowSearchByEmail is not None:
            op.writeFieldBegin('allowSearchByEmail', 0x02, 32)
            op.writeBool(self.allowSearchByEmail)
            op.writeFieldEnd()
        if self.picturePath is not None:
            op.writeFieldBegin('picturePath', 0x0b, 33)
            op.writeString(self.picturePath.encode('ascii') if sys.version_info[0] == 2 else self.picturePath)
            op.writeFieldEnd()
        if self.musicProfile is not None:
            op.writeFieldBegin('musicProfile', 0x0b, 34)
            op.writeString(self.musicProfile.encode('ascii') if sys.version_info[0] == 2 else self.musicProfile)
            op.writeFieldEnd()
        if self.videoProfile is not None:
            op.writeFieldBegin('videoProfile', 0x0b, 35)
            op.writeString(self.videoProfile.encode('ascii') if sys.version_info[0] == 2 else self.videoProfile)
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)
    
    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class Room(object):

    def __init__(self, id=None, createdTime=None, contacts=None, notificationDisabled=None, memberMids=None):
        self.id = id
        self.createdTime = createdTime
        self.contacts = contacts
        self.notificationDisabled = notificationDisabled
        self.memberMids = memberMids

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:
                break
            if D == 1:
                if M == 0x0b:
                    self.id = ip.readString().decode('utf-8') if sys.version_info[0] == 2 else ip.readString()
                else:
                    ip.skip(M)
            elif D == 2:
                if M == 0x0a:
                    self.createdTime = ip.readI64()
                else:
                    ip.skip(M)
            elif D == 10:
                if M == 0x0f:
                    self.contacts = []
                    (_etype408, _size405) = ip.readListBegin()
                    for _i409 in range(_size405):
                        _elem410 = Contact()
                        _elem410.read(ip)
                        self.contacts.append(_elem410)
                    ip.readListEnd()
                else:
                    ip.skip(M)
            elif D == 31:
                if M == 0x02:
                    self.notificationDisabled = ip.readBool()
                else:
                    ip.skip(M)
            elif D == 40:
                if M == 0x0f:
                    self.memberMids = []
                    (_etype414, _size411) = ip.readListBegin()
                    for _i415 in range(_size411):
                        _elem416 = ip.readString().decode('utf-8') if sys.version_info[0] == 2 else ip.readString()
                        self.memberMids.append(_elem416)
                    ip.readListEnd()
                else:
                    ip.skip(M)
            else:
                ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('Room')
        if self.id is not None:
            op.writeFieldBegin('mid', 0x0b, 1)
            op.writeString(self.id.encode('utf-8') if sys.version_info[0] == 2 else self.id)
            op.writeFieldEnd()
        if self.createdTime is not None:
            op.writeFieldBegin('createdTime', 0x0a, 2)
            op.writeI64(self.createdTime)
            op.writeFieldEnd()
        if self.contacts is not None:
            op.writeFieldBegin('contacts', 0x0f, 10)
            op.writeListBegin(0x0c, len(self.contacts))
            for iter417 in self.contacts:
                iter417.write(op)
            op.writeListEnd()
            op.writeFieldEnd()
        if self.notificationDisabled is not None:
            op.writeFieldBegin('notificationDisabled', 0x02, 31)
            op.writeBool(self.notificationDisabled)
            op.writeFieldEnd()
        if self.memberMids is not None:
            op.writeFieldBegin('memberMids', 0x0f, 40)
            op.writeListBegin(0x0b, len(self.memberMids))
            for iter418 in self.memberMids:
                op.writeString(iter418.encode('utf-8') if sys.version_info[0] == 2 else iter418)
            op.writeListEnd()
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)
    
    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class Message(object):

    def __init__(self, _from=None, displayName=None, picturePath=None, type=None, person=None, person2=None, personName=None, personName2=None, to=None, toType=None, id=None, createdTime=None, deliveredTime=None, text=None, location=None, hasContent=None, contentType=None, contentPreview=None, contentMetadata=None, sessionId=None, chunks=None, relatedMessageId=None, messageRelationType=None, readCount=None, relatedMessageServiceCode=None):
        self._from = _from
        self.displayName = displayName
        self.picturePath = picturePath
        self.type = type
        self.person = person
        self.person2 = person2
        self.personName = personName
        self.personName2 = personName2
        self.to = to
        self.toType = toType
        self.id = id
        self.createdTime = createdTime
        self.deliveredTime = deliveredTime
        self.text = text
        self.location = location
        self.hasContent = hasContent
        self.contentType = contentType
        self.contentPreview = contentPreview
        self.contentMetadata = contentMetadata
        self.sessionId = sessionId
        self.chunks = chunks
        self.relatedMessageId = relatedMessageId
        self.messageRelationType = messageRelationType
        self.readCount = readCount
        self.relatedMessageServiceCode = relatedMessageServiceCode

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:break
            if D == 1:
                if M == 0x0b:self._from = ip.readString().decode('ascii') if sys.version_info[0] == 2 else ip.readString()
                else:ip.skip(M)
            elif D == 99:
                if M == 0x0b:self.displayName = ip.readString().decode('ascii') if sys.version_info[0] == 2 else ip.readString()
                else:ip.skip(M)
            elif D == 98:
                if M == 0x0b:self.picturePath = ip.readString().decode('ascii') if sys.version_info[0] == 2 else ip.readString()
                else:ip.skip(M)
            elif D == 97:
                if M == 0x0b:self.type = ip.readString().decode('ascii') if sys.version_info[0] == 2 else ip.readString()
                else:ip.skip(M)
            elif D == 96:
                if M == 0x0b:self.person = ip.readString().decode('ascii') if sys.version_info[0] == 2 else ip.readString()
                else:ip.skip(M)
            elif D == 95:
                if M == 0x0b:self.person2 = ip.readString().decode('ascii') if sys.version_info[0] == 2 else ip.readString()
                else:ip.skip(M)
            elif D == 94:
                if M == 0x0b:self.personName = ip.readString().decode('ascii') if sys.version_info[0] == 2 else ip.readString()
                else:ip.skip(M)
            elif D == 93:
                if M == 0x0b:self.personName2 = ip.readString().decode('ascii') if sys.version_info[0] == 2 else ip.readString()
                else:ip.skip(M)
            elif D == 2:
                if M == 0x0b:self.to = ip.readString().decode('ascii') if sys.version_info[0] == 2 else ip.readString()
                else:ip.skip(M)
            elif D == 3:
                if M == 0x08:self.toType = ip.readI32()
                else:ip.skip(M)
            elif D == 4:
                if M == 0x0b:self.id = ip.readString().decode('ascii') if sys.version_info[0] == 2 else ip.readString()
                else:ip.skip(M)
            elif D == 5:
                if M == 0x0a:self.createdTime = ip.readI64()
                else:ip.skip(M)
            elif D == 6:
                if M == 0x0a:self.deliveredTime = ip.readI64()
                else:ip.skip(M)
            elif D == 10:
                if M == 0x0b:self.text = ip.readString().decode('ascii') if sys.version_info[0] == 2 else ip.readString()
                else:ip.skip(M)
            elif D == 14:
                if M == 0x02:self.hasContent = ip.readBool()
                else:ip.skip(M)
            elif D == 15:
                if M == 0x08:self.contentType = ip.readI32()
                else:ip.skip(M)
            elif D == 17:
                if M == 0x0b:self.contentPreview = ip.readBinary()
                else:ip.skip(M)
            elif D == 18:
                if M == 0x0d:
                    self.contentMetadata = {}
                    (_ktype300, _vtype301, _size299) = ip.readMapBegin()
                    for _i303 in range(_size299):
                        _key304 = ip.readString().decode('ascii') if sys.version_info[0] == 2 else ip.readString()
                        _val305 = ip.readString().decode('ascii') if sys.version_info[0] == 2 else ip.readString()
                        self.contentMetadata[_key304] = _val305
                    ip.readMapEnd()
                else:ip.skip(M)
            elif D == 19:
                if M == 0x08:self.sessionId = ip.readI32()
                else:ip.skip(M)
            elif D == 20:
                if M == 0x0f:
                    self.chunks = []
                    (_etype309, _size306) = ip.readListBegin()
                    for _i310 in range(_size306):
                        _elem = ip.readBinary()
                        self.chunks.append(_elem)
                    ip.readListEnd()
                else:ip.skip(M)
            elif D == 21:
                if M == 0x0b:self.relatedMessageId = ip.readString().decode('ascii') if sys.version_info[0] == 2 else ip.readString()
                else:ip.skip(M)
            elif D == 22:
                if M == 0x08:self.messageRelationType = ip.readI32()
                else:ip.skip(M)
            elif D == 23:
                if M == 0x08:self.readCount = ip.readI32()
                else:ip.skip(M)
            elif D == 24:
                if M == 0x08:self.relatedMessageServiceCode = ip.readI32()
                else:ip.skip(M)
            else:
                ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('Message')
        if self._from is not None:
            op.writeFieldBegin('_from', 0x0b, 1)
            op.writeString(self._from.encode('ascii') if sys.version_info[0] == 2 else self._from)
            op.writeFieldEnd()
        if self.to is not None:
            op.writeFieldBegin('to', 0x0b, 2)
            op.writeString(self.to.encode('ascii') if sys.version_info[0] == 2 else self.to)
            op.writeFieldEnd()
        if self.toType is not None:
            op.writeFieldBegin('toType', 0x08, 3)
            op.writeI32(self.toType)
            op.writeFieldEnd()
        if self.id is not None:
            op.writeFieldBegin('id', 0x0b, 4)
            op.writeString(self.id.encode('ascii') if sys.version_info[0] == 2 else self.id)
            op.writeFieldEnd()
        if self.createdTime is not None:
            op.writeFieldBegin('createdTime', 0x0a, 5)
            op.writeI64(self.createdTime)
            op.writeFieldEnd()
        if self.deliveredTime is not None:
            op.writeFieldBegin('deliveredTime', 0x0a, 6)
            op.writeI64(self.deliveredTime)
            op.writeFieldEnd()
        if self.text is not None:
            op.writeFieldBegin('text', 0x0b, 10)
            op.writeString(self.text.encode('ascii') if sys.version_info[0] == 2 else self.text)
            op.writeFieldEnd()
        if self.location is not None:
            op.writeFieldBegin('location', 0x0c, 11)
            self.location.write(op)
            op.writeFieldEnd()
        if self.hasContent is not None:
            op.writeFieldBegin('hasContent', 0x02, 14)
            op.writeBool(self.hasContent)
            op.writeFieldEnd()
        if self.contentType is not None:
            op.writeFieldBegin('contentType', 0x08, 15)
            op.writeI32(self.contentType)
            op.writeFieldEnd()
        if self.contentPreview is not None:
            op.writeFieldBegin('contentPreview', 0x0b, 17)
            op.writeBinary(self.contentPreview)
            op.writeFieldEnd()
        if self.contentMetadata is not None:
            op.writeFieldBegin('contentMetadata', 0x0d, 18)
            op.writeMapBegin(0x0b, 0x0b, len(self.contentMetadata))
            for kiter312, viter313 in self.contentMetadata.items():
                op.writeString(kiter312.encode('ascii') if sys.version_info[0] == 2 else kiter312)
                op.writeString(viter313.encode('ascii') if sys.version_info[0] == 2 else viter313)
            op.writeMapEnd()
            op.writeFieldEnd()
        if self.sessionId is not None:
            op.writeFieldBegin('sessionId', 0x08, 19)
            op.writeI32(self.sessionId)
            op.writeFieldEnd()
        if self.chunks is not None:
            op.writeFieldBegin('chunks', 0x0f, 20)
            op.writeListBegin(0x0b, len(self.chunks))
            for iter314 in self.chunks:
                op.writeBinary(iter314)
            op.writeListEnd()
            op.writeFieldEnd()
        if self.relatedMessageId is not None:
            op.writeFieldBegin('relatedMessageId', 0x0b, 21)
            op.writeString(self.relatedMessageId.encode('ascii') if sys.version_info[0] == 2 else self.relatedMessageId)
            op.writeFieldEnd()
        if self.messageRelationType is not None:
            op.writeFieldBegin('messageRelationType', 0x08, 22)
            op.writeI32(self.messageRelationType)
            op.writeFieldEnd()
        if self.readCount is not None:
            op.writeFieldBegin('readCount', 0x08, 23)
            op.writeI32(self.readCount)
            op.writeFieldEnd()
        if self.relatedMessageServiceCode is not None:
            op.writeFieldBegin('relatedMessageServiceCode', 0x08, 24)
            op.writeI32(self.relatedMessageServiceCode)
            op.writeFieldEnd()
        if self.personName2 is not None:
            op.writeFieldBegin('personName2', 0x0b, 93)
            op.writeString(self.personName2.encode('ascii') if sys.version_info[0] == 2 else self.personName2)
            op.writeFieldEnd()
        if self.personName is not None:
            op.writeFieldBegin('personName', 0x0b, 94)
            op.writeString(self.personName.encode('ascii') if sys.version_info[0] == 2 else self.personName)
            op.writeFieldEnd()
        if self.person2 is not None:
            op.writeFieldBegin('person2', 0x0b, 95)
            op.writeString(self.person2.encode('ascii') if sys.version_info[0] == 2 else self.person2)
            op.writeFieldEnd()
        if self.person is not None:
            op.writeFieldBegin('person', 0x0b, 96)
            op.writeString(self.person.encode('ascii') if sys.version_info[0] == 2 else self.person)
            op.writeFieldEnd()
        if self.type is not None:
            op.writeFieldBegin('type', 0x0b, 97)
            op.writeString(self.type.encode('ascii') if sys.version_info[0] == 2 else self.type)
            op.writeFieldEnd()
        if self.picturePath is not None:
            op.writeFieldBegin('picturePath', 0x0b, 98)
            op.writeString(self.picturePath.encode('ascii') if sys.version_info[0] == 2 else self.picturePath)
            op.writeFieldEnd()
        if self.displayName is not None:
            op.writeFieldBegin('displayName', 0x0b, 99)
            op.writeString(self.displayName.encode('ascii') if sys.version_info[0] == 2 else self.displayName)
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)
    
    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class Operation(object):

    def __init__(self, revision=None, createdTime=None, type=None, reqSeq=None, checksum=None, status=None, param1=None, param2=None, param3=None, message=None):
        self.revision = revision
        self.createdTime = createdTime
        self.type = type
        self.reqSeq = reqSeq
        self.checksum = checksum
        self.status = status
        self.param1 = param1
        self.param2 = param2
        self.param3 = param3
        self.message = message

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:break
            if D == 1:
                if M == 0x0a:
                    self.revision = ip.readI64()
                else:ip.skip(M)
            elif D == 2:
                if M == 0x0a:
                    self.createdTime = ip.readI64()
                else:ip.skip(M)
            elif D == 3:
                if M == 0x08:
                    self.type = ip.readI32()
                else:ip.skip(M)
            elif D == 4:
                if M == 0x08:
                    self.reqSeq = ip.readI32()
                else:ip.skip(M)
            elif D == 5:
                if M == 0x0b:
                    self.checksum = ip.readString().decode('ascii') if sys.version_info[0] == 2 else ip.readString()
                else:ip.skip(M)
            elif D == 7:
                if M == 0x08:
                    self.status = ip.readI32()
                else:ip.skip(M)
            elif D == 10:
                if M == 0x0b:
                    self.param1 = ip.readString().decode('ascii') if sys.version_info[0] == 2 else ip.readString()
                else:ip.skip(M)
            elif D == 11:
                if M == 0x0b:
                    self.param2 = ip.readString().decode('ascii') if sys.version_info[0] == 2 else ip.readString()
                else:ip.skip(M)
            elif D == 12:
                if M == 0x0b:
                    self.param3 = ip.readString().decode('ascii') if sys.version_info[0] == 2 else ip.readString()
                else:ip.skip(M)
            elif D == 20:
                if M == 0x0c:
                    self.message = Message()
                    self.message.read(ip)
                else:ip.skip(M)
            else:
                ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('Operation')
        if self.revision is not None:
            op.writeFieldBegin('revision', 0x0a, 1)
            op.writeI64(self.revision)
            op.writeFieldEnd()
        if self.createdTime is not None:
            op.writeFieldBegin('createdTime', 0x0a, 2)
            op.writeI64(self.createdTime)
            op.writeFieldEnd()
        if self.type is not None:
            op.writeFieldBegin('type', 0x08, 3)
            op.writeI32(self.type)
            op.writeFieldEnd()
        if self.reqSeq is not None:
            op.writeFieldBegin('reqSeq', 0x08, 4)
            op.writeI32(self.reqSeq)
            op.writeFieldEnd()
        if self.checksum is not None:
            op.writeFieldBegin('checksum', 0x0b, 5)
            op.writeString(self.checksum.encode('ascii') if sys.version_info[0] == 2 else self.checksum)
            op.writeFieldEnd()
        if self.status is not None:
            op.writeFieldBegin('status', 0x08, 7)
            op.writeI32(self.status)
            op.writeFieldEnd()
        if self.param1 is not None:
            op.writeFieldBegin('param1', 0x0b, 10)
            op.writeString(self.param1.encode('ascii') if sys.version_info[0] == 2 else self.param1)
            op.writeFieldEnd()
        if self.param2 is not None:
            op.writeFieldBegin('param2', 0x0b, 11)
            op.writeString(self.param2.encode('ascii') if sys.version_info[0] == 2 else self.param2)
            op.writeFieldEnd()
        if self.param3 is not None:
            op.writeFieldBegin('param3', 0x0b, 12)
            op.writeString(self.param3.encode('ascii') if sys.version_info[0] == 2 else self.param3)
            op.writeFieldEnd()
        if self.message is not None:
            op.writeFieldBegin('message', 0x0c, 20)
            self.message.write(op)
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)
    
    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class RSAKey(object):

    def __init__(self, keynm=None, nvalue=None, evalue=None, sessionKey=None):
        self.keynm = keynm
        self.nvalue = nvalue
        self.evalue = evalue
        self.sessionKey = sessionKey

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:break
            if D == 1:
                if M == 0x0b:self.keynm = ip.readString().decode('ascii') if sys.version_info[0] == 2 else ip.readString()
                else:ip.skip(M)
            elif D == 2:
                if M == 0x0b:self.nvalue = ip.readString().decode('ascii') if sys.version_info[0] == 2 else ip.readString()
                else:ip.skip(M)
            elif D == 3:
                if M == 0x0b:self.evalue = ip.readString().decode('ascii') if sys.version_info[0] == 2 else ip.readString()
                else:ip.skip(M)
            elif D == 4:
                if M == 0x0b:self.sessionKey = ip.readString().decode('ascii') if sys.version_info[0] == 2 else ip.readString()
                else:ip.skip(M)
            else:ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('RSAKey')
        if self.keynm is not None:
            op.writeFieldBegin('keynm', 0x0b, 1)
            op.writeString(self.keynm.encode('ascii') if sys.version_info[0] == 2 else self.keynm)
            op.writeFieldEnd()
        if self.nvalue is not None:
            op.writeFieldBegin('nvalue', 0x0b, 2)
            op.writeString(self.nvalue.encode('ascii') if sys.version_info[0] == 2 else self.nvalue)
            op.writeFieldEnd()
        if self.evalue is not None:
            op.writeFieldBegin('evalue', 0x0b, 3)
            op.writeString(self.evalue.encode('ascii') if sys.version_info[0] == 2 else self.evalue)
            op.writeFieldEnd()
        if self.sessionKey is not None:
            op.writeFieldBegin('sessionKey', 0x0b, 4)
            op.writeString(self.sessionKey.encode('ascii') if sys.version_info[0] == 2 else self.sessionKey)
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)

    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class getRSAKeyArgs(object):

    def __init__(self, provider=None):
        self.provider = provider

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:break
            if D == 2:
                if M == 0x08:self.provider = ip.readI32()
                else:ip.skip(M)
            else:ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('getRSAKeyInfo_args')
        if self.provider is not None:
            op.writeFieldBegin('provider', 0x08, 2)
            op.writeI32(self.provider)
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)

    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class getRSAKeyResult(object):

    def __init__(self, success=None, e=None):
        self.success = success
        self.e = e

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:break
            if D == 0:
                if M == 0x0c:
                    self.success = RSAKey()
                    self.success.read(ip)
                else:ip.skip(M)
            elif D == 1:
                if M == 0x0c:
                    self.e = TalkException()
                    self.e.read(ip)
                else:ip.skip(M)
            else:ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('getRSAKeyInfo_result')
        if self.success is not None:
            op.writeFieldBegin('success', 0x0c, 0)
            self.success.write(op)
            op.writeFieldEnd()
        if self.e is not None:
            op.writeFieldBegin('e', 0x0c, 1)
            self.e.write(op)
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)
    
    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class TalkException(TException):

    def __init__(self, code=None, reason=None, parameterMap=None):
        self.code = code
        self.reason = reason
        self.parameterMap = parameterMap

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:break
            if D == 1:
                if M == 0x08:self.code = ip.readI32()
                else:ip.skip(M)
            elif D == 2:
                if M == 0x0b:self.reason = ip.readString().decode('ascii') if sys.version_info[0] == 2 else ip.readString()
                else:ip.skip(M)
            elif D == 3:
                if M == 0x0d:
                    self.parameterMap = {}
                    (ktype, vtype, _size) = ip.readMapBegin()
                    for i in range(_size):
                        key = ip.readString().decode('ascii') if sys.version_info[0] == 2 else ip.readString()
                        val = ip.readString().decode('ascii') if sys.version_info[0] == 2 else ip.readString()
                        self.parameterMap[key] = val
                    ip.readMapEnd()
                else:ip.skip(M)
            else:ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('TalkException')
        if self.code is not None:
            op.writeFieldBegin('code', 0x08, 1)
            op.writeI32(self.code)
            op.writeFieldEnd()
        if self.reason is not None:
            op.writeFieldBegin('reason', 0x0b, 2)
            op.writeString(self.reason.encode('ascii') if sys.version_info[0] == 2 else self.reason)
            op.writeFieldEnd()
        if self.parameterMap is not None:
            op.writeFieldBegin('parameterMap', 0x0d, 3)
            op.writeMapBegin(0x0b, 0x0b, len(self.parameterMap))
            for kiter, viter in self.parameterMap.items():
                op.writeString(kiter.encode('ascii') if sys.version_info[0] == 2 else kiter)
                op.writeString(viter.encode('ascii') if sys.version_info[0] == 2 else viter)
            op.writeMapEnd()
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)

    def __repr__(self) -> ReprPMD:return ReprPMD(self,True).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class SessionData(object):

    def __init__(self, sessionId=None, method=None, callback=None, normalizedPhone=None, countryCode=None, nationalSignificantNumber=None, availableVerificationMethods=None):
        self.sessionId = sessionId
        self.method = method
        self.callback = callback
        self.normalizedPhone = normalizedPhone
        self.countryCode = countryCode
        self.nationalSignificantNumber = nationalSignificantNumber
        self.availableVerificationMethods = availableVerificationMethods

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:break
            if D == 1:
                if M == 0x0b:self.sessionId = ip.readString().decode('ascii') if sys.version_info[0] == 2 else ip.readString()
                else:ip.skip(M)
            elif D == 2:
                if M == 0x08:self.method = ip.readI32()
                else:ip.skip(M)
            elif D == 3:
                if M == 0x0b:self.callback = ip.readString().decode('ascii') if sys.version_info[0] == 2 else ip.readString()
                else:ip.skip(M)
            elif D == 4:
                if M == 0x0b:self.normalizedPhone = ip.readString().decode('ascii') if sys.version_info[0] == 2 else ip.readString()
                else:ip.skip(M)
            elif D == 5:
                if M == 0x0b:self.countryCode = ip.readString().decode('ascii') if sys.version_info[0] == 2 else ip.readString()
                else:ip.skip(M)
            elif D == 6:
                if M == 0x0b:self.nationalSignificantNumber = ip.readString().decode('ascii') if sys.version_info[0] == 2 else ip.readString()
                else:ip.skip(M)
            elif D == 7:
                if M == 0x0f:
                    self.availableVerificationMethods = []
                    (_etype279, _size276) = ip.readListBegin()
                    for _i280 in range(_size276):
                        _elem281 = ip.readI32()
                        self.availableVerificationMethods.append(_elem281)
                    ip.readListEnd()
                else:ip.skip(M)
            else:
                ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('VerificationSessionData')
        if self.sessionId is not None:
            op.writeFieldBegin('sessionId', 0x0b, 1)
            op.writeString(self.sessionId.encode('ascii') if sys.version_info[0] == 2 else self.sessionId)
            op.writeFieldEnd()
        if self.method is not None:
            op.writeFieldBegin('method', 0x08, 2)
            op.writeI32(self.method)
            op.writeFieldEnd()
        if self.callback is not None:
            op.writeFieldBegin('callback', 0x0b, 3)
            op.writeString(self.callback.encode('ascii') if sys.version_info[0] == 2 else self.callback)
            op.writeFieldEnd()
        if self.normalizedPhone is not None:
            op.writeFieldBegin('normalizedPhone', 0x0b, 4)
            op.writeString(self.normalizedPhone.encode('ascii') if sys.version_info[0] == 2 else self.normalizedPhone)
            op.writeFieldEnd()
        if self.countryCode is not None:
            op.writeFieldBegin('countryCode', 0x0b, 5)
            op.writeString(self.countryCode.encode('ascii') if sys.version_info[0] == 2 else self.countryCode)
            op.writeFieldEnd()
        if self.nationalSignificantNumber is not None:
            op.writeFieldBegin('nationalSignificantNumber', 0x0b, 6)
            op.writeString(self.nationalSignificantNumber.encode('ascii') if sys.version_info[0] == 2 else self.nationalSignificantNumber)
            op.writeFieldEnd()
        if self.availableVerificationMethods is not None:
            op.writeFieldBegin('availableVerificationMethods', 0x0f, 7)
            op.writeListBegin(0x08, len(self.availableVerificationMethods))
            for iter282 in self.availableVerificationMethods:
                op.writeI32(iter282)
            op.writeListEnd()
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)
    
    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class LoginJoined(object):

    def __init__(self, type=None, identityProvider=None, identifier=None, password=None, keepLoggedIn=None, accessLocation=None, systemName=None, certificate=None, verifier=None, secret=None, e2eeVersion=None):
        self.type = type
        self.identityProvider = identityProvider
        self.identifier = identifier
        self.password = password
        self.keepLoggedIn = keepLoggedIn
        self.accessLocation = accessLocation
        self.systemName = systemName
        self.certificate = certificate
        self.verifier = verifier
        self.secret = secret
        self.e2eeVersion = e2eeVersion

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:break
            if D == 1:
                if M == 0x08:
                    self.type = ip.readI32()
                else:ip.skip(M)
            elif D == 2:
                if M == 0x08:
                    self.identityProvider = ip.readI32()
                else:ip.skip(M)
            elif D == 3:
                if M == 0x0b:
                    self.identifier = ip.readString().decode('ascii') if sys.version_info[0] == 2 else ip.readString()
                else:ip.skip(M)
            elif D == 4:
                if M == 0x0b:
                    self.password = ip.readString().decode('ascii') if sys.version_info[0] == 2 else ip.readString()
                else:ip.skip(M)
            elif D == 5:
                if M == 0x02:
                    self.keepLoggedIn = ip.readBool()
                else:ip.skip(M)
            elif D == 6:
                if M == 0x0b:
                    self.accessLocation = ip.readString().decode('ascii') if sys.version_info[0] == 2 else ip.readString()
                else:ip.skip(M)
            elif D == 7:
                if M == 0x0b:
                    self.systemName = ip.readString().decode('ascii') if sys.version_info[0] == 2 else ip.readString()
                else:ip.skip(M)
            elif D == 8:
                if M == 0x0b:
                    self.certificate = ip.readString().decode('ascii') if sys.version_info[0] == 2 else ip.readString()
                else:ip.skip(M)
            elif D == 9:
                if M == 0x0b:
                    self.verifier = ip.readString().decode('ascii') if sys.version_info[0] == 2 else ip.readString()
                else:ip.skip(M)
            elif D == 10:
                if M == 0x0b:
                    self.secret = ip.readString().decode('ascii') if sys.version_info[0] == 2 else ip.readString()
                else:ip.skip(M)
            elif D == 11:
                if M == 0x08:
                    self.e2eeVersion = ip.readI32()
                else:ip.skip(M)
            else:
                ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('LoginRequest')
        if self.type is not None:
            op.writeFieldBegin('type', 0x08, 1)
            op.writeI32(self.type)
            op.writeFieldEnd()
        if self.identityProvider is not None:
            op.writeFieldBegin('identityProvider', 0x08, 2)
            op.writeI32(self.identityProvider)
            op.writeFieldEnd()
        if self.identifier is not None:
            op.writeFieldBegin('identifier', 0x0b, 3)
            op.writeString(self.identifier.encode('ascii') if sys.version_info[0] == 2 else self.identifier)
            op.writeFieldEnd()
        if self.password is not None:
            op.writeFieldBegin('password', 0x0b, 4)
            op.writeString(self.password.encode('ascii') if sys.version_info[0] == 2 else self.password)
            op.writeFieldEnd()
        if self.keepLoggedIn is not None:
            op.writeFieldBegin('keepLoggedIn', 0x02, 5)
            op.writeBool(self.keepLoggedIn)
            op.writeFieldEnd()
        if self.accessLocation is not None:
            op.writeFieldBegin('accessLocation', 0x0b, 6)
            op.writeString(self.accessLocation.encode('ascii') if sys.version_info[0] == 2 else self.accessLocation)
            op.writeFieldEnd()
        if self.systemName is not None:
            op.writeFieldBegin('systemName', 0x0b, 7)
            op.writeString(self.systemName.encode('ascii') if sys.version_info[0] == 2 else self.systemName)
            op.writeFieldEnd()
        if self.certificate is not None:
            op.writeFieldBegin('certificate', 0x0b, 8)
            op.writeString(self.certificate.encode('ascii') if sys.version_info[0] == 2 else self.certificate)
            op.writeFieldEnd()
        if self.verifier is not None:
            op.writeFieldBegin('verifier', 0x0b, 9)
            op.writeString(self.verifier.encode('ascii') if sys.version_info[0] == 2 else self.verifier)
            op.writeFieldEnd()
        if self.secret is not None:
            op.writeFieldBegin('secret', 0x0b, 10)
            op.writeString(self.secret.encode('ascii') if sys.version_info[0] == 2 else self.secret)
            op.writeFieldEnd()
        if self.e2eeVersion is not None:
            op.writeFieldBegin('e2eeVersion', 0x08, 11)
            op.writeI32(self.e2eeVersion)
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)
    
    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class loginArgs(object):
    
    def __init__(self, loginRequest=None):
        self.loginRequest = loginRequest

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:break
            if D == 2:
                if M == 0x0c:
                    self.loginRequest = LoginJoined()
                    self.loginRequest.read(ip)
                else:ip.skip(M)
            else:ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('loginArgs')
        if self.loginRequest is not None:
            op.writeFieldBegin('loginRequest', 0x0c, 2)
            self.loginRequest.write(op)
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)
    
    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class loginResult(object):
    
    def __init__(self, success=None, e=None):
        self.success = success
        self.e = e

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:break
            if D == 0:
                if M == 0x0c:
                    self.success = LoginLine()
                    self.success.read(ip)
                else:ip.skip(M)
            elif D == 1:
                if M == 0x0c:
                    self.e = TalkException()
                    self.e.read(ip)
                else:ip.skip(M)
            else:
                ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('loginResult')
        if self.success is not None:
            op.writeFieldBegin('success', 0x0c, 0)
            self.success.write(op)
            op.writeFieldEnd()
        if self.e is not None:
            op.writeFieldBegin('e', 0x0c, 1)
            self.e.write(op)
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)
    
    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class LoginLine(object):

    def __init__(self, authToken=None, certificate=None, verifier=None, pinCode=None, type=None, lastPrimaryBindTime=None, displayMessage=None, sessionForSMSConfirm=None):
        self.authToken = authToken
        self.certificate = certificate
        self.verifier = verifier
        self.pinCode = pinCode
        self.type = type
        self.lastPrimaryBindTime = lastPrimaryBindTime
        self.displayMessage = displayMessage
        self.sessionForSMSConfirm = sessionForSMSConfirm

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:break
            if D == 1:
                if M == 0x0b:self.authToken = ip.readString().decode('ascii') if sys.version_info[0] == 2 else ip.readString()
                else:ip.skip(M)
            elif D == 2:
                if M == 0x0b:self.certificate = ip.readString().decode('ascii') if sys.version_info[0] == 2 else ip.readString()
                else:ip.skip(M)
            elif D == 3:
                if M == 0x0b:self.verifier = ip.readString().decode('ascii') if sys.version_info[0] == 2 else ip.readString()
                else:ip.skip(M)
            elif D == 4:
                if M == 0x0b:self.pinCode = ip.readString().decode('ascii') if sys.version_info[0] == 2 else ip.readString()
                else:ip.skip(M)
            elif D == 5:
                if M == 0x08:self.type = ip.readI32()
                else:ip.skip(M)
            elif D == 6:
                if M == 0x0a:self.lastPrimaryBindTime = ip.readI64()
                else:ip.skip(M)
            elif D == 7:
                if M == 0x0b:self.displayMessage = ip.readString().decode('ascii') if sys.version_info[0] == 2 else ip.readString()
                else:ip.skip(M)
            elif D == 8:
                if M == 0x0c:
                    self.sessionForSMSConfirm = SessionData()
                    self.sessionForSMSConfirm.read(ip)
                else:ip.skip(M)
            else:ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('LoginResult')
        if self.authToken is not None:
            op.writeFieldBegin('authToken', 0x0b, 1)
            op.writeString(self.authToken.encode('ascii') if sys.version_info[0] == 2 else self.authToken)
            op.writeFieldEnd()
        if self.certificate is not None:
            op.writeFieldBegin('certificate', 0x0b, 2)
            op.writeString(self.certificate.encode('ascii') if sys.version_info[0] == 2 else self.certificate)
            op.writeFieldEnd()
        if self.verifier is not None:
            op.writeFieldBegin('verifier', 0x0b, 3)
            op.writeString(self.verifier.encode('ascii') if sys.version_info[0] == 2 else self.verifier)
            op.writeFieldEnd()
        if self.pinCode is not None:
            op.writeFieldBegin('pinCode', 0x0b, 4)
            op.writeString(self.pinCode.encode('ascii') if sys.version_info[0] == 2 else self.pinCode)
            op.writeFieldEnd()
        if self.type is not None:
            op.writeFieldBegin('type', 0x08, 5)
            op.writeI32(self.type)
            op.writeFieldEnd()
        if self.lastPrimaryBindTime is not None:
            op.writeFieldBegin('lastPrimaryBindTime', 0x0a, 6)
            op.writeI64(self.lastPrimaryBindTime)
            op.writeFieldEnd()
        if self.displayMessage is not None:
            op.writeFieldBegin('displayMessage', 0x0b, 7)
            op.writeString(self.displayMessage.encode('ascii') if sys.version_info[0] == 2 else self.displayMessage)
            op.writeFieldEnd()
        if self.sessionForSMSConfirm is not None:
            op.writeFieldBegin('sessionForSMSConfirm', 0x0c, 8)
            self.sessionForSMSConfirm.write(op)
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)
    
    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class getLastOpRevisionArgs(object):

    def read(self,ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:break
            else:ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('getLastOpRevisionArgs')
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)
    
    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class getLastOpRevisionResult(object):

    def __init__(self, success=None, e=None):
        self.success = success
        self.e = e

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:break
            if D == 0:
                if M == 0x0a:self.success = ip.readI64()
                else:ip.skip(M)
            elif D == 1:
                if M == 0x0c:
                    self.e = TalkException()
                    self.e.read(ip)
                else:ip.skip(M)
            else:ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('getLastOpRevisionResult')
        if self.success is not None:
            op.writeFieldBegin('success', 0x0a, 0)
            op.writeI64(self.success)
            op.writeFieldEnd()
        if self.e is not None:
            op.writeFieldBegin('e', 0x0c, 1)
            self.e.write(op)
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)
    
    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class GetProfileArgs(object):

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:break
            else:
                ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('getProfileArgs')
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)
    
    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class GetProfileResult(object):

    def __init__(self, success=None, e=None):
        self.success = success
        self.e = e

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:break
            if D == 0:
                if M == 0x0c:
                    self.success = Profile()
                    self.success.read(ip)
                else:ip.skip(M)
            elif D == 1:
                if M == 0x0c:
                    self.e = TalkException()
                    self.e.read(ip)
                else:ip.skip(M)
            else:ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('getProfileResult')
        if self.success is not None:
            op.writeFieldBegin('success', 0x0c, 0)
            self.success.write(op)
            op.writeFieldEnd()
        if self.e is not None:
            op.writeFieldBegin('e', 0x0c, 1)
            self.e.write(op)
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)
    
    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class GroupPreference(object):

    def __init__(self, invitationTicket=None, favoriteTimestamp=None):
        self.invitationTicket = invitationTicket
        self.favoriteTimestamp = favoriteTimestamp

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:break
            if D == 1:
                if M == 0x0b:
                    self.invitationTicket = ip.readString().decode('utf-8') if sys.version_info[0] == 2 else ip.readString()
                else:
                    ip.skip(M)
            elif D == 2:
                if M == 0x0a:
                    self.favoriteTimestamp = ip.readI64()
                else:
                    ip.skip(M)
            else:
                ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('GroupPreference')
        if self.invitationTicket is not None:
            op.writeFieldBegin('invitationTicket', 0x0b, 1)
            op.writeString(self.invitationTicket.encode('utf-8') if sys.version_info[0] == 2 else self.invitationTicket)
            op.writeFieldEnd()
        if self.favoriteTimestamp is not None:
            op.writeFieldBegin('favoriteTimestamp', 0x0a, 2)
            op.writeI64(self.favoriteTimestamp)
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)
    
    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class GetContactArgs(object):

    def __init__(self, contactid=None):
        self.id = contactid

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:
                break
            if D == 2:
                if M == 0x0b:
                    self.id = ip.readString().decode('utf-8') if sys.version_info[0] == 2 else ip.readString()
                else:
                    ip.skip(M)
            else:
                ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('getContact_args')
        if self.id is not None:
            op.writeFieldBegin('id', 0x0b, 2)
            op.writeString(self.id.encode('utf-8') if sys.version_info[0] == 2 else self.id)
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)
    
    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class GetContactResult(object):
    
    def __init__(self, success=None, e=None):
        self.success = success
        self.e = e

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:
                break
            if D == 0:
                if M == 0x0c:
                    self.success = Contact()
                    self.success.read(ip)
                else:
                    ip.skip(M)
            elif D == 1:
                if M == 0x0c:
                    self.e = TalkException()
                    self.e.read(ip)
                else:
                    ip.skip(M)
            else:
                ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('getContact_result')
        if self.success is not None:
            op.writeFieldBegin('success', 0x0c, 0)
            self.success.write(op)
            op.writeFieldEnd()
        if self.e is not None:
            op.writeFieldBegin('e', 0x0c, 1)
            self.e.write(op)
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)
    
    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class GetContactsArgs(object):

    def __init__(self, ids=None):
        self.ids = ids

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:
                break
            if D == 2:
                if M == 0x0f:
                    self.ids = []
                    (_etype1940, _size1937) = ip.readListBegin()
                    for _i1941 in range(_size1937):
                        _elem1942 = ip.readString().decode('utf-8') if sys.version_info[0] == 2 else ip.readString()
                        self.ids.append(_elem1942)
                    ip.readListEnd()
                else:
                    ip.skip(M)
            else:
                ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('getContacts_args')
        if self.ids is not None:
            op.writeFieldBegin('ids', 0x0f, 2)
            op.writeListBegin(0x0b, len(self.ids))
            for iter1943 in self.ids:
                op.writeString(iter1943.encode('utf-8') if sys.version_info[0] == 2 else iter1943)
            op.writeListEnd()
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)
    
    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class GetContactsResult(object):

    def __init__(self, success=None, e=None):
        self.success = success
        self.e = e

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:
                break
            if D == 0:
                if M == 0x0f:
                    self.success = []
                    (_etype1947, _size1944) = ip.readListBegin()
                    for _i1948 in range(_size1944):
                        _elem1949 = Contact()
                        _elem1949.read(ip)
                        self.success.append(_elem1949)
                    ip.readListEnd()
                else:
                    ip.skip(M)
            elif D == 1:
                if M == 0x0c:
                    self.e = TalkException()
                    self.e.read(ip)
                else:
                    ip.skip(M)
            else:
                ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('getContacts_result')
        if self.success is not None:
            op.writeFieldBegin('success', 0x0f, 0)
            op.writeListBegin(0x0c, len(self.success))
            for iter1950 in self.success:
                iter1950.write(op)
            op.writeListEnd()
            op.writeFieldEnd()
        if self.e is not None:
            op.writeFieldBegin('e', 0x0c, 1)
            self.e.write(op)
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)
    
    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class AddFriendArgs(object):

    def __init__(self, reqSeq=None, mid=None, type=None, reference=None):
        self.reqSeq = reqSeq
        self.mid = mid
        self.type = type
        self.reference = reference

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:
                break
            if D == 1:
                if M == 0x08:
                    self.reqSeq = ip.readI32()
                else:
                    ip.skip(M)
            elif D == 2:
                if M == 0x0b:
                    self.mid = ip.readString().decode('utf-8') if sys.version_info[0] == 2 else ip.readString()
                else:
                    ip.skip(M)
            elif D == 3:
                if M == 0x08:
                    self.type = ip.readI32()
                else:
                    ip.skip(M)
            elif D == 4:
                if M == 0x0b:
                    self.reference = ip.readString().decode('utf-8') if sys.version_info[0] == 2 else ip.readString()
                else:
                    ip.skip(M)
            else:
                ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('findAndAddContactsByMid_args')
        if self.reqSeq is not None:
            op.writeFieldBegin('reqSeq', 0x08, 1)
            op.writeI32(self.reqSeq)
            op.writeFieldEnd()
        if self.mid is not None:
            op.writeFieldBegin('mid', 0x0b, 2)
            op.writeString(self.mid.encode('utf-8') if sys.version_info[0] == 2 else self.mid)
            op.writeFieldEnd()
        if self.type is not None:
            op.writeFieldBegin('type', 0x08, 3)
            op.writeI32(self.type)
            op.writeFieldEnd()
        if self.reference is not None:
            op.writeFieldBegin('reference', 0x0b, 4)
            op.writeString(self.reference.encode('utf-8') if sys.version_info[0] == 2 else self.reference)
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)
    
    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class AddFriendResult(object):

    def __init__(self, success=None, e=None):
        self.success = success
        self.e = e

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:
                break
            if D == 0:
                if M == 0x0d:
                    self.success = {}
                    (_ktype1809, _vtype1810, _size1808) = ip.readMapBegin()
                    for _i1812 in range(_size1808):
                        _key1813 = ip.readString().decode('utf-8') if sys.version_info[0] == 2 else ip.readString()
                        _val1814 = Contact()
                        _val1814.read(ip)
                        self.success[_key1813] = _val1814
                    ip.readMapEnd()
                else:
                    ip.skip(M)
            elif D == 1:
                if M == 0x0c:
                    self.e = TalkException()
                    self.e.read(ip)
                else:
                    ip.skip(M)
            else:
                ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('findAndAddContactsByMid_result')
        if self.success is not None:
            op.writeFieldBegin('success', 0x0d, 0)
            op.writeMapBegin(0x0b, 0x0c, len(self.success))
            for kiter1815, viter1816 in self.success.items():
                op.writeString(kiter1815.encode('utf-8') if sys.version_info[0] == 2 else kiter1815)
                viter1816.write(op)
            op.writeMapEnd()
            op.writeFieldEnd()
        if self.e is not None:
            op.writeFieldBegin('e', 0x0c, 1)
            self.e.write(op)
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)
    
    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class GetAllFriendsArgs(object):

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:
                break
            else:
                ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('getAllContactIds_args')
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)
    
    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class GetAllFriendsResult(object):

    def __init__(self, success=None, e=None):
        self.success = success
        self.e = e

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:
                break
            if D == 0:
                if M == 0x0f:
                    self.success = []
                    (_etype1898, _size1895) = ip.readListBegin()
                    for _i1899 in range(_size1895):
                        _elem1900 = ip.readString().decode('utf-8') if sys.version_info[0] == 2 else ip.readString()
                        self.success.append(_elem1900)
                    ip.readListEnd()
                else:
                    ip.skip(M)
            elif D == 1:
                if M == 0x0c:
                    self.e = TalkException()
                    self.e.read(ip)
                else:
                    ip.skip(M)
            else:
                ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('getAllContactIds_result')
        if self.success is not None:
            op.writeFieldBegin('success', 0x0f, 0)
            op.writeListBegin(0x0b, len(self.success))
            for iter1901 in self.success:
                op.writeString(iter1901.encode('utf-8') if sys.version_info[0] == 2 else iter1901)
            op.writeListEnd()
            op.writeFieldEnd()
        if self.e is not None:
            op.writeFieldBegin('e', 0x0c, 1)
            self.e.write(op)
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)
    
    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class GetGroupArgs(object):

    def __init__(self,groupid=None):
        self.groupid = groupid

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if D == 2:
                if M == 0x00:
                    break
                else:ip.skip(M)
            else:
                ip.skip(M)
            ip.readFeildEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('getGroupArgs')
        if self.groupId is not None:
            op.writeFieldBegin('groupId', 0x0b, 2)
            op.writeString(self.groupId.encode('utf-8') if sys.version_info[0] == 2 else self.groupId)
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)
    
    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class GetGroupResult(object):

    def __init__(self, success=None, e=None):
        self.success = success
        self.e = e

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:break
            if D == 0:
                if M == 0x0c:
                    self.success = Group()
                    self.success.read(ip)
                else:
                    ip.skip(M)
            elif D == 1:
                if M == 0x0c:
                    self.e = TalkException()
                    self.e.read(ip)
                else:
                    ip.skip(M)
            else:
                ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('getGroupResult')
        if self.success is not None:
            op.writeFieldBegin('success', 0x0c, 0)
            self.success.write(op)
            op.writeFieldEnd()
        if self.e is not None:
            op.writeFieldBegin('e', 0x0c, 1)
            self.e.write(op)
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)
    
    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class GetGroupsArgs(object):

    def __init__(self, groupIds=None):
        self.groupIds = groupIds

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:
                break
            if D == 2:
                if M == 0x0f:
                    self.groupIds = []
                    (_etype1975, _size1972) = ip.readListBegin()
                    for _i1976 in range(_size1972):
                        _elem1977 = ip.readString().decode('utf-8') if sys.version_info[0] == 2 else ip.readString()
                        self.groupIds.append(_elem1977)
                    ip.readListEnd()
                else:
                    ip.skip(M)
            else:
                ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        if op._fast_encode is not None and self.thrift_spec is not None:
            op.trans.write(op._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        op.writeStructBegin('GetGroupsArgs')
        if self.groupIds is not None:
            op.writeFieldBegin('groupIds', 0x0f, 2)
            op.writeListBegin(0x0b, len(self.groupIds))
            for iter1978 in self.groupIds:
                op.writeString(iter1978.encode('utf-8') if sys.version_info[0] == 2 else iter1978)
            op.writeListEnd()
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)
    
    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class GetGroupsResult(object):

    def __init__(self, success=None, e=None):
        self.success = success
        self.e = e

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:
                break
            if D == 0:
                if M == 0x0f:
                    self.success = []
                    (_etype1982, _size1979) = ip.readListBegin()
                    for _i1983 in range(_size1979):
                        _elem1984 = Group()
                        _elem1984.read(ip)
                        self.success.append(_elem1984)
                    ip.readListEnd()
                else:
                    ip.skip(M)
            elif D == 1:
                if M == 0x0c:
                    self.e = TalkException()
                    self.e.read(ip)
                else:
                    ip.skip(M)
            else:
                ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('GetGroupsResult')
        if self.success is not None:
            op.writeFieldBegin('success', 0x0f, 0)
            op.writeListBegin(0x0c, len(self.success))
            for iter1985 in self.success:
                iter1985.write(op)
            op.writeListEnd()
            op.writeFieldEnd()
        if self.e is not None:
            op.writeFieldBegin('e', 0x0c, 1)
            self.e.write(op)
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)
    
    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class GetGroupidsArgs(object):

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:break
            else:
                ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('getGroupidsArgs')
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)
    
    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class GetGroupidsResult(object):

    def __init__(self, success=None, e=None):
        self.success = success
        self.e = e

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:break
            if D == 0:
                if M == 0x0f:
                    self.success = []
                    (_etype1968, _size1965) = ip.readListBegin()
                    for _i1969 in range(_size1965):
                        _elem1970 = ip.readString().decode('ascii') if sys.version_info[0] == 2 else ip.readString()
                        self.success.append(_elem1970)
                    ip.readListEnd()
                else:ip.skip(M)
            elif D == 1:
                if M == 0x0c:
                    self.e = TalkException()
                    self.e.read(ip)
                else:ip.skip(M)
            else:
                ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('getGroupidsResult')
        if self.success is not None:
            op.writeFieldBegin('success', 0x0f, 0)
            op.writeListBegin(0x0b, len(self.success))
            for iter1971 in self.success:
                op.writeString(iter1971.encode('ascii') if sys.version_info[0] == 2 else iter1971)
            op.writeListEnd()
            op.writeFieldEnd()
        if self.e is not None:
            op.writeFieldBegin('e', 0x0c, 1)
            self.e.write(op)
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)
    
    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class InvitationArgs(object):

    def __init__(self, reqSeq=None, groupId=None, contactIds=None):
        self.reqSeq = reqSeq
        self.groupId = groupId
        self.contactIds = contactIds

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:
                break
            if D == 1:
                if M == 0x08:
                    self.reqSeq = ip.readI32()
                else:
                    ip.skip(M)
            elif D == 2:
                if M == 0x0b:
                    self.groupId = ip.readString().decode('utf-8') if sys.version_info[0] == 2 else ip.readString()
                else:
                    ip.skip(M)
            elif D == 3:
                if M == 0x0f:
                    self.contactIds = []
                    (_etype2094, _size2091) = ip.readListBegin()
                    for _i2095 in range(_size2091):
                        _elem2096 = ip.readString().decode('utf-8') if sys.version_info[0] == 2 else ip.readString()
                        self.contactIds.append(_elem2096)
                    ip.readListEnd()
                else:
                    ip.skip(M)
            else:
                ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('inviteIntoGroup_args')
        if self.reqSeq is not None:
            op.writeFieldBegin('reqSeq', 0x08, 1)
            op.writeI32(self.reqSeq)
            op.writeFieldEnd()
        if self.groupId is not None:
            op.writeFieldBegin('groupId', 0x0b, 2)
            op.writeString(self.groupId.encode('utf-8') if sys.version_info[0] == 2 else self.groupId)
            op.writeFieldEnd()
        if self.contactIds is not None:
            op.writeFieldBegin('contactIds', 0x0f, 3)
            op.writeListBegin(0x0b, len(self.contactIds))
            for iter2097 in self.contactIds:
                op.writeString(iter2097.encode('utf-8') if sys.version_info[0] == 2 else iter2097)
            op.writeListEnd()
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)
    
    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class InvitationResult(object):

    def __init__(self, e=None):
        self.e = e

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:
                break
            if D == 1:
                if M == 0x0c:
                    self.e = TalkException()
                    self.e.read(ip)
                else:
                    ip.skip(M)
            else:
                ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('inviteIntoGroup_result')
        if self.e is not None:
            op.writeFieldBegin('e', 0x0c, 1)
            self.e.write(op)
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)
    
    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class KickoutArgs(object):

    def __init__(self, reqSeq=None, groupId=None, contactIds=None):
        self.reqSeq = reqSeq
        self.groupId = groupId
        self.contactIds = contactIds

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:
                break
            if D == 1:
                if M == 0x08:
                    self.reqSeq = ip.readI32()
                else:
                    ip.skip(M)
            elif D == 2:
                if M == 0x0b:
                    self.groupId = ip.readString().decode('utf-8') if sys.version_info[0] == 2 else ip.readString()
                else:
                    ip.skip(M)
            elif D == 3:
                if M == 0x0f:
                    self.contactIds = []
                    (_etype2108, _size2105) = ip.readListBegin()
                    for _i2109 in range(_size2105):
                        _elem2110 = ip.readString().decode('utf-8') if sys.version_info[0] == 2 else ip.readString()
                        self.contactIds.append(_elem2110)
                    ip.readListEnd()
                else:
                    ip.skip(M)
            else:
                ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('kickoutFromGroup_args')
        if self.reqSeq is not None:
            op.writeFieldBegin('reqSeq', 0x08, 1)
            op.writeI32(self.reqSeq)
            op.writeFieldEnd()
        if self.groupId is not None:
            op.writeFieldBegin('groupId', 0x0b, 2)
            op.writeString(self.groupId.encode('utf-8') if sys.version_info[0] == 2 else self.groupId)
            op.writeFieldEnd()
        if self.contactIds is not None:
            op.writeFieldBegin('contactIds', 0x0f, 3)
            op.writeListBegin(0x0b, len(self.contactIds))
            for iter2111 in self.contactIds:
                op.writeString(iter2111.encode('utf-8') if sys.version_info[0] == 2 else iter2111)
            op.writeListEnd()
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)
    
    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class KickoutResult(object):

    def __init__(self, e=None):
        self.e = e

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:
                break
            if D == 1:
                if M == 0x0c:
                    self.e = TalkException()
                    self.e.read(ip)
                else:
                    ip.skip(M)
            else:
                ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('kickoutFromGroup_result')
        if self.e is not None:
            op.writeFieldBegin('e', 0x0c, 1)
            self.e.write(op)
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)
    
    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class CancelInvitationArgs(object):

    def __init__(self, reqSeq=None, groupId=None, contactIds=None):
        self.reqSeq = reqSeq
        self.groupId = groupId
        self.contactIds = contactIds

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:
                break
            if D == 1:
                if M == 0x08:
                    self.reqSeq = ip.readI32()
                else:
                    ip.skip(M)
            elif D == 2:
                if M == 0x0b:
                    self.groupId = ip.readString().decode('utf-8') if sys.version_info[0] == 2 else ip.readString()
                else:
                    ip.skip(M)
            elif D == 3:
                if M == 0x0f:
                    self.contactIds = []
                    (_etype1698, _size1695) = ip.readListBegin()
                    for _i1699 in range(_size1695):
                        _elem1700 = ip.readString().decode('utf-8') if sys.version_info[0] == 2 else ip.readString()
                        self.contactIds.append(_elem1700)
                    ip.readListEnd()
                else:
                    ip.skip(M)
            else:
                ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('cancelGroupInvitation_args')
        if self.reqSeq is not None:
            op.writeFieldBegin('reqSeq', 0x08, 1)
            op.writeI32(self.reqSeq)
            op.writeFieldEnd()
        if self.groupId is not None:
            op.writeFieldBegin('groupId', 0x0b, 2)
            op.writeString(self.groupId.encode('utf-8') if sys.version_info[0] == 2 else self.groupId)
            op.writeFieldEnd()
        if self.contactIds is not None:
            op.writeFieldBegin('contactIds', 0x0f, 3)
            op.writeListBegin(0x0b, len(self.contactIds))
            for iter1701 in self.contactIds:
                op.writeString(iter1701.encode('utf-8') if sys.version_info[0] == 2 else iter1701)
            op.writeListEnd()
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)
    
    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class CancelInvitationResult(object):

    def __init__(self, e=None):
        self.e = e

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:
                break
            if D == 1:
                if M == 0x0c:
                    self.e = TalkException()
                    self.e.read(ip)
                else:
                    ip.skip(M)
            else:
                ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('cancelGroupInvitation_result')
        if self.e is not None:
            op.writeFieldBegin('e', 0x0c, 1)
            self.e.write(op)
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)
    
    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class SendMessageArgs(object):

    def __init__(self, seq=None, message=None):
        self.seq = seq
        self.message = message

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:break
            if D == 1:
                if M == 0x08:
                    self.seq = ip.readI32()
                else:ip.skip(M)
            elif D == 2:
                if M == 0x0c:
                    self.message = Message()
                    self.message.read(ip)
                else:ip.skip(M)
            else:
                ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('SendMessageArgs')
        if self.seq is not None:
            op.writeFieldBegin('seq', 0x08, 1)
            op.writeI32(self.seq)
            op.writeFieldEnd()
        if self.message is not None:
            op.writeFieldBegin('message', 0x0c, 2)
            self.message.write(op)
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)
    
    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class SendMessageResult(object):

    def __init__(self, success=None, e=None):
        self.success = success
        self.e = e

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:break
            if D == 0:
                if M == 0x0c:
                    self.success = Message()
                    self.success.read(ip)
                else:ip.skip(M)
            elif D == 1:
                if M == 0x0c:
                    self.e = TalkException()
                    self.e.read(ip)
                else:ip.skip(M)
            else:
                ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('SendMessageResult')
        if self.success is not None:
            op.writeFieldBegin('success', 0x0c, 0)
            self.success.write(op)
            op.writeFieldEnd()
        if self.e is not None:
            op.writeFieldBegin('e', 0x0c, 1)
            self.e.write(op)
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)
    
    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class RetractMessageArgs(object):

    def __init__(self, seq=None, messageId=None):
        self.seq = seq
        self.messageId = messageId

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:
                break
            if D == 1:
                if M == 0x08:
                    self.seq = ip.readI32()
                else:
                    ip.skip(M)
            elif D == 2:
                if M == 0x0b:
                    self.messageId = ip.readString().decode('utf-8') if sys.version_info[0] == 2 else ip.readString()
                else:
                    ip.skip(M)
            else:
                ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('unsendMessage_args')
        if self.seq is not None:
            op.writeFieldBegin('seq', 0x08, 1)
            op.writeI32(self.seq)
            op.writeFieldEnd()
        if self.messageId is not None:
            op.writeFieldBegin('messageId', 0x0b, 2)
            op.writeString(self.messageId.encode('utf-8') if sys.version_info[0] == 2 else self.messageId)
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)
    
    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class RetractMessageResult(object):

    def __init__(self, e=None):
        self.e = e

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:
                break
            if D == 1:
                if M == 0x0c:
                    self.e = TalkException()
                    self.e.read(ip)
                else:
                    ip.skip(M)
            else:
                ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('unsendMessage_result')
        if self.e is not None:
            op.writeFieldBegin('e', 0x0c, 1)
            self.e.write(op)
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)
    
    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class GetRecentMessagesArgs(object):

    def __init__(self, groupid=None, counter=None):
        self.groupid = groupid
        self.counter = counter

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:
                break
            if D == 2:
                if M == 0x0b:
                    self.groupid = ip.readString().decode('utf-8') if sys.version_info[0] == 2 else ip.readString()
                else:
                    ip.skip(M)
            elif D == 3:
                if M == 0x08:
                    self.counter = ip.readI32()
                else:
                    ip.skip(M)
            else:
                ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('getRecentMessages_args')
        if self.groupid is not None:
            op.writeFieldBegin('groupid', 0x0b, 2)
            op.writeString(self.groupid.encode('utf-8') if sys.version_info[0] == 2 else self.groupid)
            op.writeFieldEnd()
        if self.counter is not None:
            op.writeFieldBegin('counter', 0x08, 3)
            op.writeI32(self.counter)
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)
    
    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class GetRecentMessagesResult(object):

    def __init__(self, success=None, e=None):
        self.success = success
        self.e = e

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:
                break
            if D == 0:
                if M == 0x0f:
                    self.success = []
                    (_etype2358, _size2355) = ip.readListBegin()
                    for _i2359 in range(_size2355):
                        _elem2360 = Message()
                        _elem2360.read(ip)
                        self.success.append(_elem2360)
                    ip.readListEnd()
                else:
                    ip.skip(M)
            elif D == 1:
                if M == 0x0c:
                    self.e = TalkException()
                    self.e.read(ip)
                else:
                    ip.skip(M)
            else:
                ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        if op._fast_encode is not None and self.thrift_spec is not None:
            op.trans.write(op._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        op.writeStructBegin('getRecentMessagesV2_result')
        if self.success is not None:
            op.writeFieldBegin('success', 0x0f, 0)
            op.writeListBegin(0x0c, len(self.success))
            for iter2361 in self.success:
                iter2361.write(op)
            op.writeListEnd()
            op.writeFieldEnd()
        if self.e is not None:
            op.writeFieldBegin('e', 0x0c, 1)
            self.e.write(op)
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)
    
    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class OperationsArgs(object):

    def __init__(self, localRev=None, count=None):
        self.localRev = localRev
        self.count = count

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:break
            if D == 2:
                if M == 0x0a:
                    self.localRev = ip.readI64()
                else:ip.skip(M)
            elif D == 3:
                if M == 0x08:
                    self.count = ip.readI32()
                else:ip.skip(M)
            else:
                ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('OperationsArgs')
        if self.localRev is not None:
            op.writeFieldBegin('localRev', 0x0a, 2)
            op.writeI64(self.localRev)
            op.writeFieldEnd()
        if self.count is not None:
            op.writeFieldBegin('count', 0x08, 3)
            op.writeI32(self.count)
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)
    
    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class OperationsResult(object):

    def __init__(self, success=None, e=None):
        self.success = success
        self.e = e

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:break
            if D == 0:
                if M == 0x0f:
                    self.success = []
                    (_etype1670, _size1667) = ip.readListBegin()
                    for _i1671 in range(_size1667):
                        _elem1672 = Operation()
                        _elem1672.read(ip)
                        self.success.append(_elem1672)
                    ip.readListEnd()
                else:ip.skip(M)
            elif D == 1:
                if M == 0x0c:
                    self.e = ShouldSyncException()
                    self.e.read(ip)
                else:ip.skip(M)
            else:
                ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('OperationsResult')
        if self.success is not None:
            op.writeFieldBegin('success', 0x0f, 0)
            op.writeListBegin(0x0c, len(self.success))
            for iter1673 in self.success:
                iter1673.write(op)
            op.writeListEnd()
            op.writeFieldEnd()
        if self.e is not None:
            op.writeFieldBegin('e', 0x0c, 1)
            self.e.write(op)
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)
    
    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class ShouldSyncException(TException):

    def __init__(self, syncOpRevision=None, syncScope=None, syncReason=None, message=None):
        self.syncOpRevision = syncOpRevision
        self.syncScope = syncScope
        self.syncReason = syncReason
        self.message = message

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:break
            if D == 1:
                if M == 0x0a:
                    self.syncOpRevision = ip.readI64()
                else:ip.skip(M)
            elif D == 2:
                if M == 0x0c:
                    self.syncScope = SyncScope()
                    self.syncScope.read(ip)
                else:ip.skip(M)
            elif D == 3:
                if M == 0x08:
                    self.syncReason = ip.readI32()
                else:ip.skip(M)
            elif D == 4:
                if M == 0x0b:
                    self.message = ip.readString().decode('ascii') if sys.version_info[0] == 2 else ip.readString()
                else:ip.skip(M)
            else:
                ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('ShouldSyncException')
        if self.syncOpRevision is not None:
            op.writeFieldBegin('syncOpRevision', 0x0a, 1)
            op.writeI64(self.syncOpRevision)
            op.writeFieldEnd()
        if self.syncScope is not None:
            op.writeFieldBegin('syncScope', 0x0c, 2)
            self.syncScope.write(op)
            op.writeFieldEnd()
        if self.syncReason is not None:
            op.writeFieldBegin('syncReason', 0x08, 3)
            op.writeI32(self.syncReason)
            op.writeFieldEnd()
        if self.message is not None:
            op.writeFieldBegin('message', 0x0b, 4)
            op.writeString(self.message.encode('ascii') if sys.version_info[0] == 2 else self.message)
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)

    def __repr__(self) -> ReprPMD:return ReprPMD(self,True).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class SyncScope(object):

    def __init__(self, syncProfile=None, syncSettings=None, syncSticker=None, syncThemeShop=None, contact=None, group=None, room=None, chat=None):
        self.syncProfile = syncProfile
        self.syncSettings = syncSettings
        self.syncSticker = syncSticker
        self.syncThemeShop = syncThemeShop
        self.contact = contact
        self.group = group
        self.room = room
        self.chat = chat

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:break
            if D == 1:
                if M == 0x02:
                    self.syncProfile = ip.readBool()
                else:ip.skip(M)
            elif D == 2:
                if M == 0x02:
                    self.syncSettings = ip.readBool()
                else:ip.skip(M)
            elif D == 3:
                if M == 0x02:
                    self.syncSticker = ip.readBool()
                else:ip.skip(M)
            elif D == 4:
                if M == 0x02:
                    self.syncThemeShop = ip.readBool()
                else:ip.skip(M)
            elif D == 10:
                if M == 0x0c:
                    self.contact = SyncRelations()
                    self.contact.read(ip)
                else:ip.skip(M)
            elif D == 11:
                if M == 0x0c:
                    self.group = SyncRelations()
                    self.group.read(ip)
                else:ip.skip(M)
            elif D == 12:
                if M == 0x0c:
                    self.room = SyncRelations()
                    self.room.read(ip)
                else:ip.skip(M)
            elif D == 13:
                if M == 0x0c:
                    self.chat = SyncRelations()
                    self.chat.read(ip)
                else:ip.skip(M)
            else:
                ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('SyncScope')
        if self.syncProfile is not None:
            op.writeFieldBegin('syncProfile', 0x02, 1)
            op.writeBool(self.syncProfile)
            op.writeFieldEnd()
        if self.syncSettings is not None:
            op.writeFieldBegin('syncSettings', 0x02, 2)
            op.writeBool(self.syncSettings)
            op.writeFieldEnd()
        if self.syncSticker is not None:
            op.writeFieldBegin('syncSticker', 0x02, 3)
            op.writeBool(self.syncSticker)
            op.writeFieldEnd()
        if self.syncThemeShop is not None:
            op.writeFieldBegin('syncThemeShop', 0x02, 4)
            op.writeBool(self.syncThemeShop)
            op.writeFieldEnd()
        if self.contact is not None:
            op.writeFieldBegin('contact', 0x0c, 10)
            self.contact.write(op)
            op.writeFieldEnd()
        if self.group is not None:
            op.writeFieldBegin('group', 0x0c, 11)
            self.group.write(op)
            op.writeFieldEnd()
        if self.room is not None:
            op.writeFieldBegin('room', 0x0c, 12)
            self.room.write(op)
            op.writeFieldEnd()
        if self.chat is not None:
            op.writeFieldBegin('chat', 0x0c, 13)
            self.chat.write(op)
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)
    
    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class SyncRelations(object):

    def __init__(self, syncAll=None, syncParamContact=None, syncParamMid=None):
        self.syncAll = syncAll
        self.syncParamContact = syncParamContact
        self.syncParamMid = syncParamMid

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:break
            if D == 1:
                if M == 0x02:
                    self.syncAll = ip.readBool()
                else:ip.skip(M)
            elif D == 2:
                if M == 0x0f:
                    self.syncParamContact = []
                    (_etype, _size509) = ip.readListBegin()
                    for _i in range(_size509):
                        _elem = SyncParamContact()
                        _elem.read(ip)
                        self.syncParamContact.append(_elem)
                    ip.readListEnd()
                else:ip.skip(M)
            elif D == 3:
                if M == 0x0f:
                    self.syncParamMid = []
                    (_etype, _size) = ip.readListBegin()
                    for i in range(_size):
                        _elem = SyncParamMid()
                        _elem.read(ip)
                        self.syncParamMid.append(_elem)
                    ip.readListEnd()
                else:ip.skip(M)
            else:
                ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('SyncRelations')
        if self.syncAll is not None:
            op.writeFieldBegin('syncAll', 0x02, 1)
            op.writeBool(self.syncAll)
            op.writeFieldEnd()
        if self.syncParamContact is not None:
            op.writeFieldBegin('syncParamContact', 0x0f, 2)
            op.writeListBegin(0x0c, len(self.syncParamContact))
            for iter521 in self.syncParamContact:
                iter521.write(op)
            op.writeListEnd()
            op.writeFieldEnd()
        if self.syncParamMid is not None:
            op.writeFieldBegin('syncParamMid', 0x0f, 3)
            op.writeListBegin(0x0c, len(self.syncParamMid))
            for iter522 in self.syncParamMid:
                iter522.write(op)
            op.writeListEnd()
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)
    
    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class SyncParamContact(object):
    
    def __init__(self, syncParamMid=None, contactStatus=None):
        self.syncParamMid = syncParamMid
        self.contactStatus = contactStatus

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:break
            if D == 1:
                if M == 0x0c:
                    self.syncParamMid = SyncParamMid()
                    self.syncParamMid.read(ip)
                else:ip.skip(M)
            elif D == 2:
                if M == 0x08:
                    self.contactStatus = ip.readI32()
                else:ip.skip(M)
            else:
                ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('SyncParamContact')
        if self.syncParamMid is not None:
            op.writeFieldBegin('syncParamMid', 0x0c, 1)
            self.syncParamMid.write(op)
            op.writeFieldEnd()
        if self.contactStatus is not None:
            op.writeFieldBegin('contactStatus', 0x08, 2)
            op.writeI32(self.contactStatus)
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)
    
    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class SyncParamMid(object):

    def __init__(self, mid=None, diff=None, revision=None):
        self.mid = mid
        self.diff = diff
        self.revision = revision

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:break
            if D == 1:
                if M == 0x0b:self.mid = ip.readString().decode('ascii') if sys.version_info[0] == 2 else ip.readString()
                else:ip.skip(M)
            elif D == 2:
                if M == 0x08:self.diff = ip.readI32()
                else:ip.skip(M)
            elif D == 3:
                if M == 0x0a:self.revision = ip.readI64()
                else:ip.skip(M)
            else:ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('SyncParamMid')
        if self.mid is not None:
            op.writeFieldBegin('mid', 0x0b, 1)
            op.writeString(self.mid.encode('ascii') if sys.version_info[0] == 2 else self.mid)
            op.writeFieldEnd()
        if self.diff is not None:
            op.writeFieldBegin('diff', 0x08, 2)
            op.writeI32(self.diff)
            op.writeFieldEnd()
        if self.revision is not None:
            op.writeFieldBegin('revision', 0x0a, 3)
            op.writeI64(self.revision)
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)
    
    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class IntoGroupArgs(object):

    def __init__(self, reqSeq=None, groupId=None):
        self.reqSeq = reqSeq
        self.groupId = groupId

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:
                break
            if D == 1:
                if M == 0x08:
                    self.reqSeq = ip.readI32()
                else:
                    ip.skip(M)
            elif D == 2:
                if M == 0x0b:
                    self.groupId = ip.readString().decode('utf-8') if sys.version_info[0] == 2 else ip.readString()
                else:
                    ip.skip(M)
            else:
                ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('IntoGroupArgs')
        if self.reqSeq is not None:
            op.writeFieldBegin('reqSeq', 0x08, 1)
            op.writeI32(self.reqSeq)
            op.writeFieldEnd()
        if self.groupId is not None:
            op.writeFieldBegin('groupId', 0x0b, 2)
            op.writeString(self.groupId.encode('utf-8') if sys.version_info[0] == 2 else self.groupId)
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)
    
    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class IntoGroupResult(object):

    def __init__(self, e=None):
        self.e = e

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:break
            if D == 1:
                if M == 0x0c:
                    self.e = TalkException()
                    self.e.read(ip)
                else:ip.skip(M)
            else:ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('SendMessageResult')
        if self.e is not None:
            op.writeFieldBegin('e', 0x0c, 1)
            self.e.write(op)
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)
    
    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class FindGroupByUrlArgs(object):

    def __init__(self, ticketId=None):
        self.ticketId = ticketId

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:
                break
            if D == 1:
                if M == 0x0b:
                    self.ticketId = ip.readString().decode('utf-8') if sys.version_info[0] == 2 else ip.readString()
                else:
                    ip.skip(M)
            else:
                ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('findGroupByTicketV2_args')
        if self.ticketId is not None:
            op.writeFieldBegin('ticketId', 0x0b, 1)
            op.writeString(self.ticketId.encode('utf-8') if sys.version_info[0] == 2 else self.ticketId)
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)

    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class FindGroupByUrlResult(object):

    def __init__(self, success=None, e=None):
        self.success = success
        self.e = e

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:
                break
            if D == 0:
                if M == 0x0c:
                    self.success = Group()
                    self.success.read(ip)
                else:
                    ip.skip(M)
            elif D == 1:
                if M == 0x0c:
                    self.e = TalkException()
                    self.e.read(ip)
                else:
                    ip.skip(M)
            else:
                ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('findGroupByTicketV2_result')
        if self.success is not None:
            op.writeFieldBegin('success', 0x0c, 0)
            self.success.write(op)
            op.writeFieldEnd()
        if self.e is not None:
            op.writeFieldBegin('e', 0x0c, 1)
            self.e.write(op)
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)

    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class CreateGroupArgs(object):

    def __init__(self, seq=None, name=None, contactIds=None):
        self.seq = seq
        self.name = name
        self.contactIds = contactIds

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:
                break
            if D == 1:
                if M == 0x08:
                    self.seq = ip.readI32()
                else:
                    ip.skip(M)
            elif D == 2:
                if M == 0x0b:
                    self.name = ip.readString().decode('utf-8') if sys.version_info[0] == 2 else ip.readString()
                else:
                    ip.skip(M)
            elif D == 3:
                if M == 0x0f:
                    self.contactIds = []
                    (_etype1767, _size1764) = ip.readListBegin()
                    for _i1768 in range(_size1764):
                        _elem1769 = ip.readString().decode('utf-8') if sys.version_info[0] == 2 else ip.readString()
                        self.contactIds.append(_elem1769)
                    ip.readListEnd()
                else:
                    ip.skip(M)
            else:
                ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('createGroup_args')
        if self.seq is not None:
            op.writeFieldBegin('seq', 0x08, 1)
            op.writeI32(self.seq)
            op.writeFieldEnd()
        if self.name is not None:
            op.writeFieldBegin('name', 0x0b, 2)
            op.writeString(self.name.encode('utf-8') if sys.version_info[0] == 2 else self.name)
            op.writeFieldEnd()
        if self.contactIds is not None:
            op.writeFieldBegin('contactIds', 0x0f, 3)
            op.writeListBegin(0x0b, len(self.contactIds))
            for iter1770 in self.contactIds:
                op.writeString(iter1770.encode('utf-8') if sys.version_info[0] == 2 else iter1770)
            op.writeListEnd()
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)

    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class CreateGroupResult(object):

    def __init__(self, success=None, e=None):
        self.success = success
        self.e = e

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:
                break
            if D == 0:
                if M == 0x0c:
                    self.success = Group()
                    self.success.read(ip)
                else:
                    ip.skip(M)
            elif D == 1:
                if M == 0x0c:
                    self.e = TalkException()
                    self.e.read(ip)
                else:
                    ip.skip(M)
            else:
                ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('createGroup_result')
        if self.success is not None:
            op.writeFieldBegin('success', 0x0c, 0)
            self.success.write(op)
            op.writeFieldEnd()
        if self.e is not None:
            op.writeFieldBegin('e', 0x0c, 1)
            self.e.write(op)
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)

    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class UpdateGroupUrlArgs(object):

    def __init__(self, groupMid=None):
        self.groupMid = groupMid

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:
                break
            if D == 1:
                if M == 0x0b:
                    self.groupMid = ip.readString().decode('utf-8') if sys.version_info[0] == 2 else ip.readString()
                else:
                    ip.skip(M)
            else:
                ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('reissueGroupTicket_args')
        if self.groupMid is not None:
            op.writeFieldBegin('groupMid', 0x0b, 1)
            op.writeString(self.groupMid.encode('utf-8') if sys.version_info[0] == 2 else self.groupMid)
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)

    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class UpdateGroupUrlResult(object):

    def __init__(self, success=None, e=None):
        self.success = success
        self.e = e

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:
                break
            if D == 0:
                if M == 0x0b:
                    self.success = ip.readString().decode('utf-8') if sys.version_info[0] == 2 else ip.readString()
                else:
                    ip.skip(M)
            elif D == 1:
                if M == 0x0c:
                    self.e = TalkException()
                    self.e.read(ip)
                else:
                    ip.skip(M)
            else:
                ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('reissueGroupTicket_result')
        if self.success is not None:
            op.writeFieldBegin('success', 0x0b, 0)
            op.writeString(self.success.encode('utf-8') if sys.version_info[0] == 2 else self.success)
            op.writeFieldEnd()
        if self.e is not None:
            op.writeFieldBegin('e', 0x0c, 1)
            self.e.write(op)
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)

    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class UrlIntoGroupArgs(object):
    
    def __init__(self, reqSeq=None, GroupMid=None, ticketId=None):
        self.reqSeq = reqSeq
        self.GroupMid = GroupMid
        self.ticketId = ticketId

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:
                break
            if D == 1:
                if M == 0x08:self.reqSeq = ip.readI32()
                else:ip.skip(M)
            elif D == 2:
                if M == 0x0b:self.GroupMid = ip.readString().decode('utf-8') if sys.version_info[0] == 2 else ip.readString()
                else:ip.skip(M)
            elif D == 3:
                if M == 0x0b:self.ticketId = ip.readString().decode('utf-8') if sys.version_info[0] == 2 else ip.readString()
                else:ip.skip(M)
            else:ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('UrlIntoGroupArgs')
        if self.reqSeq is not None:
            op.writeFieldBegin('reqSeq', 0x08, 1)
            op.writeI32(self.reqSeq)
            op.writeFieldEnd()
        if self.GroupMid is not None:
            op.writeFieldBegin('GroupMid', 0x0b, 2)
            op.writeString(self.GroupMid.encode('utf-8') if sys.version_info[0] == 2 else self.GroupMid)
            op.writeFieldEnd()
        if self.ticketId is not None:
            op.writeFieldBegin('ticketId', 0x0b, 3)
            op.writeString(self.ticketId.encode('utf-8') if sys.version_info[0] == 2 else self.ticketId)
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)

    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class UrlIntoGroupResult(object):
    
    def __init__(self, e=None):
        self.e = e

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:
                break
            if D == 1:
                if M == 0x0c:
                    self.e = TalkException()
                    self.e.read(ip)
                else:
                    ip.skip(M)
            else:
                ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('UrlIntoGroupResult')
        if self.e is not None:
            op.writeFieldBegin('e', 0x0c, 1)
            self.e.write(op)
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)

    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class OutGroupArgs(object):

    def __init__(self, reqSeq=None, groupId=None):
        self.reqSeq = reqSeq
        self.groupId = groupId

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:break
            if D == 1:
                if M == 0x08:self.reqSeq = ip.readI32()
                else:ip.skip(M)
            elif D == 2:
                if M == 0x0b:self.groupId = ip.readString().decode('utf-8') if sys.version_info[0] == 2 else ip.readString()
                else:ip.skip(M)
            else:ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('OutGroupArgs')
        if self.reqSeq is not None:
            op.writeFieldBegin('reqSeq', 0x08, 1)
            op.writeI32(self.reqSeq)
            op.writeFieldEnd()
        if self.groupId is not None:
            op.writeFieldBegin('groupId', 0x0b, 2)
            op.writeString(self.groupId.encode('utf-8') if sys.version_info[0] == 2 else self.groupId)
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)
    
    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class OutGroupResult(object):

    def __init__(self, e=None):
        self.e = e

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:break
            if D == 1:
                if M == 0x0c:
                    self.e = TalkException()
                    self.e.read(ip)
                else:ip.skip(M)
            else:ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('OutGroupResult')
        if self.e is not None:
            op.writeFieldBegin('e', 0x0c, 1)
            self.e.write(op)
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)
    
    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class UpdateGroupArgs(object):

    def __init__(self, reqSeq=None, group=None):
        self.reqSeq = reqSeq
        self.group = group

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:
                break
            if D == 1:
                if M == 0x08:
                    self.reqSeq = ip.readI32()
                else:
                    ip.skip(M)
            elif D == 2:
                if M == 0x0c:
                    self.group = Group()
                    self.group.read(ip)
                else:
                    ip.skip(M)
            else:
                ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('updateGroup_args')
        if self.reqSeq is not None:
            op.writeFieldBegin('reqSeq', 0x08, 1)
            op.writeI32(self.reqSeq)
            op.writeFieldEnd()
        if self.group is not None:
            op.writeFieldBegin('group', 0x0c, 2)
            self.group.write(op)
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)
    
    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class UpdateGroupResult(object):

    def __init__(self, e=None):
        self.e = e

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:
                break
            if D == 1:
                if M == 0x0c:
                    self.e = TalkException()
                    self.e.read(ip)
                else:
                    ip.skip(M)
            else:
                ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('updateGroup_result')
        if self.e is not None:
            op.writeFieldBegin('e', 0x0c, 1)
            self.e.write(op)
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)
    
    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class CreateRoomArgs(object):

    def __init__(self, reqSeq=None, contactIds=None):
        self.reqSeq = reqSeq
        self.contactIds = contactIds

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:
                break
            if D == 1:
                if M == 0x08:
                    self.reqSeq = ip.readI32()
                else:
                    ip.skip(M)
            elif D == 2:
                if M == 0x0f:
                    self.contactIds = []
                    (_etype2314, _size2311) = ip.readListBegin()
                    for _i2315 in range(_size2311):
                        _elem2316 = ip.readString().decode('utf-8') if sys.version_info[0] == 2 else ip.readString()
                        self.contactIds.append(_elem2316)
                    ip.readListEnd()
                else:
                    ip.skip(M)
            else:
                ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('createRoomV2_args')
        if self.reqSeq is not None:
            op.writeFieldBegin('reqSeq', 0x08, 1)
            op.writeI32(self.reqSeq)
            op.writeFieldEnd()
        if self.contactIds is not None:
            op.writeFieldBegin('contactIds', 0x0f, 2)
            op.writeListBegin(0x0b, len(self.contactIds))
            for iter2317 in self.contactIds:
                op.writeString(iter2317.encode('utf-8') if sys.version_info[0] == 2 else iter2317)
            op.writeListEnd()
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)
    
    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class CreateRoomResult(object):

    def __init__(self, success=None, e=None):
        self.success = success
        self.e = e

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:
                break
            if D == 0:
                if M == 0x0c:
                    self.success = Room()
                    self.success.read(ip)
                else:
                    ip.skip(M)
            elif D == 1:
                if M == 0x0c:
                    self.e = TalkException()
                    self.e.read(ip)
                else:
                    ip.skip(M)
            else:
                ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('createRoomV2_result')
        if self.success is not None:
            op.writeFieldBegin('success', 0x0c, 0)
            self.success.write(op)
            op.writeFieldEnd()
        if self.e is not None:
            op.writeFieldBegin('e', 0x0c, 1)
            self.e.write(op)
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)
    
    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class OutRoomArgs(object):

    def __init__(self, reqSeq=None, roomId=None):
        self.reqSeq = reqSeq
        self.roomId = roomId

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:
                break
            if D == 1:
                if M == 0x08:
                    self.reqSeq = ip.readI32()
                else:
                    ip.skip(M)
            elif D == 2:
                if M == 0x0b:
                    self.roomId = ip.readString().decode('utf-8') if sys.version_info[0] == 2 else ip.readString()
                else:
                    ip.skip(M)
            else:
                ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('leaveRoom_args')
        if self.reqSeq is not None:
            op.writeFieldBegin('reqSeq', 0x08, 1)
            op.writeI32(self.reqSeq)
            op.writeFieldEnd()
        if self.roomId is not None:
            op.writeFieldBegin('roomId', 0x0b, 2)
            op.writeString(self.roomId.encode('utf-8') if sys.version_info[0] == 2 else self.roomId)
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)
    
    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)

class OutRoomResult(object):

    def __init__(self, e=None):
        self.e = e

    def read(self, ip):
        ip.readStructBegin()
        while 1:
            (P, M, D) = ip.readFieldBegin()
            if M == 0x00:
                break
            if D == 1:
                if M == 0x0c:
                    self.e = TalkException()
                    self.e.read(ip)
                else:
                    ip.skip(M)
            else:
                ip.skip(M)
            ip.readFieldEnd()
        ip.readStructEnd()

    def write(self, op):
        op.writeStructBegin('leaveRoom_result')
        if self.e is not None:
            op.writeFieldBegin('e', 0x0c, 1)
            self.e.write(op)
            op.writeFieldEnd()
        op.writeFieldStop()
        op.writeStructEnd()

    def __str__(self) -> str:return repr(self)
    
    def __repr__(self) -> ReprPMD:return ReprPMD(self).repr

    def __eq__(self, other:object) -> bool:return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other:object) -> bool:return not (self == other)