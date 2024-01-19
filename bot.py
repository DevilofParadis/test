from pyrogram import Client
from pyrogram.enums import ParseMode
import sys
from datetime import datetime
from database.database import find_channel_1, find_channel_2, channel_data, channel_dataa

from config import API_HASH, APP_ID, LOGGER, CHANNEL_ID, USELESS_TEXT, USELESS_TEXT2, TG_BOT_TOKEN

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={
                "root": "plugins"
            },
            sleep_threshold=0,
            bot_token=TG_BOT_TOKEN
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()
        FORCE_SUB_CHANNEL = await find_channel_1(USELESS_TEXT)
        FORCE_SUB_CHANNEL2 = await find_channel_2(USELESS_TEXT2)    
        
        if FORCE_SUB_CHANNEL is not None:
            try:
                link = (await self.get_chat(FORCE_SUB_CHANNEL)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_CHANNEL)
                    link = (await self.get_chat(FORCE_SUB_CHANNEL)).invite_link
                self.invitelink = link        
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("Bot can't Export Invite link from Force Sub Channel!")
                self.LOGGER(__name__).warning(f"Please Double check the FORCE_SUB_CHANNEL value and Make sure Bot is Admin in channel with Invite Users via Link Permission, Current Force Sub Channel Value: {FORCE_SUB_CHANNEL}")
                self.LOGGER(__name__).info("\nBot Stopped")
                
        if FORCE_SUB_CHANNEL2 is not None: 
            try:
                link = (await self.get_chat(FORCE_SUB_CHANNEL2)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_CHANNEL2)
                    link = (await self.get_chat(FORCE_SUB_CHANNEL2)).invite_link
                self.invitelink2 = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("Bot can't Export Invite link from Force Sub Channel!")
                self.LOGGER(__name__).warning(f"Please Double check the FORCE_SUB_CHANNEL value and Make sure Bot is Admin in channel with Invite Users via Link Permission, Current Force Sub Channel Value: {FORCE_SUB_CHANNEL}")
                self.LOGGER(__name__).info("\nBot Stopped")
                try:
                    channel_data.find_one_and_delete({'sub_channel1':USELESS_TEXT})
                    channel_dataa.find_one_and_delete({'sub_channel2':USELESS_TEXT2})
                    self.LOGGER(__name__).info("\nForceSub database also cleared. Try to run the bot again and add channel")
                except Exception as db:
                    self.LOGGER(__name__).info("\nFORCE SUB DB ERROR")
                    self.LOGGER(__name__).warning(db)
                    pass
                sys.exit()

        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id = db_channel.id, text = "Test Message")
            await test.delete()
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning(f"Make Sure bot is Admin in DB Channel, and Double check the CHANNEL_ID Value, Current Value {CHANNEL_ID}")
            self.LOGGER(__name__).info("\nBot Stopped. Join https://t.me/Anime_Locus for support")
            sys.exit()

        self.set_parse_mode(ParseMode.HTML)
        self.LOGGER(__name__).info(f"Bot Running..!\n\nCreated by \nhttps://t.me/Anime_Locus")
        self.username = usr_bot_me.username

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped.")
