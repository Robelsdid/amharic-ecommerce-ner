# Amharic E-commerce NER: EthioMart Data Extractor

## Overview
This project aims to build a modular pipeline for extracting structured business data from Amharic Telegram e-commerce channels. The extracted data will be used to fine-tune NER models for EthioMart, a centralized e-commerce hub.

## Objectives
- Ingest messages (text, images, documents) from selected Telegram channels
- Preprocess and structure Amharic text for NER
- Store data for downstream machine learning tasks

## Selected Telegram Channels
1. @ZemenExpress
2. @nevacomputer
3. @meneshayeofficial
4. @ethio_brand_collection
5. @helloomarketethiopia
6. @Fashiontera

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Add your Telegram API credentials to a `.env` file (see `.env.example`).
3. Run the ingestion script to collect data.

## Directory Structure
- `data/raw/` - Unprocessed Telegram data
- `data/processed/` - Cleaned, structured data
- `data/images/` - Downloaded images
- `src/` - Source code modules

## Authors
- EthioMart NER Team 