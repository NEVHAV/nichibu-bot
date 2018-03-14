COMMANDS = '''
@Nichibu Bot *help* xem danh sách các lệnh
@Nichibu Bot *channel* xem danh sách các channel
@Nichibu Bot *change language* thay đổi ngôn ngữ slack
@Nichibu Bot *rule* xem quy định trên slack Nichibu Inc.
'''
CHANNEL_INFO = '*<#{}>* {} · _{} members_\n'


class Respondent:
    def __init__(self, sender):
        self._sender = sender

    @staticmethod
    def make_unknow_mess():
        default_response = "Not sure what you mean. Try @Nichibu Bot *{}*.".format('help')
        return {
            'type': 'text',
            'content': default_response
        }

    @staticmethod
    def make_help_message():
        content = [
            {
                'pretext': u'Bạn có thể sử dụng các lệnh',
                'text': COMMANDS,
                'color': '#7CD197'
            }
        ]
        return {
            'type': 'attachments',
            'content': content
        }

    @staticmethod
    def make_greeting_message(member_id):
        greeting_text = u'Chào mừng <@{}> tham gia slack Nichibu Inc. :tada:\n'.format(member_id)
        commands = u'Gọi tôi khi bạn cần trợ giúp\n' + COMMANDS
        content = [
            {
                'pretext': greeting_text,
                'text': commands,
                'color': '#7CD197'
            }
        ]
        return {
            'type': 'attachments',
            'content': content
        }

    @staticmethod
    def make_channel_list(channels):
        mess = ''
        for c in channels:
            id = c['id']
            name = c['name']
            purpose = c['purpose']['value']
            if len(name) + len(purpose) > 67:
                purpose = purpose[:64 - len(name)].strip()
                while purpose[-1] in ".,-:;":
                    purpose = purpose[:-1]
                purpose += '...'
            members = c['members']
            is_private = c['is_private']
            is_archived = c['is_archived']
            if not is_private and not is_archived:
                mess += CHANNEL_INFO.format(id, purpose, len(members))
        content = [
            {
                'pretext': 'Danh sách channel',
                'text': mess,
                'color': '#7CD197'
            }
        ]
        return {
            'type': 'attachments',
            'content': content
        }

    @staticmethod
    def make_rule_message():
        name_convention = u'Sử dụng tên mà mọi người thường gọi bạn (Tên thật, tên Facebook...)\n' \
                          u'Bạn có thể cho thêm khóa học vào phía trước tên: K51 Nichibu'
        channel_comment = 'Hãy chỉ vào tin nhắn rồi chọn *Start a thread* hoặc *Reply to thread*'
        content = [
            {
                'pretext': u'*Quy tắc đặt tên*',
                'text': name_convention,
                'color': '#7CD197'
            },
            {
                'pretext': u'*Trả lời một tin nhắn*',
                'text': channel_comment,
                'color': '#7CD197'
            }
        ]
        return {
            'type': 'attachments',
            'content': content
        }

    @staticmethod
    def make_change_language_instruction():
        content = [
            {
                'pretext': u'Cách chuyển ngôn ngữ',
                'text': 'Truy cập link: https://nichibu.slack.com/account/settings',
                'color': '#7CD197'
            }
        ]
        return {
            'type': 'attachments',
            'content': content
        }

    def send_message(self, mess_wrapper, context):
        if mess_wrapper['type'] == 'attachments':
            self._sender.api_call(
                "chat.postMessage",
                channel=context['channel'],
                attachments=mess_wrapper['content']
            )
        elif mess_wrapper['type'] == 'text':
            self._sender.api_call(
                "chat.postMessage",
                channel=context['channel'],
                text=mess_wrapper['content']
            )
