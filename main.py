import discord
from discord.ext import commands

TOKEN = [line.strip() for line in open('TOKEN.txt')][0]
initial_extensions = ['cogs.maa', 'cogs.aapt']
bot = commands.Bot(command_prefix='?')
bot.remove_command("help")

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.command(name='help')
async def help(ctx):
    embed = discord.Embed(
        title='Command Usage',
        description='**Generating Random Math Problems**: \n'
                    'Generating Random AMC Problem: `?amc {10/12}`\n'
                    'Generating Random AIME Problem: `?aime`\n\n'
                    '**By Category:** \n'
                    'Easy- `?pce {alg/geo/nt/com}`\n'
                    'Hard- `?pch {alg/geo/nt/com}`\n'
                    'alg is for algebra, geo is for geometry, nt is for number theory, and com is for '
                    'combinatorics/probability\n\n\n'

                    '**Generating Random Physics Problem:**\n'
                    'Generating Random F=MA Problem: `?fma`\n\n'
                    '**By Category:** \n'
                    'Physics- `pcp {kin/dyn/nrg/col/som/rb/osc/gra/flu/misc}`\n'
                    'kin is for kinematics, dyn is for dynamics, nrg is for energy, col is for collisions, som is for '
                    'systems of masses, rb is for rigid bodies, osc is for oscillatory motion, flu is for fluids, and '
                    'misc is dimensional analysis, elasticity, waves, etc.',
        color=discord.Colour.green()
    )
    await ctx.send(embed=embed)


bot.run(TOKEN)
