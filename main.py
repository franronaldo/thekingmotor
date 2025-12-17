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
                description="🪛 `Revisión de seguridad 1/2` — **00:00**\n📷 `Reparación de cámaras 1/4` — **00:00**",
                color=0xCDA939
            ).set_author(
                name="Essencurity INC",
                icon_url="https://i.imgur.com/KidLx3S.png"
            ).add_field(
                name="**__Próxima actividad__**",
                value="\n🚗 `Servicio de escolta 1/5` — **01:00**\n\n**〰️〰️〰️〰️〰️〰️**",
                inline=False
            ).set_thumbnail(
                url="https://i.imgur.com/KidLx3S.png"
            ).set_image(
                url="https://i.imgur.com/vooataA.png"
            ).set_footer(
                text="Essency Company - Essencurity INC",
                icon_url="https://i.imgur.com/KidLx3S.png"
            )
        },
        {
            "hour": 0,
            "minute": 50,
            "id": "embed2",
            "embed": discord.Embed(
                title="**__¡En 10 minutos comienza la actividad!__**",
                description="🚗 `Servicio de escolta 1/5` — **01:00**",
                color=0xCDA939
            ).set_author(
                name="Essencurity INC",
                icon_url="https://i.imgur.com/KidLx3S.png"
            ).add_field(
                name="**__Próxima actividad__**",
                value="\n💰 `Reabastecer cajeros 1/7` — **02:00**\n🚨 `Instalación de alarmas 1/5` — **02:00**\n\n**〰️〰️〰️〰️〰️〰️**",
                inline=False
            ).set_thumbnail(
                url="https://i.imgur.com/KidLx3S.png"
            ).set_image(
                url="https://i.imgur.com/OUSCGno.png"
            ).set_footer(
                text="Essency Company - Essencurity INC",
                icon_url="https://i.imgur.com/KidLx3S.png"
            )
        },
        {
            "hour": 1,
            "minute": 50,
            "id": "embed3",
            "embed": discord.Embed(
                title="**__¡En 10 minutos comienza la actividad!__**",
                description="💰 `Reabastecer cajeros 1/7` — **02:00**\n🚨 `Instalación de alarmas 1/5` — **02:00**",
                color=0xCDA939
            ).set_author(
                name="Essencurity INC",
                icon_url="https://i.imgur.com/KidLx3S.png"
            ).add_field(
                name="**__Próxima actividad__**",
                value="\n🚨 `Instalación de alarmas 2/5` — **03:00**\n\n**〰️〰️〰️〰️〰️〰️**",
                inline=False
            ).set_thumbnail(
                url="https://i.imgur.com/KidLx3S.png"
            ).set_image(
                url="https://i.imgur.com/ZhoiLEt.png"
            ).set_footer(
                text="Essency Company - Essencurity INC",
                icon_url="https://i.imgur.com/KidLx3S.png"
            )
        },
        {
            "hour": 2,
            "minute": 50,
            "id": "embed4",
            "embed": discord.Embed(
                title="**__¡En 10 minutos comienza la actividad!__**",
                description="🚨 `Instalación de alarmas 2/5` — **03:00**",
                color=0xCDA939
            ).set_author(
                name="Essencurity INC",
                icon_url="https://i.imgur.com/KidLx3S.png"
            ).add_field(
                name="**__Próxima actividad__**",
                value="\n🚗 `Servicio de escolta 2/5` — **04:00**\n\n**〰️〰️〰️〰️〰️〰️**",
                inline=False
            ).set_thumbnail(
                url="https://i.imgur.com/KidLx3S.png"
            ).set_image(
                url="https://i.imgur.com/atBgLpE.png"
            ).set_footer(
                text="Essency Company - Essencurity INC",
                icon_url="https://i.imgur.com/KidLx3S.png"
            )
        },
        {
            "hour": 3,
            "minute": 50,
            "id": "embed5",
            "embed": discord.Embed(
                title="**__¡En 10 minutos comienza la actividad!__**",
                description="🚗 `Servicio de escolta 2/5` — **04:00**",
                color=0xCDA939
            ).set_author(
                name="Essencurity INC",
                icon_url="https://i.imgur.com/KidLx3S.png"
            ).add_field(
                name="**__Próxima actividad__**",
                value="\n🚨 `Instalación de alarmas 3/5` — **05:00**\n\n**〰️〰️〰️〰️〰️〰️**",
                inline=False
            ).set_thumbnail(
                url="https://i.imgur.com/KidLx3S.png"
            ).set_image(
                url="https://i.imgur.com/OUSCGno.png"
            ).set_footer(
                text="Essency Company - Essencurity INC",
                icon_url="https://i.imgur.com/KidLx3S.png"
            )
        },
        {
            "hour": 4,
            "minute": 50,
            "id": "embed6",
            "embed": discord.Embed(
                title="**__¡En 10 minutos comienza la actividad!__**",
                description="🚨 `Instalación de alarmas 3/5` — **05:00**",
                color=0xCDA939
            ).set_author(
                name="Essencurity INC",
                icon_url="https://i.imgur.com/KidLx3S.png"
            ).add_field(
                name="**__Próxima actividad__**",
                value="\n💰 `Reabastecer cajeros 2/7` — **06:00**\n\n**〰️〰️〰️〰️〰️〰️**",
                inline=False
            ).set_thumbnail(
                url="https://i.imgur.com/KidLx3S.png"
            ).set_image(
                url="https://i.imgur.com/atBgLpE.png"
            ).set_footer(
                text="Essency Company - Essencurity INC",
                icon_url="https://i.imgur.com/KidLx3S.png"
            )
        },
        {
            "hour": 5,
            "minute": 50,
            "id": "embed7",
            "embed": discord.Embed(
                title="**__¡En 10 minutos comienza una actividad — X2!__**",
                description="**Deben haber minimo 4 personas para unirse antes de iniciarla, el no hacer caso a esta regla puede conllevar a sanción. En caso que no haya presencia, se puede iniciar 06:55 en adelante para que haya tiempo en realizarla.**\n\n💰 `Reabastecer cajeros 2/7` — **06:00**",
                color=0xCDA939
            ).set_author(
                name="Essencurity INC",
                icon_url="https://i.imgur.com/KidLx3S.png"
            ).add_field(
                name="**__Próxima actividad — X2__**",
                value="\n💰 `Reabastecer cajeros 3/7` — **08:00**\n\n**〰️〰️〰️〰️〰️〰️**",
                inline=False
            ).set_thumbnail(
                url="https://i.imgur.com/KidLx3S.png"
            ).set_image(
                url="https://i.imgur.com/5QgpiHo.png"
            ).set_footer(
                text="Essency Company - Essencurity INC",
                icon_url="https://i.imgur.com/KidLx3S.png"
            )
        },
        {
            "hour": 7,
            "minute": 50,
            "id": "embed8",
            "embed": discord.Embed(
                title="**__¡En 10 minutos comienza una actividad — X2!__**",
                description="**Deben haber minimo 4 personas para unirse antes de iniciarla, el no hacer caso a esta regla puede conllevar a sanción. En caso que no haya presencia, se puede iniciar 08:55 en adelante para que haya tiempo en realizarla.**\n\n💰 `Reabastecer cajeros 3/7` — **08:00**",
                color=0xCDA939
            ).set_author(
                name="Essencurity INC",
                icon_url="https://i.imgur.com/KidLx3S.png"
            ).add_field(
                name="**__Próxima actividad — X2__**",
                value="\n💰 `Reabastecer cajeros 4/7` — **10:00**\n\n**〰️〰️〰️〰️〰️〰️**",
                inline=False
            ).set_thumbnail(
                url="https://i.imgur.com/KidLx3S.png"
            ).set_image(
                url="https://i.imgur.com/5QgpiHo.png"            
            ).set_footer(
                text="Essency Company - Essencurity INC",
                icon_url="https://i.imgur.com/KidLx3S.png"
            )
        },
        {
            "hour": 9,
            "minute": 50,
            "id": "embed9",
            "embed": discord.Embed(
                title="**__¡En 10 minutos comienza una actividad — X2!__**",
                description="**Deben haber minimo 4 personas para unirse antes de iniciarla, el no hacer caso a esta regla puede conllevar a sanción. En caso que no haya presencia, se puede iniciar 10:55 en adelante para que haya tiempo en realizarla.**\n\n💰 `Reabastecer cajeros 4/7` — **10:00**",
                color=0xCDA939
            ).set_author(
                name="Essencurity INC",
                icon_url="https://i.imgur.com/KidLx3S.png"
            ).add_field(
                name="**__Próxima actividad — X2__**",
                value="\n🚨 `Instalación de alarmas 4/5` — **11:00**\n\n**〰️〰️〰️〰️〰️〰️**",
                inline=False
            ).set_thumbnail(
                url="https://i.imgur.com/KidLx3S.png"
            ).set_image(
                url="https://i.imgur.com/5QgpiHo.png"            
            ).set_footer(
                text="Essency Company - Essencurity INC",
                icon_url="https://i.imgur.com/KidLx3S.png"
            )
        },
        {
            "hour": 10,
            "minute": 50,
            "id": "embed10",
            "embed": discord.Embed(
                title="**__¡En 10 minutos comienza una actividad — X2!__**",
                description="🚨 `Instalación de alarmas 4/5` — **11:00**",
                color=0xCDA939
            ).set_author(
                name="Essencurity INC",
                icon_url="https://i.imgur.com/KidLx3S.png"
            ).add_field(
                name="**__Próxima actividad — X2__**",
                value="\n📷 `Reparación de cámaras 2/4` — **12:00**\n\n**〰️〰️〰️〰️〰️〰️**",
                inline=False
            ).set_thumbnail(
                url="https://i.imgur.com/KidLx3S.png"
            ).set_image(
                url="https://i.imgur.com/atBgLpE.png"            
            ).set_footer(
                text="Essency Company - Essencurity INC",
                icon_url="https://i.imgur.com/KidLx3S.png"
            )
        },
        {
            "hour": 11,
            "minute": 50,
            "id": "embed11",
            "embed": discord.Embed(
                title="**__¡En 10 minutos comienza una actividad — X2!__**",
                description="📷 `Reparación de cámaras 2/4` — **12:00**",
                color=0xCDA939
            ).set_author(
                name="Essencurity INC",
                icon_url="https://i.imgur.com/KidLx3S.png"
            ).add_field(
                name="**__Próxima actividad — X2__**",
                value="\n💰 `Reabastecer cajeros 5/7` — **13:00**\n\n**〰️〰️〰️〰️〰️〰️**",
                inline=False
            ).set_thumbnail(
                url="https://i.imgur.com/KidLx3S.png"
            ).set_image(
                url="https://i.imgur.com/55wIj54.png"            
            ).set_footer(
                text="Essency Company - Essencurity INC",
                icon_url="https://i.imgur.com/KidLx3S.png"
            )
        },
        {
            "hour": 12,
            "minute": 50,
            "id": "embed12",
            "embed": discord.Embed(
                title="**__¡En 10 minutos comienza una actividad — X2!__**",
                description="**Deben haber minimo 4 personas para unirse antes de iniciarla, el no hacer caso a esta regla puede conllevar a sanción. En caso que no haya presencia, se puede iniciar 13:55 en adelante para que haya tiempo en realizarla.**\n\n💰 `Reabastecer cajeros 5/7` — **13:00**",
                color=0xCDA939
            ).set_author(
                name="Essencurity INC",
                icon_url="https://i.imgur.com/KidLx3S.png"
            ).add_field(
                name="**__Próxima actividad__**",
                value="\n🚗 `Servicio de escolta 3/5` — **15:00**\n\n**〰️〰️〰️〰️〰️〰️**",
                inline=False
            ).set_thumbnail(
                url="https://i.imgur.com/KidLx3S.png"
            ).set_image(
                url="https://i.imgur.com/5QgpiHo.png"            
            ).set_footer(
                text="Essency Company - Essencurity INC",
                icon_url="https://i.imgur.com/KidLx3S.png"
            )
        },
        {
            "hour": 14,
            "minute": 50,
            "id": "embed13",
            "embed": discord.Embed(
                title="**__¡En 10 minutos comienza una actividad__**",
                description="🚗 `Servicio de escolta 3/5` — **15:00**",
                color=0xCDA939
            ).set_author(
                name="Essencurity INC",
                icon_url="https://i.imgur.com/KidLx3S.png"
            ).add_field(
                name="**__Próxima actividad__**",
                value="\n📷 `Reparación de cámaras 3/4` — **16:00**\n\n**〰️〰️〰️〰️〰️〰️**",
                inline=False
            ).set_thumbnail(
                url="https://i.imgur.com/KidLx3S.png"
            ).set_image(
                url="https://i.imgur.com/OUSCGno.png"            
            ).set_footer(
                text="Essency Company - Essencurity INC",
                icon_url="https://i.imgur.com/KidLx3S.png"
            )
        },
        {
            "hour": 15,
            "minute": 50,
            "id": "embed14",
            "embed": discord.Embed(
                title="**__¡En 10 minutos comienza una actividad__**",
                description="📷 `Reparación de cámaras 3/4` — **16:00**",
                color=0xCDA939
            ).set_author(
                name="Essencurity INC",
                icon_url="https://i.imgur.com/KidLx3S.png"
            ).add_field(
                name="**__Próxima actividad__**",
                value="\n🪛 `Revisión de seguridad 2/2` — **17:00**\n\n**〰️〰️〰️〰️〰️〰️**",
                inline=False
            ).set_thumbnail(
                url="https://i.imgur.com/KidLx3S.png"
            ).set_image(
                url="https://i.imgur.com/55wIj54.png"            
            ).set_footer(
                text="Essency Company - Essencurity INC",
                icon_url="https://i.imgur.com/KidLx3S.png"
            )
        },
        {
            "hour": 16,
            "minute": 50,
            "id": "embed15",
            "embed": discord.Embed(
                title="**__¡En 10 minutos comienza una actividad__**",
                description="🪛 `Revisión de seguridad 2/2` — **17:00**",
                color=0xCDA939
            ).set_author(
                name="Essencurity INC",
                icon_url="https://i.imgur.com/KidLx3S.png"
            ).add_field(
                name="**__Próxima actividad__**",
                value="\n💰 `Reabastecer cajeros 6/7` — **18:00**\n\n**〰️〰️〰️〰️〰️〰️**",
                inline=False
            ).set_thumbnail(
                url="https://i.imgur.com/KidLx3S.png"
            ).set_image(
                url="https://i.imgur.com/evQdLAH.png"            
            ).set_footer(
                text="Essency Company - Essencurity INC",
                icon_url="https://i.imgur.com/KidLx3S.png"
            )
        },
        {
            "hour": 17,
            "minute": 50,
            "id": "embed16",
            "embed": discord.Embed(
                title="**__¡En 10 minutos comienza una actividad__**",
                description="**Deben haber mínimo 4 personas para unirse antes de iniciarla, el no hacer caso a esta regla puede conllevar a sanción. En caso que no haya presencia, se puede iniciar 18:55 en adelante para que haya tiempo en realizarla.**\n\n💰 `Reabastecer cajeros 6/7` — **18:00**",
                color=0xCDA939
            ).set_author(
                name="Essencurity INC",
                icon_url="https://i.imgur.com/KidLx3S.png"
            ).add_field(
                name="**__Próxima actividad__**",
                value="\n📷 `Reparación de cámaras 4/4` — **19:00**\n\n**〰️〰️〰️〰️〰️〰️**",
                inline=False
            ).set_thumbnail(
                url="https://i.imgur.com/KidLx3S.png"
            ).set_image(
                url="https://i.imgur.com/5QgpiHo.png"            
            ).set_footer(
                text="Essency Company - Essencurity INC",
                icon_url="https://i.imgur.com/KidLx3S.png"
            )
        },
        {
            "hour": 18,
            "minute": 50,
            "id": "embed17",
            "embed": discord.Embed(
                title="**__¡En 10 minutos comienza una actividad__**",
                description="📷 `Reparación de cámaras 4/4` — **19:00**",
                color=0xCDA939
            ).set_author(
                name="Essencurity INC",
                icon_url="https://i.imgur.com/KidLx3S.png"
            ).add_field(
                name="**__Próxima actividad__**",
                value="\n🚗 `Servicio de escolta 4/5` — **20:00**\n\n**〰️〰️〰️〰️〰️〰️**",
                inline=False
            ).set_thumbnail(
                url="https://i.imgur.com/KidLx3S.png"
            ).set_image(
                url="https://i.imgur.com/55wIj54.png"            
            ).set_footer(
                text="Essency Company - Essencurity INC",
                icon_url="https://i.imgur.com/KidLx3S.png"
            )
        },
        {
            "hour": 19,
            "minute": 50,
            "id": "embed18",
            "embed": discord.Embed(
                title="**__¡En 10 minutos comienza una actividad__**",
                description="🚗 `Servicio de escolta 4/5` — **20:00**",
                color=0xCDA939
            ).set_author(
                name="Essencurity INC",
                icon_url="https://i.imgur.com/KidLx3S.png"
            ).add_field(
                name="**__Próxima actividad__**",
                value="\n🚗 `Servicio de escolta 5/5` — **21:00**\n\n**〰️〰️〰️〰️〰️〰️**",
                inline=False
            ).set_thumbnail(
                url="https://i.imgur.com/KidLx3S.png"
            ).set_image(
                url="https://i.imgur.com/OUSCGno.png"            
            ).set_footer(
                text="Essency Company - Essencurity INC",
                icon_url="https://i.imgur.com/KidLx3S.png"
            )
        },
        {
            "hour": 20,
            "minute": 50,
            "id": "embed19",
            "embed": discord.Embed(
                title="**__¡En 10 minutos comienza una actividad__**",
                description="🚗 `Servicio de escolta 5/5` — **21:00**",
                color=0xCDA939
            ).set_author(
                name="Essencurity INC",
                icon_url="https://i.imgur.com/KidLx3S.png"
            ).add_field(
                name="**__Próxima actividad__**",
                value="\n💰 `Reabastecer cajeros 7/7` — **22:00**\n🚨 `Instalación de alarmas 5/5` — **22:00**\n\n**〰️〰️〰️〰️〰️〰️**",
                inline=False
            ).set_thumbnail(
                url="https://i.imgur.com/KidLx3S.png"
            ).set_image(
                url="https://i.imgur.com/OUSCGno.png"            
            ).set_footer(
                text="Essency Company - Essencurity INC",
                icon_url="https://i.imgur.com/KidLx3S.png"
            )
        },
        {
            "hour": 21,
            "minute": 50,
            "id": "embed20",
            "embed": discord.Embed(
                title="**__¡En 10 minutos comienza una actividad__**",
                description="💰 `Reabastecer cajeros 7/7` — **22:00**\n🚨 `Instalación de alarmas 5/5` — **22:00**",
                color=0xCDA939
            ).set_author(
                name="Essencurity INC",
                icon_url="https://i.imgur.com/KidLx3S.png"
            ).add_field(
                name="**__Próxima actividad__**",
                value="\n🪛 `Revisión de seguridad 1/2` — **00:00**\n📷 `Reparación de cámaras 1/4` — **00:00**\n\n**〰️〰️〰️〰️〰️〰️**",
                inline=False
            ).set_thumbnail(
                url="https://i.imgur.com/KidLx3S.png"
            ).set_image(
                url="https://i.imgur.com/ZhoiLEt.png"            
            ).set_footer(
                text="Essency Company - Essencurity INC",
                icon_url="https://i.imgur.com/KidLx3S.png"
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
