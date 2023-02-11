from wtfix.message import admin

logon_msg = admin.LogonMessage("testmm1fixoe", "testmm1fixoe", heartbeat_int=30)

print(str(logon_msg))

f"{logon_msg:t}"

# Example of getting the message type
logon_msg.type


# Example of getting the message type name
logon_msg.name


# Look up the sequence number
logon_msg.seq_num
