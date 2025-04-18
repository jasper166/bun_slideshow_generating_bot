import os
import pandas as pd
import json

# Construct the exact CSV path
filename = '[LMS_Growth] KBCT Cơ bản về kinh doanh trên Shopee - KBCT.csv'
csv_path = os.path.join(filename)

# Read the CSV file
df = pd.read_csv(csv_path)



# Convert to JSON and save
json_filename = filename.rsplit('.', 1)[0] + '.json'
json_path = os.path.join(json_filename)
records = df.to_dict(orient='records')
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(records, f, ensure_ascii=False, indent=2)

# Display a preview of the data
# import ace_tools as tools; tools.display_dataframe_to_user("Preview of Converted Data", df.head())

print(f"JSON file successfully saved as: {json_path}")
