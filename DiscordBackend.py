import discord
import asyncio
try:
    from tokens.discord_config import *
except ModuleNotFoundError:
    enable = False


text_function = NotImplementedError
client = discord.Client()


# this is a hack solution, those two lines need to be called from the main Thread, to prepare asyncio framework.
loop = asyncio.get_event_loop()
if enable:
    loop.create_task(client.start(TOKEN))


def run():
    loop.run_forever()


def register_text_endpoint(_message_function):
    global text_function
    text_function = _message_function


@client.event
async def on_message(message: discord.message.Message):
    if message.author == client.user: return  # ignore self ## this fixes looping on response to self
    if message.author.bot: return  # ignore all bots ## this also fixes two bots replying to each other
    # async with message.typing():
    response = text_function(message.content, str(message.author))
    await message.channel.send(response)


if __name__ == "__main__":
    # in this version there is no main code for the bot to serve, testing response will be moved here later.
    def testing_message_function(message, author):
        response = "Hey " + author + "!\nDidn't see you coming there...\n U-uh what do you mean \""+message+"\"?"
        return response

    register_text_endpoint(testing_message_function)
    run()
