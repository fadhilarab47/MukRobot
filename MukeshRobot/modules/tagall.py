import asyncio

from telethon import events
from telethon.errors import UserNotParticipantError
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import ChannelParticipantAdmin, ChannelParticipantCreator

from MukeshRobot import telethn as client

spam_chats = []

@client.on(events.NewMessage(pattern="^/all ?(.*)"))
async def mentionall(event):
    chat_id = event.chat_id
    if event.is_private:
        return await event.respond(
            "ᴍᴏᴅᴜʟᴇ ɪɴɪ ᴄᴜᴍᴀɴ ʙɪꜱᴀ ᴅɪ ᴘᴀᴋᴇ ᴅɪ ɢᴄ ᴀᴛᴀᴜ ᴅɪ ᴄʜ ᴍᴇᴋ!"
        )

    is_admin = False
    try:
        partici_ = await client(GetParticipantRequest(event.chat_id, event.sender_id))
    except UserNotParticipantError:
        is_admin = False
    else:
        if isinstance(
            partici_.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
        ):
            is_admin = True
    if not is_admin:
        return await event.respond("ᴄᴜᴍᴀɴ ᴀᴅᴍɪɴ ʏᴀɴɢ ʙɪsᴀ ɢᴜɴᴀɪɴ ᴍᴏᴅᴜʟᴇ ɪɴɪ ᴛᴏᴅ")

    if event.pattern_match.group(1) and event.is_reply:
        return await event.respond("__Give me one argument!__")
    elif event.pattern_match.group(1):
        mode = "text_on_cmd"
        msg = event.pattern_match.group(1)
    elif event.is_reply:
        mode = "text_on_reply"
        msg = await event.get_reply_message()
        if msg == None:
            return await event.respond(
                "__ɪ ᴄᴀɴ'ᴛ ᴍᴇɴᴛɪᴏɴ ᴍᴇᴍʙᴇʀs ғᴏʀ ᴏʟᴅᴇʀ ᴍᴇssᴀɢᴇs! (ᴍᴇssᴀɢᴇs ᴡʜɪᴄʜ ᴀʀᴇ sᴇɴᴛ ʙᴇғᴏʀᴇ ɪ'ᴍ ᴀᴅᴅᴇᴅ ᴛᴏ ɢʀᴏᴜᴘ__"
            )
    else:
        return await event.respond(
            "ʀᴇᴘʟʏ ᴘᴇꜱᴀɴ ᴍᴀɴᴀ ʏᴀɴɢ ᴍᴀᴜ ᴅɪ ᴛᴀɢᴀʟʟ ᴍᴇᴋ!"
        )

    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(chat_id):
        if not chat_id in spam_chats:
            break
        usrnum += 1
        usrtxt += f"❍ [{usr.first_name}](tg://user?id={usr.id})\n"
        if usrnum == 5:
            if mode == "text_on_cmd":
                txt = f"{msg}\n\n{usrtxt}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(usrtxt)
            await asyncio.sleep(3)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@client.on(events.NewMessage(pattern="^/cancel$"))
async def cancel_spam(event):
    if not event.chat_id in spam_chats:
        return await event.respond("ɢᴀ ᴀᴅᴀ ʏᴀɴɢ ʜᴀʀᴜs ɢᴡ ʙᴇʀʜᴇɴᴛɪɪɴ ᴛᴏᴅ..")
    is_admin = False
    try:
        partici_ = await client(GetParticipantRequest(event.chat_id, event.sender_id))
    except UserNotParticipantError:
        is_admin = False
    else:
        if isinstance(
            partici_.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
        ):
            is_admin = True
    if not is_admin:
        return await event.respond("__ᴄᴜᴍᴀɴ ᴀᴅᴍɪɴ ʏᴀɴɢ ʙɪsᴀ ɢᴜɴᴀɪɴ ᴍᴏᴅᴜʟᴇ ɪɴɪ ᴛᴏᴅ__")

    else:
        try:
            spam_chats.remove(event.chat_id)
        except:
            pass
        return await event.respond("sᴛᴏᴘ ᴍᴇᴍᴀɴɢɢɪʟ ᴀɴᴀᴋ ᴀɴᴊɪɴɢ.__")


__mod_name__ = "Tᴀɢᴀʟʟ"
__help__ = """
──「  ᴏɴʟʏ ғᴏʀ ᴀᴅᴍɪɴs 」──

❍ /all ' You know lah gunanya apa. '
❍ /cancel ' you know lah harus ngapain. '
"""
