import discord
import tokens.discord_config

if tokens.discord_config.enable:
    client = discord.Client()

    @client.event
    async def on_message(message: discord.message.Message):
        print(message.content)
        print(type(message))
        if message.author == client.user: return  # ignore self ## this fixes looping on response to self
        if message.author.bot: return  # ignore all bots ## this also fixes two bots replying to each other
        await message.channel.send("responding to message " + message.content)

    if __name__ == "__main__":
        pass  # in this version there is no main code for the bot to serve, testing response will be moved here later.

    client.run(tokens.discord_config.TOKEN)  # this is probably blocking, will require threading.
