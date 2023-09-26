import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(
    command(["تنصيب","التنصيب","المصنع"])
    & filters.group
    & ~filters.edited
)
async def maker(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/73f9dd795b22c7cb670d6.jpg",
        caption=f"""🔱| سورس زد إي لتنـصـيب الـمـيوزك""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "تنصيب الميوزك", url=f"https://t.me/UI_XB"),
                    InlineKeyboardButton(
                        "تنصيب التليثون ♡", url=f"https://t.me/UI_XB/38"),
                ],
                [
                   InlineKeyboardButton(
                        "𝐒𝐎𝐔𝐑𝐂𝐄 • 𝐙𝐄 𖣒. 🔱 ", url=f"https://t.me/UI_XB"),
                ],       
            ]
        ),
    )