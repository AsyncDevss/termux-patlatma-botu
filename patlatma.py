import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.message_content = True  # Mesaj içeriğini okuyabilmesi için şart

bot = commands.Bot(command_prefix='!', intents=intents)

TOKEN = "BOT_TOKENINIZI_BURAYA_YAZIN"

@bot.event
async def on_ready():
    print(f"Bot {bot.user.name} olarak giriş yaptı!")
    print("--------------------------------------")
    print(" Yapımcı: Enes tarafından yapılmıştır. ")
    print("--------------------------------------")


@bot.command()
async def spam(ctx, *, text: str = None):
    if text is None:
        await ctx.send("❌ Spam yapmam için bir metin yazmalısın! Örnek: `!spam Selam`")
        return

    await ctx.send("🔄 Spam başlatılıyor... (Enes tarafından yapılmıştır.)")
    for _ in range(1500):  # 15 adet mesaj gönderir, isteğe göre değiştirebilirsin
        try:
            await ctx.send(text)
            await asyncio.sleep(0.3)  
        except:
            pass

# 2. !kanallar <isim>
@bot.command()
async def kanallar(ctx, *, isim: str = None):
    if isim is None:
        await ctx.send("❌ Oluşturulacak kanal adını yazmalısın! Örnek: `!kanallar test`")
        return

    await ctx.send("🛠️ Kanallar oluşturuluyor...")
    guild = ctx.guild
    for i in range(100):  
        try:
            await guild.create_text_channel(name=f"{isim}-{i+1}")
            await asyncio.sleep(0.3)
        except:
            pass

@bot.command()
async def roller(ctx, *, isim: str = None):
    if isim is None:
        await ctx.send("❌ Oluşturulacak rol adını yazmalısın! Örnek: `!roller Deneme`")
        return

    await ctx.send("🎨 Roller oluşturuluyor...")
    guild = ctx.guild
    for i in range(100): 
        try:
            await guild.create_role(name=f"{isim} {i+1}", reason="Enes Altyapısı")
            await asyncio.sleep(0.3)
        except:
            pass

bot.run(TOKEN)
