from .message import Message

MENTION_REGEX = "^<@(|[WU].+?)>(.*)"


class Translator:
    def __init__(self):
        self._message = None

    def parse_message(self, message):
        self._message = Message(message)

        words = self._message.text.split(' ')
        if words[0] == 'help':
            self._message.set_intent('help')
        elif words[0] == 'channel':
            self._message.set_intent('view')
            self._message.set_entity('channel list')
        elif words[0] == 'rule':
            self._message.set_intent('view')
            self._message.set_entity('rule')
        elif words[0] == 'change':
            self._message.set_intent('ask')
            self._message.set_entity('change language')

        return self

    @property
    def message(self):
        return self._message
