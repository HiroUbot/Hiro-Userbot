from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.utils import kyy_cmd
from userbot import bot, CMD_HELP, CMD_HANDLER as cmd


@kyy_cmd(pattern="getid(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("`Mohon Reply Ke Pesan`")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await event.edit("```Mohon Balas Ke Reply```")
        return
    chat = "@getidsbot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("`Mohon Reply Ke Pesan`")
        return
    await event.edit("`Mencari ID.......`")
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1663258664))
            await bot.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("`Bot Sedang Error`")
            return
        if response.text.startswith("Forward"):
            await event.edit("`Mohon Maaf, Orang Ini Tidak Mempunyai ID`")
        else:
            await event.edit(f"{response.message.message}")


CMD_HELP.update({
    "getid":
    f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}getid`"
    "\n↳ : Balas Ke Pesan Pengguna Untuk Mendapatkan ID Nya."
})
