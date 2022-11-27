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

from flask import Flask, request

from dooray.slash_command import Message

app = Flask(__name__)


class Client:
    def __init__(self):
        self._token = None
        self._commands = {}

    def command(self, command_name=''):
        def wrapper(command_func):
            self._commands[command_name or command_func.__name__] = command_func
            return command_func
        return wrapper

    def run(self, token):
        self._token = token

        @app.route('/<command>', methods=['POST'])
        def route_command(command):
            body = request.get_json()

            if body['appToken'] != token:
                print('[Error] Token is not valid with this request')
                return ''

            request_body = self._commands[command](body)

            if type(request_body) is str:
                return Message(text=request_body).send()

            return request_body

        app.run()
