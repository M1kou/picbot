#!/usr/bin/env python
# coding: utf-8
import requests
import json
import random
from discord.ext import commands


headers = {"User_Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0",
           "Accpet":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
           "Cookie":""}
token = ''

bot = commands.Bot(command_prefix='!')

def get_imglink(tag=""):
    tag = tag.join("+").replace(":","%3A")
    url = 'https://yande.re/post.json?tags=order%3Arandom+'
    html = requests.get(url+tag,headers=headers)
    print(url+tag)
    json_to_dict = json.loads(html.text)
    random_img = random.choice(json_to_dict)
    link = random_img['file_url']
    return link

@bot.command(name='pic')
async def pic(ctx):
    await ctx.send(' I heard you! {0} {1}'.format(ctx.author,get_imglink()))

@bot.command(name='tag')
async def pic_tag(ctx,*tags):
    try:
        await ctx.send(' I heard you! {0} {1}'.format(ctx.author,get_imglink(tags)))
    except IndexError:
        await ctx.send('Nobody here but us chickens!')


bot.run(token) 
