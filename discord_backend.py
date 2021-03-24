import discord
try:
    from tokens.discord_config import *
except ModuleNotFoundError:
    enable = False


text_function = None
client = discord.Client()


def run():
    if enable:
        client.run(TOKEN)  # this is probably blocking, will require threading.


def register_text_endpoint(_message_function):
    global text_function
    text_function = _message_function


@client.event
async def on_message(message: discord.message.Message):
    if message.author == client.user: return  # ignore self ## this fixes looping on response to self
    if message.author.bot: return  # ignore all bots ## this also fixes two bots replying to each other

    response = text_function(message.content, message.author)
    await message.channel.send(response)


if __name__ == "__main__":
    # in this version there is no main code for the bot to serve, testing response will be moved here later.
    def testing_message_function(message, author):
        response = "Hey " + author + "!\nDidn't see you coming there...\n U-uh what do you mean \""+message+"\"?"
        return response

    register_text_endpoint(testing_message_function)
    run()
