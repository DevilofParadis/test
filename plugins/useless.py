import os
import subprocess
import sys
from datetime import datetime
from pyrogram.types import Message
from pyromod import listen
from pyrogram import filters, Client
from config import ADMINS, BOT_STATS_TEXT, USER_REPLY_TEXT, CHANNEL_ADMINS, USELESS_TEXT, USELESS_TEXT2
from helper_func import get_readable_time
from database.database import channel_data, channel_dataa

@Bot.on_message(filters.command('stats') & filters.user(ADMINS))
async def stats(bot: Bot, message: Message):
    now = datetime.now()
    delta = now - bot.uptime
    time = get_readable_time(delta.seconds)
    await message.reply(BOT_STATS_TEXT.format(uptime=time))

@Bot.on_message(filters.command('addchannel') & filters.user(CHANNEL_ADMINS))
async def add_channel1(bot: Bot, message: Message):
    if '|' in message.text:
        await message.reply('fuck off bitch')
    else:
        channel1 = await bot.ask(message.chat.id, text="Give channel id of force sub channel. i.e -1001234678987")
        channel1 = channel1.text
        try:
            await channel_data.find_one_and_delete({'sub_channel1': USELESS_TEXT})
        except Exception as e:
            print(f'Error: {e}')
        try:
            cluster_add = {'sub_channel1': USELESS_TEXT, 'channel1': channel1}
            await channel_data.insert_one(cluster_add)
            await message.reply('Successfully Added. Now wait 1min until the bot gets restarted')
        except Exception as e:
            await bot.send_message('Your_ErenYeager', f'Error {e}')
        os.remove("Bot.session")
        os.remove("Bot.session-journal")
        os.execv(sys.executable, ["python3", "main.py"])

@Bot.on_message(filters.command('addchannel2') & filters.user(CHANNEL_ADMINS))
async def add_channel2(bot: Bot, message: Message):
    if '|' in message.text:
        await message.reply('fuck off bitch')
    else:
        channel2 = await bot.ask(message.chat.id, text="Give channel id of force sub channel. i.e -1001234678987")
        channel2 = channel2.text
        try:
            await channel_dataa.find_one_and_delete({'sub_channel2': USELESS_TEXT2})
        except Exception as e:
            print(f'Error: {e}')
        try:
            cluster_add = {'sub_channel2': USELESS_TEXT2, 'channel2': channel2}
            await channel_dataa.insert_one(cluster_add)
            await message.reply('Successfully Added. Now wait 1min until the bot gets restarted')
        except Exception as e:
            await bot.send_message('Your_ErenYeager', f'Error {e}')
        os.remove("Bot.session")
        os.remove("Bot.session-journal")
        os.execv(sys.executable, ["python3", "main.py"])

@Bot.on_message(filters.private & filters.incoming)
async def useless(_, message: Message):
    if USER_REPLY_TEXT:
        await message.reply(USER_REPLY_TEXT)
