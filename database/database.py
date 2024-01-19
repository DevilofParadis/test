from motor import motor_asyncio
from config import DB_URI, DB_NAME

dbclient = motor_asyncio.AsyncIOMotorClient(DB_URI)
database = dbclient[DB_NAME]


user_data = database.users
channel_data = database.channel1
channel_dataa = database.channel2


async def present_user(user_id : int):
    found = await user_data.find_one({'_id': user_id})
    return bool(found)

async def add_user(user_id: int):
    await user_data.insert_one({'_id': user_id})
    return

async def full_userbase():
    user_docs = user_data.find()
    user_ids = []
    for doc in user_docs:
        user_ids.append(doc['_id'])
        
    return user_ids

async def del_user(user_id: int):
    await user_data.delete_one({'_id': user_id})
    return
   
async def find_channel_1(query):
    id = await channel_data.find_one({'sub_channel1': query})
    if id is not None:
        return id['channel1']
    else:
        return None
              
async def find_channel_2(query):
    id = await channel_dataa.find_one({'sub_channel2': query})
    if id is not None:
        return id['channel2']
    else:
        return None