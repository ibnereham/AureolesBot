import discord
from discord import Intents,app_commands
from discord.ext import commands
from dotenv import load_dotenv
import random
import os
import asyncio
from badWords import *
from dataBase import *
from RacingF1 import *
from datetime import timedelta
load_dotenv()
TOKEN = os.getenv("TOKEN")
intent = Intents.all()
bot = commands.Bot(command_prefix="/", intents= intent, )
GenChatID= os.getenv("GEN_CHAT")
MSGLogID= os.getenv("MSG_LOG_CHANNEL")
WarnLogID= os.getenv("WARN_LOG_CHANNEL")
FreeSpeechRole=os.getenv("FreeSpeechRoleID")
AdminRoleID=os.getenv("AdminRoleID")
GuildID=os.getenv("GuildID")
SRV_NAME=os.getenv("SRV_NAME")

async def ChkPrix():
    while True:
        try:
            current = CheckTodayPrix()
            if current is not None:
                try:
                    x = read_words_from_file(filename="F1Lovers.txt")
                    for user in x:
                        user = await bot.fetch_user(int(user))
                        if user:
                            await user.send(f"Event Name: {current['RaceName']} \nRace Type: {current['RaceType']}\n Race Date: {current["RaceDate"]} ")
                        else:
                            print(f"User not found.")
                except Exception as e:
                    print(f"Error sending daily message: {e}")
            else:
                pass
            
        except Exception as e:
            print(f"Error sending daily message: {e}")
        await asyncio.sleep(43200)


def checkForBadWords(str, message):
    has_role = any(role.id == FreeSpeechRole for role in message.author.roles)
    if has_role:
        return False
    bad_words = read_words_from_file()
    for word in bad_words:
        for wrd in str:
            if word.lower() in wrd.lower():
                return f" bad word is {word}, detected from {wrd}"
        
    return False
async def warnact(num, name, uid:int):
    channel = bot.get_channel(WarnLogID)
    for i in [5,10,15,20]:
        if i == num:
            await channel.send(f'{name} has reached {i} warns')
        
    if num >= 7:
        await channel.send(f'{name} has reached {num} warns')
        try:
            guild = bot.get_guild(GuildID)  
            member = guild.get_member(uid)
            if member:
                await member.timeout(timedelta(hours=0.5))
                await channel.send(f'{name} has been timed out for 0.5 hour.')
        except Exception as e:
            await channel.send(f'Failed to timeout {name}: {e}')
        except:
            pass
    
@bot.event
async def on_ready():
    print(bot.user.display_name)
    try:
        synced = await bot.tree.sync()
        print(f"SYNCED{len(synced)} command(s) ")
        bot.loop.create_task(ChkPrix())
    except Exception as e:
        print(e)
    await bot.change_presence(activity=discord.Game(name=SRV_NAME, type=3),status=discord.Status.idle)


@bot.event
async def on_member_join(member):
    Server_Name= os.getenv("SRV_NAME")
    welcome_messages = [
        f" {member.mention}Welcome to The {Server_Name}. Hope you enjoy your stay here.",
        f"Hello, {member.mention}! Welcome to The {Server_Name}. We're glad to have you with us!",
        f"Hey there, {member.mention}! Welcome to The {Server_Name}. Make yourself at home!",
        f"Greetings, {member.mention}! Welcome to The {Server_Name}. Enjoy your stay!",
        f"Hi, {member.mention}! Welcome to The {Server_Name}. We're excited to have you here!",
        f"Welcome aboard, {member.mention}! Welcome to The {Server_Name}. Let's have some fun!",
    ]
    channel = bot.get_channel(GenChatID)
    await channel.send(random.choice(welcome_messages))




@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.author.bot:
        return
    if "@" in message.content:
        message.content = message.content.replace("@","")
    wordDetected = checkForBadWords((message.content).split(), message)
    if wordDetected:
        addOneWarn(message.author.id)
        x=findUserWarns(message.author.id)
        await warnact(x, message.author.display_name,uid=message.author.id)
        await message.delete()
        x = await message.channel.send(f"{message.author.mention} Bad word detected, keep thy typing shut or bad things could happen. {wordDetected}")
        await asyncio.sleep(5)
        await x.delete()
        
    chnl = bot.get_channel(MSGLogID)
    if len(message.attachments)  > 0:
        for att in  message.attachments:
            await chnl.send(f"User: {message.author.name} ")
            await chnl.send(att.url)
    else:       
        await chnl.send(content=f'User:{message.author.name}\n content: {message.content}')


@bot.tree.command(name="rules")
async def rules(interaction: discord.Interaction):
    await interaction.response.defer(ephemeral=True)
    embed = discord.Embed(title="Rules",
                      description="> 1. **Respect Everyone**: Treat all members with respect and kindness. Harassment, discrimination, hate speech, or any form of bullying will not be tolerated.\n\n> 2. **No NSFW Content**: Keep all content safe for work (SFW). Avoid sharing or discussing explicit or adult-oriented material.\n\n> 3. **No Spamming or Flooding**: Refrain from spamming the chat with repetitive messages, emojis, or unnecessary pings. Keep conversations engaging and constructive.\n\n> 4. **Use Appropriate Channels**: Post content in the relevant channels to keep discussions organized and easy to follow. Off-topic discussions should be kept to designated channels.\n\n> 5. **No Advertising Without Permission**: Do not promote other Discord servers, websites, or products without permission from the server administrators.\n\n> 6. **Respect Privacy**: Avoid sharing personal information about yourself or others without consent. Respect the privacy of fellow members.\n\n> 7. **Follow Discord's Terms of Service and Community Guidelines**: Abide by Discord's rules and guidelines to ensure a safe and enjoyable experience for everyone.\n\n> 8. **Listen to Moderators/Admins**: Follow the instructions of moderators and administrators. They are there to maintain order and resolve any issues that may arise.\n\n> 9. **No Begging or Begging for Roles**: Refrain from begging for roles, privileges, or special treatment. Everyone is equal in the community.\n\n> 10. **Keep Conversations Civil and Constructive**: Engage in discussions respectfully and avoid engaging in arguments or heated debates. Disagreements should be handled maturely and peacefully.\n\n> 11. **Report Violations**: If you witness any violations of the rules or encounter any issues, report them to the moderators or admins immediately.\n\n> 12. **Have Fun and Chill**: The primary goal of the community is to relax and enjoy each other's company. Keep conversations light-hearted and have fun together!",
                      colour=0xf50000)
    await interaction.followup.send("check DM", ephemeral=True)
    await interaction.user.send(embed=embed)

@bot.tree.command(name="addbadwords", description="add words. seperated by space")
@app_commands.describe(prompt="Prompt")
async def addbadwords(interaction: discord.Interaction, prompt:str):
    await interaction.response.defer(ephemeral=True)
    has_role = any(role.id == AdminRoleID for role in interaction.user.roles)
    if not has_role:
        await interaction.followup.send("You dont have perms",ephemeral=True)
    else:

        x= prompt.split()   
        save_words_to_file(x)
    
        await interaction.followup.send(f"added bad words : {x}",ephemeral=True)

@bot.tree.command(name="checkbadwords")
async def addbadwords(interaction: discord.Interaction):
    await interaction.response.defer(ephemeral=True)
    has_role = any(role.id == AdminRoleID for role in interaction.user.roles)
    if not has_role:
        await interaction.followup.send("You dont have perms",ephemeral=True)
    else:
        x= read_words_from_file()
        y = "Bad words are: "
        for word in x:
            y = y+f"{word} "
        await interaction.followup.send(y,ephemeral=True)

@bot.tree.command(name="resetbadwords")
async def resetbadwords(interaction: discord.Interaction,):
    await interaction.response.defer(ephemeral=True)
    has_role = any(role.id == AdminRoleID for role in interaction.user.roles)
    if not has_role:
        await interaction.followup.send("You dont have perms",ephemeral=True)
    else:
        reset()
        await interaction.followup.send("reset done",ephemeral=True)

@bot.tree.command(name="removebadwords", description="removes word (seperated by space)")
async def removebadword(interaction: discord.Interaction, prompt:str):
    await interaction.response.defer(ephemeral=True)
    has_role = any(role.id == AdminRoleID for role in interaction.user.roles)
    if not has_role:
        await interaction.followup.send("You dont have perms",ephemeral=True)
    else:
        x = prompt.split()
        for z in x:
            remove_word(z)
        await interaction.followup.send(f"removed words: {prompt}",ephemeral=True)
@bot.tree.command(name="removeonewarn", description="removes 1 warn")
async def removewarn(interaction: discord.Interaction, mention:str):
    await interaction.response.defer(ephemeral=True)
    has_role = any(role.id == AdminRoleID for role in interaction.user.roles)
    if not has_role:
        await interaction.followup.send("You dont have perms",ephemeral=True)
    else:
        prompt= mention
        for i in ["@","<",">"]:
            prompt = prompt.replace(i,"")
        prompt = int(prompt)
        x = removeOneWarn(prompt)
        if x:
            await interaction.followup.send(f"removed 1 warn for {bot.get_user(prompt).mention}  ",ephemeral=True)
        else:
            await interaction.followup.send(f"{bot.get_user(prompt).mention}  has no warnings to remove",ephemeral=True)

@bot.tree.command(name="checkwarn", description="checks th amount of warn a guy has")
async def checkwarn(interaction: discord.Interaction, mention:str):
    await interaction.response.defer(ephemeral=True)
    has_role = any(role.id == AdminRoleID for role in interaction.user.roles)
    if not has_role:
        await interaction.followup.send("You dont have perms",ephemeral=True)
    else:
        prompt= mention
        for i in ["@","<",">"]:
            prompt = prompt.replace(i,"")
        prompt = int(prompt)
        x = findUserWarns(prompt) 
        await interaction.followup.send(f"{bot.get_user(prompt).mention} has {x} warns",ephemeral=True)
@bot.tree.command(name="resetwarn", description="sets warn to 0")
async def resetwarn(interaction: discord.Interaction, mention:str):
    await interaction.response.defer(ephemeral=True)
    has_role = any(role.id == AdminRoleID for role in interaction.user.roles)
    if not has_role:
        await interaction.followup.send("You dont have perms",ephemeral=True)
    else:
        prompt= mention
        for i in ["@","<",">"]:
            prompt = prompt.replace(i,"")
        prompt = int(prompt)
        resetWarns(prompt) 
        await interaction.followup.send(f"reset warns for {bot.get_user(prompt).mention}",ephemeral=True)  





@bot.tree.command(name="addtof1",description="Adds you to f1 notification List")
async def addtof1(interaction: discord.Interaction,):
    await interaction.response.defer(ephemeral=True)
    save_words_to_file(filename="F1Lovers.txt",words=[interaction.user.id])
    await interaction.followup.send("Added you",ephemeral=True)
@bot.tree.command(name="removefromf1",description="removees you from f1 notification List")
async def removefromf1(interaction: discord.Interaction,):
    await interaction.response.defer(ephemeral=True)
    remove_word(filename="F1Lovers.txt",words=[interaction.user.id])
    await interaction.followup.send("Removed you.",ephemeral=True)

bot.run(TOKEN)