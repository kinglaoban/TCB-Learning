from discord import Webhook, RequestsWebhookAdapter, Embed
import datetime
import random
def balko_send_wehook():
    url = str(input_wehook)
    webhook = Webhook.from_url(url, adapter=RequestsWebhookAdapter())
    embed = Embed(title='Success - '+str(input_shoes),color=2699323)
    embed.add_field(name="Size", value=str(input_size), inline=True)
    embed.add_field(name="Product", value=str(input_shoes), inline=True)
    embed.add_field(name="Delay", value='10', inline=True)
    embed.add_field(name="Profile", value=str(input_profile), inline=False)
    embed.add_field(name="Tasks", value='10', inline=False)
    embed.set_footer(
        icon_url='https://cdn.discordapp.com/attachments/618450257692459008/699229474369175612/9whojPiW_400x400.jpg',
        text='Balkobot')
    embed.set_thumbnail(
        url=str(input_img))
    webhook.send(embed=embed, username=str(input_authorname),
                 avatar_url=str(input_touxiang))
#balko_send_wehook()
def tks_send_wehook(content):
    url = str(input_wehook)
    webhook = Webhook.from_url(url, adapter=RequestsWebhookAdapter())
    embed = Embed(title='You cooked', color=10181046)
    embed.add_field(name="Website", value='Yeezysupply', inline=True)
    embed.add_field(name="Product", value=str(input_shoes), inline=True)
    embed.add_field(name="Size", value=str(input_size), inline=True)
    embed.add_field(name="Price", value='1122211', inline=True)
    embed.add_field(name="Link", value='https://twitter.com/Meow_cook/status/1247722940579418118', inline=True)
    embed.add_field(name="Profile", value=str(input_profile), inline=True)
    embed.add_field(name="Proxy", value='||1122211||', inline=True)
    embed.add_field(name="Time stamp(utc)", value=str(datetime.datetime.utcnow()), inline=True)
    embed.add_field(name="Order id", value='||1122211||', inline=True)
    embed.add_field(name="Checkout Delay", value='0', inline=True)

    embed.set_thumbnail(
        url=str(input_img))
    webhook.send(content,embed=embed, username=str(input_authorname),
                 avatar_url=str(input_touxiang))
#tks_send_wehook(content='Success:'+str(datetime.datetime.utcnow()))

def Cyber_send_webhook():
    url = str(input_wehook)
    webhook = Webhook.from_url(url, adapter=RequestsWebhookAdapter())
    embed = Embed(title='Successfully checked out!',color=5290067)
    embed.description = str(input_shoes)
    embed.add_field(name="Store", value='Yeezysupply', inline=True)
    embed.add_field(name="Size", value=str(input_size), inline=True)
    embed.add_field(name="Profile",value=str(input_profile), inline=True)
    embed.add_field(name="Order", value='||1122211||', inline=True)
    embed.add_field(name="ProxyList", value='||nyc 3.0||', inline=True)
    embed.add_field(name="Mode", value='fast 2', inline=True)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_thumbnail(url=str(input_img))
    embed.add_field(name="Store", value="YS")
    embed.set_footer(icon_url='https://cdn.discordapp.com/attachments/618450257692459008/699214656211910666/P98ia02p_400x400.jpg',text='CyberAIO')
    webhook.send(embed=embed, username=str(input_authorname),  avatar_url=str(input_touxiang))



choose_bot=input('please choose one bot :Cyber,Tks,Balko')
input_wehook=input('please input your wehook link:')
input_shoes=input("please input your shoes'name:")
input_size=input('your size:')
input_profile=input('your profile name:')
input_img=input('your img link:')
input_authorname=input('your name:')
input_touxiang=input('your photo:')
if choose_bot.lower() == 'cyber':
    Cyber_send_webhook()
elif choose_bot.lower() == 'tks':
    tks_send_wehook(content='Success:' + str(input_shoes))
elif choose_bot.lower() == 'balko':
    balko_send_wehook()
else:
    print('ops something wrong!')

