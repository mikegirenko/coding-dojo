"""
As a health insurer
I want to be able to search for patients who have a medicine clash
So that I can alert their doctor and get their prescription changed
"""

# return collection of days on which all the medicines were being taken

DAYS_TO_CONSIDER = 90
PATIENT_LIST = [{"name": "Steve", "medicine": ["Paxlovid", "Remdesivir"]},
                {"name": "Bob", "medicine": ["Remdesivir"]}]
MEDICINE = [{"name": "Paxlovid", "prescription": DAYS_TO_CONSIDER - 45},
            {"name": "Paxlovid", "prescription": DAYS_TO_CONSIDER - 30},
            {"name": "Remdesivir", "prescription": DAYS_TO_CONSIDER - 45},
            {"name": "Vitamin D", "prescription": DAYS_TO_CONSIDER - 45}]
PRESCRIPTION = [{"dispense date": DAYS_TO_CONSIDER - 30, "days supply": 10},
                {"dispense date": DAYS_TO_CONSIDER - 45, "days supply": 45}]


class Patient:

    def clash(self, list_of_medicines, days_to_consider=DAYS_TO_CONSIDER):
        return list_of_medicines, days_to_consider

    def clash_exists(self):
        has_clash = False
        vals = []
        meds_with_same_days_to_consider = []
        for medicine in MEDICINE:
            vals.append(medicine["prescription"])
        for patient in PATIENT_LIST:
            for medicine in MEDICINE:
                if medicine["name"] in patient["medicine"]:
                    pass
        return has_clash
