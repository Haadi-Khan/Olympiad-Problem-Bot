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
2014    : 12/13 23/24
2015    : 7/8 9/10 12/13 14/15 19/20
2016    : 5/6 14/15 21/22  
2017    : 20/21/22
2018A   :
2018B   : 
2019A   :
2019B   : 16/17
2020A   : 9/10
2020B   : 9/10
2021    : 1/2

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
    '2014': [13, 24],
    '2015': [8, 10, 13, 15, 20],
    '2016': [6, 15, 22],
    '2017': [8, 12, 15, 21, 22],
    '2018A': [],
    '2018B': [],
    '2019A': [],
    '2019B': [17],
    '2020A': [10],
    '2020B': [10],
    '2021': [2]
}
source_questions = {
    '20084': 'https://i0.wp.com/kevinshuang.com/wp-content/uploads/2016/07/2008-4.png?resize=639%2C387&ssl=1',
    '200810': 'https://i2.wp.com/kevinshuang.com/wp-content/uploads/2016/07/2008-10.png?resize=639%2C295&ssl=1',
    '20092': 'https://i0.wp.com/kevinshuang.com/wp-content/uploads/2016/07/2009-2.png?resize=639%2C282&ssl=1',
    '20098': 'https://i2.wp.com/kevinshuang.com/wp-content/uploads/2016/07/2009-8.png?resize=639%2C416&ssl=1',
    '200921': 'https://i0.wp.com/kevinshuang.com/wp-content/uploads/2016/07/2009-21.png?resize=639%2C398&ssl=1',
    '20101': 'https://i0.wp.com/kevinshuang.com/wp-content/uploads/2016/07/2010-1.png?resize=639%2C338&ssl=1',
    '201015': 'https://i0.wp.com/kevinshuang.com/wp-content/uploads/2016/07/2010-15.png?resize=639%2C352&ssl=1',
    '201018': 'https://i1.wp.com/kevinshuang.com/wp-content/uploads/2016/07/2010-18.png?resize=639%2C802&ssl=1',
    '20112': 'https://i0.wp.com/kevinshuang.com/wp-content/uploads/2016/07/2011-2.png?resize=639%2C329&ssl=1',
    '201116': 'https://i0.wp.com/kevinshuang.com/wp-content/uploads/2016/07/2011-16.png?resize=639%2C368&ssl=1',
    '201119': 'https://i2.wp.com/kevinshuang.com/wp-content/uploads/2016/07/2011-19.png?resize=639%2C240&ssl=1',
    '20126': 'https://i1.wp.com/kevinshuang.com/wp-content/uploads/2016/07/2012-61.png?resize=639%2C496&ssl=1',
    '20135': 'https://i0.wp.com/kevinshuang.com/wp-content/uploads/2016/07/2013-5.png?resize=639%2C466&ssl=1',
    '20138': 'https://i2.wp.com/kevinshuang.com/wp-content/uploads/2016/07/2013-8.png?resize=639%2C214&ssl=1',
    '201319': 'https://i0.wp.com/kevinshuang.com/wp-content/uploads/2016/07/2013-19.png?resize=639%2C198&ssl=1',
    '201323': 'https://i0.wp.com/kevinshuang.com/wp-content/uploads/2016/07/2013-23.png?resize=639%2C234&ssl=1',
    '201412': 'https://i0.wp.com/kevinshuang.com/wp-content/uploads/2016/07/2014-12.png?resize=639%2C477&ssl=1',
    '201423': 'https://i1.wp.com/kevinshuang.com/wp-content/uploads/2016/07/2014-23.png?resize=639%2C238&ssl=1',
    '20157': 'https://i2.wp.com/kevinshuang.com/wp-content/uploads/2016/07/2015-7.png?resize=639%2C346&ssl=1',
    '20159': 'https://i1.wp.com/kevinshuang.com/wp-content/uploads/2016/07/2015-9.png?resize=639%2C255&ssl=1',
    '201512': 'https://i1.wp.com/kevinshuang.com/wp-content/uploads/2016/07/2015-12.png?resize=639%2C233&ssl=1',
    '201514': 'https://i2.wp.com/kevinshuang.com/wp-content/uploads/2016/07/2015-14.png?resize=639%2C282&ssl=1',
    '201519': 'https://i2.wp.com/kevinshuang.com/wp-content/uploads/2016/07/2015-19.png?resize=639%2C272&ssl=1',
    '20165': 'https://i0.wp.com/kevinshuang.com/wp-content/uploads/2016/10/51.png?resize=639%2C561&ssl=1',
    '201614': 'https://i1.wp.com/kevinshuang.com/wp-content/uploads/2016/10/142.png?resize=639%2C533&ssl=1',
    '201621': 'https://i1.wp.com/kevinshuang.com/wp-content/uploads/2016/10/21-222.png?resize=639%2C421&ssl=1',
    '20177': 'https://i0.wp.com/kevinshuang.com/wp-content/uploads/2017/10/screen-shot-2017-10-14-at-9-18-50-pm.png?resize=639%2C403&ssl=1',
    '201711': 'https://i2.wp.com/kevinshuang.com/wp-content/uploads/2017/10/screen-shot-2017-10-14-at-9-20-49-pm.png?resize=639%2C519&ssl=1',
    '201714': 'https://i1.wp.com/kevinshuang.com/wp-content/uploads/2017/10/screen-shot-2017-10-14-at-9-21-20-pm.png?resize=639%2C364&ssl=1',
    '201720': 'https://i2.wp.com/kevinshuang.com/wp-content/uploads/2017/10/screen-shot-2017-10-14-at-9-22-32-pm.png?resize=639%2C242&ssl=1',
    '2019B16': 'https://i1.wp.com/kevinshuang.com/wp-content/uploads/2019/05/B16.png?resize=768%2C342&ssl=1',
    '2020A9': 'https://i0.wp.com/kevinshuang.com/wp-content/uploads/2020/08/a9.png?resize=768%2C145&ssl=1',
    '2020B9': 'https://i1.wp.com/kevinshuang.com/wp-content/uploads/2020/08/b9.png?resize=768%2C270&ssl=1',
    '20211': 'https://i1.wp.com/kevinshuang.com/wp-content/uploads/2021/04/1.png?resize=768%2C490&ssl=1',

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
                description='[Solution](https://kevinshuang.com/%s-problems-%d-%d)' % (year, question - 1, question),
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
        year, question = str(randint(2008, 2021)), randint(1, 25)
        year = year + choice(('A', 'B')) if year in ('2018', '2019', '2020') else year
        await prob(ctx, year, question)

    @commands.command(name='pcp')
    async def fma_cat(self, ctx, cat):
        ver, year, question = ..., ..., ...  # str
        if cat == 'kin':
            i = randint(0, len(kin) - 1)
            ver, year, question = kin[i][0:1], kin[i][1:5], kin[i][5:]

        if cat == 'dyn':
            i = randint(0, len(dyn) - 1)
            ver, year, question = dyn[i][0:1], dyn[i][1:5], dyn[i][5:]

        if cat == 'nrg':
            i = randint(0, len(nrg) - 1)
            ver, year, question = nrg[i][0:1], nrg[i][1:5], nrg[i][5:]

        if cat == 'col':
            i = randint(0, len(col) - 1)
            ver, year, question = col[i][0:1], col[i][1:5], col[i][5:]

        if cat == 'som':
            i = randint(0, len(som) - 1)
            ver, year, question = som[i][0:1], som[i][1:5], som[i][5:]

        if cat == 'rb':
            i = randint(0, len(rb) - 1)
            ver, year, question = rb[i][0:1], rb[i][1:5], rb[i][5:]

        if cat == 'osc':
            i = randint(0, len(osc) - 1)
            ver, year, question = osc[i][0:1], osc[i][1:5], osc[i][5:]

        if cat == 'gra':
            i = randint(0, len(gra) - 1)
            ver, year, question = gra[i][0:1], gra[i][1:5], gra[i][5:]

        if cat == 'flu':
            i = randint(0, len(flu) - 1)
            ver, year, question = flu[i][0:1], flu[i][1:5], flu[i][5:]

        if cat == 'misc':
            i = randint(0, len(misc) - 1)
            ver, year, question = misc[i][0:1], misc[i][1:5], misc[i][5:]



        year = year + ver if year in ('2018', '2019', '2020') else year
        await prob(ctx, year, int(question))


def setup(bot):
    bot.add_cog(AAPTCog(bot))
