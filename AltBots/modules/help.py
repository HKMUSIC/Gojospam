from telethon import events, Button

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, SUDO_USERS, CMD_HNDLR as hl


HELP_STRING = f"★ 𝗦ᴘᴀᴍxᴅ 𝗛ᴇʟᴘ 𝗠ᴇɴᴜ ★\n\n» **ᴄʟɪᴄᴋ ᴏɴ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴꜱ ꜰᴏʀ ʜᴇʟᴘ**\n» **ᴅᴇᴠᴇʟᴏᴘᴇʀ: @II_YOUR_GOJO_ll**"

HELP_BUTTON = [
    [
      Button.inline("• ꜱᴘᴀᴍ •", data="spam"),
      Button.inline("• ʀᴀɪᴅ •", data="raid")
    ],
    [
      Button.inline("• ᴇxᴛʀᴀ •", data="extra")
    ],
    [
      Button.url("• ᴄʜᴀɴɴᴇʟ •", "https://t.me/GOJO_SUPPORT_GROUP_II"),
      Button.url("• sᴜᴘᴘᴏʀᴛ •", "https://t.me/II_CHATS_II")
    ]
  ]


@X1.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):
    if event.sender_id in SUDO_USERS:
        try:
          await event.client.send_file(event.chat_id,
              "https://telegra.ph/file/719e7092b9a37a100468d.jpg",
              caption=HELP_STRING,
              buttons=HELP_BUTTON
              )
        except Exception as e:
            await event.client.send_message(event.chat_id, f"An Exception Occured!\n\n**ERROR:** {str(e)}")


extra_msg = f"""
**» ᴇxᴛʀᴀ ᴄᴏᴍᴍᴀɴᴅꜱ:**

𝗨sᴇʙ𝗕ᴏᴛ: **ᴜꜱᴇʀʙᴏᴛ ᴄᴍᴅꜱ**
  1) {hl}ping 
  2) {hl}reboot
  3) {hl}sudo <reply to user>  --> ᴏᴡɴᴇʀ ᴄᴍᴅ
  4) {hl}logs --> Owner Cmd

𝗘ᴄʜᴏ: **ᴛᴏ ᴀᴄᴛɪᴠᴇ ᴇᴄʜᴏ ᴏɴ ᴀɴʏ ᴜꜱᴇʀ**
  1) {hl}echo <reply to user>
  2) {hl}rmecho <reply to user>

𝗟ᴇᴀᴠᴇ: **ᴛᴏ ʟᴇᴀᴠᴇ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ**
  1) {hl}leave <group/chat id> --> ᴏᴡɴᴇʀ ᴄᴍᴅ
  2) {hl}leave : Type in the Group bot will auto leave that group


**© @II_YOUR_GOJO_ll**
"""

                 
raid_msg = f"""
**» ʀᴀɪᴅ ᴄᴏᴍᴍᴀɴᴅꜱ:**

𝗥ᴀɪᴅ: **ᴀᴄᴛɪᴠᴀᴛᴇꜱ ʀᴀɪᴅ ᴏɴ ᴀɴʏ ɪɴᴅɪᴠɪᴅᴜᴀʟ ᴜꜱᴇʀ ꜰᴏʀ ɢɪᴠᴇɴ ʀᴀɴɢᴇ.**
  1) {hl}raid <count> <username>
  2) {hl}raid <count> <reply to user>

𝗥ᴇᴘʟʏʀᴀɪᴅ: **ᴀᴄᴛɪᴠᴀᴛᴇꜱ ʀᴇᴘʟʏ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ.**
  1) {hl}rraid <replying to user>
  2) {hl}rraid <username>

𝗗ʀᴇᴘʟʏʀᴀɪᴅ: **ᴅᴇᴀᴄᴛɪᴠᴀᴛᴇꜱ ʀᴇᴘʟʏ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ.**
  1) {hl}drraid <replying to user>
  2) {hl}drraid <username>

𝐌ʀᴀɪᴅ: **ʟᴏᴠᴇ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ.**
  1) {hl}mraid <count> <username>
  2) {hl}mraid <count> <reply to user>

𝐒ʀᴀɪᴅ: **ꜱʜᴀʏᴀʀɪ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ.**
  1) {hl}sraid <count> <username>
  2) {hl}sraid <count> <reply to user>

𝐂ʀᴀɪᴅ: **ᴀʙᴄᴅ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ.**
  1) {hl}craid <count> <username>
  2) {hl}craid <count> <reply to user>


**© @II_YOUR_GOJO_ll**
"""

spam_msg = f"""
**» ꜱᴘᴀᴍ ᴄᴏᴍᴍᴀɴᴅꜱ:**

𝗦ᴘᴀᴍ: **ꜱᴘᴀᴍꜱ ᴀ ᴍᴇꜱꜱᴀɢᴇ.**
  1) {hl}spam <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
  2) {hl}spam <count> <replying any message>

𝗣ᴏʀɴ𝗦ᴘᴀᴍ: **ᴘᴏʀᴍᴏɢʀᴀᴘʜʏ ꜱᴘᴀᴍ.**
  1) {hl}pspam <count>

𝗛ᴀɴɢ: **ꜱᴘᴀᴍꜱ ʜᴀɴɢɪɴɢ ᴍᴇꜱꜱᴀɢᴇ ꜰᴏʀ ɢɪᴠᴇɴ ᴄᴏᴜɴᴛᴇʀ.**
  1) {hl}hang <counter>


** © @II_YOUR_GOJO_ll**
"""                     
           
           
@X1.on(events.CallbackQuery(pattern=r"help_back"))
@X2.on(events.CallbackQuery(pattern=r"help_back"))
@X3.on(events.CallbackQuery(pattern=r"help_back"))
@X4.on(events.CallbackQuery(pattern=r"help_back"))
@X5.on(events.CallbackQuery(pattern=r"help_back"))
@X6.on(events.CallbackQuery(pattern=r"help_back"))
@X7.on(events.CallbackQuery(pattern=r"help_back"))
@X8.on(events.CallbackQuery(pattern=r"help_back"))
@X9.on(events.CallbackQuery(pattern=r"help_back"))
@X10.on(events.CallbackQuery(pattern=r"help_back"))
async def helpback(event):
    if event.query.user_id in SUDO_USERS:    
        await event.edit(
            HELP_STRING,
            buttons=[
              [
                Button.inline("• ꜱᴘᴀᴍ •", data="spam"),
                Button.inline("• ʀᴀɪᴅ •", data="raid")
              ],
              [
                Button.inline("• ᴇxᴛʀᴀ •", data="extra")
              ],
              [
                Button.url("• ᴄʜᴀɴɴᴇʟ •", "https://t.me/GOJO_SUPPORT_GROUP_II"),
                Button.url("• sᴜᴘᴘᴏʀᴛ •", "https://t.me/II_CHATS_II")
              ]
            ]
          )
    else:
        await event.answer("ɢᴏᴊᴏ ᴘᴀᴘᴀ ᴋᴇ ᴘss ᴊᴀᴀ ᴋʀ sᴜᴅᴏ ʟᴇ ᴋʀ ᴀᴀᴏ ʙᴇᴛᴀ", cache_time=0, alert=True)


@X1.on(events.CallbackQuery(pattern=r"spam"))
@X2.on(events.CallbackQuery(pattern=r"spam"))
@X3.on(events.CallbackQuery(pattern=r"spam"))
@X4.on(events.CallbackQuery(pattern=r"spam"))
@X5.on(events.CallbackQuery(pattern=r"spam"))
@X6.on(events.CallbackQuery(pattern=r"spam"))
@X7.on(events.CallbackQuery(pattern=r"spam"))
@X8.on(events.CallbackQuery(pattern=r"spam"))
@X9.on(events.CallbackQuery(pattern=r"spam"))
@X10.on(events.CallbackQuery(pattern=r"spam"))
async def help_spam(event):
    if event.query.user_id in SUDO_USERS:    
        await event.edit(spam_msg,
              buttons=[[Button.inline("< Back", data="help_back"),],],
              ) 
    else:
        await event.answer("ɢᴏᴊᴏ ᴘᴀᴘᴀ ᴋᴇ ᴘss ᴊᴀᴀ ᴋʀ sᴜᴅᴏ ʟᴇ ᴋʀ ᴀᴀᴏ ʙᴇᴛᴀ", cache_time=0, alert=True)


@X1.on(events.CallbackQuery(pattern=r"raid"))
@X2.on(events.CallbackQuery(pattern=r"raid"))
@X3.on(events.CallbackQuery(pattern=r"raid"))
@X4.on(events.CallbackQuery(pattern=r"raid"))
@X5.on(events.CallbackQuery(pattern=r"raid"))
@X6.on(events.CallbackQuery(pattern=r"raid"))
@X7.on(events.CallbackQuery(pattern=r"raid"))
@X8.on(events.CallbackQuery(pattern=r"raid"))
@X9.on(events.CallbackQuery(pattern=r"raid"))
@X10.on(events.CallbackQuery(pattern=r"raid"))
async def help_raid(event):
    if event.query.user_id in SUDO_USERS:
        await event.edit(raid_msg,
            buttons=[[Button.inline("< Back", data="help_back"),],],
          )
    else:
        await event.answer("ɢᴏᴊᴏ ᴘᴀᴘᴀ ᴋᴇ ᴘss ᴊᴀᴀ ᴋʀ sᴜᴅᴏ ʟᴇ ᴋʀ ᴀᴀᴏ ʙᴇᴛᴀ", cache_time=0, alert=True)


@X1.on(events.CallbackQuery(pattern=r"extra"))
@X2.on(events.CallbackQuery(pattern=r"extra"))
@X3.on(events.CallbackQuery(pattern=r"extra"))
@X4.on(events.CallbackQuery(pattern=r"extra"))
@X5.on(events.CallbackQuery(pattern=r"extra"))
@X6.on(events.CallbackQuery(pattern=r"extra"))
@X7.on(events.CallbackQuery(pattern=r"extra"))
@X8.on(events.CallbackQuery(pattern=r"extra"))
@X9.on(events.CallbackQuery(pattern=r"extra"))
@X10.on(events.CallbackQuery(pattern=r"extra"))
async def help_extra(event):
    if event.query.user_id in SUDO_USERS:
        await event.edit(extra_msg,
            buttons=[[Button.inline("< Back", data="help_back"),],],
            )
    else:
        await event.answer("Wɢᴏᴊᴏ ᴘᴀᴘᴀ ᴋᴇ ᴘss ᴊᴀᴀ ᴋʀ sᴜᴅᴏ ʟᴇ ᴋʀ ᴀᴀᴏ ʙᴇᴛᴀ", cache_time=0, alert=True)
