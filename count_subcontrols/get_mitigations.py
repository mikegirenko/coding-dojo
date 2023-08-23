import json

FILE_PATH = "/Users/mike.girenko/response.json"


def read_file(file_path) -> dict:
    with open (file_path, "r") as file:
        read_data = file.read()
        data_to_dict = json.loads(read_data)

    return data_to_dict


def get_mitigations(data: dict) -> list:
    mitigations_list = []
    for k, v in data.items():
        if k == "data":
            for m, s in v.items():
                for t, p in s.items():
                    if t == "mappedControls":
                        for item in p:
                            for w, y in item.items():
                                if w == "grxControls":
                                    for this_item in y:
                                        for x, z in this_item.items():
                                            if x == "mitigation":
                                                print(z)


file_data = read_file(FILE_PATH)
get_mitigations(file_data)
