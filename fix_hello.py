from wtfix.message import admin
from wtfix.conf import settings
from wtfix.apps.base import MessageTypeHandlerApp, on


logger = settings.logger
logon_msg = admin.LogonMessage("testmm1fixoe", "testmm1fixoe", heartbeat_int=30)




print(str(logon_msg))

f"{logon_msg:t}"


mes = MessageTypeHandlerApp
print(dir(mes))
mes.initialize

# Example of getting the message type
logon_msg.type


# Example of getting the message type name
logon_msg.name


# Look up the sequence number
logon_msg.seq_num
