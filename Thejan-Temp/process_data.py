import json


data = [
    {
        "text": """Discharge Summary
Patient Name: chaminda weerasinghe
Patient ID: 182
Date of Birth: May 15, 1990
Report ID: DS78901
Admitting Physician: Dr. Sunil Mahinda 
Consulting Physician(s): Dr. Maheesh Ekanayake
Date of Admission: 2021 December 15
Date of Discharge: 2022 January 20

Admission Diagnosis
Acute appendicitis

Discharge Diagnosis
Acute appendicitis treated with laparoscopic appendectomy
Procedures Performed

Laparoscopic appendectomy performed on 2021-12-16, 
Hospital Course
The patient was admitted on 2021-12-15, with complaints of abdominal pain, nausea, and fever. A physical examination and imaging confirmed acute appendicitis. A laparoscopic appendectomy was successfully performed on 2021-12-16. The patient recovered well postoperatively with no complications. Pain was managed with oral analgesics, and the patient was mobilized within 24 hours. Routine labs, including a complete blood count, showed improvement. No infections or other complications were noted during the hospital stay.

Discharge Medications
Acetaminophen 500 mg: Take one tablet every 6 hours as needed for pain
Amoxicillin 500 mg: Take one capsule every 8 hours for 7 days

Follow-Up Instructions
Schedule a follow-up appointment with Dr. Sunil Mahinda  in 2 weeks.
Maintain a soft diet for the next few days and gradually return to a normal diet.
Keep the surgical site clean and dry; remove dressing as instructed.
Monitor for signs of infection, such as redness, swelling, or fever, and contact the physician if symptoms occur.
Condition at Discharge
The patient is in stable condition, ambulatory, and tolerating oral intake well.

Discharging Physician:
Dr. Sunil Mahinda 

Facility: Rathgama Hospital
Contact: 0112 395 378""",
        "meta": {
            "note_id": "3014",
            "patient_id": "10231"
        },
        "spans": [
            
        ]
    }
]

for d in data:
    d['meta'].pop('patient_id')
    d.pop('spans')
print(data)

# Labeled data map
labeled_data_map = {
    "3014": [
        ["chaminda weerasinghe", "PATIENT"],
        ["182", "ID"],
        ["May 15, 1990", "DATE"],
        ["DS78901", "ID"],
        ["Dr. Sunil Mahinda ", "STAFF"],
        ["Dr. Maheesh Ekanayake", "STAFF"],
        ["2021 December 15", "DATE"],
        ["2022 January 20", "DATE"],
        ["2021-12-16", "DATE"],
        ["2021-12-15", "DATE"],
        ["2021-12-16", "DATE"],
        ["Dr. Sunil Mahinda ", "STAFF"],
        ["Rathgama Hospital", "HOSP"],
        ["0112 395 378", "PHONE"]
    ]
}

# Output file path
output_file = "Thejan-Temp/processed_data-thejan.json"

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
        index += + len(labals[i][0])

with open(output_file, 'w') as f:
    json.dump(data, f, indent=4)

print("Data saved to", output_file)
