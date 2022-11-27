from dooray import slash_command
from token import TOKEN

client = slash_command.Client()


@client.command('hello')
def hello_world():
    return 'hello world!'


client.run(TOKEN)
