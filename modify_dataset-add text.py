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
        changed = 0
        sentence = entry["sentence"]
        last_end = 0
        id = -1
        for span in entry["spans"]:
            id += 1
            # print("entry[sentence]: ", entry["sentence"])
            span_text = span["text"]
            start = sentence.find(span_text, last_end)
            end = start + len(span_text)
            last_end = end
            if span.get('text') and span.get('start') is None:
                changed = 1
                # only add start and end if text is present and start is not already present
                print("Sentence: ", sentence, "Changed")
                span["id"] = id
                span["start"] = start
                span["end"] = end
                
            if changed:
                span["id"] = id

    with open('all_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print("Added start and end to spans in the dataset")

print("Updated dataset saved as 'updated_dataset.json'")
