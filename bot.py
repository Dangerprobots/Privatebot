import logging, asyncio
#from os import environ
from pyrogram import Client, filters
from pyrogram.types import Message
#from pyrogram.errors import FloodWait

logging.basicConfig(level=logging.ERROR)

CHANNELS = [int(CHANNEL) for CHANNEL in environ.get("CHANNELS", "-1001928315111").split()]       
AuthChat = filters.chat(CHANNELS) if CHANNELS else (filters.group | filters.channel)         
User     = Client(name = "AcceptUser", session_string = "AQAWgXwASfQaqtA5ciBxPU9x1p8TgHbFPgKb1UU7Yio6KHtttRhbElxeaYfKAqlyGBBvlK6fOibO19VjkTEeaXcc16sY9Mc_MV7jYHwL9xKZiTQVL99OzOptVqKo1H8NhK9DfK5ZL9B0jkKftAR3hdk6jnhIsS0m_u3_XIiZ7wdbNjQawvwqKhSllB0FTugjg_q3jKeiyJZr0Q1PJzsALkXIGVxl4Ak0ok8VxSrKd6zFW6LcqlQBTHZ0TWl1vXalAQZYplpztm2kQVLxpVfGzC-qV5FMwfaw8I6XbZ5_qd4O0V9-t_C4g_qmyszS1RDwlfHefWPma314RnyyafS8N3EDdaGYwAAAAAGN00lEAA"


@User.on_message(filters.command(["run", "approve", "start"], [".", "/"]) & AuthChat)                     
async def approve(pro:User, m:Message):
    Id = m.chat.id
    await m.delete(True)
 
    try:
       while True: # create loop is better techniq 🙃
           try:
               await pro.approve_all_chat_join_requests(Id)         
           except FloodWait as t:
               asyncio.sleep(t.value)
               await pro.approve_all_chat_join_requests(Id) 
           except Exception as e:
               logging.error(str(e))
    except FloodWait as s:
        asyncio.sleep(s.value)
        while True:
           try:
               await pro.approve_all_chat_join_requests(Id)         
           except FloodWait as t:
               asyncio.sleep(t.value)
               await pro.approve_all_chat_join_requests(Id) 
           except Exception as e:
               logging.error(str(e))

    msg = await pro.send_message(Id, "**Task Completed** ✓ **Approved Pending All Join Request**")
    await asyncio.sleep(3)
    await msg.delete()


logging.info("Bot Started....")
User.run()







