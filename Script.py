class script(object):   
    HELP_TXT = """<b>нαʏ {}, нєʀє ιѕ τнє нєʟᴘ ғοʀ мʏ ϲοммαɴᴅѕ..🔰</b>"""

    ABOUT_TXT = """<b>╭────🔰 𝐀𝐁𝐎𝐔𝐓 𝐌𝐄 🔰──────
‣ мʏ ɴαмє :-: {}
‣ мʏ ϲʀєατοʀ ʙʏ :-: <a href=https://t.me/TG_x_filter>🇮🇳ᴍᴀɴᴛɪs™◢ ◤</a>
‣ ʟαɴɢυαɢє :-: ᴘʏτнοɴ3
‣ ᴅαταʙαѕє :-: мοɴɢο ᴅʙ
‣ мʏ ѕυᴘᴘοʀτ :-: <a href=https://t.me/Bot_Mechanic_Updates>ϲʟιϲκ нєʀє</a>
╰─────────────────────</b>"""

    SOURCE_TXT = """<b>🍿𝗝𝗼𝗶𝗻 𝗢𝘂𝗿 𝗖𝗵𝗮𝗻𝗻𝗲𝗹𝘀 𝗚𝗿𝗼𝘂𝗽𝘀 𝗢𝘁𝘁 𝗨𝗽𝗱𝗮𝘁𝗲𝘀👇</b>"""


    FILE_TXT = """𝗛𝗲𝗹𝗽 :-: 𝗙𝗶𝗹𝗲 𝗦𝘁𝗼𝗿𝗲 𝗠𝗼𝗱𝘂𝗹𝗲.../

𝗕𝘆 𝗨𝘀𝗶𝗻𝗴 𝗧𝗵𝗶𝘀 𝗠𝗼𝗱𝘂𝗹𝗲 𝗬𝗼𝘂 𝗖𝗮𝗻 𝗦𝘁𝗼𝗿𝗲 𝗙𝗶𝗹𝗲𝘀 𝗜𝗻 𝗠𝘆 𝗗𝗮𝘁𝗮𝗯𝗮𝘀𝗲 𝗔𝗻𝗱 𝗜 𝗪𝗶𝗹𝗹 𝗚𝗶𝘃𝗲 𝗬𝗼𝘂 𝗔 𝗣𝗲𝗿𝗺𝗮𝗻𝗲𝗻𝘁 𝗟𝗶𝗻𝗸 𝗧𝗼 𝗔𝗰𝗰𝗲𝘀𝘀 𝗧𝗵𝗲 𝗦𝗮𝘃𝗲𝗱 𝗙𝗶𝗹𝗲𝘀. 𝗜𝗳 𝗬𝗼𝘂 𝗪𝗮𝗻𝘁 𝗧𝗼 𝗔𝗱𝗱 𝗙𝗶𝗹𝗲𝘀 𝗙𝗿𝗼𝗺 𝗔 𝗣𝘂𝗯𝗹𝗶𝗰 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 𝗦𝗲𝗻𝗱 𝗧𝗵𝗲 𝗙𝗶𝗹𝘄𝗹𝗶𝗻𝗸 𝗢𝗻𝗹𝘆 𝗢𝗿 𝗬𝗼𝘂 𝗪𝗮𝗻𝘁 𝗧𝗼 𝗔𝗱𝗱 𝗙𝗶𝗹𝗲𝘀 𝗙𝗿𝗼𝗺 𝗔 𝗣𝗿𝗶𝘃𝗮𝘁𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 𝗬𝗼𝘂 𝗠𝘂𝘀𝘁 𝗠𝗮𝗸𝗲 𝗠𝗲 𝗔𝗱𝗺𝗶𝗻 𝗢𝗻 𝗧𝗵𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 𝗧𝗼 𝗔𝗰𝗰𝗲𝘀𝘀 𝗙𝗶𝗹𝗲𝘀...//

𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦 𝗔𝗡𝗗 𝗨𝗦𝗔𝗚𝗘👇

• /plink ≈ 𝗥𝗲𝗽𝗹𝘆 𝗧𝗼 𝗔𝗻𝘆 𝗠𝗲𝗱𝗶𝗮 𝗧𝗼 𝗚𝗲𝘁 𝗟𝗶𝗻𝗸.
• /pbatch ≈ 𝗨𝗲𝘀 𝗬𝗼𝘂𝗿 𝗠𝗲𝗱𝗶𝗮 𝗟𝗶𝗻𝗸 𝗪𝗶𝘁𝗵 𝗧𝗵𝗶𝘀 𝗖𝗼𝗺𝗺𝗮𝗻𝗱
• /batch ≈ 𝗧𝗼 𝗖𝗿𝗲𝗮𝘁𝗲 𝗟𝗶𝗻𝗸 𝗙𝗼𝗿 𝗠𝘂𝗹𝘁𝗶𝗽𝗹𝗲 𝗙𝗶𝗹𝗲𝘀.

 𝗘𝗫𝗔𝗠𝗣𝗟𝗘👇

<code>/𝗯𝗮𝘁𝗰𝗵 𝗵𝘁𝘁𝗽𝘀://𝘁.𝗺𝗲/+𝗭𝗶𝗗𝗲𝗲𝗡9𝘆𝘂𝗯𝗸5𝗡𝗗𝗵𝗹</code>"""
    MANUELFILTER_TXT = """𝗛𝗲𝗹𝗽 :-: 𝗙𝗶𝗹𝘁𝗲𝗿𝘀

≈ 𝗙𝗶𝗹𝘁𝗲𝗿 𝗜𝘀 𝗧𝗵𝗲 𝗙𝗲𝗮𝘁𝘂𝗿𝗲 𝗪𝗲𝗿𝗲 𝗨𝘀𝗲𝗿𝘀 𝗖𝗮𝗻 𝗦𝗲𝘁 𝗔𝘂𝘁𝗼𝗺𝗮𝘁𝗲𝗱 𝗥𝗲𝗽𝗹𝗶𝗲𝘀 𝗙𝗼𝗿 𝗔 𝗣𝗮𝗿𝘁𝗶𝗰𝘂𝗹𝗮𝗿 𝗞𝗲𝘆𝘄𝗼𝗿𝗱 𝗪𝗶𝗹𝗹 𝗥𝗲𝘀𝗽𝗼𝗻𝗱 𝗪𝗵𝗲𝗻𝗲𝘃𝗲𝗿 𝗔 𝗞𝗲𝘆𝘄𝗼𝗿𝗱 𝗜𝘀 𝗙𝗼𝘂𝗻𝗱 𝗧𝗵𝗲 𝗠𝗲𝘀𝘀𝗮𝗴𝗲

𝗡𝗢𝗧𝗘👇

1• 𝗧𝗵𝗶𝘀 𝗕𝗼𝘁 𝗦𝗵𝗼𝘂𝗹𝗱 𝗛𝗮𝘃𝗲 𝗔𝗱𝗺𝗶𝗻 𝗣𝗿𝗶𝘃𝗶𝗹𝗲𝗴𝗲𝘀.
2• 𝗢𝗻𝗹𝘆 𝗔𝗱𝗺𝗶𝗻 𝗖𝗮𝗻 𝗔𝗱𝗱 𝗙𝗶𝗹𝘁𝗲𝗿𝘀 𝗜𝗻 𝗔 𝗖𝗵𝗮𝘁.
3• 𝗔𝗹𝗲𝗿𝘁 𝗕𝘂𝘁𝘁𝗼𝗻 𝗛𝗮𝘃𝗲 𝗔 𝗟𝗶𝗺𝗶𝘁 𝗢𝗳 64 𝗖𝗵𝗮𝗿𝗮𝗰𝘁𝗲𝗿𝘀.

𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦 𝗔𝗡𝗗 𝗨𝗦𝗔𝗚𝗘👇

• /filter ≈ <code>𝗔𝗱𝗱 𝗔 𝗙𝗶𝗹𝘁𝗲𝗿 𝗶𝗻 𝗖𝗵𝗮𝘁</code>
• /filters ≈ <code>𝗟𝗶𝘀𝘁 𝗔𝗹𝗹 𝗧𝗵𝗲 𝗙𝗶𝗹𝘁𝗲𝗿𝘀 𝗢𝗳 𝗔 𝗖𝗵𝗮𝘁</code>
• /del ≈ <code>𝗗𝗲𝗹𝗲𝘁𝗲 𝗧𝗵𝗲 𝗦𝗽𝗲𝗰𝗶𝗳𝗶𝗰 𝗙𝗶𝗹𝘁𝗲𝗿 𝗶𝗻 𝗖𝗵𝗮𝘁</code>
• /delall ≈ <code>𝗗𝗲𝗹𝗲𝘁𝗲 𝗧𝗵𝗲 𝗪𝗵𝗼𝗹𝗲 𝗙𝗶𝗹𝘁𝗲𝗿𝘀 𝗶𝗻 𝗮 𝗖𝗵𝗮𝘁 (𝗖𝗵𝗮𝘁 𝗢𝘄𝗻𝗲𝗿 𝗢𝗻𝗹𝘆)</code>

• <code> /g_filter </code> 𝗢𝗳𝗳 𝗨𝘀𝗲 𝗧𝗵𝗶𝘀 𝗖𝗼𝗺𝗺𝗮𝗻𝗱 + 𝗢𝗻/𝗢𝗳𝗳 𝗶𝗻 𝗬𝗼𝘂𝗿 𝗚𝗿𝗼𝘂𝗽 𝗧𝗼 𝗖𝗼𝗻𝘁𝗿𝗼𝗹 𝗚𝗹𝗼𝗯𝗮𝗹 𝗙𝗶𝗹𝘁𝗲𝗿 𝗶𝗻 𝗬𝗼𝘂𝗿 𝗚𝗿𝗼𝘂𝗽."""
   
    BUTTON_TXT = """ʜᴇʟᴘ : <b>ʙᴜᴛᴛᴏɴs</b>

‣ ᴛʜɪs ʙᴏᴛ sᴜᴘᴘᴏʀᴛs ʙᴏᴛʜ ᴜʀʟ ᴀɴᴅ ᴀʟᴇʀᴛ ɪɴʟɪɴᴇ ʙᴜᴛᴛᴏɴs.

<b>ɴᴏᴛᴇ ➾</b>

1. ᴛᴇʟᴇɢʀᴀᴍ ᴡɪʟʟ ɴᴏᴛ ᴀʟʟᴏᴡs ʏᴏᴜ ᴛᴏ sᴇɴᴅ ʙᴜᴛᴛᴏɴs ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴄᴏɴᴛᴇɴᴛ, sᴏ ᴄᴏɴᴛᴇɴᴛ ɪs ᴍᴀɴᴅᴀᴛᴏʀʏ.
2. ᴛʜɪs ʙᴏᴛ sᴜᴘᴘᴏʀᴛs ʙᴜᴛᴛᴏɴs ᴡɪᴛʜ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇᴅɪᴀ ᴛʏᴘᴇ.
3. ʙᴜᴛᴛᴏɴs sʜᴏᴜʟᴅ ʙᴇ ᴘʀᴏᴘᴇʀʟʏ ᴘᴇsᴇᴅ ᴀs ᴍᴀʀᴋᴅᴏᴡɴ ғᴏʀᴍᴀᴛ

<b>ᴜʀʟ ʙᴜᴛᴛᴏɴs ➾</b>

<code>[ʙᴜᴛᴛᴏɴ ᴛᴇxᴛ](buttonurl: ᴀɴᴛʀ ʏᴏᴜʀ ʙᴜᴛᴛᴏɴᴜʀʟ)</code>

<b>ᴀʟᴇʀᴛ ʙᴜᴛᴛᴏɴs ➾</b>

<code>[ʙᴜᴛᴛᴏɴ ᴛᴇxᴛ](buttonalert: ᴛʜɪs ɪs ᴀɴ ᴀʟᴇʀᴛ ᴍᴇssᴀɢᴇ)</code>"""

    AUTOFILTER_TXT = """ᴀᴜᴛᴏ ғɪʟᴛᴇʀ ᴏɴ/ᴏғғ ᴍᴏᴅᴜʟᴇ
ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ
〰〰〰〰〰〰〰〰〰〰〰〰〰

‣ /autofilter ᴏɴ - ᴀᴜᴛᴏғɪʟᴛᴇ ᴇɴᴀʙʟᴇ ɪɴ ʏᴏᴜʀ ᴄʜᴀᴛ
‣ /autofilter ᴏғғ - ᴀᴜᴛᴏғɪʟᴛᴇʀ ᴅɪsᴀʙʟᴇ ɪɴ ʏᴏᴜʀ ᴄʜᴀᴛ

ᴀᴜᴛᴏ ғɪʟᴛᴇʀ ɪs ᴛʜᴇ ғᴇᴀᴛᴜʀᴇ ᴛᴏ ғɪʟᴛᴇʀ ᴀɴᴅ sᴀᴠᴇ ᴛʜᴇ ғɪʟᴇs ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ғʀᴏᴍ ᴄʜᴀɴɴᴇʟ ᴛᴏ ɢʀᴏᴜᴘ. ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ ᴄᴏᴍᴍᴀɴᴅs ᴛᴏ ᴏɴ ᴀɴᴅ ᴏғғ ᴛʜᴇ ᴀᴜᴛᴏғɪʟᴛᴇʀ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ..../

ᴄᴏᴍᴍᴀɴᴅs ➾
‣ /set_template - sᴇᴛ ᴄᴜsᴛᴏᴍ ɪᴍᴅʙ ᴛᴇᴍᴘʟᴀᴛᴇ ғᴏʀ ᴀᴜᴛᴏ ғɪʟᴛᴇʀ
‣ /get_template - ɢᴇᴛ ᴄᴜʀʀᴇɴᴛ ɪᴍᴅʙ ᴛᴇᴍᴘʟᴀᴛᴇ ᴏғ ᴀᴜᴛᴏ ғɪʟᴛᴇʀ

"""

    CONNECTION_TXT = """ʜᴇʟᴘ : <b>ᴄᴏɴɴᴇᴄᴛɪᴏɴs</b>

- ᴜsᴇᴅ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʙᴏᴛ ᴛᴏ ᴘᴍ ғᴏʀ ᴍᴀɴᴀɢɪɴɢ ғɪʟᴛᴇʀs
- ɪᴛ ʜᴇʟᴘs ᴛᴏ ᴀᴠᴏɪᴅ sᴘᴀᴍᴍɪɴɢ ɪɴ ɢʀᴏᴜᴘs.

<b>ɴᴏᴛᴇ ➾</b>

1. ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴀᴅᴅ ᴀ ᴄᴏɴɴᴇᴄᴛɪᴏɴ.
2. sᴇɴᴅ <code>/connect</code> ғᴏʀ ᴄᴏɴɴᴇᴄᴛɪɴɢ ᴍᴇ ᴛᴏ ᴜʀ ᴘᴍ

<b>ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ᴜsᴇɢᴇ ➾</b>

‣  /connect - <code>ᴄᴏɴɴᴇᴄᴛ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴄʜᴀᴛ ᴛᴏ ʏᴏᴜʀ ᴘᴍ</code>
‣ /disconnect - <code>ᴅɪsᴄᴏɴɴᴇᴄᴛ ғʀᴏᴍ ᴀ ᴄʜᴀᴛ</code>
‣ /connections - <code>ʟɪsᴛ ᴀʟʟ ʏᴏᴜʀ ᴄᴏɴɴᴇᴄᴛɪᴏɴs</code>"""

    EXTRAMOD_TXT = """ʜᴇʟᴘ : <b>ᴇxᴛʀᴀ ᴍᴏᴅᴜʟᴇs</b>

<b>ɴᴏᴛᴇ ➾</b>
ᴛʜᴇsᴇ ᴀʀᴇ ᴛʜᴇ ᴇxᴛʀᴀ ғᴇᴀᴛᴜʀᴇs ᴏғ ᴛʜɪs ʙᴏᴛ

<b>ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ᴜsᴀɢᴇ ➾</b>
‣ /id - <code>ɢᴇᴛ ɪᴅ ᴏғ ᴀ sᴘᴇᴄɪғᴇᴅ ᴜsᴇʀ.</code>
‣ /info - <code>ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴀ ᴜsᴇʀ.</code>
‣ /imdb - <code>ɢᴇᴛ ᴛʜᴇ ғɪʟᴍ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ғʀᴏᴍ ɪᴍᴅʙ sᴏᴜʀᴄᴇ.</code>
‣ /search - <code>ɢᴇᴛ ᴛʜᴇ ғɪʟᴍ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ғʀᴏᴍ ᴠᴀʀɪᴏᴜs sᴏᴜʀᴄᴇ.</code>"""

    ADMIN_TXT = """<b>ɴᴏᴛᴇ:</b>
<code>Tʜɪs Mᴏᴅᴜʟᴇ Oɴʟʏ Wᴏʀᴋs Fᴏʀ Mʏ Aᴅᴍɪɴs</code>

🔋 <u><b>Basic Command</b></u>
• /logs - <code>ᴛᴏ ɢᴇᴛ ᴛʜᴇ ʀᴇᴄᴇɴᴛ ᴇʀʀᴏʀꜱ</code>
• /stats - <code>ᴛᴏ ɢᴇᴛ ꜱᴛᴀᴛᴜꜱ ᴏꜰ ꜰɪʟᴇꜱ ɪɴ ᴅʙ.</code>

🗂️ <u><b>Database & Server Command</b></u>
• /status - <code>ᴛᴏ ɢᴇᴛ sᴛᴀᴛᴜs ᴏғ sᴇʀᴠᴇʀ</code>
• /stats - <code>ᴛᴏ ɢᴇᴛ ᴅᴀᴛᴀᴛʙᴀꜱᴇ ꜱᴛᴀᴛᴜꜱ</code>
• /delete - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴇ ꜰʀᴏᴍ ᴅʙ.</code>
• /deleteall - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀʟʟ ꜰɪʟᴇs ꜰʀᴏᴍ ᴅʙ.</code>
• /users - <code>ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴍʏ ᴜꜱᴇʀꜱ ᴀɴᴅ ɪᴅꜱ.</code>
• /chats - <code>ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴍʏ ᴄʜᴀᴛꜱ ᴀɴᴅ ɪᴅꜱ</code>
• /channel - <code>ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴛᴏᴛᴀʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴄʜᴀɴɴᴇʟꜱ</code>"""

    US_CHAT_TXT = """<b>ɴᴏᴛᴇ:</b>
<code>Tʜɪs Mᴏᴅᴜʟᴇ Oɴʟʏ Wᴏʀᴋs Fᴏʀ Mʏ Aᴅᴍɪɴs</code>

📯 <u><b>Chat & User</b></u>
• /broadcast - <code>ᴛᴏ ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴀʟʟ ᴜꜱᴇʀꜱ</code>
• /group_broadcast - <code>ᴛᴏ ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ɢʀᴏᴜᴘs</code>
• /leave  - <code>ᴛᴏ ʟᴇᴀᴠᴇ ꜰʀᴏᴍ ᴀ ᴄʜᴀᴛ.</code>
• /disable  -  <code>ᴛᴏ ᴅɪꜱᴀʙʟᴇ ᴀ ᴄʜᴀᴛ.</code>
• /invite - <code>Tᴏ ɢᴇᴛ ᴛʜᴇ ɪɴᴠɪᴛᴇ ʟɪɴᴋ ᴏғ ᴀɴʏ ᴄʜᴀᴛ ᴡʜᴇʀᴇ ᴛʜᴇ ʙᴏᴛ ɪs ᴀᴅᴍɪɴ.</code>
• /ban_user  - <code>ᴛᴏ ʙᴀɴ ᴀ ᴜꜱᴇʀ.</code>
• /unban_user  - <code>ᴛᴏ ᴜɴʙᴀɴ ᴀ ᴜꜱᴇʀ.</code>
• /restart - <code>Tᴏ Rᴇsᴛᴀʀᴛ ᴀ Bᴏᴛ</code>
• /usend - <code>Tᴏ Sᴇɴᴅ ᴀ Mᴇssɢᴀᴇ ᴛᴏ Pᴇʀᴛɪᴄᴜʟᴀʀ Usᴇʀ</code>
• /gsend - <code>Tᴏ Sᴇɴᴅ ᴀ Mᴇssᴀɢᴇ ᴛᴏ Pᴇʀᴛɪᴄᴜʟᴀʀ Cʜᴀᴛ</code>"""

    G_FIL_TXT = """<b>ɴᴏᴛᴇ:</b>
<code>Tʜɪs Mᴏᴅᴜʟᴇ Oɴʟʏ Wᴏʀᴋs Fᴏʀ Mʏ Aᴅᴍɪɴs</code>

🔥 <u><b>Adv Global Filter </b></u>
• /gfilter - <code>ᴛᴏ ᴀᴅᴅ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs</code>
• /gfilters - <code>ᴛᴏ ᴠɪᴇᴡ ʟɪsᴛ ᴏғ ᴀʟʟ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs<code>
• /delg - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀ sᴘᴇᴄɪғɪᴄ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ</code>
• /delallg - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀʟʟ ɢʟᴏʙᴀʟ ꜰɪʟᴛᴇʀꜱ</code>
"""

    STATUS_TXT = """<b>╭──᛬⚡️sᴛᴀᴛᴜs ʙᴏᴀʀᴅ⚡️᛬─╮
├╼<b> 📂 ᴛᴏᴛᴀʟ ғɪʟᴇs : <code>{}</code></b>
├╼<b> 🔴 ᴛᴏᴛᴀʟ ᴜsᴇʀs : <code>{}</code></b>
├╼<b> 🟢 ᴛᴏᴛᴀʟ ᴄʜᴀᴛs : <code>{}</code></b>
├╼<b> 🔴 ᴜsᴇᴅ sᴛᴏʀᴀɢᴇ : <code>{}</code> 𝙼𝙱</b>
├╼<b> 🟢 ғʀᴇᴇ sᴛᴏʀᴀɢᴇ : <code>{}</code> 𝙼𝙱</b>
╰────────────────╯</b>"""
    LOG_TEXT_G = """#𝐍𝐞𝐰𝐆𝐫𝐨𝐮𝐩
    
<b>᚛› 𝐆𝐫𝐨𝐮𝐩 ⪼ {a}</b>
<b>᚛› 𝐆 𝐈𝐃 ⪼ <code>{b}</code></b>
<b>✯ group username ⪼ @{c}</b>
<b>᚛› 𝐓𝐨𝐭𝐚𝐥 𝐌𝐞𝐦𝐛𝐞𝐫𝐬 ⪼ {d}</b>
<b>᚛› 𝐀𝐝𝐝𝐞𝐝 𝐁𝐲 ⪼ {e}</b>

By {f}
"""
    LOG_TEXT_P = """#𝐍𝐞𝐰𝐔𝐬𝐞𝐫
    
<b>᚛› 𝐈𝐃 - <code>{}</code></b>
<b>᚛› 𝐍𝐚𝐦𝐞 - {}</b>
<b>᚛› 𝐔𝐍 - @{}</b>

By @{} """
   
    ZOMBIES_TXT = """𝙷𝙴𝙻𝙿 𝚈𝙾𝚄 𝚃𝙾 𝙺𝙸𝙲𝙺 𝚄𝚂𝙴𝚁𝚂

<b>ᴋɪᴄᴋ ɪɴᴄᴀᴛɪᴠᴇ ᴍᴇᴍʙᴇʀs ғʀᴏᴍ ɢʀᴏᴜᴘ. ᴀᴅᴅ ᴍᴇ ᴀs ᴀᴅᴍɪɴ ᴡɪᴛʜ ʙᴀɴ ᴜsᴇʀs ᴘᴇʀᴍɪssɪᴏɴ ɪɴ ɢʀᴏᴜᴘ.</b>

<b>ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ᴜsᴀɢᴇ:</b>
• /inkick - ᴄᴏᴍᴍᴀɴᴅ ᴡɪᴛʜ ʀᴇϙᴜɪʀᴇᴅ ᴀʀɢᴜᴍᴇɴᴛs ᴀɴᴅ ɪ ᴡɪʟʟ ᴋɪᴄᴋ ᴍᴇᴍʙᴇʀs ғʀᴏᴍ ɢʀᴏᴜᴘ.
• /instatus - ᴛᴏ ᴄʜᴇᴄᴋ ᴄᴜʀʀᴇɴᴛ sᴛᴀᴛᴜs ᴏғ ᴄʜᴀᴛ ᴍᴇᴍʙᴇʀ ғʀᴏᴍ ɢʀᴏᴜᴘ.
• /inkick ᴡɪᴛʜɪɴ_ᴍᴏɴᴛʜ ʟᴏɴɢ_ᴛɪᴍᴇ_ᴀɢᴏ - ᴛᴏ ᴋɪᴄᴋ ᴜsᴇʀs ᴡʜᴏ ᴀʀᴇ ᴏғғʟɪɴᴇ ғᴏʀ ᴍᴏʀᴇ ᴛʜᴀɴ 6-7 ᴅᴀʏs.
• /inkick long_time_ago - ᴛᴏ ᴋɪᴄᴋ ᴍᴇᴍʙᴇʀs ᴡʜᴏ ᴀʀᴇ ᴏғғʟɪɴᴇ ғᴏʀ ᴍᴏʀᴇ ᴛʜᴀɴ ᴀ ᴍᴏɴᴛʜ ᴀɴᴅ ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs.
• /dkick - ᴛᴏ ᴋɪᴄᴋ ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs."""


    RESTRIC_TXT = """➤ 𝐇𝐞𝐥𝐩: Mᴜᴛᴇ 🚫

𝚃𝚑𝚎𝚜𝚎 𝚊𝚛𝚎 𝚝𝚑𝚎 𝚌𝚘𝚖𝚖𝚊𝚗𝚍𝚜 𝚊 𝚐𝚛𝚘𝚞𝚙 𝚊𝚍𝚖𝚒𝚗 𝚌𝚊𝚗 𝚞𝚜𝚎 𝚝𝚘 𝚖𝚊𝚗𝚊𝚐𝚎 𝚝𝚑𝚎𝚒𝚛 𝚐𝚛𝚘𝚞𝚙 𝚖𝚘𝚛𝚎 𝚎𝚏𝚏𝚒𝚌𝚒𝚎𝚗𝚝𝚕𝚢.

➪/ban: 𝖳𝗈 𝖻𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋 𝖿𝗋𝗈𝗆 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
➪/unban: 𝖳𝗈 𝗎𝗇𝖻𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋 𝗂𝗇 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
➪/tban: 𝖳𝗈 𝗍𝖾𝗆𝗉𝗈𝗋𝖺𝗋𝗂𝗅𝗒 𝖻𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋.
➪/mute: 𝖳𝗈 𝗆𝗎𝗍𝖾 𝖺 𝗎𝗌𝖾𝗋 𝗂𝗇 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
➪/unmute: 𝖳𝗈 𝗎𝗇𝗆𝗎𝗍𝖾 𝖺 𝗎𝗌𝖾𝗋 𝗂𝗇 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
➪/tmute: 𝖳𝗈 𝗍𝖾𝗆𝗉𝗈𝗋𝖺𝗋𝗂𝗅𝗒 𝗆𝗎𝗍𝖾 𝖺 𝗎𝗌𝖾𝗋.

➤ 𝖭𝗈𝗍𝖾:
𝖶𝗁𝗂𝗅𝖾 𝗎𝗌𝗂𝗇𝗀 /tmute 𝗈𝗋 /tban 𝗒𝗈𝗎 𝗌𝗁𝗈𝗎𝗅𝖽 𝗌𝗉𝖾𝖼𝗂𝖿𝗒 𝗍𝗁𝖾 𝗍𝗂𝗆𝖾 𝗅𝗂𝗆𝗂𝗍.

➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾: /𝗍𝖻𝖺𝗇 2𝖽 𝗈𝗋 /𝗍𝗆𝗎𝗍𝖾 2𝖽.
𝖸𝗈𝗎 𝖼𝖺𝗇 𝗎𝗌𝖾 𝗏𝖺𝗅𝗎𝖾𝗌: 𝗆/𝗁/𝖽. 
 • 𝗆 = 𝗆𝗂𝗇𝗎𝗍𝖾𝗌
 • 𝗁 = 𝗁𝗈𝗎𝗋𝗌
 • 𝖽 = 𝖽𝖺𝗒𝗌"""


    PIN_TXT ="""<b>PIN MODULE</b>
<b>𝙿𝙸𝙽 𝙰 𝙼𝙴𝚂𝚂𝙰𝙶𝙴../</b>

<b>𝙰𝙻𝙻 𝚃𝙷𝙴 𝙿𝙸𝙽 𝚁𝙴𝙿𝙻𝙰𝚃𝙴𝙳 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝙲𝙰𝙽 𝙱𝙴 𝙵𝙾𝚄𝙽𝙳 𝙷𝙴𝚁𝙴::</b>

<b>📌𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝙰𝙽𝙳 𝚄𝚂𝙰𝙶𝙴📌</b>

◉ /pin :- 𝚃𝙾 𝙿𝙸𝙽 𝚃𝙷𝙴 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 𝙾𝙽 𝚈𝙾𝚄𝚁 𝙲𝙷𝙰𝚃𝚂
◉ /unpin :- 𝚃𝙾 𝚄𝙽𝙿𝙸𝙽 𝚃𝙷𝙴 𝙲𝚄𝚁𝚁𝙴𝙴𝙽𝚃 𝙿𝙸𝙽𝙽𝙴𝙳 𝙼𝙴𝚂𝙰𝙰𝙶𝙴"""

    PASTE_TXT = """ʜᴇʟᴘ : <b>ᴘᴀsᴛᴇ ➾</b>

ᴘᴀsᴛᴇ sᴏᴍᴇ ᴛᴇxᴛs ᴏʀ ᴅᴏᴄᴜᴍᴇɴᴛs ᴏɴ ᴀ ᴡᴇʙsɪᴛᴇ!

<b>ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ᴜsᴀɢᴇ ➾</b>

‣ /paste - [ᴛᴇxᴛ] - ᴘᴀsᴛᴇ ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ ᴏɴ ᴘᴀsᴛʏ

<b>ɴᴏᴛᴇ ➾</b>

‣ ᴛʜᴇʀᴇ ᴄᴏᴍᴍᴀɴᴅs ᴡᴏʀᴋs ᴏɴ ʙᴏᴛʜ ᴘᴍ ᴀɴᴅ ɢʀᴏᴜᴘ
‣ ᴛʜᴇʀᴇ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ʙʏ ᴀɴʏ ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀ.."""

    TTS_TXT = """ʜᴇʟᴘ : <b>ᴛᴛs 🔊 ᴍᴏᴅᴜʟᴇ ➾</b>

ᴛʀᴀɴsʟᴀᴛᴇ ᴛᴇxᴛ sᴘᴇᴇᴄʜ

<b>ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ᴜsᴀɢᴇ ➾</b>

‣ /tts : ᴄᴏɴᴠᴇʀᴛ ᴛᴇxᴛ ᴛᴏ sᴘᴇᴇᴄʜ

<b>ɴᴏᴛᴇ ➾</b>


‣ ɪᴍᴅʙ sʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟʟᴀɢᴇ.
‣ ᴛʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴡᴏʀᴋs ᴏɴ ʙᴏᴛʜ ᴘᴍ ᴀɴᴅ ɢʀᴏᴜᴘ.
‣ ɪᴍᴅʙ ᴄᴀɴ ᴛʀᴀɴsʟᴀᴛᴇ ᴛᴇxᴛs ᴛᴏ 200+ ʟᴀɴɢᴜᴀɢᴇ."""

    PINGS_TXT ="""<b>🌟 ᴘɪɴɢ:</b>

ʜᴇʟᴘs ʏᴏᴜ ᴛᴏ ᴋɴᴏᴡ ʏᴏᴜʀ ᴘɪɴɢ 🚶🏼‍♂️

<b>ᴄᴏᴍᴍᴀɴᴅs:</b>

• /alive - ᴛᴏ ᴄʜᴇᴄᴋ ʏᴏᴜ ᴀʀᴇ ᴀʟɪᴠᴇ.
• /ping - ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ᴘɪɴɢ.
<b>🏹Usage🏹 :</b>

• ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ɪɴ ᴘᴍs ᴀɴᴅ ɢʀᴏᴜᴘs
• ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ʙᴜʏ ᴇᴠᴇʀʏᴏɴᴇ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘs ᴀɴᴅ ʙᴏᴛs ᴘᴍ
• sʜᴀʀᴇ ᴜs ғᴏʀ ᴍᴏʀᴇ ғᴇᴀᴛᴜʀᴇs"""

    TELE_TXT = """ʜᴇʟᴘ : <b>⋄ᴛᴇʟᴇɢʀᴀᴘʜ⋄</b>

ᴅᴏ ᴀs ʏᴏᴜ ᴡɪsʜ ᴡɪᴛʜ telegra.ph ᴍᴏᴅᴜʟᴇ!

<b>ᴜsᴀɢᴇ ➾</b>

 /telegraph - sᴇɴᴅ ᴍᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ʀᴇᴘʟʏ ᴡɪᴛʜ ᴘɪᴄᴛᴜʀᴇ ᴏʀ ᴠɪᴅᴇ ᴜɴᴅᴇʀ (5ᴍʙ)

<b>ɴᴏᴛᴇ ➾</b>

‣ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ɪs ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ ɢʀᴏᴜᴘ ᴀɴᴅ ᴘᴍs
‣ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ʙʏ ᴇᴠᴇʀʏᴏɴᴇ"""

    JSON_TXT ="""<b>ᴊsᴏɴ ➾</b>

ʙᴏᴛ ʀᴇᴛᴜʀɴs ᴊsᴏɴ ғᴏʀ ᴀʟʟ ʀᴇᴘʟɪᴇᴅ ᴍᴇssᴀɢᴇs ᴡɪᴛʜ /json

<b>ғᴇᴀᴛᴜʀᴇs ➾</b>

ᴍᴇssᴀɢᴇ ᴇᴅɪᴛᴛɪɴɢ ᴊsᴏɴ
ᴘᴍ sᴜᴘᴘᴏʀᴛ
ɢʀᴏᴜᴘ sᴜᴘᴘᴏʀᴛ

<b>ɴᴏᴛᴇ ➾</b>

ᴇᴠᴇʀʏᴏɴᴇ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ, ɪғ sᴘᴀᴍɪɴɢ ʜᴀᴘᴘᴇɴs ʙᴏᴛ ᴡɪʟʟ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ʙᴀɴ ʏᴏᴜ ғʀᴏᴍ ᴛʜᴇ ɢʀᴏᴜᴘ."""

    URLSHORT_TXT = """➤ 𝐇𝐞𝐥𝐩: 𝖴𝗋𝗅 𝗌𝗁𝗈𝗋𝗍𝗇𝖾𝗋

<i><b>𝚃𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚑𝚎𝚕𝚙𝚜 𝚢𝚘𝚞 𝚝𝚘 𝚜𝚑𝚘𝚛𝚝 𝚊 𝚞𝚛𝚕 </i></b>

➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:

➪ /short: <b>𝗎𝗌𝖾 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗐𝗂𝗍𝗁 𝗒𝗈𝗎𝗋 𝗅𝗂𝗇𝗄 𝗍𝗈 𝗀𝖾𝗍 𝗌𝗁𝗈𝗋𝗍𝖾𝖽 𝗅𝗂𝗇𝗄𝗌</b>

➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾:

<code>/short https://youtu.be/example...</code>"""

    PURGE_TXT = """<b>ᴘᴜʀɢᴇ ➾</b>

ᴅᴇʟᴇᴛᴇ ᴀ ʟᴏᴛ ᴏғ ᴍᴇssᴀɢᴇs ғʀᴏᴍ ɢʀᴏᴜᴘ!

<b>ᴀᴅᴍɪɴ ➾</b>

‣ /purge - ᴅᴇʟᴇᴛᴇ ᴀʟʟ ᴍᴇssᴀɢᴇs ғʀᴏᴍ ᴛʜᴇ ʀᴇᴘʟɪᴇᴅ ᴛᴏ ᴍᴇssᴀɢᴇ, ᴛᴏ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴍᴇssᴀɢᴇ"""

    CREATOR_REQUIRED = """❗<b>You have To Be The Group Creator To Do That.</b>"""
      
    INPUT_REQUIRED = "❗ **Arguments Required**"
      
    KICKED = """✔️ Successfully Kicked {} Members According To The Arguments Provided."""
      
    START_KICK = """🚮 Removing Inactive Members This May Take A While..."""
      
    ADMIN_REQUIRED = """❗<b>എന്നെ Admin ആക്കത്ത സ്ഥലത്ത് ഞാൻ നിക്കില്ല പോകുവാ Bii..Add Me Again with all admin rights.</b>"""
      
    DKICK = """✔️ Kicked {} Deleted Accounts Successfully."""
      
    FETCHING_INFO = """<b>ഇപ്പൊ എല്ലാം അടിച്ചുമാറ്റി തരാം...</b>"""
      
    CARB_TXT = """☾︎𝗛𝗘𝗟𝗣 𝗙𝗢𝗥 𝗖𝗔𝗥𝗕𝗢𝗡☽︎
𝙲𝙰𝚁𝙱𝙾𝙽 𝙸𝚂 𝙰 𝙵𝙴𝚄𝚃𝚄𝚁𝙴 𝚃𝙾 𝙼𝙰𝙺𝙴 𝚃𝙷𝙴 𝙸𝙼𝙰𝙶𝙴 𝙰𝚂 𝚂𝙷𝙾𝚆𝙽 𝙸𝙽 𝚃𝙷𝙴 𝚃𝙾𝙿 𝚆𝙸𝚃𝙷 𝚈𝙾𝚄𝚁𝙴 𝚃𝙴𝚇𝚃𝚂.
𝙵𝙾𝚁 𝚄𝚂𝙸𝙽𝙶 𝚃𝙷𝙴 𝙼𝙾𝙳𝚄𝙻𝙴 𝙹𝚄𝚂𝚃 𝚂𝙴𝙽𝙳 𝚃𝙷𝙴 𝚃𝙴𝚇𝚃 𝙰𝙽𝙳 𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙸𝚃 𝚆𝙸𝚃𝙷 /carbon 𝙲𝙾𝙼𝙼𝙰𝙽𝙳 𝚃𝙷𝙴 𝙱𝙾𝚃 𝚆𝙸𝙻𝙻 𝚁𝙴𝙿𝙻𝚈 𝚆𝙸𝚃𝙷 𝚃𝙷𝙴 𝙲𝙰𝚁𝙱𝙾𝙽 𝙸𝙼𝙰𝙶𝙴"""

    FOND_TXT = """☾︎𝗛𝗘𝗟𝗣 𝗙𝗢𝗥 𝗙𝗢𝗡𝗧𝗦☽︎
𝙵𝙾𝙽𝚃 𝙸𝚂 𝙰 𝙼𝙾𝙳𝚄𝙻𝙴 𝙵𝙾𝚁 𝙼𝙰𝙺𝙴 𝚈𝙾𝚄𝚁 𝚃𝙴𝚇𝚃 𝚂𝚃𝚈𝙻𝙸𝚂𝙷.
𝙵𝙾𝚁 𝚄𝚂𝙴 𝚃𝙷𝙰𝚃 𝙵𝙴𝚄𝚃𝚄𝚁𝙴 𝚃𝚈𝙿𝙴 /font <your text> 𝚃𝙷𝙴𝙽 𝚈𝙾𝚄𝚁 𝚃𝙴𝚇𝚃 𝙸𝚂 𝚁𝙴𝙰𝙳𝚈."""

    SHARE_TXT = """<b>☾︎𝗛𝗘𝗟𝗣 𝗙𝗢𝗥 𝗦𝗛𝗔𝗥𝗘 𝗧𝗘𝗫𝗧☽︎</b>

<b>ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ᴜsᴀɢᴇ ➾</b>

‣ /share - ʀᴇᴘʟʏ ᴡɪᴛʜ ᴀɴʏ ᴛᴇxᴛ ᴛᴏ sᴇɴᴅ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ"""

    STICKER_TXT ="""<b>yᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ᴍᴏᴅᴜʟᴇ ᴛᴏ ꜰɪɴᴅᴀɴy  ꜱᴛɪᴄᴋᴇʀꜱ ɪᴅ. 
 • ᴜꜱᴀɢᴇ :ᴛᴏ ɢᴇᴛ ꜱᴛɪᴄᴋᴇʀ 
   
 ⭕ ʜᴏᴡ ᴛᴏ ᴜꜱᴇ 
 ◉ Reply To Any Sticker [/stickerid]</b>"""
    
    SONG_TXT = """<b>𝚂𝙾𝙽𝙶 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙼𝙾𝙳𝚄𝙻𝙴</b>

<i>𝚂𝙾𝙽𝙶 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙼𝙾𝙳𝚄𝙻𝙴, 𝙵𝙾𝚁 𝚃𝙷𝙾𝚂𝙴 𝚆𝙷𝙾 𝙻𝙾𝚅𝙴 𝙼𝚄𝚂𝙸𝙲. 𝚈𝙾𝚄 𝙲𝙰𝙽 𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙵𝙴𝙰𝚃𝚄𝙴 𝙵𝙾𝚁 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙰𝙽𝚈 𝚂𝙾𝙽𝙶 𝚆𝙸𝚃𝙷 𝚂𝚄𝙿𝙴𝚁 𝙵𝙰𝚂𝚃 𝚂𝙿𝙴𝙴𝙳.𝚆𝙾𝚁𝙺𝚂 𝙾𝙽𝙻𝚈 𝙾𝙽 𝙶𝚁𝙾𝚄𝙿𝚂../</i>

<b>𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂</b>

⏭️ /song 𝚂𝙾𝙽𝙶 𝙽𝙰𝙼𝙴 

<b>𝚆𝙾𝚁𝙺𝚂 𝙱𝙾𝚃𝙷 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙿𝙼</b>
@MLZ_BOTZ"""
   


    SUNEESH_TXT = """<b>•𝗡𝗮𝗺𝗲 :-: 🇮🇳ᴍᴀɴᴛɪs™◢ ◤
•𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲 :-: @TG_x_filter
•𝗨𝘀𝗲𝗿 𝗟𝗶𝗻𝗸 :-:  <a href=https://t.me/TG_x_filter>𝗟𝗶𝗻𝗸</a></b>"""
    SUPPORT_TXT = """<b>𝗜𝘆 𝗬𝗼𝘂 𝗙𝗮𝗰𝗶𝗻𝗴 𝗔𝗻𝘆 𝗶𝘀𝘀𝘂𝗲 𝗶𝗻 𝗧𝗵𝗲 𝗥𝗲𝗽𝗼 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 𝗠𝗲..!!</b>"""

    FILTERS = """<b>ʜᴇʏ{}, ᴛʜᴇsᴇ ᴀʀᴇ ᴍʏ ᴛʜʀᴇᴇ ᴛʏᴘᴇs ᴏғ ғɪʟᴛᴇʀs..!!</b>"""
