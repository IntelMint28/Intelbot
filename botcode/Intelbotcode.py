import discord
import random
import string
import asyncio
import traceback
from discord.ext import commands



TOKEN = 0

DevelopmentBuild = False
if DevelopmentBuild == True:
    TOKEN = open("devtoken.txt", "r")
else:
    TOKEN = open("token.txt", "r")


intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='i?', intents=intents)



# --------------------------------------- CHANGELOG -----------------------------------------------
changelog = '''
# HAII CUTIES!!1! :3
intelbot has been reached v0.2.1, so pack up your ass, cause here are the new stuff :3

* What's new:
  * Added i?spamfooy [int]
      what it does is that ping-spams fooy, make sure the number you are going to set is not decimal.
  * Added i?changelog
      this command displays the changelog.

* BUGFIXES:
  * Fixed the 'i?wingdings [str]' command
'''
# ------------------------------------ END OF CHANGELOG -----------------------------------------------



Add_text = '''# Oh, so, do you want me on your own discord server?
Well, the link below will help you add me, so you can execute the most stupid commands ever!
> Click [HERE](OAUTH2 LINK HERE) to add me :3'''

BannedAccounts = []

Unsupported = False

rudeMessages = [
    'Why are you still existing here? Bro, get a life.',
    'I dont think you are 13 or above.',
    'Your opinion has not been considered because you suck at making opinions tho :sob:',
    'intel would told something better than that lol :wilted_rose:',
    'Can i please go near you and reorder your brain to make it work?'
    ]
help_text = \
'''## You don't know how to get started with IntelBot?
- Well i wrote this so people can know how to mess around with me! :3

> You can see all the existing commands at:
> https://sites.google.com/view/intelbot/commands-list

# Hope this helps moron!'''

badJokes = [
    '''# guys im touching discord settings
    ## > Kid named Discord settings:''',
    '# S K E L E T A L   J E R K I N I G A N S',
    'https://cdn.discordapp.com/attachments/1365723004616839201/1388009607569342574/image.png?ex=685f6c2e&is=685e1aae&hm=63d66cf2d2ee3b6388e9ccda3b916adff253bc30dc1bc044ebd4c36918ff88f7&',
    'what do you call a bee from the usa? a usb. ah. ah. ah.',
    'https://cdn.discordapp.com/attachments/1268366668384440352/1388166013178089664/cc2302dfaae45bf19e40df41323e6eb1.jpg?ex=685ffdd8&is=685eac58&hm=4f8616e7e03b7270f1be16854b928fa438622d95b857dcfd53a9234e91601b82&',
    'What do you call a person with no arms? An unarmed person.',
    'https://cdn.discordapp.com/attachments/1268366668384440352/1388166550317568144/654c16aff947ab17629f3059415ef02c.jpg?ex=685ffe58&is=685eacd8&hm=2b4631c6ce85db467786016517f6b6d741152240de68dda2036cff99e974b942&',
    'https://tenor.com/view/clown-hannibal-clown-meme-gif-746263137396848489',
    'https://cdn.discordapp.com/attachments/1268366668384440352/1388287384986189985/image.png?ex=68606ee1&is=685f1d61&hm=462953d263abc30116b4ce504db6609556acded7a2825ca79d9d7502733a8c25&',
    'https://cdn.discordapp.com/attachments/1268366668384440352/1388346741467779081/eb4.jpeg?ex=6860a629&is=685f54a9&hm=731de42d4a8bd384b70889040c81c7051ef39c5de8278f9518a1d85983385490&',
    'https://tenor.com/view/baldis-basic-baldi-ruler-hitting-spanking-gif-2834030865869804911',
    'https://media.discordapp.net/attachments/1268366668384440352/1372312428792254585/Screenshot_20250514_163930.png?ex=6860fbcb&is=685faa4b&hm=43ed62df2c48c84add05804e2044538740eb14caa0a9c6bbd5038801d4526a5f&=&format=webp&quality=lossless&width=819&height=662',
    'https://cdn.discordapp.com/attachments/1268366668384440352/1388596075824414750/IMG_7694.jpg?ex=68618e5f&is=68603cdf&hm=055da8ed98b4afd33d80022a80dd932050965e560add7d0053e8f1455aedd3c2&',
    'https://cdn.discordapp.com/attachments/1268366668384440352/1388604412293021796/314554d18342ef5291203a6d32c99100f372bfb3.mov?ex=68619622&is=686044a2&hm=bd914e448620a445f9ebc7a9e1599bb25393f2cdf4203e543bc7822f5a19193a&',
    'https://cdn.discordapp.com/attachments/1268368801892667412/1388630288514416821/audio.compress.mp4?ex=6861ae3c&is=68605cbc&hm=bb0783993ec83fa657a8f423479c016af29e1c987f57cae1c6d759ea57274fd3&',
    'https://media.discordapp.net/attachments/1268366668384440352/1388912537197744219/image.png?ex=6862b519&is=68616399&hm=75b1b97bfca24736a3dd20f93ab40a1d4e21562586fd6f63439991132b6e34c0&=&format=webp&quality=lossless&width=864&height=89'
    ]

ReadFileHelpText = '''# How does `i?readfile` works
> You should create a file on your desktop called _readfile.txt_ and write the contents of your message inside. Make sure to save the contents before closing.
> Then run: ```i?readfile``` and wait to the message you inserted in your txt file to appear.

## :warning: NOTE:
> if your txt file has python code, add `# py` to the code's start.'''

PhoenixLines = [
    '_hey kiddo... come here, near me; i promise im not doing nothing with you~_',
    'I would love you, only if you are under 18 and a girl; if you have both attributes, i may invite you to a date~',
    'phoenix wright is pedo yes or no'
]

# FUNCTIONS

def Serif(text):
    serifchars = str.maketrans('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', '𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙')
    return text.translate(serifchars)

def Italic(text):
    italicchars = str.maketrans('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙', '𝘢𝘣𝘤𝘥𝘦𝘧𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸𝘹𝘺𝘻𝘈𝘉𝘊𝘋𝘌𝘍𝘎𝘏𝘐𝘑𝘒𝘓𝘔𝘕𝘖𝘗𝘘𝘙𝘚𝘛𝘜𝘝𝘞𝘟𝘠𝘡𝒂𝒃𝒄𝒅𝒆𝒇𝒈𝒉𝒊𝒋𝒌𝒍𝒎𝒏𝒐𝒑𝒒𝒓𝒔𝒕𝒖𝒗𝒘𝒙𝒚𝒛𝑨𝑩𝑪𝑫𝑬𝑭𝑮𝑯𝑰𝑱𝑲𝑳𝑴𝑵𝑶𝑷𝑸𝑹𝑺𝑻𝑼𝑽𝑾𝑿𝒀𝒁')
    return text.translate(italicchars) 

def Mirror(text):
    mirrorchars = str.maketrans('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 'ɒdↄbɘʇϱʜiįʞlmᴎoqpᴙꙅɈυvwxγzAꓭↃꓷƎꟻӘHIႱꓘ⅃MИOꟼϘЯꙄTUVWXYZ')
    mirroredtext = text[::-1]
    return mirroredtext.translate(mirrorchars) 

def Bold(text):
    boldchars = str.maketrans('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ𝒶𝒷𝒸𝒹ℯ𝒻ℊ𝒽𝒾𝒿𝓀𝓁𝓂𝓃ℴ𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏𝒜ℬ𝒞𝒟ℰℱ𝒢ℋℐ𝒥𝒦ℒℳ𝒩𝒪𝒫𝒬ℛ𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵', '𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩')
    return text.translate(boldchars)

def Superitalic(text):
    superitalicchars = str.maketrans('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', '𝘢𝘣𝘤𝘥𝘦𝘧𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸𝘹𝘺𝘻𝘈𝘉𝘊𝘋𝘌𝘍𝘎𝘏𝘐𝘑𝘒𝘓𝘔𝘕𝘖𝘗𝘘𝘙𝘚𝘛𝘜𝘝𝘞𝘟𝘠𝘡')
    translation = text.translate(superitalicchars)
    superitalictext = f'_{translation}_'
    return superitalictext

def Script(text):
    scriptchars = str.maketrans('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', '𝒶𝒷𝒸𝒹ℯ𝒻ℊ𝒽𝒾𝒿𝓀𝓁𝓂𝓃ℴ𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏𝒜ℬ𝒞𝒟ℰℱ𝒢ℋℐ𝒥𝒦ℒℳ𝒩𝒪𝒫𝒬ℛ𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵')
    return text.translate(scriptchars)

def Fraktur(text):
    frakturchars = str.maketrans('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', '𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ')
    return text.translate(frakturchars)

def Smallcaps(text):
    smallchars = str.maketrans('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 'ᴀʙᴄᴅᴇꜰɢʜɪᴊᴋʟᴍɴᴏᴩꞯʀꜱᴛᴜᴠᴡxʏᴢABCDEFGHIJKLMNOPQRSTUVWXYZ')
    return text.translate(smallchars)

def Dstruck(text):
    struckchars = str.maketrans('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', '𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ')
    return text.translate(struckchars)

def Fwidth(text):
    widthchars = str.maketrans('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 'ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ')
    return text.translate(widthchars)

def Windings(text):
    normal_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    wingdings_chars = '♋♌♍♎♏♐♑♒♓🙰🙵●❍■□◻❑❒⬧⧫◆❖⬥⌧⍓⌘✌👌👍👎☜☞☝☟✋☺😐☹💣☠⚐🏱✈☼💧❄🕆✞🕈✠✡☪'
    
    trans_table = {normal_chars[i]: wingdings_chars[i] + '\uFE0E' for i in range(len(normal_chars))}

    wingdings_text = text.translate(str.maketrans(trans_table))
    return wingdings_text


@client.event
async def on_ready():
    if DevelopmentBuild == False:
        print('Intelbot is ready, hit "Ctrl + C" to stop')
    else:
        print('Development Build of Intelbot is ready, hit "Ctrl + C" to stop')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    
    if message.author.id in BannedAccounts:
        if message.content.startswith('i?'):
            MessageAuthorID = message.author.id
            MessageContent = message.content
            BannedMessage = f'''# Command "`{MessageContent}`"failed to execute!
## _Exception Information:_
> <@{MessageAuthorID}>, seems that your account got banned for IntelBot, and may vary the reasons.
> 
> You will not be able to use Intelbot, unless you get unbanned.

## Good luck tho!'''
            async with message.channel.typing():
                await message.channel.send(BannedMessage)
    elif Unsupported == False:
        if message.content == 'i?changelog':
            async with message.channel.typing():
                await message.channel.send(changelog)
        elif message.content == 'i?invitelink':
            async with message.channel.typing():
                random_text_disc = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
                await message.reply(f'https://discord.gg/{random_text_disc}') 
        elif message.content == 'i?randomyoutube':
            async with message.channel.typing():
                random_text_yt = ''.join(random.choices(string.ascii_letters + string.digits + '_' , k=11))
                await message.reply(f'https://www.youtube.com/watch?v={random_text_yt}')
        elif message.content == 'i?kindspanishmessage':
            async with message.channel.typing():
                await message.reply('https://cdn.discordapp.com/attachments/1370582084107767888/1387604041206595615/lv_0_20220501131853.mp4?ex=685e9b37&is=685d49b7&hm=e1251cb4ed2c6325f6c851e2fa83f4fb5cb99d5619d9f44ddac778fa72a5b9f4&')
        elif message.content == 'i?help':
            async with message.channel.typing():
                await message.reply(help_text)
        elif message.content == 'i?aubrey':
            async with message.channel.typing():
                await message.reply(f"{''.join(random.choice(rudeMessages))}\n-# this is pretty much probably what aubrey said for your response lol")
        elif '<@1387606948027039906>' in message.content:
            async with message.channel.typing():
                await message.reply('why did you ping me you fucking idiot')
        elif message.content == 'i?badjoke':
            async with message.channel.typing():
                await message.reply(f"{''.join(random.choice(badJokes))}")
        elif 'who is dyrs' in message.content:
            async with message.channel.typing():
                await message.reply("https://tenor.com/view/fnaf-fnaf-meme-fnaf-memes-five-nights-at-freddy's-nikolai-gif-14768080639478563321")
        elif 'i?gamble' in message.content:
            async with message.channel.typing():
                await message.reply('Sorry, im not adding gambling to this bot :wilted_rose:')
        elif 'i?gambling' in message.content:
            async with message.channel.typing():
                await message.reply('Sorry, im not adding gambling to this bot :wilted_rose:')
        elif message.content == 'i?embedtest':
            async with message.channel.typing():
                embedmessage = discord.Embed(title="Embed message test", description="Ts embed has been sent sucessfully!!!11!!1!", color=0x0000ff)
                await message.reply(embed=embedmessage)
        elif message.content == 'i?fart':
            async with message.channel.typing():
                await message.reply('*proceeds to fart*')
        elif 'Thinking Space II' in message.content:
            async with message.channel.typing():
                await message.reply('https://tenor.com/view/thinking-space-ii-thinking-space-2-alpha-react-geometry-dash-gif-16226532207789742856')
        elif message.content == 'i?iwanttoaddyou':
            async with message.channel.typing():
                await message.reply(Add_text)
        elif message.content == 'i?lore':
            async with message.channel.typing():
                await message.reply('https://cdn.discordapp.com/attachments/1365723004616839201/1388230226684940349/fnaf_movie_lore.mp4?ex=686039a6&is=685ee826&hm=2b27449e0b2a5628675d0392c8c82a7698ead2ca2bea0f1093231c7ec49a0977&')
        elif message.content == 'i?readfilehelp':
            async with message.channel.typing():
                await message.reply(ReadFileHelpText)
        elif message.content == 'i?readfile':
            async with message.channel.typing():
                embedmessage2 = discord.Embed(title="Access Denied", description="The command is still being developed, please wait until its done.", color=0xff0000)
                await message.reply(embed=embedmessage2)
        elif message.content == 'i?randomtext':
            async with message.channel.typing():
                random_text = ''.join(random.choices(string.ascii_letters + string.digits, k=1500))
                await message.reply(random_text)
        elif message.content == 'i?phoenixwright':
            async with message.channel.typing():
                await message.reply(f"{''.join(random.choice(PhoenixLines))}\n-# phoenix wright loves to date children")
        elif message.content.startswith('i?askage ') or message.content == ('i?askage'):
            if '<@' in message.content:
                OnlyPing = message.content.replace('i?askage ', '')
                async with message.channel.typing():
                    await message.reply(f"Hey {OnlyPing}, how old are you?")
            else:
                await message.reply('you missed the ping lmfao')
        elif message.content.startswith('i?serif '):
            OnlyMessage0 = message.content.replace('i?serif ', '')
            async with message.channel.typing():
                SerifText = Serif(OnlyMessage0)
                await message.reply(SerifText)
        elif message.content.startswith('i?italic '):
            OnlyMessage1 = message.content.replace('i?italic ', '')
            async with message.channel.typing():
                ItalicText = Italic(OnlyMessage1)
                await message.reply(ItalicText)
        elif message.content.startswith('i?bold '):
            OnlyMessage2 = message.content.replace('i?bold ', '')
            async with message.channel.typing():
                BoldText = Bold(OnlyMessage2)
                await message.reply(BoldText)
        elif message.content.startswith('i?superitalic '):
            OnlyMessage4 = message.content.replace('i?superitalic ', '')
            async with message.channel.typing():
                SuperitalicText = Superitalic(OnlyMessage4)
                await message.reply(SuperitalicText)
        elif message.content.startswith('i?mirror '):
            OnlyMessage5 = message.content.replace('i?mirror ', '')
            async with message.channel.typing():
                MirrorText = Mirror(OnlyMessage5)
                await message.reply(MirrorText)
        elif message.content.startswith('i?script '):
            OnlyMessage6 = message.content.replace('i?script ', '')
            async with message.channel.typing():
                ScriptText = Script(OnlyMessage6)
                await message.reply(ScriptText)
        elif message.content.startswith('i?fraktur '):
            OnlyMessage7 = message.content.replace('i?fraktur ', '')
            async with message.channel.typing():
                FrakturText = Fraktur(OnlyMessage7)
                await message.reply(FrakturText)
        elif message.content.startswith('i?smallcaps '):
            OnlyMessage8 = message.content.replace('i?smallcaps ', '')
            async with message.channel.typing():
                SmallcapsText = Smallcaps(OnlyMessage8)
                await message.reply(SmallcapsText)
        elif message.content.startswith('i?doublestruck '):
            OnlyMessage9 = message.content.replace('i?doublestruck ', '')
            async with message.channel.typing():
                DoublestruckText = Dstruck(OnlyMessage9)
                await message.reply(DoublestruckText)
        elif message.content.startswith('i?fullwidth '):
            OnlyMessage00 = message.content.replace('i?fullwidth ', '')
            async with message.channel.typing():
                FullwidthText = Fwidth(OnlyMessage00)
                await message.reply(FullwidthText)
        elif message.content.startswith('i?wingdings '):
            OnlyMessage01 = message.content.replace('i?wingdings ', '')
            async with message.channel.typing():
                WindingsText = Windings(OnlyMessage01)
                await message.reply(WindingsText)
        elif message.content.startswith('i?spamfooy '):
            OnlyNumber0 = int(message.content.replace('i?spamfooy ', ''))

            if OnlyNumber0 > 25:
                OnlyNumber0 = 25

            async def repeat(first=False):
                async with message.channel.typing():
                    if first == True:
                        await message.reply('<@1015031565950140457>')
                    else:
                        await message.channel.send('<@1015031565950140457>')
            
            
            for i in range(OnlyNumber0):
                if i == 0:
                    await repeat(first=True)
                else:
                    await repeat()
                await asyncio.sleep(0.5)
    elif message.content.startswith('i?'):
        if Unsupported:
            await message.channel.send('no')
        else:
            await message.reply(f'''# Command "`{message.content}`"failed to execute!
## _Exception Information:_
> The command you provided does not exist in the data.
> 
> Try fixing a typo, or use i?help to get the commands list

## ts pmo''')








client.run(TOKEN.read())
