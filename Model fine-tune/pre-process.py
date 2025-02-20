import json
import random

def change_id_to_int(file_path="all_data.json"):
    with open(file_path, "r", encoding="utf-8") as f:
        data1 = json.load(f)
        f.close()

    for d in data1:
        d['meta']["note_id"] = str(d['meta']["note_id"])
        for s in d['spans']:
            s["id"] = int(s["id"])

    with open(file_path, 'w') as f:
        json.dump(data1, f, indent=4)
        f.close()

def split_data(input_file="all_data.json", train_file="train.json", validation_file="validation.json", val_percentage=0.15):
    """
    Randomly selects `val_count` entries for validation.json, saves the rest in train.json.
    """
    with open(input_file) as f:
        data = json.load(f)

    random.shuffle(data)
    print(f"Total data: {len(data)}")
    val_count = int(len(data) * val_percentage)
    validation_data = data[:val_count]
    train_data = data[val_count:]

    with open(validation_file, 'w') as val_f:
        json.dump(validation_data, val_f, indent=4)
    
    with open(train_file, 'w') as train_f:
        json.dump(train_data, train_f, indent=4)
    
    print(f"Split data into {len(validation_data)} entries in {validation_file} and {len(train_data)} entries in {train_file}")


if __name__ == "__main__":
    change_id_to_int()
    split_data()

    print("Pre process done!")


