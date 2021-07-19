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

'''
 file naming scheme is Test/Year/Level/Version/Question
 for AIMEs, threw in a 10 for the version just so I didn't have to change code, it's easier this way
 also, the I and II of AIME naming was turned into A/B for same reason as before
 examples: AM201810A13 (2018 AMC 10A Problem 13) | AI200210A12 (2002 AIME I Problem 12)
 
 Also quick sidenote as to why there are more AIME years than AMCs:
 AIME has had the convention of I and II for longer and this format makes it easier to webscrape due to the link style
 being standard. Other AMCs or former AIMEs might be added in the future but for now this is the format
'''


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.command(name='amc')
async def rand_prob(ctx, level):
    if level == 10 or level == 12:
        year, version, question = randint(2002, 2021), choice(('A', 'B')), randint(1, 25)
        path = 'AMC/%s/%d/%s/%d.png' % (level, year, version, question)
        file = discord.File(path, filename='image.png')
        embed = discord.Embed(
            title='AMC ' + level + version + ' Problem',
            description='[Solution](https://artofproblemsolving.com/wiki/index.php/%d_AMC_%s%s_Problems/Problem_%d)'
                        % (year, level, version, question),
            color=discord.Colour.blue()
        )
        embed.set_image(url="attachment://image.png")
        await ctx.send(file=file, embed=embed)
    else:
        await ctx.send("Invalid Level")


@client.command(name='aime')
async def rand_prob(ctx):
    year, version, question = randint(2002, 2021), choice(('I', 'II')), randint(1, 15)
    path = 'AIME/%d/%s/%d.png' % (year, version, question)
    file = discord.File(path, filename='image.png')
    embed = discord.Embed(
        title='AIME ' + version + ' Problem',
        description='[Solution](https://artofproblemsolving.com/wiki/index.php/%d_AIME_%s_Problems/Problem_%s)'
                    % (year, version, question),
        color=discord.Colour.blue()
    )
    embed.set_image(url="attachment://image.png")
    await ctx.send(file=file, embed=embed)


# Easy Questions
@client.command(name='pce')
async def cat_prob_easy(ctx, cat):
    if cat == 'alg':
        i = randint(0, len(e_alg) - 1)
        exam, year, level, version, question = e_alg[i][0:2], e_alg[i][2:6], e_alg[i][6:8], e_alg[i][8:9], e_alg[i][9:]
        await cat_problem(ctx, exam, level, year, version, question)

    if cat == 'com':
        i = randint(0, len(e_com) - 1)
        exam, year, level, version, question = e_com[i][0:2], e_com[i][2:6], e_com[i][6:8], e_com[i][8:9], e_com[i][9:]
        await cat_problem(ctx, exam, level, year, version, question)

    if cat == 'geo':
        i = randint(0, len(e_geo) - 1)
        exam, year, level, version, question = e_geo[i][0:2], e_geo[i][2:6], e_geo[i][6:8], e_geo[i][8:9], e_geo[i][9:]
        await cat_problem(ctx, exam, level, year, version, question)

    if cat == 'nt':
        i = randint(0, len(e_nt) - 1)
        exam, year, level, version, question = e_nt[i][0:2], e_nt[i][2:6], e_nt[i][6:8], e_nt[i][8:9], e_nt[i][9:]
        await cat_problem(ctx, exam, level, year, version, question)


# Hard Questions
@client.command(name='pch')
async def cat_prob_hard(ctx, cat):
    if cat == 'alg':
        i = randint(0, len(h_alg) - 1)
        exam, year, level, version, question = h_alg[i][0:2], h_alg[i][2:6], h_alg[i][6:8], h_alg[i][8:9], h_alg[i][9:]
        await cat_problem(ctx, exam, level, year, version, question)

    if cat == 'com':
        i = randint(0, len(h_com) - 1)
        exam, year, level, version, question = h_com[i][0:2], h_com[i][2:6], h_com[i][6:8], h_com[i][8:9], h_com[i][9:]
        await cat_problem(ctx, exam, level, year, version, question)

    if cat == 'geo':
        i = randint(0, len(h_geo) - 1)
        exam, year, level, version, question = h_geo[i][0:2], h_geo[i][2:6], h_geo[i][6:8], h_geo[i][8:9], h_geo[i][9:]
        await cat_problem(ctx, exam, level, year, version, question)

    if cat == 'nt':
        i = randint(0, len(h_nt) - 1)
        exam, year, level, version, question = h_nt[i][0:2], h_nt[i][2:6], h_nt[i][6:8], h_nt[i][8:9], h_nt[i][9:]
        await cat_problem(ctx, exam, level, year, version, question)


async def cat_problem(ctx, exam, level, year, version, question):
    if exam == 'AM':
        path = 'AMC/%s/%s/%s/%s.png' % (level, year, version, question)
        file = discord.File(path, filename='image.png')
        link = 'https://artofproblemsolving.com/wiki/index.php/%s_AMC_%s%s_Problems/Problem_%s' % (
            year, level, version, question)
        embed = discord.Embed(
            title='AMC ' + level + version + ' Problem',
            description='[Solution](' + link + ')',
            color=discord.Colour.blue()
        )
        embed.set_image(url="attachment://image.png")
        await ctx.send(file=file, embed=embed)
    if exam == 'AI':
        version = 'I' if version == 'A' else 'II'
        path = 'AIME/%s/%s/%s.png' % (year, version, question)
        file = discord.File(path, filename='image.png')
        link = 'https://artofproblemsolving.com/wiki/index.php/%s_AIME_%s_Problems/Problem_%s' % (
            year, version, question)
        embed = discord.Embed(
            title='AIME ' + version + ' Problem',
            description='[Solution](' + link + ')',
            color=discord.Colour.blue()
        )
        embed.set_image(url="attachment://image.png")
        await ctx.send(file=file, embed=embed)


client.run(TOKEN)
