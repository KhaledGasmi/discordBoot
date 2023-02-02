import discord

TOKEN = "MTA3MDM3NjM0Mjg4Mjg4NTc3NQ.GXdbIZ.CloNYX9znhWqaKEniXV0zTG47uTXk7t8HxI9GE"
questions = {
    "Q1":"why can't the link of your platform be opened directly?",
    "Q2":"why weren’t people who filed out the form and wanted to join the club contacted?",
    "Q3":"When I enter the server,I find two rooms : general and announcement why?",
    "Q4":"on the platform, why can’t we access the Event earlier ?",
}

answares = {
    "Q1":"the link must be copied and pasted directly into the browser to access the platform.",
    "Q2":"Registrations are opened by the Human Resources Department once a month . you must fill out the form and wait for the interview appointment mail",
    "Q3":"you have to wait for the human resources members to add you to your department .it will not exceed 48h as a maximum" ,
    "Q4":"you can join the event at the specified time ."
}


def jsonToString(json):
    strs = ""
    for i in json.keys():
        strs += f"{i}:{json[i]}\n"
    return strs

menu = {
    "departments":"no connection", 
    "events":"no connection", 
    "tasks":"no connection", 
    "q&a":jsonToString(questions), 
    "website":"no connection", 
    "social_media":"no connection"
}

def message_send(message):
    try:      
        if(not message[0]=='.'):
            return 404
        msg = message.lower()
        msg = msg[1:]
        if msg == "help":
            return "what do you want to ask about:\n."+"\n.".join(menu)
        return menu[msg]
    except:
        return "command not recognized"

def answ(message):
    try:      
        if(not message[0]=='.'):
            return 404
        msg = message.lower()
        msg = msg[1:]
        if msg == "q1":
            return answares["Q1"]
        elif msg == "q2":
            return answares["Q2"]
        elif msg == "q3":
            return answares["Q3"]
        elif msg == "q4":
            return answares["Q4"]
    except:
        return "command not recognized"
        


intents = discord.Intents.all()

bot = discord.Client(command_prifix = '.', intents = intents)


@bot.event
async def on_ready():
    print("connect")

@bot.event 
async def on_message(message):
    print(message.content)
    if message.author==bot.user:
        return 
    res = message_send(message.content)
    if message.content[1]=="q":
        res = answ(message.content)
    if res==404:
        return
    await message.channel.send(res)


bot.run(TOKEN)



