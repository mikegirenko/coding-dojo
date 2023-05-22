import json

FILE_PATH = "/Users/mike.girenko/response_1683729395919.json"


def read_file(file_path) -> dict:
    with open (file_path, "r") as file:
        read_data = file.read()
        data_to_dict = json.loads(read_data)

    return data_to_dict


def count_subcontrols_answered_notanswered(data: dict) -> int:
    answer_state_list = []
    not_answered_list = []
    for k, v in data.items():
        if k == "control_scores":
            for control_score in v:
                for key, value in control_score.items():
                    if key == "question_type" and value == "SubControl":
                        answer_state_list.append(control_score.get("answer_state"))
    for answer_state in answer_state_list:
        if answer_state == "NotAnswered":
            not_answered_list.append(answer_state)

    return len(not_answered_list)


file_data = read_file(FILE_PATH)
print(f"There are {count_subcontrols_answered_notanswered(file_data)} SubControls which have NotAnswered "
      f"answer_state")
