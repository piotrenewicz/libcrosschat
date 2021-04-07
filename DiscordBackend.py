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
full_function = unconfigured


def register_text_endpoint(_text_function):
    global text_function
    text_function = _text_function


def register_full_endpoint(_full_function):
    global full_function
    full_function = _full_function


@client.event
async def on_message(message: discord.message.Message):
    if message.author == client.user \
            or (ignore_other_bots and message.author.bot) \
            or (not message.content.startswith(prefix)):
        # ignores when attempting to respond to ourself,
        # ignores other bots when ignore_other_bots set to True in discord_config.py,
        # ignores when message doesn't match the prefix defined in discord_config.py
        return

    if text_function is not unconfigured:
        await dispatch_text(message)
    if full_function is not unconfigured:
        await dispatch_full(message)


async def dispatch_text(message: discord.message.Message):
    async with message.channel.typing():
        response = await loop.run_in_executor(None, text_function, message.content[len(prefix):], str(message.author))
    if response is None:
        return  # displays an awkward 'bot is typing' for a few seconds, and then changes mind and doesn't answer.
    await message.channel.send(response)


async def dispatch_full(message: discord.message.Message):
    def nagger(content):
        perform_nag(message.channel, content)

    await loop.run_in_executor(None, full_function, ("DC", message.channel.id), message.content[len(prefix):], str(message.author), nagger)


def perform_nag(channel: discord.message.Message.channel, content):
    asyncio.run_coroutine_threadsafe(channel.send(content), loop)


if __name__ == "__main__":
    import time

    def testing_message_function(message: str, author: str):
        if not message.startswith("text"):
            return
        response = "Hey " + author + "!\nDidn't see you coming there...\n U-uh what do you mean \"" + message + "\"?"
        return response

    def testing_nagging_function(platform, room_id, message: str, author: str, nagger):
        if not message.startswith("nagger"):
            return
        time.sleep(2)
        nagger("oh no "+author+" you've become a victim to a nagger function!")
        time.sleep(1)
        nagger("and it was just sending that \n\""+message+"\"\n that got you here")
        time.sleep(5)
        nagger("Now now, don't #panik.\nYou're lucky, this is nagger is only going to count up to 60 before giving up!")
        time.sleep(10)
        nagger("oh here it goes...")
        for i in range(60):
            nagger(str(i+1))
            time.sleep(1)


    register_text_endpoint(testing_message_function)
    register_full_endpoint(testing_nagging_function)
    run()
