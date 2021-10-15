import os
import discord
import sys
from dotenv import load_dotenv
import random
from discord.ext import commands

path = sys.path[0]+'/config/.env'
load_dotenv(path)

TOKEN=os.getenv("DISCORD_TOKEN")

def selectRandom(names):
        return random.choice(names)

class DocBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!")
        self.remove_command('help')
        self.add_command(self.print)
        self.add_command(self.help)
        self.add_command(self.quizz)
        self.matiere=["algo","sysInfo","methode","web","sysReseau","bdd","anglais","archi","prog","spec"]
        self.sysReseau_quizz=["C'est quoi un système d'exploitation?","Quels sont les différentes couches d'un système informatique"]

    
    #@client.event
    #async def on_ready(self):
        #print("Le bot est prêt.")

    @commands.command()
    async def print(self,message):
        await self.channel.send(message)


    @commands.command()
    async def help(ctx):
        #Envoie la liste des commandes et leurs fonctions par message privé
        embed = discord.Embed(colour=discord.Colour.blue())
        embed.set_author(name='Liste des commandes')

        #Commandes User
        embed.add_field(name="**!print**", value="Le bot affiche le message passer en paramètre", inline=False)
        embed.add_field(name="**!quizz**", value="Le bot va vous poser des questions pour vérifier vos révisions", inline=False)
        #Commandes Admin 
        for role in ctx.message.author.roles:
            if role.name == 'Admins':
                embed.add_field(name="**!load [extension]**", value="Charge l'extension mentionnée", inline=False)
                embed.add_field(name="**!unload [extension]**", value="Désactive l'extension mentionnée", inline=False)
                embed.add_field(name="**!reload [extension]**", value="Recharge l'extension mentionnée", inline=False)
    
        await ctx.channel.send(embed=embed)

    @commands.command()
    async def quizz(self,matiere,nb):
        nb=int(nb)
        if matiere=="sysReseau":
            if nb>0 and nb!="None":
                for _ in range(nb):
                    str=selectRandom(bot.sysReseau_quizz)
                    await self.channel.send(str)


    #@client.event
    #async def on_message(self,message):
        #-await message.channel.send(message.content)
        

if __name__ == "__main__":
    bot = DocBot()
    bot.run(TOKEN)
