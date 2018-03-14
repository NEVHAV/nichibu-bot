import os
import time
import re

from slackclient import SlackClient
from nichibubot.respondent.respondent import Respondent
from nichibubot.translator.translator import Translator
from nichibubot.processor.processor import Processor

slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
nichibot_id = None

# constants
RTM_READ_DELAY = 0.5  # 1 second delay between reading from RTM
MENTION_REGEX = "^<@(|[WU].+?)>(.*)"
GENERAL_CHANNEL = 'C9M5GRPLG'

response = Respondent(slack_client)
translator = Translator()
processor = Processor()


def parse_bot_commands(slack_events):
    """
        Parses a list of events coming from the Slack RTM API to find bot commands.
        If a bot command is found, this function returns a tuple of command and channel.
        If its not found, then this function returns None, None.
    """
    for event in slack_events:
        context = event

        if event["type"] == "message" and not "subtype" in event:
            user_id, message = parse_direct_mention(event["text"])
            if user_id == nichibot_id:
                mess = translator.parse_message(message).message
                return processor.run(mess, context, response, slack_client)

        elif event["type"] == "member_joined_channel":
            message_wraper = response.make_greeting_message(event['user'])
            return response.send_message(message_wraper, context)

    return None, None


def parse_direct_mention(message_text):
    """
        Finds a direct mention (a mention that is at the beginning) in message text
        and returns the user ID which was mentioned. If there is no direct mention, returns None
    """
    matches = re.search(MENTION_REGEX, message_text)
    # the first group contains the username, the second group contains the remaining message
    return (matches.group(1), matches.group(2).strip()) if matches else (None, None)


if __name__ == '__main__':
    if slack_client.rtm_connect(with_team_state=False):
        print('Nichibu bot connected and running.')
        nichibot_id = slack_client.api_call('auth.test')["user_id"]

        while True:
            parse_bot_commands(slack_client.rtm_read())
            time.sleep(RTM_READ_DELAY)
    else:
        print("Connection failed. Exception traceback printed above.")
