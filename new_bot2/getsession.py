
from pyrogram import Client
from pyrogram import filters
from pyrogram import idle
from pyrogram import errors

from pyrogram.types import InlineKeyboardButton as button
from pyrogram.types import InlineKeyboardMarkup as markup
from pyrogram.types import ForceReply as reply

api_id, api_hash = 11319910, "13e94abcfd81630967c9f5cea0ffa6b3"
with Client("session_me",api_id,api_hash) as cli:
        cli.send_message("me","Log in session pyrogram")

            

