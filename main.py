import discord
from discord.ext import commands
from random import randint, choice

TOKEN = ''
client = commands.Bot(command_prefix='?')

alg = [line.strip() for line in open('categories/Algebra.txt')]
geo = [line.strip() for line in open('categories/Geometry.txt')]
nt = [line.strip() for line in open('categories/NumberTheory.txt')]
pr = [line.strip() for line in open('categories/Probability.txt')]

'''
TODO

provide a problem based on its category
format the txts like this: 102020A4
level, then year, then version, then question num


'''


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.command(pass_context=True, aliases=['pr'])
async def rand_prob(ctx, level):
    try:
        if level == '10' or level == '12':
            year, version, question = randint(2002, 2021), choice(('A', 'B')), randint(1, 25)
            path = 'AMC/%d/%d/%s/%d.png' % (int(level), year, version, question)
            file = discord.File(path, filename='image.png')
            embed = discord.Embed(
                title='AMC ' + version + ' Problem',
                description='%d AMC %d%s Question %d' % (year, int(level), version, question),
                color=discord.Colour.blue()
            )
            embed.set_image(url="attachment://image.png")
            await ctx.send(file=file, embed=embed)
        else:
            await ctx.send("Invalid Version")
    except ValueError:
        await ctx.send("Invalid Version")


# User inputs should be alg, geo, nt, pr
@client.command(name='pc')
async def cat_prob(ctx, cat):
    if cat == 'alg':
        i = randint(0, len(alg) - 1)
        level, year, version, question = alg[i][0:2], alg[i][2:6], alg[i][6:7], alg[7:]
        await cat_problem(ctx, level, year, version, question)

    if cat == 'geo':
        i = randint(0, len(geo) - 1)
        level, year, version, question = geo[i][0:2], geo[i][2:6], geo[i][6:7], geo[7:]
        await cat_problem(ctx, level, year, version, question)

    if cat == 'nt':
        i = randint(0, len(nt) - 1)
        level, year, version, question = nt[i][0:2], nt[i][2:6], nt[i][6:7], nt[7:]
        await cat_problem(ctx, level, year, version, question)

    if cat == 'pr':
        i = randint(0, len(pr) - 1)
        level, year, version, question = pr[i][0:2], pr[i][2:6], pr[i][6:7], pr[7:]
        await cat_problem(ctx, level, year, version, question)


async def cat_problem(ctx, level, year, version, question):
    path = 'AMC/%s/%s/%s/%s.png' % (level, year, version, question)
    file = discord.File(path, filename='image.png')
    embed = discord.Embed(
        title='AMC ' + version + ' Problem',
        description='%s AMC %s%s Question %s' % (year, level, version, question),
        color=discord.Colour.blue()
    )
    embed.set_image(url="attachment://image.png")

    await ctx.send(embed=embed)


client.run(TOKEN)
