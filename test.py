
data = [
   
]

for datapoint in data:
    datapoint["sentence"] = datapoint["sentence"].replace(" ", "_")

    print("id: ", datapoint["meta"]["note_id"], "| spans: ", len(datapoint["spans"]))
    print(datapoint["sentence"])
    for span in datapoint["spans"]:
        print("\t", span["label"],"\t", datapoint["sentence"][span["start"]:span["end"]])
    print()