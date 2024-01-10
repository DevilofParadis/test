#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.errors import MessageIdInvalid
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    msg = None  # Initialize msg variable before the try block
    if data == "about":
        try:
            if msg is not None:
                await msg.edit(content)  
            else:
                
                pass
        except MessageIdInvalid:
            msg = await message.reply(content)  # Assuming `msg` is defined somewhere in your code
            await query.message.edit_text(
                text=f"Bot For - <a href='https://t.me/Anime_Locus'>Anime Locus</a>\nMaster : <a href='https://t.me/YourErenYeager'>𝙀𝙧𝙚𝙣 𝙔𝙚𝙖𝙜𝙚𝙧 • 悪</a>",
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🔒 Close", callback_data="close")
                        ]
                    ]
                )
            )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass  # Handle exception if needed
