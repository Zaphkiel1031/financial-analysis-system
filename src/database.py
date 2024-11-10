import json
import pandas as pd
from datetime import datetime

class DataStorage:
    def __init__(self, data_dir='data'):
        self.data_dir = data_dir
        
    def save_to_json(self, data, filename):
        full_path = f"{self.data_dir}/{filename}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(full_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        return full_path
    
    def save_to_csv(self, data, filename):
        full_path = f"{self.data_dir}/{filename}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df = pd.DataFrame(data)
        df.to_csv(full_path, index=False, encoding='utf-8')
        return full_path 