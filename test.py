
data = [
    {
        "text": "Doctor: Yes, you can call us anytime at +1-212-555-4567 for updates.",
        "meta": {
            "note_id": "550",
            "patient_id": "37990123"
        },
        "spans": [
            {
                "id": "0",
                "start": 34,
                "end": 48,
                "label": "PHONE"
            }
        ]
    },
    {
        "text": "Patient: I visited Central Clinic on October 15th for a check-up.",
        "meta": {
            "note_id": "551",
            "patient_id": "38001234"
        },
        "spans": [
            {
                "id": "0",
                "start": 10,
                "end": 24,
                "label": "HOSP"
            },
            {
                "id": "1",
                "start": 28,
                "end": 40,
                "label": "DATE"
            }
        ]
    },
    {
        "text": "Doctor: Your records from Central Clinic on October 15th are available.",
        "meta": {
            "note_id": "552",
            "patient_id": "38001234"
        },
        "spans": [
            {
                "id": "0",
                "start": 20,
                "end": 34,
                "label": "HOSP"
            },
            {
                "id": "1",
                "start": 38,
                "end": 50,
                "label": "DATE"
            }
        ]
    },
    {
        "text": "Patient: My email address is moore.alice@microsoft.com. Is that on record?",
        "meta": {
            "note_id": "553",
            "patient_id": "38112345"
        },
        "spans": [
            {
                "id": "0",
                "start": 23,
                "end": 50,
                "label": "EMAIL"
            }
        ]
    },
    {
        "text": "Doctor: Yes, your email moore.alice@microsoft.com is in our records.",
        "meta": {
            "note_id": "554",
            "patient_id": "38112345"
        },
        "spans": [
            {
                "id": "0",
                "start": 20,
                "end": 47,
                "label": "EMAIL"
            }
        ]
    },
    {
        "text": "Patient: My son, Ben Carter, needs to revisit Maplewood Health Center.",
        "meta": {
            "note_id": "555",
            "patient_id": "38223456"
        },
        "spans": [
            {
                "id": "0",
                "start": 14,
                "end": 24,
                "label": "PATIENT"
            },
            {
                "id": "1",
                "start": 40,
                "end": 66,
                "label": "HOSP"
            }
        ]
    },
    {
        "text": "Doctor: Ben\u00e2\u20ac\u2122s next appointment at Maplewood Health Center is scheduled.",
        "meta": {
            "note_id": "556",
            "patient_id": "38223456"
        },
        "spans": [
            {
                "id": "0",
                "start": 8,
                "end": 11,
                "label": "PATIENT"
            },
            {
                "id": "1",
                "start": 28,
                "end": 54,
                "label": "HOSP"
            }
        ]
    },
    {
        "text": "Patient: I recently visited Tokyo, and now I feel unwell.",
        "meta": {
            "note_id": "557",
            "patient_id": "38334567"
        },
        "spans": [
            {
                "id": "0",
                "start": 20,
                "end": 25,
                "label": "LOC"
            }
        ]
    },
    {
        "text": "Doctor: Traveling to places like Tokyo can sometimes cause fatigue.",
        "meta": {
            "note_id": "558",
            "patient_id": "38334567"
        },
        "spans": [
            {
                "id": "0",
                "start": 27,
                "end": 32,
                "label": "LOC"
            }
        ]
    },
    {
        "text": "Patient: My ID is BC678901. Can you update my records accordingly?",
        "meta": {
            "note_id": "559",
            "patient_id": "38445678"
        },
        "spans": [
            {
                "id": "0",
                "start": 11,
                "end": 19,
                "label": "ID"
            }
        ]
    }
]
for datapoint in data:
    datapoint["text"] = datapoint["text"].replace(" ", "_")

    print(datapoint["text"], " ", len(datapoint["spans"]))
    for span in datapoint["spans"]:
        print(span["label"],"\t", datapoint["text"][span["start"]:span["end"]])
    print()