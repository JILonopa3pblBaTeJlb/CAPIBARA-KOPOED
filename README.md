# CAPIBARA-KOPOED
This repository contains a Python script that uses the Telethon library to automate the editing of messages in a Telegram channel. The script replaces the media and caption of each message within a specified range of message IDs with new media and a new caption.

Requirements

    Python 3.6+
    Telethon library (pip install telethon)

Configuration

The script requires the following variables to be set:

    API_ID: Your Telegram API ID.
    api_hash: Your Telegram API hash.
    token: Your Telegram bot token.
    chat_id: The ID of the channel to edit messages in.
    media_files: A list of filenames for the media to be uploaded.
    caption_text: The text to replace the captions with.

Usage

To run the script, execute the following command in your terminal:

python capibara-kopoed.py

Make sure to replace the values of the required variables in the script before running it.
Script A: Replacing media

The first script in the main function (main()) is responsible for replacing the media of each message within the specified range of message IDs. It selects a random media file from the media_files list, uploads it to Telegram using the upload_file() method of the TelegramClient, and creates an InputMedia object with the appropriate type (InputMediaUploadedPhoto for images and InputMediaUploadedDocument for videos). It then uses the EditMessageRequest method of the TelegramClient to edit the message with the new media.

Script B: Replacing captions

The second script in the main function is responsible for replacing the captions of each message within the specified range of message IDs. It retrieves the message using the get_messages() method of the TelegramClient, checks if it has media (photo or video), and replaces the caption with caption_text using the edit_message() method of the TelegramClient. If the message has no media, the script simply skips it.
Error handling

The script handles errors that may occur during execution (e.g. messages that cannot be edited) and logs them using the logging module.
License

This script is licensed under the MIT License. See the LICENSE file for details.
