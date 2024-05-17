# test-bot(bot class)
# This example requires the 'members' and 'message_content' privileged intents to function.

import discord
import random
from discord.ext import commands
from bot_logic import gen_pass
import requests

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
# command prefix 
bot = commands.Bot(command_prefix='>', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

# adding two numbers
@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

# spamming word
@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)
        
# password generator        
@bot.command()
async def pw(ctx):
    await ctx.send(f'Kata sandi yang dihasilkan: {gen_pass(10)}')

# coinflip
@bot.command()
async def coinflip(ctx):
    num = random.randint(1,2)
    if num == 1:
        await ctx.send('It is Head!')
    if num == 2:
        await ctx.send('It is Tail!')

# rolling dice
@bot.command()
async def dice(ctx):
    nums = random.randint(1,6)
    if nums == 1:
        await ctx.send('It is 1!')
    elif nums == 2:
        await ctx.send('It is 2!')
    elif nums == 3:
        await ctx.send('It is 3!')
    elif nums == 4:
        await ctx.send('It is 4!')
    elif nums == 5:
        await ctx.send('It is 5!')
    elif nums == 6:
        await ctx.send('It is 6!')

# welcome message
@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def count(ctx, numbers: int):
    if numbers == 1:
        await ctx.send("1")

    elif numbers == 2:
        await ctx.send("1")
        await ctx.send("2")

    elif numbers == 3:
        await ctx.send("1")
        await ctx.send("2")
        await ctx.send("3")
    
    elif numbers == 4:
        await ctx.send("1")
        await ctx.send("2")
        await ctx.send("3")
        await ctx.send("4")
    
    elif numbers == 5:
        await ctx.send("1")
        await ctx.send("2")
        await ctx.send("3")
        await ctx.send("4")
        await ctx.send("5")
    
    elif numbers == 6:
        await ctx.send("1")
        await ctx.send("2")
        await ctx.send("3")
        await ctx.send("4")
        await ctx.send("5")
        await ctx.send("6")
    
    elif numbers == 7:
        await ctx.send("1")
        await ctx.send("2")
        await ctx.send("3")
        await ctx.send("4")
        await ctx.send("5")
        await ctx.send("6")
        await ctx.send("7")

    elif numbers == 8:
        await ctx.send("1")
        await ctx.send("2")
        await ctx.send("3")
        await ctx.send("4")
        await ctx.send("5")
        await ctx.send("6")
        await ctx.send("7")
        await ctx.send("8")
    
    elif numbers == 9:
        await ctx.send("1")
        await ctx.send("2")
        await ctx.send("3")
        await ctx.send("4")
        await ctx.send("5")
        await ctx.send("6")
        await ctx.send("7")
        await ctx.send("8")
        await ctx.send("9")
    
    elif numbers == 10:
        await ctx.send("1")
        await ctx.send("2")
        await ctx.send("3")
        await ctx.send("4")
        await ctx.send("5")
        await ctx.send("6")
        await ctx.send("7")
        await ctx.send("8")
        await ctx.send("9")
        await ctx.send("10")

@bot.command()
async def mem(ctx):
    randmeme = random.randint(1,3)
    if randmeme == 1:
        with open('Memes/mem1.jpg', 'rb') as f:
            # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
            picture = discord.File(f)
    # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
        await ctx.send(file=picture)
    elif randmeme == 2:
        with open('Memes/mem2.jpg', 'rb') as f:
            # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
            picture = discord.File(f)
    # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
        await ctx.send(file=picture)
    elif randmeme == 3:
        with open('Memes/mem3.jpg', 'rb') as f:
            # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
            picture = discord.File(f)
    # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
        await ctx.send(file=picture)

@bot.command()
async def mem1(ctx):
    rate = random.randint(1, 10)
    with open('Memes/mem1.jpg', 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)

@bot.command()
async def mem2(ctx):
    rate = random.randint(1, 10)
    with open('Memes/mem2.jpg', 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)

@bot.command()
async def mem3(ctx):
    rate = random.randint(1, 10)
    with open('Memes/mem3.jpg', 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)

# API to get random dog and duck image 
def get_dog_image_url():
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']
@bot.command('dog')
async def dog(ctx):
    '''Setiap kali permintaan dog (anjing) dipanggil, program memanggil fungsi get_dog_image_url'''
    image_url = get_dog_image_url()
    await ctx.send(image_url)
def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']
@bot.command('duck')
async def duck(ctx):
    '''Setiap kali permintaan duck (bebek) dipanggil, program memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def animal(ctx):
    with open('Memes/animal.jpg', 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)

@bot.command()
async def polusi(ctx):
    await ctx.send("https://sehatnegeriku.kemkes.go.id/baca/rilis-media/20230829/1543740/begini-upaya-sektor-kesehatan-tangani-polusi-udara/#:~:text=Kemenkes%20telah%20merilis%20protokol%20kesehatan%20pencegahan%20polusi%20udara,daring%2Fluring%20dengan%20tenaga%20kesehatan%20jika%20muncul%20keluhan%20pernapasan")

@bot.command()
async def sampah(ctx):
    await ctx.send("https://zerowaste.id/zero-waste-lifestyle/cara-memilah-sampah-di-rumah/")

@bot.command()
async def cmds(ctx):
    await ctx.send("Here's a list of commands that are in my systems:")
    await ctx.send("1. >add x y (x is left and y is right, only works with numbers!)")
    await ctx.send("2. >repeat x hi (x is the number that will repeat and hi is just an example)")
    await ctx.send("3. >pw (generates a new password)")
    await ctx.send("4. >coinflip (flips a coin)")
    await ctx.send("5. >dice (generates a number between 1-6)")
    await ctx.send("6. >count x (x is the number it will count to, only works to 10)")
    await ctx.send("7-9. >mem1, mem2, mem3 (post memes)")
    await ctx.send("10. >mem (post random memes)")
    await ctx.send("11. >dog (post dog pictures)")
    await ctx.send("12. >duck (post dog pictures)")
    await ctx.send("13. >animal (post an animal meme)")

# overwriting kalimat.txt
@bot.command()
async def tulis(ctx, *, my_string: str):
    with open('kalimat.txt', 'w', encoding='utf-8') as t:
        text = ""
        text += my_string
        t.write(text)
# append kalimat.txt
@bot.command()
async def tambahkan(ctx, *, my_string: str):
    with open('kalimat.txt', 'a', encoding='utf-8') as t:
        text = "\n"
        text += my_string
        t.write(text)
# reading kalimat.txt
@bot.command()
async def baca(ctx):
    with open('kalimat.txt', 'r', encoding='utf-8') as t:
        document = t.read()
        await ctx.send(document)

bot.run('')