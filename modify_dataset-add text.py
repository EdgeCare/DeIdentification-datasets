import json

ADD_TEXT = 0
ADD_START_END = 1

with open('all_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

if ADD_TEXT:
    for entry in data:
        sentence = entry["sentence"] 
        for span in entry["spans"]:
            span_text = sentence[span["start"]:span["end"]]
            if span.get('text') is None:
                span["text"] = span_text 

    with open('all_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print("Added text to spans in the dataset")

if ADD_START_END:
    for entry in data:
        sentence = entry["sentence"]
        last_end = 0
        id = -1
        for span in entry["spans"]:
            id += 1
            # print("entry[sentence]: ", entry["sentence"])
            span_text = span["text"]
            start = sentence.find(span_text, last_end)
            if start == -1:
                print("Span text start not found in sentence:", sentence)
            end = start + len(span_text)
            last_end = end
            if span.get('text'):
                # only add start and end if text is present
                span["id"] = id
                span["start"] = start
                span["end"] = end
            else: 
                print("Span['text'] not found. sentence:", sentence)

    with open('all_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print("Added start and end to spans in the dataset")


# # label counts in the dataset
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
