import pandas as pd

# JSONファイルを読み込み（ファイル名を入力）

df = pd.read_json('SAMPLE.json')

# CSVに変換して保存（任意のファイル名を入力）
df.to_csv("SAMPLE.csv", encoding="UTF-8")
