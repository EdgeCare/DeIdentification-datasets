import json


data = [
    
]

new_data = []

TOKENS = {
    "0": "O",
    "1": "PATIENT",
    "2": "STAFF",
    "3": "AGE",
    "4": "DATE",
    "5": "PHONE",
    "6": "ID",
    "7": "EMAIL",
    "8": "LOC",
    "9": "HOSP",
    "10": "PATORG"
}

for datapoint in data:
    print('-'*100)
    new_datapoint = {"text": datapoint["text"], "meta": datapoint["meta"], "spans": []}

    datapoint["text"] = datapoint["text"].replace(" ", "_")
    length = len(datapoint["text"])
    
    i = 0
    index = 0
    while True:
        print("\n\n",len(datapoint["spans"]), "|", datapoint["text"])
        print(' | '.join(i["label"] for i in datapoint["spans"]))
        span_text = input("Enter the span text: ")

        if span_text == "":
            break
        elif span_text == ".":
            new_datapoint["spans"].pop()
            i -= 1
            continue
        token = input("Enter the token: ")

        index = index + datapoint["text"][index:].find(span_text)
        new_datapoint["spans"].append({
            "id": i,
            "start": index,
            "end": index + len(span_text),
            "label": TOKENS[token]
        })
        index += len(span_text)

        i += 1

    new_data.append(new_datapoint)
    

with open("recorrected_data.json", "w") as f:
    json.dump(new_data, f, indent=4)
print("\n\nData saved to recorrected_data.json")