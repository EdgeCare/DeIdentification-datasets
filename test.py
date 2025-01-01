
data = [
   
]

for datapoint in data:
    datapoint["text"] = datapoint["text"].replace(" ", "_")

    print("id: ", datapoint["meta"]["note_id"], "| spans: ", len(datapoint["spans"]))
    print(datapoint["text"])
    for span in datapoint["spans"]:
        print("\t", span["label"],"\t", datapoint["text"][span["start"]:span["end"]])
    print()