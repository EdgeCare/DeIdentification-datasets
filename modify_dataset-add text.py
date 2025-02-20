import json

with open('all_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for entry in data:
    sentence = entry["sentence"] 
    for span in entry["spans"]:
        span_text = sentence[span["start"]:span["end"]] 
        span["text"] = span_text 

with open('updated_all_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("Updated dataset saved as 'updated_dataset.json'")
