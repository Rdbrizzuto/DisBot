import discord
import responses


async def send_message(message, user_message):
    try:
        response = responses.get_response(user_message)
        print(response)
        await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = ''                                        #INSERT DISCORD API TOKEN HERE AS A STRING
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents = intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said "{user_message}" in {channel}')


        await send_message(message, user_message)

    
    client.run(TOKEN)