class Processor:
    def __init__(self):
        self._message = None
        self._context = None

    def run(self, mess, context, respondent, client):
        self._message = mess
        self._context = context

        mess_wrapper = respondent.make_unknow_mess()

        if self._message.intent == 'help':
            mess_wrapper = respondent.make_help_message()
        elif self._message.intent == 'view':
            if self._message.entity == 'rule':
                mess_wrapper = respondent.make_rule_message()
            else:
                channels, _ = self._get_channel_list(client)
                mess_wrapper = respondent.make_channel_list(channels)
        elif self._message.intent == 'ask':
            if self._message.entity == 'change language':
                mess_wrapper = respondent.make_change_language_instruction()

        respondent.send_message(mess_wrapper, context)

    @staticmethod
    def _get_channel_list(client):
        channels = []

        res = client.api_call('channels.list')
        if res and res['ok']:
            channels = res['channels']

        return channels, len(channels)
