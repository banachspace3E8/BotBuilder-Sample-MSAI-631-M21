#Shishir Khanal
#06-08-2025
#Echo bot that prints the string reversed

from .echo_bot import EchoBot
from botbuilder.core import ActivityHandler, MessageFactory, TurnContext

class EchoBotReverseString(EchoBot):

    async def on_message_activity(self, turn_context: TurnContext):
        input = turn_context.activity.text
        output = input[::-1]
        return await turn_context.send_activity(
            MessageFactory.text(f"Echo: {output}")
        )