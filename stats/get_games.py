import cbbpy.mens_scraper as s
import json
import pandas as pd

df = s.get_games_range(start_date='2021-11-09', end_date='2021-12-20')
a = df[0].to_json('file.json', orient = 'split', compression = 'infer', index = 'true')
