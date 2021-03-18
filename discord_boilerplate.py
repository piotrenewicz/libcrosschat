import discord

token = "ODE5MjU3MDU4ODQzMDMzNjEx.YEj-lw.ZaxAr0iPPXwMqlJUkqv-lswW-ik"

client = discord.Client()


@client.event
async def on_message(message: discord.message.Message):
    print(message.content)
    print(type(message))
    # FIXME looping on response to self
    if message.author == client.user: return  # ignore self
    if message.author.bot: return  # ignore all bots
    await message.channel.send("responding to message " + message.content)


# run after
client.run(token)
