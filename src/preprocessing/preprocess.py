import os
import json
import re
from glob import glob

RAW_DIR = 'data/raw'
PROCESSED_DIR = 'data/processed'
os.makedirs(PROCESSED_DIR, exist_ok=True)

def clean_amharic_text(text):
    if not text:
        return ''
    # Remove unwanted characters (example: emojis, non-Amharic, excessive whitespace)
    text = re.sub(r'[\u200c\u200d\u202a-\u202e]', '', text)  # Remove special unicode chars
    text = re.sub(r'[\x00-\x1F\x7F-\x9F]', '', text)  # Remove control chars
    text = re.sub(r'\s+', ' ', text).strip()  # Normalize whitespace
    return text

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        messages = json.load(f)
    processed = []
    for msg in messages:
        processed.append({
            'message_id': msg.get('message_id'),
            'channel': msg.get('channel'),
            'timestamp': msg.get('timestamp'),
            'sender_id': msg.get('sender_id'),
            'text': clean_amharic_text(msg.get('text', '')),
            'media': msg.get('media'),
            'media_type': msg.get('media_type')
        })
    return processed

def main():
    raw_files = glob(os.path.join(RAW_DIR, '*.json'))
    for raw_file in raw_files:
        processed_data = process_file(raw_file)
        base = os.path.basename(raw_file)
        out_path = os.path.join(PROCESSED_DIR, base)
        with open(out_path, 'w', encoding='utf-8') as f:
            json.dump(processed_data, f, ensure_ascii=False, indent=2)
        print(f'Processed and saved: {out_path}')

if __name__ == '__main__':
    main() 