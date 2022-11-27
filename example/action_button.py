from dooray.slash_command import Client, Message
from token import TOKEN

client = Client()


@client.command('choose')
def choose(context):
    return Message(text='hello world!', in_channel=True).send()


client.run(TOKEN)
