import os
import json
import re

def tokenize(text):
    # Simple whitespace tokenizer for Amharic
    return text.split()

INPUT_FILE = 'data/processed/ZemenExpress_20250623_231105.json'
OUTPUT_FILE = 'data/processed/ner_labels_template.conll'

with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    messages = json.load(f)

count = 0
with open(OUTPUT_FILE, 'w', encoding='utf-8') as out:
    for msg in messages:
        text = msg.get('text', '').strip()
        if not text:
            continue
        tokens = tokenize(text)
        for token in tokens:
            out.write(f"{token} O\n")
        out.write("\n")  # Blank line between messages
        count += 1
        if count >= 30:
            break
print(f"CoNLL template created with {count} messages: {OUTPUT_FILE}") 