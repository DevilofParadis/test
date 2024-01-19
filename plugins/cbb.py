from pyrogram import __version__
from bot import Bot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.reply_text(
            text = f"Bot For - <a href='https://t.me/Anime_Locus'>Anime Locus</a>\nMaster : <a href='https://t.me/YourErenYeager'>𝙀𝙧𝙚𝙣 𝙔𝙚𝙖𝙜𝙚𝙧 • 悪</a>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
        await query.message.delete()
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
