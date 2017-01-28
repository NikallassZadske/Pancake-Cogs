import discord
from discord.ext import commands


class barbaric:
    """Absolutely"""

    def __init__(self, bot):
        self.bot = bot
        self.image = "data/barbaric/barbaric.jpg"

    @commands.command(pass_context=True)
    async def barbaric(self, ctx):
        """Barbaric"""

        # code
        channel = ctx.message.channel
        await self.bot.send_file(channel, self.image)

    async def listener(self, message):
        if message.author.id != self.bot.user.id:
            if 'barbaric' in message.content.lower():
                await self.bot.send_file(channel, self.image)


def setup(bot):
    n = barbaric(bot)
    bot.add_listener(n.listener, "on_message")
    bot.add_cog(n)