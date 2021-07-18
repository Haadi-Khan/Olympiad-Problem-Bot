from random import randint, choice
import discord
from discord.ext import commands

TOKEN = [line.strip() for line in open('TOKEN.txt')][0]
client = commands.Bot(command_prefix='?')

e_alg = [line.strip() for line in open('categories/Easy/Algebra.txt')]
e_com = [line.strip() for line in open('categories/Easy/Combinatorics.txt')]
e_geo = [line.strip() for line in open('categories/Easy/Geometry.txt')]
e_nt = [line.strip() for line in open('categories/Easy/NumberTheory.txt')]

h_alg = [line.strip() for line in open('categories/Hard/Algebra.txt')]
h_com = [line.strip() for line in open('categories/Hard/Combinatorics.txt')]
h_geo = [line.strip() for line in open('categories/Hard/Geometry.txt')]
h_nt = [line.strip() for line in open('categories/Hard/NumberTheory.txt')]


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
                title='AMC ' + level + version + ' Problem',
                description='[Solution](https://artofproblemsolving.com/wiki/index.php/%d_AMC_%s%s_Problems/Problem_%d)' % (year, level, version, question),
                color=discord.Colour.blue()
            )
            embed.set_image(url="attachment://image.png")
            await ctx.send(file=file, embed=embed)
        else:
            await ctx.send("Invalid Version")
    except ValueError:
        await ctx.send("Invalid Version")


# Easy Questions
@client.command(name='pce')
async def cat_prob(ctx, cat):
    if cat == 'alg':
        i = randint(0, len(e_alg) - 1)
        year, level, version, question = e_alg[i][0:4], e_alg[i][4:6], e_alg[i][6:7], e_alg[i][7:]
        await cat_problem(ctx, level, year, version, question)

    if cat == 'com':
        i = randint(0, len(e_com) - 1)
        year, level, version, question = e_com[i][0:4], e_com[i][4:6], e_com[i][6:7], e_com[i][7:]
        await cat_problem(ctx, level, year, version, question)

    if cat == 'geo':
        i = randint(0, len(e_geo) - 1)
        year, level, version, question = e_geo[i][0:4], e_geo[i][4:6], e_geo[i][6:7], e_geo[i][7:]
        await cat_problem(ctx, level, year, version, question)

    if cat == 'nt':
        i = randint(0, len(e_nt) - 1)
        year, level, version, question = e_nt[i][0:4], e_nt[i][4:6], e_nt[i][6:7], e_nt[i][7:]
        await cat_problem(ctx, level, year, version, question)


# Hard Questions
@client.command(name='pch')
async def cat_prob(ctx, cat):
    if cat == 'alg':
        i = randint(0, len(h_alg) - 1)
        year, level, version, question = h_alg[i][0:4], h_alg[i][4:6], h_alg[i][6:7], h_alg[i][7:]
        await cat_problem(ctx, level, year, version, question)

    if cat == 'com':
        i = randint(0, len(h_com) - 1)
        year, level, version, question = h_com[i][0:4], h_com[i][4:6], h_com[i][6:7], h_com[i][7:]
        await cat_problem(ctx, level, year, version, question)

    if cat == 'geo':
        i = randint(0, len(h_geo) - 1)
        year, level, version, question = h_geo[i][0:4], h_geo[i][4:6], h_geo[i][6:7], h_geo[i][7:]
        await cat_problem(ctx, level, year, version, question)

    if cat == 'nt':
        i = randint(0, len(h_nt) - 1)
        year, level, version, question = h_nt[i][0:4], h_nt[i][4:6], h_nt[i][6:7], h_nt[i][7:]
        await cat_problem(ctx, level, year, version, question)


async def cat_problem(ctx, level, year, version, question):
    path = 'AMC/%s/%s/%s/%s.png' % (level, year, version, question)
    file = discord.File(path, filename='image.png')
    embed = discord.Embed(
        title='AMC ' + level + version + ' Problem',
        description='[Solution](https://artofproblemsolving.com/wiki/index.php/%s_AMC_%s%s_Problems/Problem_%s)' % (year, level, version, question),
        color=discord.Colour.blue()
    )
    embed.set_image(url="attachment://image.png")

    await ctx.send(file=file, embed=embed)


client.run(TOKEN)
