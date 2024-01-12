from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from MukeshRobot import MUST_JOIN,START_IMG


@pbot.on_message( filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if MUST_JOIN:  # compulsory
        return
    try:
        try:
            await bot.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/Berlinmusic_support" + MUST_JOIN
            else:
                chat_info = await bot.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.delete()
                await msg.reply_photo(START_IMG
                    f"Join Dulu Kampang Baru Pencet /start Lagi !!",
                
                    reply_markup=InlineKeyboardMarkup(
                        [InlineKeyboardButton(text= "Masuk sini nyet, Jangan Lupa Salam", url=f"https://t.me/berlinmusic_support")],
                    )
                ),
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"ɪ'ᴍ ɴᴏᴛ ᴀᴅᴍɪɴ ɪɴ ᴛʜᴇ MUST_JOIN ᴄʜᴀᴛ : {MUST_JOIN} !")
