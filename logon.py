from wtfix.apps.base import MessageTypeHandlerApp, on
# from wtfix.apps.admin import AuthenticationApp
# from wtfix.pipeline import BasePipeline
from wtfix.conf import settings
from wtfix.message import admin
from wtfix.protocol.contextlib import connection
import logging
# import os


logger = settings.logger

class SecretAlgoTradingRecipe(MessageTypeHandlerApp):

    @on(connection.protocol.MsgType.Logon)  # Only invoked when 'Logon (type A)' messages are received.
    def on_logon(self, message):
        # self.send_security_definition_request()
        return message

    def on_receive(self, message):  # Invoked for every type of message.
      logger.info(f"Received message {message}!")
      

# WTFIX_SETTINGS_MODULE=config.settings.local
# settings
logging.basicConfig(level=logging.INFO)
logon_msg = admin.LogonMessage()
print(logon_msg)
logon_msg.ResetSeqNumFlag = True
logging.info(f"TIME_ZONE == {settings.TIME_ZONE}")
logging.info(f"BEGIN_STRING == {settings.BEGIN_STRING}")

logging.info(type(settings))
logging.info(dir(settings))


SecretAlgoTradingRecipe.start
MessageTypeHandlerApp.start

    # setting_value = getattr(settings, set)
    # logging.info(f"setting == {set, setting_value}")

# print(settings.WTFIX_SETTINGS_MODULE)

# from dotenv import load_dotenv
# load_dotenv(dotenv_path=env_path)

# my_instance = AuthenticationApp(BasePipeline, settings.WTFIX_SETTINGS_MODULE)
# value = my_instance.on_logon(logon_msg)
# my_instance.initialize()
