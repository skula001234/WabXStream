class script(object):
    START_TXT = """<b>Hᴇʏ {}, </b>\n\n<i>𝖲𝖾𝗇𝖽 𝗆𝖾 𝗒𝗈𝗎𝗋 𝖿𝗂𝗅𝖾 𝖿𝗈𝗋 𝗂𝗇𝗌𝗍𝖺𝗇𝗍𝗅𝗒 𝗀𝖾𝗇𝖾𝗋𝖺𝗍𝖾 𝗌𝗍𝗋𝖾𝖺𝗆 𝗅𝗂𝗇𝗄𝗌 & 𝗁𝗂𝗀𝗁 𝗌𝗉𝖾𝖾𝖽 𝖽𝗂𝗋𝖾𝖼𝗍 𝖽𝗈𝗐𝗇𝗅𝗈𝖺𝖽 𝗅𝗂𝗇𝗄𝗌.

𝖠𝖽𝖽 𝗆𝖾 𝗍𝗈 𝗒𝗈𝗎𝗋 𝖼𝗁𝖺𝗇𝗇𝖾𝗅 𝗍𝗈 𝗂𝗇𝗌𝗍𝖺𝗇𝗍𝗅𝗒 𝗀𝖾𝗇𝖾𝗋𝖺𝗍𝖾 𝗌𝗍𝗋𝖾𝖺𝗆 & 𝖽𝗈𝗐𝗇𝗅𝗈𝖺𝖽 𝗅𝗂𝗇𝗄𝗌 𝖿𝗈𝗋 𝗒𝗈𝗎 𝗎𝗉𝖼𝗈𝗆𝗂𝗇𝗀 𝖿𝗂𝗅𝖾𝗌 . 𝖨 𝗐𝗂𝗅𝗅 𝖺𝗎𝗍𝗈𝗆𝖺𝗍𝗂𝖼𝖺𝗅𝗅𝗒 𝖺𝗍𝗍𝖺𝖼𝗁 𝖺𝗉𝗉𝗋𝗈𝗉𝗋𝗂𝖺𝗍𝖾 𝖻𝗎𝗍𝗍𝗈𝗇 𝗍𝗈 𝗍𝗁𝖺 𝗉𝗈𝗌𝗍 𝖼𝗈𝗇𝗍𝖺𝗂𝗇𝗂𝗇𝗀 𝗍𝗁𝖾 𝖴𝖱𝖫..</i>\n\n<b><blockquote><a href=https://t.me/{}?startchannel&admin=post_messages+edit_messages+delete_messages>𝖠𝖽𝖽 𝖳𝗈 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 📣</a></blockquote></b>"""

    RESTART_TXT = """
<b>Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ !

📅 Dᴀᴛᴇ : <code>{}</code>
⏰ Tɪᴍᴇ : <code>{}</code>
🌐 Tɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code>
🛠️ Bᴜɪʟᴅ Sᴛᴀᴛᴜs: <code>v4.6.00 [ Sᴛᴀʙʟᴇ ]</code></b>"""

    HELP_TXT = """<b>ʏᴏᴜ ᴅᴏɴ'ᴛ ɴᴇᴇᴅ ᴍᴀɴʏ ᴄᴏᴍᴍᴇɴᴛs ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ \n\nᴊᴜsᴛ sᴇɴᴅ ᴍᴇ ғɪʟᴇs ᴀɴᴅ I ᴡɪʟʟ ɢɪᴠᴇ ʏᴏᴜ ᴅɪʀᴇᴄᴛ ʙᴏᴡɴʟᴏᴀᴅ & sᴛʀᴇᴀᴍɪɴɢ ʟɪɴᴋ\n\nᴀʟsᴏ ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴍᴇ ɪɴ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴀɴᴅ ᴍᴀᴋᴇ ᴍᴇ ᴀᴅᴍɪɴ ᴀɴᴅ sᴇᴇ ᴍʏ ᴘᴏᴡᴇʀ 💥\n\nғᴏʀ ᴍᴏʀᴇ, ᴜꜱᴇ /help ᴄᴏᴍᴍᴀɴᴅ\nᴍᴏʀᴇ, ᴜꜱᴇ /about ᴄᴏᴍᴍᴀɴᴅ</b>"""
    
    ADMIN_CMD_TXT = """<b>
    
Olay aman vishwakarma ne add Kiya hai 
  
# Admin Only Commands 👑  
/ban - Ban a user/channel [FOR ADMINS USE ONLY]  
/unban - Unban a user/channel [FOR ADMINS USE ONLY]  
/broadcast - Send broadcast message [FOR ADMINS USE ONLY]  
/pin_broadcast - Pin broadcast message [FOR ADMINS USE ONLY]  
/restart - Restart the bot [FOR ADMINS USE ONLY]  
/stats - Show bot statistics [FOR ADMINS USE ONLY]  
/blocked - List of blocked users [FOR ADMINS USE ONLY]  
/verified_users - List of verified users [FOR ADMINS USE ONLY]  

# Premium Control 💎  
/add_premium - Grant premium access to a user [ADMINS ONLY]  
/remove_premium - Remove premium access [ADMINS ONLY]
/premium_user - All premium user [ADMINS ONLY]</b>"""

    HELP2_TXT = """<b>Hᴏᴡ ᴛᴏ Uꜱᴇ Fɪʟᴇ ᴛᴏ Lɪɴᴋ Bᴏᴛ

Bᴀꜱɪᴄ Uꜱᴀɢᴇ:
• Sᴇɴᴅ ᴀɴʏ ғɪʟᴇ ᴏʀ ᴍᴇᴅɪᴀ ғʀᴏᴍ Tᴇʟᴇɢʀᴀᴍ
• Bᴏᴛ ᴡɪʟʟ ɢᴇɴᴇʀᴀᴛᴇ ᴘᴇʀᴍᴀɴᴇɴᴛ ᴅᴏᴡɴʟᴏᴀᴅ ᴀɴᴅ ꜱᴛʀᴇᴀᴍ ʟɪɴᴋꜱ
• Uꜱᴇ ᴛʜᴇꜱᴇ ʟɪɴᴋꜱ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴏʀ ꜱᴛʀᴇᴀᴍ ᴄᴏɴᴛᴇɴᴛ ᴛʜʀᴏᴜɢʜ ᴏᴜʀ ꜱᴇʀᴠᴇʀꜱ
• Fᴏʀ ꜱᴛʀᴇᴀᴍɪɴɢ, ᴘᴀꜱᴛᴇ ᴛʜᴇ ᴘʀᴏᴠɪᴅᴇᴅ ʟɪɴᴋ ɪɴ ᴀɴʏ ᴠɪᴅᴇᴏ ᴘʟᴀʏᴇʀ

Kᴇʏ Fᴇᴀᴛᴜʀᴇꜱ:
• Pᴇʀᴍᴀɴᴇɴᴛ ʟɪɴᴋ ɢᴇɴᴇʀᴀᴛɪᴏɴ
• Dɪʀᴇᴄᴛ ᴅᴏᴡɴʟᴏᴀᴅ ꜱᴜᴘᴘᴏʀᴛ 
• Vɪᴅᴇᴏ ꜱᴛʀᴇᴀᴍɪɴɢ ᴄᴀᴘᴀʙɪʟɪᴛʏ
• Cʜᴀɴɴᴇʟ ꜱᴜᴘᴘᴏʀᴛ (Aᴅᴅ ʙᴏᴛ ᴀꜱ ᴀᴅᴍɪɴ)
• Cᴜꜱᴛᴏᴍ ꜱʜᴏʀᴛᴇɴᴇʀ ɪɴᴛᴇɢʀᴀᴛɪᴏɴ
• Uɴʟɪᴍɪᴛᴇᴅ ғɪʟᴇ ꜱɪᴢᴇ ꜱᴜᴘᴘᴏʀᴛ

Cʜᴀɴɴᴇʟ Uꜱᴀɢᴇ:
𝟷. Aᴅᴅ ʙᴏᴛ ᴀꜱ ᴀᴅᴍɪɴ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ
𝟸. Bᴏᴛ ᴡɪʟʟ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴘʀᴏᴄᴇꜱꜱ ғɪʟᴇꜱ
𝟹. Lɪɴᴋꜱ ᴡɪʟʟ ʙᴇ ɢᴇɴᴇʀᴀᴛᴇᴅ ғᴏʀ ᴀʟʟ ᴍᴇᴅɪᴀ

⚠️ Iᴍᴘᴏʀᴛᴀɴᴛ Nᴏᴛᴇꜱ:
• Aʟʟ ʟɪɴᴋꜱ ᴀʀᴇ ᴘᴇʀᴍᴀɴᴇɴᴛ ᴀɴᴅ ᴡᴏɴ'ᴛ ᴇxᴘɪʀᴇ
• Sʜᴀʀɪɴɢ ɪɴᴀᴘᴘʀᴏᴘʀɪᴀᴛᴇ ᴄᴏɴᴛᴇɴᴛ ᴡɪʟʟ ʀᴇꜱᴜʟᴛ ɪɴ ᴘᴇʀᴍᴀɴᴇɴᴛ ʙᴀɴ
• Rᴇᴘᴏʀᴛ ᴀɴʏ ɪꜱꜱᴜᴇꜱ ᴛᴏ ᴏᴜʀ ꜱᴜᴘᴘᴏʀᴛ ᴛᴇᴀᴍ

🔞 ᴀᴅᴜʟᴛ ᴄᴏɴᴛᴇɴᴛ sᴛʀɪᴄᴛʟʏ ᴘʀᴏʜɪʙɪᴛᴇᴅ.

📮 Hᴇʟᴘ & Sᴜᴘᴘᴏʀᴛ:
• Uᴘᴅᴀᴛᴇꜱ: @AV_BOTz_UPDATE
• Sᴜᴘᴘᴏʀᴛ: @AV_SUPPORT_GROUP

 <u><i>ʀᴇᴘᴏʀᴛ ʙᴜɢs ᴛᴏ  <a href='https://t.me/AV_OWNER_BOT'>ᴅᴇᴠᴇʟᴏᴘᴇʀ</a></u></i></b>"""

    CAPTION = """🎬 <i><a href='{}'>{}</a></i>"""
    
    LOG_TEXT = """<b>#NewUser {}
    
ID - <code>{}</code>
Nᴀᴍᴇ - {}</b>"""

    ABOUT_TXT = """<b>╔══❰ {} ❱═════❍
║╭━━━━━━━━━━━━━━━━━━➣
║┣⪼🤖ᴍʏ ɴᴀᴍᴇ : {}
║┣⪼👦ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href='https://t.me/AV_OWNER_BOT'>ᴀᴠ ᴄʜᴀᴛ ᴏᴡɴᴇʀ</a>
║┣⪼❣️ᴜᴘᴅᴀᴛᴇ : <a href=https://t.me/AV_BOTz_UPDATE>ᴀᴠ ʙᴏᴛᴢ</a>
║┣⪼⏲️ʙᴏᴛ ᴜᴘᴛɪᴍᴇ :- {}
║┣⪼📡Hᴏsᴛᴇᴅ ᴏɴ : ᴋᴏʏᴇʙ 
║┣⪼🗣️ʟᴀɴɢᴜᴀɢᴇ : ᴘʏᴛʜᴏɴ 
║┣⪼📚ʟɪʙʀᴀʀʏ : ᴘʏʀᴏɢʀᴀᴍ
║┣⪼🗒️ᴠᴇʀsɪᴏɴ : {} [sᴛᴀʙʟᴇ]
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍ </b>"""

    AUTH_TXT = """<b> <blockquote> Wᴇʟᴄᴏᴍᴇ {} ✨</blockquote> \n\nꜱɪʀ ᴘʟᴇᴀꜱᴇ ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜꜱᴇ ᴍᴇ </>\n\n🌐  ᴅᴜᴇ ᴛᴏ ꜱᴇʀᴠᴇʀ ɪꜱꜱᴜᴇ ᴏɴʟʏ ᴄʜᴀɴɴᴇʟ\n🤖  ꜱᴜʙꜱᴄʀɪʙᴇᴇʀꜱ ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ʙᴏᴛ ...</b>"""
    
    CAPTION_TXT = """
<i><u>𝗬𝗼𝘂𝗿 𝗟𝗶𝗻𝗸 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱 !</u></i>

<b>📧 ꜰɪʟᴇ ɴᴀᴍᴇ :- </b> <i><a href={}>{}</a></i>

<b>📦 ꜰɪʟᴇ sɪᴢᴇ :- </b> <i>{}</i>

<b><u><i>Tap To Copy Link 👇</u></i></b>

<b>🖥 Stream  : </b> <code>{}</code>

<b>📥 Download : </b> <code>{}</code>

<b>🚸 Nᴏᴛᴇ : LINK WON'T EXPIRE TILL I DELETE 🤡</b>"""

    VERIFICATION_TEXT = """<b>👋 ʜᴇʏ {},

📌 <u>ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴠᴇʀɪꜰɪᴇᴅ ᴛᴏᴅᴀʏ, ᴛᴀᴘ ᴏɴ ᴛʜᴇ ᴠᴇʀɪꜰʏ ʟɪɴᴋ & ɢᴇᴛ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇss ꜰᴏʀ ɴᴇxᴛ ꜰᴜʟʟ ᴅᴀʏ.</u>

<blockquote>ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴅɪʀᴇᴄᴛ ꜰɪʟᴇs ᴛʜᴇɴ ʏᴏᴜ ᴄᴀɴ ᴛᴀᴋᴇ ᴘʀᴇᴍɪᴜᴍ sᴇʀᴠɪᴄᴇ (ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴠᴇʀɪꜰʏ)</blockquote>\n\n💶 ꜱᴇɴᴅ /plan ᴛᴏ ʙᴜʏ ꜱᴜʙꜱᴄʀɪᴘᴛɪᴏɴ</b>"""
    
    VERIFIED_COMPLETE_TEXT = """<b>👋 ʜᴇʏ {},

ʏᴏᴜ ᴀʀᴇ ɴᴏᴡ ᴠᴇʀɪꜰɪᴇᴅ ꜰᴏʀ ᴛᴏᴅᴀʏ ☺️.
ᴇɴᴊᴏʏ ᴜɴʟɪᴍɪᴛᴇᴅ ᴍᴏᴠɪᴇs ᴏʀ sᴇʀɪᴇs ʟɪɴᴋs 💥.

<blockquote>ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴅɪʀᴇᴄᴛ ꜰɪʟᴇs ᴛʜᴇɴ ʏᴏᴜ ᴄᴀɴ ᴛᴀᴋᴇ ᴘʀᴇᴍɪᴜᴍ sᴇʀᴠɪᴄᴇ (ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴠᴇʀɪꜰʏ)</blockquote></b>"""
    
    VERIFIED_LOG_TEXT = """<b><u>☄ ᴜsᴇʀ ᴠᴇʀɪꜰɪᴇᴅ sᴜᴄᴄᴇssꜰᴜʟʟʏ ☄</u>

⚡️ ɴᴀᴍᴇ:- {} [ <code>{}</code> ] 
📆 ᴅᴀᴛᴇ:- <code>{} </code></b>

#verified_completed"""
    
    CHECK_PLAN_TXT = """<b>👋 ʜᴇʏ {}
    
<blockquote>🎖️ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʀᴇᴍɪᴜᴍ ᴘʟᴀɴꜱ :</blockquote>

 ❏ 𝟶𝟹𝟿₹    ➠    𝟶𝟷 ᴍᴏɴᴛʜ
 ❏ 𝟷𝟷𝟶₹    ➠    𝟶𝟹 ᴍᴏɴᴛʜ
 ❏ 𝟹𝟼𝟶₹    ➠    𝟷𝟸 ᴍᴏɴᴛʜ

🆔 ᴜᴘɪ ɪᴅ ➩ <code>.......</code> [ᴛᴀᴘ ᴛᴏ ᴄᴏᴘʏ]
 
⛽️ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ: /myplan

🏷️ <a href='https://t.me/AV_PREMIUM_PROOF'>ᴘʀᴇᴍɪᴜᴍ ᴘʀᴏᴏꜰ</a>

‼️ ᴍᴜsᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ.
‼️ ɢɪᴠᴇ ᴜꜱ ꜱᴏᴍᴇᴛɪᴍᴇ ᴛᴏ ᴀᴅᴅ ʏᴏᴜ ɪɴ ᴘʀᴇᴍɪᴜᴍ ʟɪꜱᴛ.
</b>"""
    
    PREMIUM_TEXT = """<b>👋 ʜᴇʏ {}

<blockquote>🎁 ᴘʀᴇᴍɪᴜᴍ ғᴇᴀᴛᴜʀᴇ ʙᴇɴɪꜰɪᴛꜱ:</blockquote>

❏ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴏᴘᴇɴ ʟɪɴᴋꜱ
❏ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴠᴇʀɪғʏ
❏ ɢᴇᴛ ᴅɪʀᴇᴄᴛ ʟɪɴᴋs   
❏ ᴀᴅ-ғʀᴇᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇ 
❏ ʜɪɢʜ-sᴘᴇᴇᴅ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ                         
❏ ᴍᴜʟᴛɪ-ᴘʟᴀʏᴇʀ sᴛʀᴇᴀᴍɪɴɢ ʟɪɴᴋs                       
❏ ᴜɴʟɪᴍᴛᴇᴅ ғɪʟᴇs ɪɴ ᴀ ᴅᴀʏ                                                   
❏ ꜰᴜʟʟ ᴀᴅᴍɪɴ sᴜᴘᴘᴏʀᴛ                              
❏ ʀᴇǫᴜᴇsᴛ ᴡɪʟʟ ʙᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ɪɴ 𝟷ʜ [ ɪꜰ ᴀᴠᴀɪʟᴀʙʟᴇ ]

⛽️ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ: /myplan
</b>"""
