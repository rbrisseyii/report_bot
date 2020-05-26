import re
import string
from pprint import pprint

from botbuilder.core import TurnContext
from botbuilder.core.teams import TeamsActivityHandler


class ReportBot(TeamsActivityHandler):
    def __init__(self, app_id: str, secret: str):
        self._app_id = app_id
        self._secret = secret

    async def on_message_activity(self, turn_context: TurnContext):
        print(f'Message activity detected.')
        pprint(f'activity: {turn_context.activity}')
        TurnContext.remove_recipient_mention(turn_context.activity)

        # Remove punctuation and spaces
        regex = re.compile('[%s]' % re.escape(string.punctuation))
        text = regex.sub('', turn_context.activity.text)
        text = text.strip()
        print(text)
