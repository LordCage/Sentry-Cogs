from discord.ext import commands
from random import choice
from __main__ import settings

class Nep:
    "Nep Nep [Discontinued]"
    def __init__(self, bot):
        self.bot = bot


    @commands.command(no_pm=True)
    async def nep(self):
        """Displays a random Nep. [Discontinued]"""

        if settings.owner == "137268543874924544":
            await self.bot.say("```Please stop putting my bot through this```")
        else:
            nep = ["http://i.imgur.com/13hoMVJ.jpg", "http://i.imgur.com/kIzXdwN.jpg", "http://i.imgur.com/DICh64t.jpg", "http://i.imgur.com/nMp3NMp.png", "http://i.imgur.com/MMf1YfR.png", "http://i.imgur.com/CGABJEs.jpg", "http://i.imgur.com/GRz1oCo.jpg"]
            nep = choice(nep)
            await self.bot.say(nep)

def setup(bot):
    n = Nep(bot)
    bot.add_cog(n)
