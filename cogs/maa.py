from random import randint, choice
import discord
from discord.ext import commands

e_alg = [line.strip() for line in open('categories/math/easy/Algebra.txt')]
e_com = [line.strip() for line in open('categories/math/easy/Combinatorics.txt')]
e_geo = [line.strip() for line in open('categories/math/easy/Geometry.txt')]
e_nt = [line.strip() for line in open('categories/math/easy/NumberTheory.txt')]

h_alg = [line.strip() for line in open('categories/math/hard/Algebra.txt')]
h_com = [line.strip() for line in open('categories/math/hard/Combinatorics.txt')]
h_geo = [line.strip() for line in open('categories/math/hard/Geometry.txt')]
h_nt = [line.strip() for line in open('categories/math/hard/NumberTheory.txt')]


async def math_cat_prob(ctx, exam, level: int, year: int, version, question: int):
    if exam == 'AM':
        path = 'Exams/amc/%d/%d/%s/%d.png' % (level, year, version, question)
        file = discord.File(path, filename='image.png')
        link = 'https://artofproblemsolving.com/wiki/index.php/%d_AMC_%d%s_Problems/Problem_%d' % (
            year, level, version, question)
        embed = discord.Embed(
            title='%d AMC %d%s Question %d' % (year, level, version, question),
            description='[Solution](' + link + ')',
            color=discord.Colour.blue()
        )
        embed.set_image(url="attachment://image.png")
        await ctx.send(file=file, embed=embed)
    else:
        version = 'I' if version == 'A' else 'II'
        path = 'Exams/aime/%d/%s/%d.png' % (year, version, question)
        file = discord.File(path, filename='image.png')
        link = 'https://artofproblemsolving.com/wiki/index.php/%d_AIME_%s_Problems/Problem_%d' % (
            year, version, question)
        embed = discord.Embed(
            title='%d AIME %s Question %d' % (year, version, question),
            description='[Solution](' + link + ')',
            color=discord.Colour.blue()
        )
        embed.set_image(url="attachment://image.png")
        await ctx.send(file=file, embed=embed)


class MAACog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='amc')
    async def amc_prob(self, ctx, level: int):
        if level == 10 or level == 12:
            year, version, question = randint(2002, 2021), choice(('A', 'B')), randint(1, 25)
            path = 'Exams/amc/%d/%d/%s/%d.png' % (level, year, version, question)
            file = discord.File(path, filename='image.png')
            embed = discord.Embed(
                title='%d AMC %d%s Question %d' % (year, level, version, question),
                description='[Solution](https://artofproblemsolving.com/wiki/index.php/%d_AMC_%d%s_Problems/Problem_%d)'
                            % (year, level, version, question),
                color=discord.Colour.blue()
            )
            embed.set_image(url="attachment://image.png")
            await ctx.send(file=file, embed=embed)
        else:
            await ctx.send("Invalid Level")

    @commands.command(name='aime')
    async def aime_prob(self, ctx):
        year, version, question = randint(2002, 2021), choice(('I', 'II')), randint(1, 15)
        path = 'Exams/aime/%d/%s/%d.png' % (year, version, question)
        file = discord.File(path, filename='image.png')
        embed = discord.Embed(
            title='%d AIME %s Question %d' % (year, version, question),
            description='[Solution](https://artofproblemsolving.com/wiki/index.php/%d_AIME_%s_Problems/Problem_%s)'
                        % (year, version, question),
            color=discord.Colour.blue()
        )
        embed.set_image(url="attachment://image.png")
        await ctx.send(file=file, embed=embed)

    @commands.command(name='pce')
    async def math_easy(self, ctx, cat):
        exam, year, level, version, question = ..., ..., ..., ..., ...  # str
        if cat == 'alg':
            i = randint(0, len(e_alg) - 1)
            exam, year, level, version, question = e_alg[i][0:2], e_alg[i][2:6], e_alg[i][6:8], e_alg[i][8:9], e_alg[i][9:]

        if cat == 'com':
            i = randint(0, len(e_com) - 1)
            exam, year, level, version, question = e_com[i][0:2], e_com[i][2:6], e_com[i][6:8], e_com[i][8:9], e_com[i][9:]

        if cat == 'geo':
            i = randint(0, len(e_geo) - 1)
            exam, year, level, version, question = e_geo[i][0:2], e_geo[i][2:6], e_geo[i][6:8], e_geo[i][8:9], e_geo[i][9:]

        if cat == 'nt':
            i = randint(0, len(e_nt) - 1)
            exam, year, level, version, question = e_nt[i][0:2], e_nt[i][2:6], e_nt[i][6:8], e_nt[i][8:9], e_nt[i][9:]

        await math_cat_prob(ctx, exam, int(level), int(year), version, int(question))

    @commands.command(name='pch')
    async def math_hard(self, ctx, cat):
        exam, year, level, version, question = ..., ..., ..., ..., ...  # str
        if cat == 'alg':
            i = randint(0, len(h_alg) - 1)
            exam, year, level, version, question = h_alg[i][0:2], h_alg[i][2:6], h_alg[i][6:8], h_alg[i][8:9], h_alg[i][9:]

        if cat == 'com':
            i = randint(0, len(h_com) - 1)
            exam, year, level, version, question = h_com[i][0:2], h_com[i][2:6], h_com[i][6:8], h_com[i][8:9], h_com[i][9:]

        if cat == 'geo':
            i = randint(0, len(h_geo) - 1)
            exam, year, level, version, question = h_geo[i][0:2], h_geo[i][2:6], h_geo[i][6:8], h_geo[i][8:9], h_geo[i][9:]
        if cat == 'nt':
            i = randint(0, len(h_nt) - 1)
            exam, year, level, version, question = h_nt[i][0:2], h_nt[i][2:6], h_nt[i][6:8], h_nt[i][8:9], h_nt[i][9:]

        await math_cat_prob(ctx, exam, int(level), int(year), version, int(question))


def setup(bot):
    bot.add_cog(MAACog(bot))
