import datetime
from datetime import date
import discord
from discord.ext import commands


class XmasClock:
    """Simple display of days left until next xmas"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def блинблинский(self):
        """Display days left 'til xmas"""

        now = datetime.datetime.now()
        today = date(now.year, now.month, now.day)

        year = now.year
        if (now.month == 12 and now.day > 31):
            year = now.year + 1

        xmasday = date(2018, 1, 1)

        delta = xmasday - today

        await self.bot.say("```до нового года " + str(delta.days) + " дней!```")


def setup(bot):
    bot.add_cog(XmasClock(bot))
