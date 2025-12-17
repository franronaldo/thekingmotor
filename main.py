import os
import discord
from discord.ext import tasks
from flask import Flask
import threading
from datetime import datetime

intents = discord.Intents.default()
client = discord.Client(intents=intents)

CHANNEL_ID = int(os.getenv("CHANNEL_ID"))
ROLE_ID = os.getenv("ROLE_ID")

app = Flask('')

@app.route('/')
def home():
    return "Bot funcionando"

def run_web():
    app.run(host='0.0.0.0', port=8080)

@client.event
async def on_ready():
    print(f'✅ Bot conectado como {client.user}')
    
    # Establecer estado del bot como "Escuchando /play"
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="GTAHUB.GG | Orion"))

    send_scheduled_embeds.start()

sent_today = {}

@tasks.loop(minutes=1)
async def send_scheduled_embeds():
    now = datetime.utcnow()
    utc_hour = now.hour
    utc_minute = now.minute
    today = now.strftime('%Y-%m-%d')

    scheduled_embeds = [
        {
            "hour": 23,
            "minute": 50,
            "id": "embed1",
            "embed": discord.Embed(
                title="**__¡En 10 minutos comienza la actividad!__**",
                description="🚗 `Reparación industrial 1/4` — **00:00**",
                color=0xCDA939
            ).set_author(
                name="The King Motor",
                icon_url="https://i.imgur.com/ws748KD.png"
            ).add_field(
                name="**__Próxima actividad__**",
                value="\n🧰 `Reparación en carretera 1/6` — **01:00**\n\n**〰️〰️〰️〰️〰️〰️**",
                inline=False
            ).set_thumbnail(
                url="https://i.imgur.com/ws748KD.png"
            ).set_image(
                url="https://i.imgur.com/s3zRf60.png"
            ).set_footer(
                text="The King Motor",
                icon_url="https://i.imgur.com/ws748KD.png"
            )
        },
        {
            "hour": 0,
            "minute": 50,
            "id": "embed2",
            "embed": discord.Embed(
                title="**__¡En 10 minutos comienza la actividad!__**",
                description="🧰 `Reparación en carretera 1/6` — **01:00**",
                color=0xCDA939
            ).set_author(
                name="The King Motor",
                icon_url="https://i.imgur.com/ws748KD.png"
            ).add_field(
                name="**__Próxima actividad__**",
                value="\n🪛 `Entrega de herramientas 1/5` — **02:00**\n\n**〰️〰️〰️〰️〰️〰️**",
                inline=False
            ).set_thumbnail(
                url="https://i.imgur.com/ws748KD.png"
            ).set_image(
                url="https://i.imgur.com/d2wi2VG.png"
            ).set_footer(
                text="The King Motor",
                icon_url="https://i.imgur.com/ws748KD.png"
            )
        },
        {
            "hour": 1,
            "minute": 50,
            "id": "embed3",
            "embed": discord.Embed(
                title="**__¡En 10 minutos comienza la actividad!__**",
                description="🪛 `Entrega de herramientas 1/5` — **02:00**",
                color=0xCDA939
            ).set_author(
                name="The King Motor",
                icon_url="https://i.imgur.com/ws748KD.png"
            ).add_field(
                name="**__Próxima actividad__**",
                value="\n🚗 `Reparación industrial 2/4` — **03:00**\n\n**〰️〰️〰️〰️〰️〰️**",
                inline=False
            ).set_thumbnail(
                url="https://i.imgur.com/ws748KD.png"
            ).set_image(
                url="https://i.imgur.com/T7P4tFJ.png"
            ).set_footer(
                text="The King Motor",
                icon_url="https://i.imgur.com/ws748KD.png"
            )
        },
        {
            "hour": 2,
            "minute": 50,
            "id": "embed4",
            "embed": discord.Embed(
                title="**__¡En 10 minutos comienza la actividad!__**",
                description="🚗 `Reparación industrial 2/4` — **03:00**",
                color=0xCDA939
            ).set_author(
                name="The King Motor",
                icon_url="https://i.imgur.com/ws748KD.png"
            ).add_field(
                name="**__Próxima actividad__**",
                value="\n🪛 `Entrega de herramientas 2/5` — **05:00**\n\n**〰️〰️〰️〰️〰️〰️**",
                inline=False
            ).set_thumbnail(
                url="https://i.imgur.com/ws748KD.png"
            ).set_image(
                url="https://i.imgur.com/s3zRf60.png"
            ).set_footer(
                text="The King Motor",
                icon_url="https://i.imgur.com/ws748KD.png"
            )
        },
        {
            "hour": 4,
            "minute": 50,
            "id": "embed5",
            "embed": discord.Embed(
                title="**__¡En 10 minutos comienza la actividad!__**",
                description="🪛 `Entrega de herramientas 2/5` — **05:00**",
                color=0xCDA939
            ).set_author(
                name="The King Motor",
                icon_url="https://i.imgur.com/ws748KD.png"
            ).add_field(
                name="**__Próxima actividad__**",
                value="\n🧰 `Reparación en carretera 2/6` — **08:00**\n\n**〰️〰️〰️〰️〰️〰️**",
                inline=False
            ).set_thumbnail(
                url="https://i.imgur.com/ws748KD.png"
            ).set_image(
                url="https://i.imgur.com/T7P4tFJ.png"
            ).set_footer(
                text="The King Motor",
                icon_url="https://i.imgur.com/ws748KD.png"
            )
        },
        {
            "hour": 7,
            "minute": 50,
            "id": "embed6",
            "embed": discord.Embed(
                title="**__¡En 10 minutos comienza la actividad!__**",
                description="🧰 `Reparación en carretera 2/6` — **08:00**",
                color=0xCDA939
            ).set_author(
                name="The King Motor",
                icon_url="https://i.imgur.com/ws748KD.png"
            ).add_field(
                name="**__Próxima actividad__**",
                value="\n🚗 `Reparación industrial 3/4` — **11:00**\n\n**〰️〰️〰️〰️〰️〰️**",
                inline=False
            ).set_thumbnail(
                url="https://i.imgur.com/ws748KD.png"
            ).set_image(
                url="https://i.imgur.com/d2wi2VG.png"
            ).set_footer(
                text="The King Motor",
                icon_url="https://i.imgur.com/ws748KD.png"
            )
        },
        {
            "hour": 10,
            "minute": 50,
            "id": "embed13",
            "embed": discord.Embed(
                title="**__¡En 10 minutos comienza una actividad__**",
                description="🚗 `Reparación industrial 3/4` — **11:00**",
                color=0xCDA939
            ).set_author(
                name="The King Motor",
                icon_url="https://i.imgur.com/ws748KD.png"
            ).add_field(
                name="**__Próxima actividad__**",
                value="\n🧰 `Reparación en carretera 3/6` — **13:00**\n\n**〰️〰️〰️〰️〰️〰️**",
                inline=False
            ).set_thumbnail(
                url="https://i.imgur.com/ws748KD.png"
            ).set_image(
                url="https://i.imgur.com/s3zRf60.png"            
            ).set_footer(
                text="The King Motor",
                icon_url="https://i.imgur.com/ws748KD.png"
            )
        },
        {
            "hour": 12,
            "minute": 50,
            "id": "embed14",
            "embed": discord.Embed(
                title="**__¡En 10 minutos comienza una actividad__**",
                description="🧰 `Reparación en carretera 3/6` — **13:00**",
                color=0xCDA939
            ).set_author(
                name="The King Motor",
                icon_url="https://i.imgur.com/ws748KD.png"
            ).add_field(
                name="**__Próxima actividad__**",
                value="\n🪛 `Entrega de herramientas 3/5` — **15:00**\n\n**〰️〰️〰️〰️〰️〰️**",
                inline=False
            ).set_thumbnail(
                url="https://i.imgur.com/ws748KD.png"
            ).set_image(
                url="https://i.imgur.com/d2wi2VG.png"            
            ).set_footer(
                text="The King Motor",
                icon_url="https://i.imgur.com/ws748KD.png"
            )
        },
        {
            "hour": 14,
            "minute": 50,
            "id": "embed15",
            "embed": discord.Embed(
                title="**__¡En 10 minutos comienza una actividad__**",
                description="🪛 `Entrega de herramientas 3/5` — **15:00**",
                color=0xCDA939
            ).set_author(
                name="The King Motor",
                icon_url="https://i.imgur.com/ws748KD.png"
            ).add_field(
                name="**__Próxima actividad__**",
                value="\n🧰 `Reparación en carretera 4/6` — **17:00**\n\n**〰️〰️〰️〰️〰️〰️**",
                inline=False
            ).set_thumbnail(
                url="https://i.imgur.com/ws748KD.png"
            ).set_image(
                url="https://i.imgur.com/T7P4tFJ.png"            
            ).set_footer(
                text="The King Motor",
                icon_url="https://i.imgur.com/ws748KD.png"
            )
        },
        {
            "hour": 16,
            "minute": 50,
            "id": "embed17",
            "embed": discord.Embed(
                title="**__¡En 10 minutos comienza una actividad__**",
                description="🧰 `Reparación en carretera 4/6` — **17:00**",
                color=0xCDA939
            ).set_author(
                name="The King Motor",
                icon_url="https://i.imgur.com/ws748KD.png"
            ).add_field(
                name="**__Próxima actividad__**",
                value="\n🪛 `Entrega de herramientas 4/5` — **18:00**\n🧰 `Reparación en carretera 5/6` — **18:00**\n\n**〰️〰️〰️〰️〰️〰️**",
                inline=False
            ).set_thumbnail(
                url="https://i.imgur.com/ws748KD.png"
            ).set_image(
                url="https://i.imgur.com/d2wi2VG.png"            
            ).set_footer(
                text="The King Motor",
                icon_url="https://i.imgur.com/ws748KD.png"
            )
        },
        {
            "hour": 17,
            "minute": 50,
            "id": "embed18",
            "embed": discord.Embed(
                title="**__¡En 10 minutos comienza una actividad__**",
                description="🪛 `Entrega de herramientas 4/5` — **18:00**\n🧰 `Reparación en carretera 5/6` — **18:00**",
                color=0xCDA939
            ).set_author(
                name="The King Motor",
                icon_url="https://i.imgur.com/ws748KD.png"
            ).add_field(
                name="**__Próxima actividad__**",
                value="\n🚗 `Reparación industrial 4/4` — **20:00**\n\n**〰️〰️〰️〰️〰️〰️**",
                inline=False
            ).set_thumbnail(
                url="https://i.imgur.com/ws748KD.png"
            ).set_image(
                url="https://i.imgur.com/iynl2lp.png"            
            ).set_footer(
                text="The King Motor",
                icon_url="https://i.imgur.com/ws748KD.png"
            )
        },
        {
            "hour": 19,
            "minute": 50,
            "id": "embed19",
            "embed": discord.Embed(
                title="**__¡En 10 minutos comienza una actividad__**",
                description="🚗 `Reparación industrial 4/4` — **20:00**",
                color=0xCDA939
            ).set_author(
                name="The King Motor",
                icon_url="https://i.imgur.com/ws748KD.png"
            ).add_field(
                name="**__Próxima actividad__**",
                value="\n🪛 `Entrega de herramientas 5/5` — **21:00**\n\n**〰️〰️〰️〰️〰️〰️**",
                inline=False
            ).set_thumbnail(
                url="https://i.imgur.com/ws748KD.png"
            ).set_image(
                url="https://i.imgur.com/s3zRf60.png"            
            ).set_footer(
                text="The King Motor",
                icon_url="https://i.imgur.com/ws748KD.png"
            )
        },
        {
            "hour": 20,
            "minute": 50,
            "id": "embed19",
            "embed": discord.Embed(
                title="**__¡En 10 minutos comienza una actividad__**",
                description="🪛 `Entrega de herramientas 5/5` — **21:00**",
                color=0xCDA939
            ).set_author(
                name="The King Motor",
                icon_url="https://i.imgur.com/ws748KD.png"
            ).add_field(
                name="**__Próxima actividad__**",
                value="\n🧰 `Reparación en carretera 6/6` — **22:00**\n\n**〰️〰️〰️〰️〰️〰️**",
                inline=False
            ).set_thumbnail(
                url="https://i.imgur.com/ws748KD.png"
            ).set_image(
                url="https://i.imgur.com/T7P4tFJ.png"            
            ).set_footer(
                text="The King Motor",
                icon_url="https://i.imgur.com/ws748KD.png"
            )
        },
        {
            "hour": 21,
            "minute": 50,
            "id": "embed20",
            "embed": discord.Embed(
                title="**__¡En 10 minutos comienza una actividad__**",
                description="🧰 `Reparación en carretera 6/6` — **22:00**",
                color=0xCDA939
            ).set_author(
                name="The King Motor",
                icon_url="https://i.imgur.com/ws748KD.png"
            ).add_field(
                name="**__Próxima actividad__**",
                value="\n🚗 `Reparación industrial 1/4` — **00:00**\n\n**〰️〰️〰️〰️〰️〰️**",
                inline=False
            ).set_thumbnail(
                url="https://i.imgur.com/ws748KD.png"
            ).set_image(
                url="https://i.imgur.com/d2wi2VG.png"            
            ).set_footer(
                text="The King Motor",
                icon_url="https://i.imgur.com/ws748KD.png"
            )
        }
    ]

    for item in scheduled_embeds:
        if utc_hour == item["hour"] and utc_minute == item["minute"] and sent_today.get(item["id"]) != today:
            channel = client.get_channel(CHANNEL_ID)
            if channel:
                await channel.send(f"<@&{ROLE_ID}>")
                await channel.send(embed=item["embed"])
                print(f"📨 Enviado {item['id']} a las {utc_hour}:{utc_minute} UTC")
                sent_today[item["id"]] = today

# Iniciar servidor Flask en segundo plano
threading.Thread(target=run_web).start()

client.run(os.getenv("DISCORD_TOKEN"))
