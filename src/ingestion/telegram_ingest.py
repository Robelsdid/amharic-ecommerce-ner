import os
import json
from datetime import datetime
from telethon import TelegramClient
from telethon.tl.types import MessageMediaPhoto, MessageMediaDocument
from telethon.errors import ChannelInvalidError, ChannelPrivateError, ChannelPublicGroupNaError
from dotenv import load_dotenv
import logging
import asyncio

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

load_dotenv()
API_ID = os.getenv('TELEGRAM_API_ID')
API_HASH = os.getenv('TELEGRAM_API_HASH')
PHONE = os.getenv('TELEGRAM_PHONE')

# Validate environment variables
if not API_ID or not API_HASH or not PHONE:
    logging.error('Missing one or more required environment variables: TELEGRAM_API_ID, TELEGRAM_API_HASH, TELEGRAM_PHONE')
    exit(1)
API_ID = int(API_ID)

# Configurable parameters
CHANNELS = os.getenv('TELEGRAM_CHANNELS')
if CHANNELS:
    CHANNELS = [c.strip() for c in CHANNELS.split(',') if c.strip()]
else:
    CHANNELS = [
        'ZemenExpress',
        'nevacomputer',
        'meneshayeofficial',
        'ethio_brand_collection',
        'helloomarketethiopia',
        'Fashiontera',
    ]
MESSAGE_LIMIT = int(os.getenv('TELEGRAM_MESSAGE_LIMIT', 100))
RAW_DATA_DIR = os.getenv('RAW_DATA_DIR', 'data/raw')
MEDIA_DIR = os.getenv('MEDIA_DIR', 'data/images')
MEDIA_TIMEOUT = 30  # seconds

os.makedirs(RAW_DATA_DIR, exist_ok=True)
os.makedirs(MEDIA_DIR, exist_ok=True)

def connect_telegram():
    return TelegramClient('session_name', API_ID, API_HASH)

async def fetch_messages(client, channels):
    for channel in channels:
        messages = []
        try:
            async for message in client.iter_messages(channel, limit=MESSAGE_LIMIT):
                msg_data = {
                    "message_id": message.id,
                    "channel": channel,
                    "timestamp": message.date.isoformat() if message.date else None,
                    "sender_id": message.sender_id,
                    "text": message.text,
                    "media": None,
                    "media_type": None
                }
                # Download media if present, with timeout
                if message.media:
                    try:
                        if isinstance(message.media, (MessageMediaPhoto, MessageMediaDocument)):
                            file_path = await asyncio.wait_for(
                                client.download_media(message, MEDIA_DIR), timeout=MEDIA_TIMEOUT
                            )
                            msg_data["media"] = file_path
                            msg_data["media_type"] = "photo" if isinstance(message.media, MessageMediaPhoto) else "document"
                        else:
                            msg_data["media"] = str(message.media)
                            msg_data["media_type"] = "other"
                    except asyncio.TimeoutError:
                        logging.warning(f"Timeout: Skipped media for message {message.id} in {channel} after {MEDIA_TIMEOUT} seconds.")
                        msg_data["media"] = None
                        msg_data["media_type"] = None
                    except Exception as e:
                        logging.warning(f"Failed to download media for message {message.id} in {channel}: {e}")
                        msg_data["media"] = None
                        msg_data["media_type"] = None
                messages.append(msg_data)
        except (ChannelInvalidError, ChannelPrivateError, ChannelPublicGroupNaError) as e:
            logging.error(f"Failed to fetch messages from {channel}: {e}")
            continue
        except Exception as e:
            logging.error(f"Unexpected error fetching from {channel}: {e}")
            continue
        filename = f"{RAW_DATA_DIR}/{channel}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(messages, f, ensure_ascii=False, indent=2)
        logging.info(f"Saved {len(messages)} messages from {channel} to {filename}")

def main():
    client = connect_telegram()
    with client:
        client.loop.run_until_complete(fetch_messages(client, CHANNELS))

if __name__ == '__main__':
    main()
