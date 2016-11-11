from discord.ext import commands
from cogs.utils import checks
from cogs.utils.chat_formatting import pagify
from cogs.utils.chat_formatting import box
from subprocess import check_output, CalledProcessError
from platform import system, release

class Terminal:
    """Terminal inside Discord"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @checks.is_owner()
    async def os(self):
        """Displays your current Operating System"""

        await self.bot.say(box(system() + "\n" + release(), 'Bash'))

    @commands.command()
    @checks.is_owner()
    async def osname(self):
        """Displays your current Operating System name"""

        await self.bot.say(box(system(), 'Bash'))

    @commands.command()
    @checks.is_owner()
    async def osversion(self):
        """Displays your current Operating System version"""

        await self.bot.say(box(release(), 'Bash'))

    @commands.command(name="shell")
    @checks.is_owner()
    async def _terminal_(self, *, command : str):
        """Terminal inside Discord"""

        try:
            output = check_output(command, shell=True)
        except CalledProcessError as e:
            output = e.output

        shell = output.decode('utf_8')
        if shell == "":
            shell = "No Output recieved from '{}'".format(command)

        for page in pagify(shell, ["\n"], shorten_by=11, page_length=2000):
            await self.bot.say(box(page, 'Bash'))

def setup(bot):
    n = Terminal(bot)
    bot.add_cog(n)
