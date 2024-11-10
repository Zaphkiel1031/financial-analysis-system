import os

# 建立所需的資料夾
folders = [
    'src',
    'data',
    'tests',
    'logs'
]

for folder in folders:
    os.makedirs(folder, exist_ok=True) 