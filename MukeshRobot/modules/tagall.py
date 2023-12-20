import asyncio
import random

from telethon import events
from telethon.errors import UserNotParticipantError
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import ChannelParticipantAdmin, ChannelParticipantCreator

from MukeshRobot import telethn as client

spam_chats = []

emoji_tag = ["😀", "😃",  "😄", "😁", "😆", "😅", "😂", "🤣", "😭", "😗", "😙", "😚", "😘", "🥰", "😍", "🤩", "🥳", "🤗", "🙃", "🙂", "☺️", "😊", "😏", "😌", "😉", "🤭", "😶", "😐", "😑", "😔", "😋", "😛", "😝", "😜", "🤪", "🤔", "🤨", "🧐", "🙄", "😒", "😤", "😠", "🤬", "☹️", "🙁", "😕", "😟", "🥺", "😳", "😬", "🤐", "🤫", "😰", "😨", "😧", "😦", "😮", "😯", "😲", "😱", "🤯", "😢", "😥", "😓", "😞", "😖", "😣", "😩", "😫", "🤤", "🥱", "😴", "😪", "🌛", "🌜", "🌚", "🌝", "🎲", "🧩", "♟", "🎯", "🎳", "🎭", "💕", "💞", "💓", "💗", "💖", "❤️‍🔥", "💔", "🤎", "🤍", "🖤", "❤️", "🧡", "💛", "💚", "💙", "💜", "💘", "💝", "🐵", "🦁", "🐯", "🐱", "🐶", "🐺", "🐻", "🐨", "🐼", "🐹", "🐭", "🐰", "🦊", "🦝", "🐮", "🐷", "🐽", "🐗", "🦓", "🦄", "🐴", "🐸", "🐲", "🦎", "🐉", "🦖", "🦕", "🐢", "🐊", "🐍", "🐁", "🐀", "🐇", "🐈", "🐩", "🐕", "🦮", "🐕‍🦺", "🐅", "🐆", "🐎", "🐖", "🐄", "🐂", "🐃", "🐏", "🐑", "🐐", "🦌", "🦙", "🦥", "🦘", "🐘", "🦏", "🦛", "🦒", "🐒", "🦍", "🦧", "🐪", "🐫", "🐿️", "🦨", "🦡", "🦔", "🦦", "🦇", "🐓", "🐔", "🐣", "🐤", "🐥", "🐦", "🦉", "🦅", "🦜", "🕊️", "🦢", "🦩", "🦚", "🦃", "🦆", "🐧", "🦈", "🐬", "🐋", "🐳", "🐟", "🐠", "🐡", "🦐", "🦞", "🦀", "🦑", "🐙", "🦪", "🦂", "🕷️", "🦋", "🐞", "🐝", "🦟", "🦗", "🐜", "🐌", "🐚", "🕸️", "🐛", "🐾", "🌞", "🤢", "🤮", "🤧", "🤒", "🍓", "🍒", "🍎", "🍉", "🍑", "🍊", "🥭", "🍍", "🍌", "🌶", "🍇", "🥝", "🍐", "🍏", "🍈", "🍋", "🍄", "🥕", "🍠", "🧅", "🌽", "🥦", "🥒", "🥬", "🥑", "🥯", "🥖", "🥐",]

@client.on(events.NewMessage(pattern="^/tagall ?(.*)"))
@client.on(events.NewMessage(pattern="^@all ?(.*)"))
async def mentionall(event):
    chat_id = event.chat_id
    if event.is_private:
        return await event.respond(
            "__ᴘᴇʀɪɴᴛᴀʜ ɪɴɪ ᴅᴀᴘᴀᴛ ᴅɪɢᴜɴᴀᴋᴀɴ ᴅᴀʟᴀᴍ ɢʀᴜᴘ ᴅᴀɴ ᴄʜᴀɴɴᴇʟ!!__"
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
        return await event.respond("__ʜᴀɴʏᴀ ᴀᴅᴍɪɴ ʏᴀɴɢ ʙɪꜱᴀ ɴɢᴇᴛᴀɢᴀʟʟ!!__")

    if event.pattern_match.group(1) and event.is_reply:
        return await event.respond("__ᴋᴀꜱɪʜ ꜱᴀʏᴀ ᴘᴇʀɪɴᴛᴀʜ ʏᴀɴɢ ᴊᴇʟᴀꜱ!__")
    elif event.pattern_match.group(1):
        mode = "text_on_cmd"
        msg = event.pattern_match.group(1)
    elif event.is_reply:
        mode = "text_on_reply"
        msg = await event.get_reply_message()
        if msg == None:
            return await event.respond(
                "__ɢᴜᴀ ɢᴀ ʙɪꜱᴀ ɴɢᴇᴛᴀɢᴀʟʟ ᴘᴇꜱᴀɴ ʏᴀɴɢ ᴜᴅᴀʜ ʟᴀᴍᴀ ʙʟᴏᴋ! (messages which are sent before I'm added to group)__"
            )
    else:
        return await event.respond(
            "__ᴋᴀꜱɪʜ ᴘᴇꜱᴀɴ ᴀᴛᴀᴜ ʀᴇᴘʟʏ ᴋᴇ ᴘᴇꜱᴀɴ ᴋᴀʟᴏ ᴍᴀᴜ ᴛᴀɢᴀʟʟ ʙᴏᴅᴏʜ!!__"
        )

    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(chat_id):
        if not chat_id in spam_chats:
            break
        usrnum += 1
        usrtxt += f"[{random.choice(emoji_tag)}](tg://user?id={usr.id})"
        if usrnum == 5:
            if mode == "text_on_cmd":
                txt = f"{usrtxt}\n\n{msg}"
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
        return await event.respond("__ᴜᴅᴀʜ ɢᴀ ᴀᴅᴀ ᴛᴀɢᴀʟʟ ʙᴏᴅᴏʜ...__")
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
        return await event.respond("__ᴄᴜᴍᴀɴ ᴀᴅᴍɪɴ ʏᴀɴɢ ʙɪꜱᴀ ɴɢᴀꜱɪʜ ᴘᴇʀɪɴᴛᴀʜ!__")

    else:
        try:
            spam_chats.remove(event.chat_id)
        except:
            pass
        return await event.respond("__ᴛᴀɢᴀʟʟ-ɴʏᴀ ᴜᴅᴀʜ ʙᴇʀᴇɴᴛɪ ᴍᴇᴋ.__")



__mod_name__ = "Tᴀɢᴀʟʟ"
__help__ = """
──「  ᴏɴʟʏ ғᴏʀ ᴀᴅᴍɪɴs 」──

❍ /tagall ᴏʀ @all '(ʀᴇᴘʟʏ ᴛᴏ ᴍᴇssᴀɢᴇ ᴏʀ ᴀᴅᴅ ᴀɴᴏᴛʜᴇʀ ᴍᴇssᴀɢᴇ) ᴛᴏ ᴍᴇɴᴛɪᴏɴ ᴀʟʟ ᴍᴇᴍʙᴇʀs ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ, ᴡɪᴛʜᴏᴜᴛ ᴇxᴄᴇᴘᴛɪᴏɴ.'
"""
