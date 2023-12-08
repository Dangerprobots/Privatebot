import logging
#import random, asyncio
from os import environ
from pyrogram import Client,filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait

logging.basicConfig(level=logging.ERROR)

User = Client(name="AcceptUser", api_id=environ.get("API_ID"), api_hash=environ.get("API_HASH"),
              session_string="AQAWgXwASfQaqtA5ciBxPU9x1p8TgHbFPgKb1UU7Yio6KHtttRhbElxeaYfKAqlyGBBvlK6fOibO19VjkTEeaXcc16sY9Mc_MV7jYHwL9xKZiTQVL99OzOptVqKo1H8NhK9DfK5ZL9B0jkKftAR3hdk6jnhIsS0m_u3_XIiZ7wdbNjQawvwqKhSllB0FTugjg_q3jKeiyJZr0Q1PJzsALkXIGVxl4Ak0ok8VxSrKd6zFW6LcqlQBTHZ0TWl1vXalAQZYplpztm2kQVLxpVfGzC-qV5FMwfaw8I6XbZ5_qd4O0V9-t_C4g_qmyszS1RDwlfHefWPma314RnyyafS8N3EDdaGYwAAAAAGN00lEAA"

#MAX_RETRIES = 5  # Maximum number of retries for approval
#RETRY_INTERVAL = 11  # Interval (in seconds) to wait before retrying

def approve_all_join_requests(user, chat_id):
    max_users_per_run = 10000  # Maximum users to approve in one run

    try:
        while True:
            join_requests = await user.get_chat_members(chat_id, filter="restricted")
            user_ids_to_approve = [member.user.id for member in join_requests]

            if not user_ids_to_approve:
                break  # No more join requests, exit the loop

            for i in range(0, len(user_ids_to_approve), max_users_per_run):
                # Approve users in batches to avoid overwhelming the Telegram API
                await user.approve_chat_members(chat_id, user_ids_to_approve[i:i + max_users_per_run])

                # Introduce a delay between batches to comply with potential rate limits
                await asyncio.sleep(RETRY_INTERVAL)

    except FloodWait as t:
        await asyncio.sleep(t.x)
    except Exception as e:
        logging.error(f"Error during approval: {str(e)}")


@User.on_message(filters.command(["run", "start"], [".", "/"]) & (filters.group | filters.channel))
async def approve_command(client: User, message: Message):
    chat_id = message.chat.id
    await message.delete(True)
 
    try:
       while True: # create loop is better techniq 🙃
           try:
               await user.approve_all_chat_join_requests(chat_id)         
           except FloodWait as t:
               asyncio.sleep(t.value)
               await user.approve_all_chat_join_requests(chat_id) 
           except Exception as e:
               logging.error(str(e))
    except FloodWait as s:
        asyncio.sleep(s.value)
        while True:
           try:
               await user.approve_all_chat_join_requests(chat_id)         
           except FloodWait as t:
               asyncio.sleep(t.value)
               await user.approve_all_chat_join_requests(chat_id) 
           except Exception as e:
               logging.error(str(e))

logging.info("Bot Started....")
app.run()
