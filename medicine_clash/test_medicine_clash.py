from medicine_clash.medicine_clash import *

obj_patient = Patient()


def test_clash_returns_list_of_meds():
    list_of_medicines = ["Paxlovid", "Remdesivir", "Vitamin D"]
    list_of_meds, days_to_cons = obj_patient.clash(list_of_medicines)
    assert list_of_meds  == ["Paxlovid", "Remdesivir", "Vitamin D"]


def test_clash_returns_default_days_to_consider():
    list_of_medicines = ["Paxlovid", "Remdesivir", "Vitamin D"]
    list_of_meds, days_to_cons = obj_patient.clash(list_of_medicines)
    assert days_to_cons == 90


def test_patient_returns_provided_days_to_consider():
    list_of_medicines = ["Paxlovid", "Remdesivir", "Vitamin D"]
    days_to_consider = 120
    list_of_meds, days_to_cons = obj_patient.clash(list_of_medicines, days_to_consider)
    assert days_to_cons == 120


def test_clash_exists():
    assert not obj_patient.clash_exists()
