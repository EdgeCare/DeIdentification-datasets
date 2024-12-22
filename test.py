
data = [
    
]
for datapoint in data:
    datapoint["text"] = datapoint["text"].replace(" ", "_")

    print(datapoint["text"], " ", len(datapoint["spans"]))
    for span in datapoint["spans"]:
        print(span["label"],"\t", datapoint["text"][span["start"]:span["end"]])
    print()