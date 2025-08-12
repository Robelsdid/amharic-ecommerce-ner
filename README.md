# Amharic E-commerce NER: EthioMart Data Extractor & Vendor Analytics

## Overview
This project implements a comprehensive pipeline for extracting structured business data from Amharic Telegram e-commerce channels and provides vendor analytics for micro-lending decisions. The system fine-tunes NER models to identify products, prices, and locations from Amharic text, enabling EthioMart to become a centralized e-commerce hub with data-driven lending capabilities.

##  Project Objectives
-  **Data Ingestion**: Collect messages from Ethiopian Telegram e-commerce channels
-  **NER Model Development**: Fine-tune transformer models for Amharic entity extraction
-  **Model Comparison**: Evaluate multiple approaches (XLM-RoBERTa, BERT-Multilingual)
-  **Model Interpretability**: Implement SHAP/LIME for explainable AI
-  **Vendor Analytics**: Create scorecard system for micro-lending decisions

##  Completed Tasks

### Task 1: Data Ingestion and Preprocessing 
- Telegram API integration for real-time data collection
- Amharic text preprocessing and normalization
- Structured data storage and management

### Task 2: NER Data Labeling 
- CoNLL format labeling for 30+ messages
- Entity types: Product, Price, Location
- High-quality training dataset creation

### Task 3: Model Fine-tuning 
- XLM-RoBERTa fine-tuning for Amharic NER
- BERT-Multilingual model comparison
- Model performance optimization

### Task 4: Model Comparison 
- Systematic evaluation of multiple models
- Performance metrics: F1-score, Precision, Recall
- Best model selection for production

### Task 5: Model Interpretability 
- SHAP (SHapley Additive exPlanations) implementation
- LIME (Local Interpretable Model-agnostic Explanations)
- Model behavior analysis and insights

### Task 6: Vendor Scorecard Analytics 
- **Vendor Analytics Engine**: Processes vendor posts and calculates KPIs
- **Key Metrics**: Posting frequency, engagement rates, price analysis
- **Lending Score Algorithm**: Weighted scoring for micro-lending decisions
- **Business Intelligence**: Data-driven vendor recommendations

##  Selected Telegram Channels
1. @ZemenExpress
2. @nevacomputer  
3. @meneshayeofficial
4. @ethio_brand_collection
5. @helloomarketethiopia
6. @Fashiontera

##  Quick Start

### Prerequisites
- Python 3.8+
- GPU support (recommended for model training)
- Telegram API credentials

### Installation
```bash
# Clone the repository
git clone https://github.com/Robelsdid/amharic-ecommerce-ner.git
cd amharic-ecommerce-ner

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your Telegram API credentials
```

### Usage

#### 1. Data Collection
```bash
python src/ingestion/telegram_ingest.py
```

#### 2. Model Training
```bash
# Run the fine-tuning notebook
jupyter notebook notebooks/fine_tune_ner.ipynb
```

#### 3. Vendor Analytics
```bash
# Run the vendor scorecard analysis
jupyter notebook notebooks/vendor_scorecard.ipynb
```

##  Project Structure
```
amharic-ecommerce-ner/
├── data/
│   ├── raw/           # Unprocessed Telegram data
│   ├── processed/     # Cleaned, structured data
│   └── images/        # Downloaded images
├── src/
│   ├── ingestion/     # Data collection modules
│   ├── preprocessing/ # Text processing utilities
│   └── utils/         # Helper functions
├── notebooks/
│   ├── fine_tune_ner.ipynb              # Model training
│   ├── model_comparison.ipynb           # Model evaluation
│   ├── model_explainability_shap_lime.ipynb  # Interpretability
│   ├── vendor_scorecard.ipynb           # Vendor analytics
│   └── vendor_scorecard_results.json    # Analysis results
├── models/
│   └── ner-finetuned-amharic-final/     # Best performing model
└── requirements.txt
```

##  Key Results

### Model Performance
- **Best Model**: XLM-RoBERTa fine-tuned for Amharic
- **Entity Detection**: Product, Price, Location extraction
- **Accuracy**: High performance on Amharic e-commerce text

### Vendor Analytics Results
- **ZemenExpress**: Lending Score 61.03/100 (Moderate Candidate)
- **FashionTera**: Lending Score 44.83/100 (Weak Candidate)
- **Metrics**: Posting frequency, engagement rates, price analysis

### Business Impact
- Data-driven micro-lending decisions
- Vendor performance tracking
- Automated entity extraction from Amharic text

## 🔧 Technical Stack
- **NLP**: Transformers (Hugging Face), XLM-RoBERTa, BERT
- **Interpretability**: SHAP, LIME
- **Data Processing**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn
- **Telegram API**: Telethon

##  Environment Variables
Create a `.env` file with:
```
TELEGRAM_API_ID=your_api_id
TELEGRAM_API_HASH=your_api_hash
TELEGRAM_PHONE=your_phone_number
```

##  Contributing
This project was developed for the EthioMart NER Team as part of the B5W4 challenge.

##  License
This project is part of the EthioMart e-commerce initiative.

##  Authors
- **EthioMart NER Team**
- **Challenge**: B5W4 - Building an Amharic E-commerce Data Extractor 