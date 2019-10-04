from userbot import CMD_LIST

@command(pattern="^.get_cmd")
async def cmd_list(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        string = ""
        for i in CMD_LIST:
            string += i + "\n"
            for iter_list in CMD_LIST[i]:
                string += "    ℹ️ `" + str(iter_list) + "`"
                string += "\n"
            string += "\n"
        if len(string) > 4095:
            with io.BytesIO(str.encode(string)) as out_file:
                out_file.name = "cmd.txt"
                await bot.send_file(
                    event.chat_id,
                    out_file,
                    force_document=True,
                    allow_cache=False,
                    caption="**COMMANDS**",
                    reply_to=reply_to_id
                )
                await event.delete()
        else:
            await event.edit(string)
