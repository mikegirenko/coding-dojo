from count_subcontrols.count_subcontrols import *


def test_read_file():
    assert type(read_file(FILE_PATH)) == dict
    assert bool(read_file(FILE_PATH)) is not False


def test_count_subcontrols_answered_notanswered():
    this_response = {"control_scores": [
    {
      "number": "1.1",
      "maturity_score": 0,
      "name": "Cyber Security Risk Management",
      "question_type": "Family",
      "answer_state": "AnsweredNo",
      "comments": [],
      "id": "7c225e00-2929-4770-ad78-95004451200e",
      "effectiveness_score": 0,
      "parent_number": "1",
      "coverage_score": 0
    },
    {
      "number": "1.1.1",
      "name": "Risk Planning",
      "question_type": "Control",
      "answer_state": "NotAnswered",
      "comments": [],
      "id": "2e843de0-011c-43da-9dbb-f6dee5e5a83d",
      "effectiveness_score": 0,
      "parent_number": "1.1",
      "coverage_score": 0
    },
    {
      "number": "1.1.1.1",
      "name": "Risk Planning",
      "question_type": "SubControl",
      "answer_state": "NotAnswered",
      "comments": [],
      "id": "9c938c09-8212-4b80-a69b-92eaf28ebec8",
      "effectiveness_score": 0,
      "parent_number": "1.1.1",
      "validation_state": "NotSelectedForValidation"
    }]}

    assert count_subcontrols_answered_notanswered(this_response) == 1
