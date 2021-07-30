from random import randint, choice
import discord
from discord.ext import commands

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

Use a dictionary with all the exceptions for F=MA Solutions stored in an array
storing the second or third question in a combined diagram, send back to first
'''
exceptions = {
    '2008': [5, 11],
    '2009': [3, 9, 22],
    '2010': [2, 3, 16, 19, 20],
    '2011': [3, 4, 17, 20],
    '2012': [7],
    '2013': [6, 9, 20, 21, 24],
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
source_questions = {
    '20084': 'https://i0.wp.com/kevinshuang.com/wp-content/uploads/2016/07/2008-4.png?resize=639%2C387&ssl=1',
    '200810': 'https://i2.wp.com/kevinshuang.com/wp-content/uploads/2016/07/2008-10.png?resize=639%2C295&ssl=1',
    '20092': '',
    '20098': '',
    '200921': '',
    '20101': '',
    '201015': '',
    '201018': '',
    '20112': '',
    '201116': '',
    '201119': '',
    '20126': '',
    '20135': '',
    '20138': '',
    '201319': '',
    '201323': ''
}

kin = [line.strip() for line in open('categories/physics/Kinematics.txt')]
dyn = [line.strip() for line in open('categories/physics/Dynamics.txt')]
nrg = [line.strip() for line in open('categories/physics/Energy.txt')]
col = [line.strip() for line in open('categories/physics/Collisions.txt')]
som = [line.strip() for line in open('categories/physics/System_Of_Masses.txt')]
rb = [line.strip() for line in open('categories/physics/Rigid_Bodies.txt')]
osc = [line.strip() for line in open('categories/physics/Oscillatory_Motion.txt')]
gra = [line.strip() for line in open('categories/physics/Gravity.txt')]
flu = [line.strip() for line in open('categories/physics/Fluids.txt')]
misc = [line.strip() for line in open('categories/physics/Miscellaneous.txt')]


async def prob(ctx, year: str, question: int):
    path = 'Exams/fma/%s/%d.webp' % (year, question)
    file = discord.File(path, filename='image.webp')

    if question in exceptions[year]:
        if question - 1 in exceptions[year]:
            embed = discord.Embed(
                title='%s F=MA Question %d' % (year, question),
                description='[Solution](https://kevinshuang.com/%s-problem-%d)' % (year, question - 2),
                color=discord.Colour.blue()
            )
            embed.set_image(url="attachment://image.webp")
            embed.set_thumbnail(url=source_questions[year + str(question - 2)])
            await ctx.send(file=file, embed=embed)
        else:
            embed = discord.Embed(
                title='%s F=MA Question %d' % (year, question),
                description='[Solution](https://kevinshuang.com/%s-problems-%d-%d)' % (
                    year, question - 1, question),
                color=discord.Colour.blue()
            )
            embed.set_image(url="attachment://image.webp")
            embed.set_thumbnail(url=source_questions[year + str(question - 1)])
            await ctx.send(file=file, embed=embed)
    else:
        embed = discord.Embed(
            title='%s F=MA Question %d' % (year, question),
            description='[Solution](https://kevinshuang.com/%s-problem-%d)' % (year, question),
            color=discord.Colour.blue()
        )
        embed.set_image(url="attachment://image.webp")
        await ctx.send(file=file, embed=embed)


class AAPTCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='fma')
    async def fma_prob(self, ctx):
        year, question = str(2008), randint(1, 25)
        year = year + choice('A', 'B') if year == '2020' else year

        await prob(ctx, year, question)

    @commands.command(name='pcp')
    async def fma_cat(self, ctx, cat):
        version, year, question = ..., ..., ...  # str
        if cat == 'kin':
            i = randint(0, len(kin) - 1)
            version, year, question = kin[i][0:1], kin[i][1:5], kin[i][5:]

        year = year + version if year == '2020' else year
        await prob(ctx, year, int(question))


def setup(bot):
    bot.add_cog(AAPTCog(bot))
