import discord
import asyncio

try:
    from tokens.discord_config import *
except ModuleNotFoundError:
    enable = False

client = discord.Client()

# this is a hack solution, those two lines need to be called from the main Thread, to prepare asyncio framework.
loop = asyncio.get_event_loop()
if enable:
    loop.create_task(client.start(TOKEN))


def run():
    loop.run_forever()


def unconfigured(*args, **kwargs):
    return None


text_function = unconfigured


def register_text_endpoint(_message_function):
    global text_function
    text_function = _message_function


@client.event
async def on_message(message: discord.message.Message):
    if text_function is unconfigured \
            or message.author == client.user \
            or (ignore_other_bots and message.author.bot) \
            or (not message.content.startswith(prefix)):
        # ignores when user_code didn't attach a text_function,
        # ignores when attempting to respond to ourself,
        # ignores other bots when ignore_other_bots set to True in discord_config.py,
        # ignores when message doesn't match the prefix defined in discord_config.py
        return

    async with message.channel.typing():
        response = await loop.run_in_executor(None, text_function, message.content[len(prefix):], str(message.author))
    if response is None:
        return  # displays an awkward 'bot is typing' for a few seconds, and then changes mind and doesn't answer.
    await message.channel.send(response)


if __name__ == "__main__":
    # in this version there is no main code for the bot to serve, testing response will be moved here later.
    def testing_message_function(message, author):
        response = "Hey " + author + "!\nDidn't see you coming there...\n U-uh what do you mean \"" + message + "\"?"
        return response


    register_text_endpoint(testing_message_function)
    run()
