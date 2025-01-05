# open 1.json and 2.json and combine them into 3.json
import json

def change_id_to_int(file_path):
    with open(file_path) as f:
        data1 = json.load(f)
        f.close()

    for d in data1:
        d['meta']["note_id"] = str(d['meta']["note_id"])
        for s in d['spans']:
            s["id"] = int(s["id"])

    with open(file_path, 'w') as f:
        json.dump(data1, f, indent=4)
        f.close()



if __name__ == "__main__":
    change_id_to_int('train.json')
    change_id_to_int('validation.json')

    print("Pre process done!")


