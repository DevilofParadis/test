#(©)CodeXBotz




import pymongo, os
import subprocess
from config import DB_URI, DB_NAME, CHANNEL_ADMINS, USELESS_TEXT, USELESS_TEXT2
from pyrogram import Client, filters, __version__
from pyrogram.enums import ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import FloodWait, UserIsBlocked, InputUserDeactivated


dbclient = pymongo.MongoClient(DB_URI)
database = dbclient[DB_NAME]


user_data = database['users']
channel_data = database['channel1']
channel_data = database['channel2']



async def present_user(user_id : int):
    found = user_data.find_one({'_id': user_id})
    return bool(found)

async def add_user(user_id: int):
    user_data.insert_one({'_id': user_id})
    return

async def full_userbase():
    user_docs = user_data.find()
    user_ids = []
    for doc in user_docs:
        user_ids.append(doc['_id'])
        
    return user_ids

async def del_user(user_id: int):
    user_data.delete_one({'_id': user_id})
    return
    

        
        
def find_channel_1(query):
    NOTHING = 0
    id = channel1.find_one({'sub_channel1':query})
    if id is not None:
        channel1_id = int(id['channel1'])
        return channel1_id
    else:
        return None
              
def find_channel_2(query):
    NOTHING = 0
    id = channel2.find_one({'sub_channel2':query})
    if id is not None:
        channel2_id = int(id['channel2'])
        return channel2_id
    else:
        return None
