#Shishir Khanal
#06-14-2025
#Echo bot that uses azure AI Language to run sentiment analysis

from .echo_bot import EchoBot
from botbuilder.core import ActivityHandler, MessageFactory, TurnContext
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from config import DefaultConfig

#Supply keys to connect with Azure
CONFIG = DefaultConfig()
credential = AzureKeyCredential(CONFIG.API_KEY)
endpointURI = CONFIG.ENDPOINT_URI
text_analytics_client = TextAnalyticsClient(endpoint=endpointURI, credential=credential)

class EchoBotSentimentAnalysis(EchoBot):

    async def on_message_activity(self, turn_context: TurnContext):
        input = turn_context.activity.text
        print(f"textTouse = {input}")
        documents = [{"id": "1", "language":"en","text":input}]
        response = text_analytics_client.analyze_sentiment(documents)
        successful_responses = [doc for doc in response if not doc.is_error]
        output = successful_responses
        return await turn_context.send_activity(
            MessageFactory.text(f"Echo: {output}")
        )