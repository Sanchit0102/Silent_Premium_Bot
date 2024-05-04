import os
import config
import pyrogram
from pyrogram import Client, filters

Bot = Client(
    "Premium Bot",
    bot_token=config.BOT_TOKEN,
    api_id=config.API_ID,
    api_hash=config.API_HASH
)

START_TEXT = """<b>𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐓𝐨 𝐒𝐢𝐥𝐞𝐧𝐭 𝐏𝐫𝐞𝐦𝐢𝐮𝐦 𝐘𝐨𝐣𝐚𝐧𝐚</b>

<b><blockquote>🔥 𝐅𝐨𝐫 𝐌𝐨𝐯𝐢𝐞𝐬 🔥</blockquote></b>

𝟷. Gᴇᴛ Aʟʟ Nᴇᴡ/Oʟᴅ Mᴏᴠɪᴇꜱ ᴀɴᴅ Sᴇʀɪᴇꜱ !
𝟸. Gᴇᴛ Sᴏᴍᴇ Aᴜᴅɪᴏ Bᴏᴏᴋ 📚 📖
𝟹. Oɴʟʏ Lᴀᴛᴇꜱᴛ Tᴠ Rᴇᴀʟɪᴛʏ Sʜᴏᴡꜱ (Nᴏᴛ Sᴇʀɪᴀʟ)
𝟺. Gᴇᴛ Aʟʟ Nᴇᴡ/Oʟᴅ Aɴɪᴍᴇꜱ !
𝟻. Gᴇᴛ Aʟʟ Nᴇᴡ/Oʟᴅ Cᴀʀᴛᴏᴏɴꜱ !

<b>Prices: 2 month - 100₹ 
             3 month - 150₹ 
             6 month -  300₹</b>

<b><blockquote>🔞 𝐅𝐨𝐫 𝐏@𝐫𝐧 / 𝟏𝟖+ 𝐕𝐢𝐝𝐞𝐨𝐬 🔞</blockquote></b>

𝟷. Dᴇꜱɪ & Vɪᴅᴇꜱʜɪ Vɪᴅᴇᴏꜱ (Bʀᴀᴢᴢᴇʀꜱ, Pᴏʀɴʜᴜʙ & Mᴏʀᴇ)
𝟸. Oᴛᴛ Aᴅᴜʟᴛ Vɪᴅᴇᴏꜱ (Uʟʟᴜ, Aʟᴛ, Rᴀʙʙɪᴛ & Mᴏʀᴇ)
𝟹. Aᴅᴜʟᴛ Cᴏᴍɪᴄꜱ (Sᴀᴠɪᴛᴀ ʙʜᴀʙʜɪ, Vᴇʟᴀᴍᴍᴀ, ᴇᴛᴄ) 
𝟺. 𝟷𝟾+ Mᴏᴠɪᴇꜱ
𝟻. Lᴇᴀᴋᴇᴅ & Vɪʀᴀʟ Vɪᴅᴇᴏꜱ

<b>Prices: 1 month - 75₹ 
             2 month - 150₹ 
             3 month - 200₹</b>
             
<b><blockquote>💥 𝐅𝐨𝐫 𝐁𝐨𝐭𝐡 [𝐌𝐨𝐯𝐢𝐞𝐬 + 𝟏𝟖+ 𝐕𝐢𝐝𝐞𝐨] 💥</b></blockquote>

Oᴜʀ Bᴇꜱᴛ & Cʜᴇᴀᴘ Sᴜʙꜱᴄʀɪᴘᴛɪᴏɴ ❤️‍🔥
Cᴏᴍʙɪɴᴇᴅ Pʟᴀɴ [Mᴏᴠɪᴇꜱ + 𝟷𝟾+ Vɪᴅᴇᴏ] 
Tᴏᴘ Pʟᴀɴ ⭐️

<b>Prices: 2 month - 180₹
             3 month - 280₹
             6 month - 580₹</b>

<b>आपको जो Membership लेनी है वो नीचे लिखके भेजिए !</b>"""

@Bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT,
        disable_web_page_preview=True
    )
