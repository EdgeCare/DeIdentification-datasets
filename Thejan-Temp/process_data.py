import json


data = [
    {
        "text": "Patient: I need a refill for the medication prescribed by Dr. Jane Adams.\nDoctor: Sure. I also need your MRN.\nPatient: It's 87654321.",
        "meta": {
            "note_id": "21",
            "patient_id": "6789013"
        },
        "spans": [
            {
                "id": "0",
                "start": 49,
                "end": 61,
                "label": "STAFF"
            },
            {
                "id": "1",
                "start": 90,
                "end": 98,
                "label": "ID"
            }
        ]
    },
    {
        "text": "Doctor: Have you been to any hospital recently?\nPatient: Yes, I visited Mount Sinai Hospital two weeks ago.",
        "meta": {
            "note_id": "22",
            "patient_id": "7890124"
        },
        "spans": [
            {
                "id": "0",
                "start": 24,
                "end": 46,
                "label": "HOSP"
            },
            {
                "id": "1",
                "start": 47,
                "end": 61,
                "label": "DATE"
            }
        ]
    },
    {
        "text": "Patient: My email is john.doe123@example.com. Please update your records.\nDoctor: Done. Do you have an emergency contact?\nPatient: Yes, you can reach my wife at 987-654-3210.",
        "meta": {
            "note_id": "23",
            "patient_id": "8901235"
        },
        "spans": [
            {
                "id": "0",
                "start": 13,
                "end": 43,
                "label": "EMAIL"
            },
            {
                "id": "1",
                "start": 102,
                "end": 115,
                "label": "PHONE"
            }
        ]
    },
    {
        "text": "Doctor: What's the name of your insurance provider?\nPatient: It's Blue Cross Blue Shield.",
        "meta": {
            "note_id": "24",
            "patient_id": "9012346"
        },
        "spans": [
            {
                "id": "0",
                "start": 39,
                "end": 63,
                "label": "PATORG"
            }
        ]
    },
    {
        "text": "Patient: My father is 65 years old. He has been experiencing chest pain for a week.\nDoctor: Can you confirm his ID?\nPatient: Yes, it's FATHER-ID-56789.",
        "meta": {
            "note_id": "25",
            "patient_id": "1234568"
        },
        "spans": [
            {
                "id": "0",
                "start": 13,
                "end": 19,
                "label": "PATIENT"
            },
            {
                "id": "1",
                "start": 23,
                "end": 25,
                "label": "AGE"
            },
            {
                "id": "2",
                "start": 92,
                "end": 111,
                "label": "ID"
            }
        ]
    },
    {
        "text": "Patient: I was born on January 15, 1975.\nDoctor: Thank you, Sarah.",
        "meta": {
            "note_id": "26",
            "patient_id": "2345679"
        },
        "spans": [
            {
                "id": "0",
                "start": 19,
                "end": 35,
                "label": "DATE"
            },
            {
                "id": "1",
                "start": 50,
                "end": 55,
                "label": "PATIENT"
            }
        ]
    },
    {
        "text": "Doctor: When did you visit Mayo Clinic?\nPatient: Around March this year.",
        "meta": {
            "note_id": "27",
            "patient_id": "3456780"
        },
        "spans": [
            {
                "id": "0",
                "start": 18,
                "end": 29,
                "label": "HOSP"
            },
            {
                "id": "1",
                "start": 37,
                "end": 42,
                "label": "DATE"
            }
        ]
    },
    {
        "text": "Patient: I traveled to London last summer.\nDoctor: Were you on vacation?",
        "meta": {
            "note_id": "28",
            "patient_id": "4567891"
        },
        "spans": [
            {
                "id": "0",
                "start": 18,
                "end": 24,
                "label": "LOC"
            },
            {
                "id": "1",
                "start": 30,
                "end": 41,
                "label": "DATE"
            }
        ]
    },
    {
        "text": "My contact number is 800-555-0199. Please update your records.",
        "meta": {
            "note_id": "29",
            "patient_id": "5678902"
        },
        "spans": [
            {
                "id": "0",
                "start": 25,
                "end": 37,
                "label": "PHONE"
            }
        ]
    },
    {
        "text": "Doctor: Can I have your insurance ID?\nPatient: Sure, it's INSID-2024.",
        "meta": {
            "note_id": "30",
            "patient_id": "6789013"
        },
        "spans": [
            {
                "id": "0",
                "start": 31,
                "end": 43,
                "label": "ID"
            }
        ]
    },
    {
        "text": "I attended Harvard Medical School in 1995.",
        "meta": {
            "note_id": "31",
            "patient_id": "7890124"
        },
        "spans": [
            {
                "id": "0",
                "start": 11,
                "end": 37,
                "label": "PATORG"
            },
            {
                "id": "1",
                "start": 41,
                "end": 45,
                "label": "DATE"
            }
        ]
    },
    {
        "text": "Dr. Nathan from City Hospital treated me for pneumonia.",
        "meta": {
            "note_id": "32",
            "patient_id": "8901235"
        },
        "spans": [
            {
                "id": "0",
                "start": 8,
                "end": 18,
                "label": "STAFF"
            },
            {
                "id": "1",
                "start": 24,
                "end": 37,
                "label": "HOSP"
            }
        ]
    },
    {
        "text": "Doctor: Please confirm your address.\nPatient: 123 Main St, Springfield, IL, USA.",
        "meta": {
            "note_id": "33",
            "patient_id": "9012346"
        },
        "spans": [
            {
                "id": "0",
                "start": 8,
                "end": 36,
                "label": "LOC"
            }
        ]
    },
    {
        "text": "I was born on April 12, 1988, in Chicago.",
        "meta": {
            "note_id": "34",
            "patient_id": "1234567"
        },
        "spans": [
            {
                "id": "0",
                "start": 15,
                "end": 30,
                "label": "DATE"
            },
            {
                "id": "1",
                "start": 35,
                "end": 42,
                "label": "LOC"
            }
        ]
    },
    {
        "text": "My cousin, Rachel Green, is also a patient here.",
        "meta": {
            "note_id": "35",
            "patient_id": "2345678"
        },
        "spans": [
            {
                "id": "0",
                "start": 14,
                "end": 27,
                "label": "PATIENT"
            }
        ]
    },
    {
        "text": "Doctor: Do you have an email I can contact you at?\nPatient: Yes, it's jane.doe@hospital.org.",
        "meta": {
            "note_id": "36",
            "patient_id": "3456789"
        },
        "spans": [
            {
                "id": "0",
                "start": 31,
                "end": 51,
                "label": "EMAIL"
            }
        ]
    },
    {
        "text": "Patient: My son's name is Tyler, and he's 7 years old.",
        "meta": {
            "note_id": "37",
            "patient_id": "4567890"
        },
        "spans": [
            {
                "id": "0",
                "start": 22,
                "end": 27,
                "label": "PATIENT"
            },
            {
                "id": "1",
                "start": 38,
                "end": 47,
                "label": "AGE"
            }
        ]
    },
    {
        "text": "Doctor: Do you recall the date of your accident?\nPatient: Yes, it was on September 14, 2024.",
        "meta": {
            "note_id": "38",
            "patient_id": "5678901"
        },
        "spans": [
            {
                "id": "0",
                "start": 32,
                "end": 50,
                "label": "DATE"
            }
        ]
    },
    {
        "text": "Patient: I live in Seattle, WA.",
        "meta": {
            "note_id": "39",
            "patient_id": "6789012"
        },
        "spans": [
            {
                "id": "0",
                "start": 11,
                "end": 23,
                "label": "LOC"
            }
        ]
    },
    {
        "text": "Doctor: Can you verify your pharmacy details?\nPatient: Walgreens Pharmacy, 1234 Oak St, Boston, MA.",
        "meta": {
            "note_id": "40",
            "patient_id": "7890123"
        },
        "spans": [
            {
                "id": "0",
                "start": 9,
                "end": 28,
                "label": "HOSP"
            },
            {
                "id": "1",
                "start": 30,
                "end": 50,
                "label": "LOC"
            }
        ]
    },
    {
        "text": "Doctor: Can I have the date of your last checkup?\nPatient: It was on July 3, 2023.",
        "meta": {
            "note_id": "41",
            "patient_id": "8901234"
        },
        "spans": [
            {
                "id": "0",
                "start": 34,
                "end": 47,
                "label": "DATE"
            }
        ]
    },
    {
        "text": "Patient: My contact email is patient.john@yahoo.com.",
        "meta": {
            "note_id": "42",
            "patient_id": "9012345"
        },
        "spans": [
            {
                "id": "0",
                "start": 23,
                "end": 49,
                "label": "EMAIL"
            }
        ]
    },
    {
        "text": "Patient: I was admitted to Bellevue Hospital last winter.",
        "meta": {
            "note_id": "43",
            "patient_id": "1234566"
        },
        "spans": [
            {
                "id": "0",
                "start": 21,
                "end": 38,
                "label": "HOSP"
            },
            {
                "id": "1",
                "start": 39,
                "end": 50,
                "label": "DATE"
            }
        ]
    },
    {
        "text": "Doctor: When did you visit Dr. Emily Watson?\nPatient: Around November 12th.",
        "meta": {
            "note_id": "44",
            "patient_id": "2345677"
        },
        "spans": [
            {
                "id": "0",
                "start": 24,
                "end": 39,
                "label": "STAFF"
            },
            {
                "id": "1",
                "start": 48,
                "end": 63,
                "label": "DATE"
            }
        ]
    },
    {
        "text": "Patient: I live in San Francisco, California, 94123.",
        "meta": {
            "note_id": "45",
            "patient_id": "3456788"
        },
        "spans": [
            {
                "id": "0",
                "start": 11,
                "end": 41,
                "label": "LOC"
            }
        ]
    },
    {
        "text": "Doctor: What's the name of the pharmacy you use?\nPatient: CVS Pharmacy on Elm Street, Austin, TX.",
        "meta": {
            "note_id": "46",
            "patient_id": "4567899"
        },
        "spans": [
            {
                "id": "0",
                "start": 23,
                "end": 35,
                "label": "HOSP"
            },
            {
                "id": "1",
                "start": 39,
                "end": 58,
                "label": "LOC"
            }
        ]
    },
    {
        "text": "Patient: My son, Eric, is 15 years old and has allergies.",
        "meta": {
            "note_id": "47",
            "patient_id": "5678900"
        },
        "spans": [
            {
                "id": "0",
                "start": 12,
                "end": 16,
                "label": "PATIENT"
            },
            {
                "id": "1",
                "start": 22,
                "end": 31,
                "label": "AGE"
            }
        ]
    },
    {
        "text": "Doctor: Your ID shows as PX123456. Can you confirm it?\nPatient: Yes, that's correct.",
        "meta": {
            "note_id": "48",
            "patient_id": "6789011"
        },
        "spans": [
            {
                "id": "0",
                "start": 17,
                "end": 26,
                "label": "ID"
            }
        ]
    },
    {
        "text": "Patient: My daughter, Lucy, is starting treatment tomorrow, December 15th.",
        "meta": {
            "note_id": "49",
            "patient_id": "7890122"
        },
        "spans": [
            {
                "id": "0",
                "start": 15,
                "end": 19,
                "label": "PATIENT"
            },
            {
                "id": "1",
                "start": 48,
                "end": 63,
                "label": "DATE"
            }
        ]
    },
    {
        "text": "Doctor: Please confirm your ZIP code.\nPatient: It's 90210.",
        "meta": {
            "note_id": "50",
            "patient_id": "8901233"
        },
        "spans": [
            {
                "id": "0",
                "start": 31,
                "end": 36,
                "label": "LOC"
            }
        ]
    },
    {
        "text": "Patient: My primary doctor is Dr. Lisa Thompson.",
        "meta": {
            "note_id": "51",
            "patient_id": "9012344"
        },
        "spans": [
            {
                "id": "0",
                "start": 25,
                "end": 41,
                "label": "STAFF"
            }
        ]
    },
    {
        "text": "Patient: I was born on February 20, 1980, in Miami, Florida.",
        "meta": {
            "note_id": "52",
            "patient_id": "1234565"
        },
        "spans": [
            {
                "id": "0",
                "start": 15,
                "end": 32,
                "label": "DATE"
            },
            {
                "id": "1",
                "start": 37,
                "end": 50,
                "label": "LOC"
            }
        ]
    },
    {
        "text": "Doctor: Have you visited Johns Hopkins Hospital before?\nPatient: Yes, last year in October.",
        "meta": {
            "note_id": "53",
            "patient_id": "2345676"
        },
        "spans": [
            {
                "id": "0",
                "start": 18,
                "end": 44,
                "label": "HOSP"
            },
            {
                "id": "1",
                "start": 55,
                "end": 71,
                "label": "DATE"
            }
        ]
    },
    {
        "text": "Patient: My phone number is 123-456-7890.",
        "meta": {
            "note_id": "54",
            "patient_id": "3456787"
        },
        "spans": [
            {
                "id": "0",
                "start": 24,
                "end": 36,
                "label": "PHONE"
            }
        ]
    },
    {
        "text": "Patient: I'm working at Microsoft Corporation as a software engineer.",
        "meta": {
            "note_id": "55",
            "patient_id": "4567898"
        },
        "spans": [
            {
                "id": "0",
                "start": 14,
                "end": 35,
                "label": "PATORG"
            }
        ]
    },
    {
        "text": "Doctor: Can you confirm your birth date?\nPatient: Yes, it's May 15, 1990.",
        "meta": {
            "note_id": "56",
            "patient_id": "5678909"
        },
        "spans": [
            {
                "id": "0",
                "start": 32,
                "end": 44,
                "label": "DATE"
            }
        ]
    },
    {
        "text": "Patient: My father, Robert, is being treated by Dr. William Harris.",
        "meta": {
            "note_id": "57",
            "patient_id": "6789010"
        },
        "spans": [
            {
                "id": "0",
                "start": 13,
                "end": 19,
                "label": "PATIENT"
            },
            {
                "id": "1",
                "start": 40,
                "end": 58,
                "label": "STAFF"
            }
        ]
    },
    {
        "text": "Doctor: Can I have your fax number?\nPatient: It's 555-987-6543.",
        "meta": {
            "note_id": "58",
            "patient_id": "7890121"
        },
        "spans": [
            {
                "id": "0",
                "start": 27,
                "end": 39,
                "label": "PHONE"
            }
        ]
    },
    {
        "text": "Patient: I visited Stanford Hospital on October 9th.",
        "meta": {
            "note_id": "59",
            "patient_id": "8901232"
        },
        "spans": [
            {
                "id": "0",
                "start": 11,
                "end": 29,
                "label": "HOSP"
            },
            {
                "id": "1",
                "start": 33,
                "end": 44,
                "label": "DATE"
            }
        ]
    },
    {
        "text": "Patient: My account ID is ACCT2024.",
        "meta": {
            "note_id": "60",
            "patient_id": "9012341"
        },
        "spans": [
            {
                "id": "0",
                "start": 18,
                "end": 26,
                "label": "ID"
            }
        ]
    },
    {
        "text": "Doctor: Can you provide the date of the surgery?\nPatient: Yes, it was March 10, 2022.",
        "meta": {
            "note_id": "61",
            "patient_id": "9123456"
        },
        "spans": [
            {
                "id": "0",
                "start": 37,
                "end": 52,
                "label": "DATE"
            }
        ]
    },
    {
        "text": "Patient: I was treated at St. Mary's Hospital in February.",
        "meta": {
            "note_id": "62",
            "patient_id": "8234567"
        },
        "spans": [
            {
                "id": "0",
                "start": 21,
                "end": 41,
                "label": "HOSP"
            },
            {
                "id": "1",
                "start": 45,
                "end": 53,
                "label": "DATE"
            }
        ]
    },
    {
        "text": "Patient: You can reach me at 987-654-3210 if needed.",
        "meta": {
            "note_id": "63",
            "patient_id": "7345678"
        },
        "spans": [
            {
                "id": "0",
                "start": 21,
                "end": 33,
                "label": "PHONE"
            }
        ]
    },
    {
        "text": "Patient: My son, Alex, turned 7 years old last week.",
        "meta": {
            "note_id": "64",
            "patient_id": "6456789"
        },
        "spans": [
            {
                "id": "0",
                "start": 12,
                "end": 16,
                "label": "PATIENT"
            },
            {
                "id": "1",
                "start": 23,
                "end": 31,
                "label": "AGE"
            },
            {
                "id": "2",
                "start": 40,
                "end": 49,
                "label": "DATE"
            }
        ]
    },
    {
        "text": "Doctor: Could you confirm your email address?\nPatient: Yes, it's jane.doe@healthmail.com.",
        "meta": {
            "note_id": "65",
            "patient_id": "5567890"
        },
        "spans": [
            {
                "id": "0",
                "start": 38,
                "end": 65,
                "label": "EMAIL"
            }
        ]
    },
    {
        "text": "Patient: I've been working at Tesla for the last 5 years.",
        "meta": {
            "note_id": "66",
            "patient_id": "4678901"
        },
        "spans": [
            {
                "id": "0",
                "start": 23,
                "end": 28,
                "label": "PATORG"
            }
        ]
    },
    {
        "text": "Doctor: What is your current ZIP code?\nPatient: It's 10001.",
        "meta": {
            "note_id": "67",
            "patient_id": "3789012"
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
        "text": "Patient: My pharmacist is Dr. Clara Roberts.",
        "meta": {
            "note_id": "68",
            "patient_id": "2890123"
        },
        "spans": [
            {
                "id": "0",
                "start": 20,
                "end": 37,
                "label": "STAFF"
            }
        ]
    },
    {
        "text": "Doctor: What's your MRN?\nPatient: It's MRN67890.",
        "meta": {
            "note_id": "69",
            "patient_id": "1901234"
        },
        "spans": [
            {
                "id": "0",
                "start": 17,
                "end": 26,
                "label": "ID"
            }
        ]
    },
    {
        "text": "Patient: I stayed at Hilton Hotel during my trip to Miami.",
        "meta": {
            "note_id": "70",
            "patient_id": "1012345"
        },
        "spans": [
            {
                "id": "0",
                "start": 13,
                "end": 25,
                "label": "LOC"
            },
            {
                "id": "1",
                "start": 48,
                "end": 53,
                "label": "LOC"
            }
        ]
    },
    {
        "text": "Patient: My daughter, Sarah, was born on August 12, 2015.",
        "meta": {
            "note_id": "71",
            "patient_id": "2123456"
        },
        "spans": [
            {
                "id": "0",
                "start": 15,
                "end": 20,
                "label": "PATIENT"
            },
            {
                "id": "1",
                "start": 34,
                "end": 49,
                "label": "DATE"
            }
        ]
    },
    {
        "text": "Patient: Dr. Daniel Grey suggested the medication.",
        "meta": {
            "note_id": "72",
            "patient_id": "3234567"
        },
        "spans": [
            {
                "id": "0",
                "start": 8,
                "end": 23,
                "label": "STAFF"
            }
        ]
    },
    {
        "text": "Doctor: Please confirm your hospital name.\nPatient: I go to Boston General Hospital.",
        "meta": {
            "note_id": "73",
            "patient_id": "4345678"
        },
        "spans": [
            {
                "id": "0",
                "start": 19,
                "end": 44,
                "label": "HOSP"
            }
        ]
    },
    {
        "text": "Doctor: Do you know when your symptoms started?\nPatient: Around March 14th.",
        "meta": {
            "note_id": "74",
            "patient_id": "5456789"
        },
        "spans": [
            {
                "id": "0",
                "start": 38,
                "end": 51,
                "label": "DATE"
            }
        ]
    },
    {
        "text": "Patient: My mother, Grace, lives in Chicago, Illinois.",
        "meta": {
            "note_id": "75",
            "patient_id": "6567890"
        },
        "spans": [
            {
                "id": "0",
                "start": 13,
                "end": 18,
                "label": "PATIENT"
            },
            {
                "id": "1",
                "start": 30,
                "end": 47,
                "label": "LOC"
            }
        ]
    },
    {
        "text": "Patient: I called the clinic at 123-555-0123 to reschedule.",
        "meta": {
            "note_id": "76",
            "patient_id": "7678901"
        },
        "spans": [
            {
                "id": "0",
                "start": 25,
                "end": 37,
                "label": "PHONE"
            }
        ]
    },
    {
        "text": "Doctor: Did you go to the ER at Mercy Medical Center?\nPatient: Yes, last December.",
        "meta": {
            "note_id": "77",
            "patient_id": "8789012"
        },
        "spans": [
            {
                "id": "0",
                "start": 22,
                "end": 43,
                "label": "HOSP"
            },
            {
                "id": "1",
                "start": 48,
                "end": 60,
                "label": "DATE"
            }
        ]
    },
    {
        "text": "Patient: I got vaccinated at CVS Pharmacy in Los Angeles.",
        "meta": {
            "note_id": "78",
            "patient_id": "9890123"
        },
        "spans": [
            {
                "id": "0",
                "start": 25,
                "end": 37,
                "label": "HOSP"
            },
            {
                "id": "1",
                "start": 41,
                "end": 53,
                "label": "LOC"
            }
        ]
    },
    {
        "text": "Doctor: What's your driver's license number?\nPatient: It's DL902345.",
        "meta": {
            "note_id": "79",
            "patient_id": "1001234"
        },
        "spans": [
            {
                "id": "0",
                "start": 17,
                "end": 26,
                "label": "ID"
            }
        ]
    },
    {
        "text": "Patient: My birth date is April 2, 1995, and I live in Portland, Oregon.",
        "meta": {
            "note_id": "80",
            "patient_id": "1112345"
        },
        "spans": [
            {
                "id": "0",
                "start": 21,
                "end": 32,
                "label": "DATE"
            },
            {
                "id": "1",
                "start": 41,
                "end": 56,
                "label": "LOC"
            }
        ]
    },
    {
        "text": "Patient: My father's name is Robert Green, and he is 58 years old.",
        "meta": {
            "note_id": "81",
            "patient_id": "1223456"
        },
        "spans": [
            {
                "id": "0",
                "start": 20,
                "end": 32,
                "label": "PATIENT"
            },
            {
                "id": "1",
                "start": 47,
                "end": 49,
                "label": "AGE"
            }
        ]
    },
    {
        "text": "Doctor: When was your last visit to our clinic?\nPatient: It was on January 20, 2024.",
        "meta": {
            "note_id": "82",
            "patient_id": "1334567"
        },
        "spans": [
            {
                "id": "0",
                "start": 31,
                "end": 48,
                "label": "DATE"
            }
        ]
    },
    {
        "text": "Patient: I'm currently staying at 345 Elm Street, San Francisco.",
        "meta": {
            "note_id": "83",
            "patient_id": "1445678"
        },
        "spans": [
            {
                "id": "0",
                "start": 25,
                "end": 39,
                "label": "LOC"
            },
            {
                "id": "1",
                "start": 41,
                "end": 55,
                "label": "LOC"
            }
        ]
    },
    {
        "text": "Patient: You can call me at 876-543-2109 after 5 PM.",
        "meta": {
            "note_id": "84",
            "patient_id": "1556789"
        },
        "spans": [
            {
                "id": "0",
                "start": 21,
                "end": 33,
                "label": "PHONE"
            }
        ]
    },
    {
        "text": "Patient: I visited Universal Hospital last Tuesday.",
        "meta": {
            "note_id": "85",
            "patient_id": "1667890"
        },
        "spans": [
            {
                "id": "0",
                "start": 10,
                "end": 30,
                "label": "HOSP"
            },
            {
                "id": "1",
                "start": 36,
                "end": 43,
                "label": "DATE"
            }
        ]
    },
    {
        "text": "Doctor: Do you have an email we can reach you at?\nPatient: Sure, john.doe@hospitalmail.org.",
        "meta": {
            "note_id": "86",
            "patient_id": "1778901"
        },
        "spans": [
            {
                "id": "0",
                "start": 38,
                "end": 65,
                "label": "EMAIL"
            }
        ]
    },
    {
        "text": "Patient: My medical ID is PAT1234567.",
        "meta": {
            "note_id": "87",
            "patient_id": "1889012"
        },
        "spans": [
            {
                "id": "0",
                "start": 18,
                "end": 28,
                "label": "ID"
            }
        ]
    },
    {
        "text": "Doctor: Was the injury during your trip to Tokyo in September?\nPatient: Yes, exactly.",
        "meta": {
            "note_id": "88",
            "patient_id": "1990123"
        },
        "spans": [
            {
                "id": "0",
                "start": 39,
                "end": 44,
                "label": "LOC"
            },
            {
                "id": "1",
                "start": 48,
                "end": 57,
                "label": "DATE"
            }
        ]
    },
    {
        "text": "Patient: My mother, Alice, turned 72 this year.",
        "meta": {
            "note_id": "89",
            "patient_id": "2001234"
        },
        "spans": [
            {
                "id": "0",
                "start": 13,
                "end": 18,
                "label": "PATIENT"
            },
            {
                "id": "1",
                "start": 27,
                "end": 29,
                "label": "AGE"
            }
        ]
    },
    {
        "text": "Doctor: What's the name of the pharmacy you use?\nPatient: CVS Pharmacy in Chicago.",
        "meta": {
            "note_id": "90",
            "patient_id": "2112345"
        },
        "spans": [
            {
                "id": "0",
                "start": 0,
                "end": 12,
                "label": "HOSP"
            },
            {
                "id": "1",
                "start": 16,
                "end": 23,
                "label": "LOC"
            }
        ]
    },
    {
        "text": "Patient: My birth date is October 15, 1985.",
        "meta": {
            "note_id": "91",
            "patient_id": "2223456"
        },
        "spans": [
            {
                "id": "0",
                "start": 21,
                "end": 36,
                "label": "DATE"
            }
        ]
    },
    {
        "text": "Doctor: Do you remember your employee ID?\nPatient: Yes, EMP90876.",
        "meta": {
            "note_id": "92",
            "patient_id": "2334567"
        },
        "spans": [
            {
                "id": "0",
                "start": 19,
                "end": 27,
                "label": "ID"
            }
        ]
    },
    {
        "text": "Patient: My wife, Anna, has an appointment tomorrow at Mercy General.",
        "meta": {
            "note_id": "93",
            "patient_id": "2445678"
        },
        "spans": [
            {
                "id": "0",
                "start": 10,
                "end": 14,
                "label": "PATIENT"
            },
            {
                "id": "1",
                "start": 42,
                "end": 56,
                "label": "HOSP"
            },
            {
                "id": "2",
                "start": 30,
                "end": 38,
                "label": "DATE"
            }
        ]
    },
    {
        "text": "Patient: I was advised to call 111-222-3333 for follow-up.",
        "meta": {
            "note_id": "94",
            "patient_id": "2556789"
        },
        "spans": [
            {
                "id": "0",
                "start": 23,
                "end": 35,
                "label": "PHONE"
            }
        ]
    },
    {
        "text": "Doctor: Did your son, Jacob, go to school in London?\nPatient: Yes, he did.",
        "meta": {
            "note_id": "95",
            "patient_id": "2667890"
        },
        "spans": [
            {
                "id": "0",
                "start": 16,
                "end": 21,
                "label": "PATIENT"
            },
            {
                "id": "1",
                "start": 41,
                "end": 47,
                "label": "LOC"
            }
        ]
    },
    {
        "text": "Patient: I took the vaccine at Global Health Clinic last week.",
        "meta": {
            "note_id": "96",
            "patient_id": "2778901"
        },
        "spans": [
            {
                "id": "0",
                "start": 25,
                "end": 46,
                "label": "HOSP"
            },
            {
                "id": "1",
                "start": 47,
                "end": 56,
                "label": "DATE"
            }
        ]
    },
    {
        "text": "Patient: I'm currently employed by IBM.",
        "meta": {
            "note_id": "97",
            "patient_id": "2889012"
        },
        "spans": [
            {
                "id": "0",
                "start": 25,
                "end": 28,
                "label": "PATORG"
            }
        ]
    },
    {
        "text": "Doctor: When did you get married?\nPatient: On July 4, 2010.",
        "meta": {
            "note_id": "98",
            "patient_id": "2990123"
        },
        "spans": [
            {
                "id": "0",
                "start": 15,
                "end": 26,
                "label": "DATE"
            }
        ]
    },
    {
        "text": "Patient: My son is 3 years old and lives in Texas.",
        "meta": {
            "note_id": "99",
            "patient_id": "3001234"
        },
        "spans": [
            {
                "id": "0",
                "start": 10,
                "end": 11,
                "label": "PATIENT"
            },
            {
                "id": "1",
                "start": 13,
                "end": 22,
                "label": "AGE"
            },
            {
                "id": "2",
                "start": 37,
                "end": 42,
                "label": "LOC"
            }
        ]
    },
    {
        "text": "Patient: I've been consulting Dr. Marcus Jones for years.",
        "meta": {
            "note_id": "100",
            "patient_id": "3112345"
        },
        "spans": [
            {
                "id": "0",
                "start": 23,
                "end": 37,
                "label": "STAFF"
            }
        ]
    }
]

for d in data:
    d['meta'].pop('patient_id')
    d.pop('spans')
print(data)

# [{'text': "Patient: I need a refill for the medication prescribed by Dr. Jane Adams.\nDoctor: Sure. I also need your MRN.\nPatient: It's 87654321.", 'meta': {'note_id': '21'}}, 
# {'text': 'Doctor: Have you been to any hospital recently?\nPatient: Yes, I visited Mount Sinai Hospital two weeks ago.', 'meta': {'note_id': '22'}}, 
# {'text': 'Patient: My email is john.doe123@example.com. Please update your records.\nDoctor: Done. Do you have an emergency contact?\nPatient: Yes, you can reach my wife at 987-654-3210.', 'meta': {'note_id': '23'}}, 
# {'text': "Doctor: What's the name of your insurance provider?\nPatient: It's Blue Cross Blue Shield.", 'meta': {'note_id': '24'}}, 
# {'text': "Patient: My father is 65 years old. He has been experiencing chest pain for a week.\nDoctor: Can you confirm his ID?\nPatient: Yes, it's FATHER-ID-56789.", 'meta': {'note_id': '25'}}, 
# {'text': 'Patient: I was born on January 15, 1975.\nDoctor: Thank you, Sarah.', 'meta': {'note_id': '26'}}, 
# {'text': 'Doctor: When did you visit Mayo Clinic?\nPatient: Around March this year.', 'meta': {'note_id': '27'}}, 
# {'text': 'Patient: I traveled to London last summer.\nDoctor: Were you on vacation?', 'meta': {'note_id': '28'}}, 
# {'text': 'Patient: My contact number is 800-555-0199. Please update your records.', 'meta': {'note_id': '29'}}, 
# {'text': "Doctor: Can I have your insurance ID?\nPatient: Sure, it's INSID-2024.", 'meta': {'note_id': '30'}}, 
# {'text': 'Patient: I attended Harvard Medical School in 1995.', 'meta': {'note_id': '31'}}, 
# {'text': 'Patient: Dr. Nathan from City Hospital treated me for pneumonia.', 'meta': {'note_id': '32'}}, 
# {'text': 'Doctor: Please confirm your address.\nPatient: 123 Main St, Springfield, IL, USA.', 'meta': {'note_id': '33'}}, 
# {'text': 'Patient: I was born on April 12, 1988, in Chicago.', 'meta': {'note_id': '34'}}, 
# {'text': 'Patient: My cousin, Rachel Green, is also a patient here.', 'meta': {'note_id': '35'}},

# {'text': "Doctor: Do you have an email I can contact you at?\nPatient: Yes, it's jane.doe@hospital.org.", 'meta': {'note_id': '36'}}, 
# {'text': "Patient: My son's name is Tyler, and he's 7 years old.", 'meta': {'note_id': '37'}}, 
# {'text': 'Doctor: Do you recall the date of your accident?\nPatient: Yes, it was on September 14, 2024.', 'meta': {'note_id': '38'}}, 
# {'text': 'Patient: I live in Seattle, WA.', 'meta': {'note_id': '39'}}, 
# {'text': 'Doctor: Can you verify your pharmacy details?\nPatient: Walgreens Pharmacy, 1234 Oak St, Boston, MA.', 'meta': {'note_id': '40'}}, 
# {'text': 'Doctor: Can I have the date of your last checkup?\nPatient: It was on July 3, 2023.', 'meta': {'note_id': '41'}}, 
# {'text': 'Patient: My contact email is patient.john@yahoo.com.', 'meta': {'note_id': '42'}}, 
# {'text': 'Patient: I was admitted to Bellevue Hospital last winter.', 'meta': {'note_id': '43'}}, 
# {'text': 'Doctor: When did you visit Dr. Emily Watson?\nPatient: Around November 12th.', 'meta': {'note_id': '44'}}, 
# {'text': 'Patient: I live in San Francisco, California, 94123.', 'meta': {'note_id': '45'}}, 
# {'text': "Doctor: What's the name of the pharmacy you use?\nPatient: CVS Pharmacy on Elm Street, Austin, TX.", 'meta': {'note_id': '46'}}, 
# {'text': 'Patient: My son, Eric, is 15 years old and has allergies.', 'meta': {'note_id': '47'}}, 
# {'text': "Doctor: Your ID shows as PX123456. Can you confirm it?\nPatient: Yes, that's correct.", 'meta': {'note_id': '48'}}, 
# {'text': 'Patient: My daughter, Lucy, is starting treatment tomorrow, December 15th.', 'meta': {'note_id': '49'}}, 
# {'text': "Doctor: Please confirm your ZIP code.\nPatient: It's 90210.", 'meta': {'note_id': '50'}}, 
# {'text': 'Patient: My primary doctor is Dr. Lisa Thompson.', 'meta': {'note_id': '51'}}, 
# {'text': 'Patient: I was born on February 20, 1980, in Miami, Florida.', 'meta': {'note_id': '52'}}, 
# {'text': 'Doctor: Have you visited Johns Hopkins Hospital before?\nPatient: Yes, last year in October.', 'meta': {'note_id': '53'}}, 
# {'text': 'Patient: My phone number is 123-456-7890.', 'meta': {'note_id': '54'}}, 
# {'text': "Patient: I'm working at Microsoft Corporation as a software engineer.", 'meta': {'note_id': '55'}}, 
# {'text': "Doctor: Can you confirm your birth date?\nPatient: Yes, it's May 15, 1990.", 'meta': {'note_id': '56'}}, 
# {'text': 'Patient: My father, Robert, is being treated by Dr. William Harris.', 'meta': {'note_id': '57'}}, 
# {'text': "Doctor: Can I have your fax number?\nPatient: It's 555-987-6543.", 'meta': {'note_id': '58'}}, 
# {'text': 'Patient: I visited Stanford Hospital on October 9th.', 'meta': {'note_id': '59'}}, 
# {'text': 'Patient: My account ID is ACCT2024.', 'meta': {'note_id': '60'}}, 
# {'text': 'Doctor: Can you provide the date of the surgery?\nPatient: Yes, it was March 10, 2022.', 'meta': {'note_id': '61'}}, 
# {'text': "Patient: I was treated at St. Mary's Hospital in February.", 'meta': {'note_id': '62'}}, 
# {'text': 'Patient: You can reach me at 987-654-3210 if needed.', 'meta': {'note_id': '63'}}, 
# {'text': 'Patient: My son, Alex, turned 7 years old last week.', 'meta': {'note_id': '64'}}, 
# {'text': "Doctor: Could you confirm your email address?\nPatient: Yes, it's jane.doe@healthmail.com.", 'meta': {'note_id': '65'}}, 
# {'text': "Patient: I've been working at Tesla for the last 5 years.", 'meta': {'note_id': '66'}}, 
# {'text': "Doctor: What is your current ZIP code?\nPatient: It's 10001.", 'meta': {'note_id': '67'}}, 
# {'text': 'Patient: My pharmacist is Dr. Clara Roberts.', 'meta': {'note_id': '68'}}, 
# {'text': "Doctor: What's your MRN?\nPatient: It's MRN67890.", 'meta': {'note_id': '69'}}, 
# {'text': 'Patient: I stayed at Hilton Hotel during my trip to Miami.', 'meta': {'note_id': '70'}}, 
# {'text': 'Patient: My daughter, Sarah, was born on August 12, 2015.', 'meta': {'note_id': '71'}}, 
# {'text': 'Patient: Dr. Daniel Grey suggested the medication.', 'meta': {'note_id': '72'}}, 
# {'text': 'Doctor: Please confirm your hospital name.\nPatient: I go to Boston General Hospital.', 'meta': {'note_id': '73'}}, 
# {'text': 'Doctor: Do you know when your symptoms started?\nPatient: Around March 14th.', 'meta': {'note_id': '74'}}, 
# {'text': 'Patient: My mother, Grace, lives in Chicago, Illinois.', 'meta': {'note_id': '75'}}, 
# {'text': 'Patient: I called the clinic at 123-555-0123 to reschedule.', 'meta': {'note_id': '76'}}, 
# {'text': 'Doctor: Did you go to the ER at Mercy Medical Center?\nPatient: Yes, last December.', 'meta': {'note_id': '77'}}, 
# {'text': 'Patient: I got vaccinated at CVS Pharmacy in Los Angeles.', 'meta': {'note_id': '78'}}, 
# {'text': "Doctor: What's your driver's license number?\nPatient: It's DL902345.", 'meta': {'note_id': '79'}}, 
# {'text': 'Patient: My birth date is April 2, 1995, and I live in Portland, Oregon.', 'meta': {'note_id': '80'}}, 
# {'text': "Patient: My father's name is Robert Green, and he is 58 years old.", 'meta': {'note_id': '81'}}, 
# {'text': 'Doctor: When was your last visit to our clinic?\nPatient: It was on January 20, 2024.', 'meta': {'note_id': '82'}}, 
# {'text': "Patient: I'm currently staying at 345 Elm Street, San Francisco.", 'meta': {'note_id': '83'}}, 
# {'text': 'Patient: You can call me at 876-543-2109 after 5 PM.', 'meta': {'note_id': '84'}}, 
# {'text': 'Patient: I visited Universal Hospital last Tuesday.', 'meta': {'note_id': '85'}}, 
# {'text': 'Doctor: Do you have an email we can reach you at?\nPatient: Sure, john.doe@hospitalmail.org.', 'meta': {'note_id': '86'}}, 
# {'text': 'Patient: My medical ID is PAT1234567.', 'meta': {'note_id': '87'}}, 
# {'text': 'Doctor: Was the injury during your trip to Tokyo in September?\nPatient: Yes, exactly.', 'meta': {'note_id': '88'}}, 
# {'text': 'Patient: My mother, Alice, turned 72 this year.', 'meta': {'note_id': '89'}}, 
# {'text': "Doctor: What's the name of the pharmacy you use?\nPatient: CVS Pharmacy in Chicago.", 'meta': {'note_id': '90'}}, 
# {'text': 'Patient: My birth date is October 15, 1985.', 'meta': {'note_id': '91'}}, 
# {'text': 'Doctor: Do you remember your employee ID?\nPatient: Yes, EMP90876.', 'meta': {'note_id': '92'}}, 
# {'text': 'Patient: My wife, Anna, has an appointment tomorrow at Mercy General.', 'meta': {'note_id': '93'}}, 
# {'text': 'Patient: I was advised to call 111-222-3333 for follow-up.', 'meta': {'note_id': '94'}}, 
# {'text': 'Doctor: Did your son, Jacob, go to school in London?\nPatient: Yes, he did.', 'meta': {'note_id': '95'}}, 
# {'text': 'Patient: I took the vaccine at Global Health Clinic last week.', 'meta': {'note_id': '96'}}, 
# {'text': "Patient: I'm currently employed by IBM.", 'meta': {'note_id': '97'}}, 
# {'text': 'Doctor: When did you get married?\nPatient: On July 4, 2010.', 'meta': {'note_id': '98'}}, 
# {'text': 'Patient: My son is 3 years old and lives in Texas.', 'meta': {'note_id': '99'}}, 
# {'text': "Patient: I've been consulting Dr. Marcus Jones for years.", 'meta': {'note_id': '100'}}]



# Labeled data map
labeled_data_map = {
    "21": [
        ["Dr. Jane Adams", "STAFF"],
        ["87654321", "ID"]
    ],
    "22": [
        ["Mount Sinai Hospital", "HOSP"],
        ["two weeks ago", "DATE"]
    ],
    "23": [
        ["john.doe123@example.com", "EMAIL"],
        ["987-654-3210", "PHONE"]
    ],
    "24": [
        ["Blue Cross Blue Shield", "PATORG"]
    ],
    "25": [
        ["65 years old", "AGE"],
        ["chest pain", "PATORG"],
        ["FATHER-ID-56789", "ID"]
    ],
    "26": [
        ["January 15, 1975", "DATE"],
        ["Sarah", "PATIENT"]
    ],
    "27": [
        ["Mayo Clinic", "HOSP"],
        ["March this year", "DATE"]
    ],
    "28": [
        ["London", "LOC"],
        ["last summer", "DATE"]
    ],
    "29": [
        ["800-555-0199", "PHONE"]
    ],
    "30": [
        ["INSID-2024", "ID"]
    ],
    "31": [
        ["Harvard Medical School", "PATORG"],
        ["1995", "DATE"]
    ],
    "32": [
        ["Dr. Nathan", "STAFF"],
        ["City Hospital", "HOSP"],
        ["pneumonia", "PATORG"]
    ],
    "33": [
        ["123 Main St, Springfield, IL, USA", "LOC"]
    ],
    "34": [
        ["April 12, 1988", "DATE"],
        ["Chicago", "LOC"]
    ],
    "35": [
        ["Rachel Green", "PATIENT"]
    ]
}

# Output file path
output_file = "processed_data.json"

for d in data:
    d['spans'] = []
    
    try:
        labals = labeled_data_map[d['meta']['note_id']]
    except:
        continue
    
    index = 0
    for i in range(len(labals)):
        index = index + d["text"][index:].find(labals[i][0])
        d['spans'].append({
            "id": i,
            "start": index,
            "end": index + len(labals[i][0]),
            "label": labals[i][1]
        })
        index += 1

with open(output_file, 'w') as f:
    json.dump(data, f, indent=4)

print("Data saved to", output_file)
