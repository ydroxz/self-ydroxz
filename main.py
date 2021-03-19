import discord, asyncio

from os import system

import shutil

import subprocess

from sys import argv

import psutil

import logging

from requests import get

from time import sleep

from discord.ext import commands

from colorama import init, Fore

from bs4 import BeautifulSoup

from os import system

def logo():

    try:

        print(Fore.LIGHTRED_EX)

        msg = f"""

░▒█░░   █▄▄▄██▀▀▄░░░░░

░█░░░▀▄░▄▄▄▄▄░▄▀░░░█

░░▀▄░░░▀░░░░░▀░░░▄▀

░░░░▌░▄▄░░░▄▄░▐▀▀

░░░▐░░█▄░░░▄█░░▌▄▄▀▀▀▀█ Created by ydroxz.π#4547

░░░▌▄▄▀▀░▄░▀▀▄▄▐░░░░░░█

▄▀▀▐▀▀░▄▄▄▄▄░▀▀▌▄▄▄░░░█

█░░░▀▄░█░░░█░▄▀░░░░█▀▀▀

░▀▄░░▀░░▀▀▀░░▀░░░▄█▀

░░░█░░░░░░░░░░░▄▀▄░▀▄

░░░█░░░░░░░░░▄▀█░░█░░█

░░░█░░░░░░░░░░░█▄█░░▄▀

░░░█░░░░░░░░░░░████▀

░░░▀▄▄▀▀▄▄▀▀▄▄▄█▀   \n

        """

        for l in msg:

            print(l, end="")

    except KeyboardInterrupt:

        sys.exit()

logo()

print(Fore.RESET)

print('  ')

print('{}╔═════ Commands ════════════════════════════════╗{}'.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))

print('{}║{}'.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))

print('{}║ [1] limpar :{} (apagar mensagens)'.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))

print('{}║ [2] lmp :{} (clrs abre mensagens diretas e as apaga)'.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))

print('{}║ [3] status :{} (stream status ex: status swag https://www.twitch.tv/ydroxz)'.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))

print('{}║ [4] removerstt :{} (remover status)'.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))

print('{}║ [5] sairservidores :{} (deixa todos os seus grupos)'.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))

print('{}║{}'.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))

print('{}╚══════════════════════════════════════════════╝{}'.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))

print('  ')

client = discord.Client()

token = "SUA TOKEN!!!"

def murder(cmd):

    subprocess.call(cmd, shell=True)

@client.event

async def on_ready():

    width = shutil.get_terminal_size().columns

    def ui():

        print()

        print("ydroxz.π#4547".center(width))

        print()

        print("[-] ydroxz.π [-]".center(width))

        print("[-] user: {0} [-]".format(client.user).center(width))

        print()

    ui()

 

 

@client.event

async def on_message(message):

    if message.author == client.user:

        commands = []

        z = 0

        for index, a in enumerate(message.content):

            if a == " ":

                commands.append(message.content[z:index])

                z = index + 1

        commands.append(message.content[z:])

        channel = message.channel

        if commands[0] == 'limpar':

                    if len(commands) == 1:

                        async for msg in channel.history(limit=9999):

                            if msg.author == client.user:

                                try:

                                    await msg.delete()

                                except Exception as x:

                                    pass

        if commands[0] == 'lmp':

            for channel in client.private_channels:

                if isinstance(channel, discord.DMChannel):

                    async for msg in channel.history(limit=9999):

                        try:

                            if msg.author == client.user:

                                await msg.delete()

                                print(msg)

                        except:

                             pass

        if commands[0] == 'status':

                        msg = message.content.split("status", 1)

                        args = msg[1].split(" https", 1)

                        name = args[0]

                        url = "https://twitch.tv/ydroxz"+args[1]

                        await message.delete()

                        await client.change_presence(status=discord.Status.dnd, activity=discord.Streaming(name=name, url=url))

                        container = discord.Embed(title="ydroxz.π#4547", color=0xFF3633)

                        container.add_field(name="status:", value="**"+name+"**")

                        container.set_footer(text="//")

                        await channel.send(embed=container)

        if commands[0] == "removerstt":

                await message.delete()

                await client.change_presence(status=discord.Status.dnd)

        

        if commands[0] == "sairservidores":

                await message.delete()

                count = 0

                for channel in client.private_channels:

                        if isinstance(channel, discord.GroupChannel):

                                if channel.id != message.channel.id:

                                        count = count + 1

                                        await channel.leave()

        if commands[0] == "sairservidores":

                await message.delete()

                count = 0

                for channel in client.private_channels:

                        if isinstance(channel, discord.GroupChannel):

                                if channel.id != message.channel.id:

                                        count = count + 1

                                        await channel.leave()

client.run(token, bot=False)

