from discord.ext import commands
import uuid
import os

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready(): print("Bot is online.")

@client.command()
async def download(ctx):
		messages = await ctx.message.channel.history(limit=200).flatten()
	
		for ms in messages:
			if len(ms.attachments) > 0:
				for atc in ms.attachments:
					imageName = str(uuid.uuid4())
					await atc.save(imageName)

		await ctx.message.delete()

client.run("BOT_TOKEN")
