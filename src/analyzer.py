import spacy
import pandas as pd
import numpy as np
from textblob import TextBlob

class TextAnalyzer:
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')
        
    def analyze_text(self, text):
        doc = self.nlp(text)
        
        # 實體識別
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        
        # 情感分析
        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity
        
        # 關鍵詞提取
        keywords = [token.text for token in doc if not token.is_stop and token.is_alpha]
        
        return {
            'entities': entities,
            'sentiment': sentiment,
            'keywords': keywords
        }
    
    def analyze_financial_metrics(self, text):
        # 這裡可以添加更多財務相關的分析邏輯
        doc = self.nlp(text)
        
        # 尋找數字和貨幣相關的實體
        financial_data = {
            'numbers': [token.text for token in doc if token.like_num],
            'currencies': [ent.text for ent in doc.ents if ent.label_ == 'MONEY']
        }
        
        return financial_data 