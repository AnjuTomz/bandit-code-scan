import pandas as pd
import os

df = pd.read_csv('codes.csv')  # make sure your file is called codes.csv
os.makedirs('code_snippets', exist_ok=True)
for idx, row in df.iterrows():
    code = row['full_code']
    with open(f'code_snippets/snippet_{idx}.py', 'w', encoding='utf-8') as f:
        f.write(str(code))
