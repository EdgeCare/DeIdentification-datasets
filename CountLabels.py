# label counts in the dataset

import json

with open('all_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

    label_count = {}
    for row in data:
        for span in row['spans']:
            label = span['label']
            if label in label_count:
                label_count[label] += 1
            else:
                label_count[label] = 1

with open('label_count.json', 'w') as f:
    json.dump(label_count, f, indent=4)
    print('label count saved to label_count.json')
    print(label_count)