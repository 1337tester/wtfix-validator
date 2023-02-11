from wtfix.apps.base import MessageTypeHandlerApp, on
from wtfix.conf import settings

logger = settings.logger

class SecretAlgoTradingRecipe(MessageTypeHandlerApp):

    @on(context.protocol.MsgType.Logon)  # Only invoked when 'Logon (type A)' messages are received.
    def on_logon(self, message):
        self.send_security_definition_request()
        return message

    def on_receive(self, message):  # Invoked for every type of message.
      logger.info(f"Received message {message}!")
      
      
new