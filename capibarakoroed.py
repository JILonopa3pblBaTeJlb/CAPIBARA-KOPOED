import logging
import random
import os
import asyncio
from telethon import TelegramClient, functions, types

logging.basicConfig(level=logging.DEBUG)

api_id = API_ID
api_hash = 'api_hash'
token = 'bot_token'
chat_id = chat_id

media_files = ['image1.jpg', 'image2.jpg', 'image3.jpg', 'video.mp4']
caption_text = 'CAPTION TEXT!!!111\n<a href="your_link">LINK_TEXT</a>'

async def main():
    client = TelegramClient('session_name', api_id, api_hash)
    await client.start(bot_token=token)

    for msg_id in range(YOUR_START_POST, YOUR_END_POST+1):
        # Script A: Process and replace media
        random_media = random.choice(media_files)
        with open(random_media, 'rb') as f:
            result = await client.upload_file(f)

        if random_media.endswith('.jpg'):
            media = types.InputMediaUploadedPhoto(result)
        else:
            attributes = [
                types.DocumentAttributeVideo(
                    duration=60,
                    w=640,
                    h=480,
                    round_message=True,
                    supports_streaming=True
                )
            ]
            media = types.InputMediaUploadedDocument(result, attributes=attributes, mime_type='video/mp4')

        try:
            await client(functions.messages.EditMessageRequest(
                peer=chat_id,
                id=msg_id,
                media=media
            ))
        except:
            pass

        await asyncio.sleep(1)

        # Script B: Replace caption
        try:
            message = await client.get_messages(chat_id, ids=msg_id)

            if message:
                if message.photo or message.video or (message.grouped_id and (message.media.document or message.media.photo)):
                    if message.text:
                        await client.edit_message(chat_id, msg_id, text=caption_text, parse_mode='html')
                    else:
                        await client.edit_message(chat_id, msg_id, text=caption_text, parse_mode='html')

                await asyncio.sleep(1)
            else:
                logging.debug(f"Message not found with ID: {msg_id}")
        except Exception as e:
            logging.debug(f"Error processing message with ID {msg_id}: {e}")
            continue

    await client.disconnect()

if __name__ == '__main__':
    asyncio.run(main())
