from random import randint, choice
import discord
from discord.ext import commands

# Use a dictionary with all the exceptions for F=MA Solutions stored in an array
# storing the second or third question in a combined diagram, send back to first
exceptions = {
    '2008': [5, 11],
    '2009': [3, 9, 22],
    '2010': [2, 3, 16, 19, 20],  # 1, 2, 3 are a triple, 18, 19, 20 are a triple
    '2011': [3, 4, 17, 20],  # 2, 3, 4 are a triple
    '2012': [7],
    '2013': [6, 9, 20, 21, 24],  # 19, 20, 21 are a triple
    '2014': [],
    '2015': [],
    '2016': [],
    '2017': [],
    '2018': [],
    '2019': [],
    '2020A': [],
    '2020B': [],
    '2021': []
}


class AAPTCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    '''
    He combined a few questions per exam bc of combined questions on the exam itself, gotta take care of that

    2008    : 4/5 10/11
    2009    : 2/3 8/9 21/22
    2010    : 1/2/3 15/16 18/19/20
    2011    : 2/3/4 16/17 19/20
    2012    : 6/7
    2013    : 5/6 8/9 19/20/21 23/24

    rest tbd later lmao
    2014    : 
    2015    : 
    2016    : 
    2017    : 
    2018    : 
    2019    : 
    2020A   : 
    2020B   : 
    2021    : 
    '''
    @commands.command(name='fma')
    async def fma_prob(self, ctx):
        year, question = 2008, randint(1, 25)
        year = year + choice('A', 'B') if year == 2020 else year  # 2020 was the only year to have 2 versions
        path = 'Exams/F=MA/%s/%d.webp' % (str(year), question)
        file = discord.File(path, filename='image.webp')
        embed = discord.Embed(
            title='%s F=MA Question %d' % (year, question),
            description='[Solution](https://kevinshuang.com/%s-problem-%d)'
                        % (year, question),
            color=discord.Colour.blue()
        )
        embed.set_image(url="attachment://image.webp")
        await ctx.send(file=file, embed=embed)


def setup(bot):
    bot.add_cog(AAPTCog(bot))
