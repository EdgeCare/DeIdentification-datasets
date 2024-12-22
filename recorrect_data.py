import json


data = [
    {
        "text": "Doctor: James needs further evaluation to rule out any heart conditions.",
        "meta": {
            "note_id": "462",
            "patient_id": "33556789"
        },
        "spans": [
            {
                "id": "0",
                "start": 8,
                "end": 13,
                "label": "PATIENT"
            }
        ]
    },
    {
        "text": "Patient: My name is Michael Davis. My email address is michael.davis@xyz.com.",
        "meta": {
            "note_id": "463",
            "patient_id": "33667890"
        },
        "spans": [
            {
                "id": "0",
                "start": 14,
                "end": 27,
                "label": "PATIENT"
            },
            {
                "id": "1",
                "start": 46,
                "end": 72,
                "label": "EMAIL"
            }
        ]
    }
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
    "9": "HOSP"
}

for datapoint in data:
    print('-'*100)
    new_datapoint = {"text": datapoint["text"], "meta": datapoint["meta"], "spans": []}

    datapoint["text"] = datapoint["text"].replace(" ", "_")
    length = len(datapoint["text"])
    
    i = 0
    while True:
        print("\n\n",len(datapoint["spans"]), "|", datapoint["text"])
        span_text = input("Enter the span text: ")

        if span_text == "":
            break
        elif span_text == ".":
            new_datapoint["spans"].pop()
            i -= 1
            continue
        token = input("Enter the token: ")

        new_datapoint["spans"].append({
            "id": i,
            "start": datapoint["text"].find(span_text),
            "end": datapoint["text"].find(span_text) + len(span_text),
            "label": TOKENS[token]
        })

        i += 1

    new_data.append(new_datapoint)
    

with open("recorrected_data.json", "w") as f:
    json.dump(new_data, f, indent=4)
print("\n\nData saved to recorrected_data.json")