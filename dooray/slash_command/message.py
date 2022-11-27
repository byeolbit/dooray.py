"""
The MIT License (MIT)

Copyright (c) 2022~present Yeonwoo Jo

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""


class Message:
    def __init__(self, text, in_channel=False, send_type='new'):
        self.text = text
        self.response_type = 'inChannel' if in_channel else 'ephemeral'
        self.send_type = send_type
        self.attachments = []
        # self._tenantId = context.get('tenantId')
        # self._tenantDomain = context.get('tenantDomain')
        # self._channelName = context.get('channelName')
        # self._channelId = context.get('channelId')

    def add_attachment(self, context, text, title, title_link, author_name, author_link, fields, actions, callbackId,
                       imageUrl, thumbUrl, color):
        return {}

    def send(self):
        message = {'text': self.text, 'responseType': self.response_type}
        if self.send_type is 'replace':
            message['replaceOriginal'] = True
        if self.send_type is 'delete':
            message['deleteOriginal'] = True

        if len(self.attachments) > 0:
            message['attachments'] = self.attachments

        return message
