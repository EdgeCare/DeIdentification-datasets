import json
import os

def getSentenseList(outfile):
    with open(input_file, 'r') as f:
        data = json.load(f)

    for entry in data:
        text = entry["text"]
        meta = entry["meta"]
        note_id = meta["note_id"]
        if int(note_id) >150:
            print(f"note_id : {note_id}, text: {text}")
        if int(note_id) >200:
            break

def process_texts_from_file(input_file, output_file, labeled_data_map):
    """
    Processes a JSON file of texts with metadata and labeled data, appending only if note_id is not in the output file.

    Parameters:
    input_file (str): Path to the input JSON file.
    output_file (str): Path to the output JSON file.
    labeled_data_map (dict): A dictionary where keys are note_ids, and values are labeled data lists.

    Returns:
    None
    """
    # Read input JSON
    with open(input_file, 'r') as f:
        data = json.load(f)

    # Load existing content from the output file if it exists
    if os.path.exists(output_file):
        with open(output_file, 'r') as f:
            try:
                existing_results = json.load(f)
            except json.JSONDecodeError:
                existing_results = []  # If file is empty or invalid JSON
    else:
        existing_results = []

    # Extract existing note_ids
    existing_note_ids = {entry["meta"]["note_id"] for entry in existing_results}

    new_results = []

    for entry in data:
        text = entry["text"]
        meta = entry["meta"]
        note_id = meta["note_id"]

        if int(note_id)<100:
            continue
        if int(note_id)>200:
            break

        # Skip if the note_id already exists
        if note_id in existing_note_ids:
            print(f"Skipping note_id {note_id}: already exists in the output file.")
            continue

        # Get the labeled data for this note_id
        if note_id not in labeled_data_map:
            print(f"Warning: No labeled data for note_id {note_id}")
            continue
        
        labeled_data = labeled_data_map[note_id]
        spans = []
        current_id = 0

        for word, label in labeled_data:
            # Find the start and end indices of the word in the text
            start = text.find(word)
            if start == -1:
                print(f"Warning: Word '{word}' not found in text for note_id {note_id}")
                continue
            end = start + len(word)

            # Add to spans
            spans.append({
                "id": str(current_id),
                "start": start,
                "end": end,
                "label": label
            })
            current_id += 1

        # Create the new result entry
        new_results.append({
            "text": text,
            "meta": meta,
            "spans": spans
        })

    # Append new results to existing results
    updated_results = existing_results + new_results

    # Write updated results to the output file
    with open(output_file, 'w') as f:
        json.dump(updated_results, f, indent=4)

    print(f"Processed data appended to {output_file}. Total entries: {len(updated_results)}")

# Input file path
input_file = "edge_care_deid_dataset.json"

# Output file path
output_file = "processed_texts.json"

# Labeled data map
labeled_data_map = {
    "151": [
        ("Dr. Alice Green", "STAFF"),
        ("neurology", "ORG")
    ],
    "152": [
        ("Global Tech Solutions", "ORG")
    ],
    "153": [
        ("John Smith", "PATIENT"),
        ("Westview Hospital", "HOSP")
    ],
    "154": [
        ("Dr. Karen White", "STAFF"),
        ("June 10th", "DATE")
    ],
    "155": [
        ("ABC12345", "ID"),
        ("777-888-9999", "PHONE")
    ],
    "156": [
        ("Lakeview Hospital", "HOSP")
    ],
    "157": [
        ("Miami", "LOC"),
        ("April 2022", "DATE")
    ],
    "158": [
        ("City Labs", "ORG")
    ],
    "159": [
        ("Mary Davis", "PATIENT"),
        ("National Health Solutions", "ORG")
    ],
    "160": [
        ("Dr. Henry Adams", "STAFF"),
        ("back pain", "ORG")
    ],
    "161": [
        ("mother", "PATIENT"),
        ("65 years old", "AGE"),
        ("Dr. Thomas Lee", "STAFF")
    ],
    "162": [
        ("Elm Street Clinic", "HOSP")
    ],
    "163": [
        ("Daniel Green", "PATIENT"),
        ("Brookside Hospital", "HOSP")
    ],
    "164": [
        ("911", "ID"),
        ("ER", "LOC")
    ],
    "165": [
        ("Hannah Smith", "PATIENT"),
        ("15 years old", "AGE"),
        ("asthma", "ORG")
    ],
    "166": [
        ("Healthy Life Pharmacy", "ORG")
    ],
    "167": [
        ("San Francisco", "LOC"),
        ("September", "DATE")
    ],
    "168": [
        ("Dr. Julia Roberts", "STAFF"),
        ("last May", "DATE")
    ],
    "169": [
        ("6789XYZ", "ID"),
        ("123 Elm Street", "LOC")
    ],
    "170": [
        ("Baker Solutions", "ORG")
    ],
    "171": [
        ("Dr. Edward Clark", "STAFF"),
        ("July 3rd", "DATE")
    ],
    "172": [
        ("dr.jane.doe@example.com", "EMAIL")
    ],
    "173": [
        ("Stanford University", "ORG"),
        ("California", "LOC")
    ],
    "174": [
        ("Dr. Anne Taylor", "STAFF"),
        ("Riverdale Clinic", "HOSP")
    ],
    "175": [
        ("ABC-123", "ID"),
        ("jane.doe@gmail.com", "EMAIL")
    ],
    "176": [
        ("Los Angeles", "LOC")
    ],
    "177": [
        ("Robert Lee", "PATIENT"),
        ("45 years old", "AGE"),
        ("hypertension", "ORG")
    ],
    "178": [
        ("Dr. Michael Wilson", "STAFF"),
        ("General Hospital", "HOSP")
    ],
    "179": [
        ("456 Maple Avenue", "LOC"),
        ("Springfield, IL", "LOC")
    ],
    "180": [
        ("March 15th", "DATE")
    ],
    "181": [
        ("UN123456", "ID"),
        ("Redwood Hospital", "HOSP")
    ],
    "182": [
        ("Tech Innovations Inc.", "ORG"),
        ("last November", "DATE")
    ],
    "183": [
        ("Rajesh Patel", "PATIENT"),
        ("+1-234-567-8901", "PHONE"),
        ("RP890123", "ID")
    ],
    "184": [
        ("Anita Sharma", "PATIENT"),
        ("Blue Ridge Pharmacy", "ORG")
    ],
    "185": [
        ("789 Pine Street", "LOC"),
        ("Dallas, TX", "LOC")
    ],
    "186": [
        ("Dr. Steven Brown", "STAFF"),
        ("City Hospital", "HOSP"),
        ("June 10th", "DATE")
    ],
    "187": [
        ("+44-123-456-7890", "PHONE")
    ],
    "188": [
        ("John Smith", "PATIENT"),
        ("hypertension", "ORG"),
        ("Dr. Alice Cooper", "STAFF")
    ],
    "189": [
        ("Northwood Clinic", "HOSP"),
        ("August 1st", "DATE")
    ],
    "190": [
        ("AB456789", "ID"),
        ("Central Park", "LOC"),
        ("New York", "LOC")
    ],
    "191": [
        ("Dr. Emily Taylor", "STAFF"),
        ("July 14th", "DATE")
    ],
    "192": [
        ("rahul.kumar@domain.com", "EMAIL"),
        ("RK567890", "ID")
    ],
    "193": [
        ("Green Valley Clinic", "HOSP"),
        ("September 20th", "DATE")
    ],
    "194": [
        ("Bright Solutions Pvt Ltd.", "ORG"),
        ("Mumbai", "LOC")
    ],
    "195": [
        ("Dr. Kevin White", "STAFF"),
        ("Sunrise Hospital", "HOSP"),
        ("last year", "DATE")
    ],
    "196": [
        ("+91-9876543210", "PHONE")
    ],
    "197": [
        ("INS12345", "ID")
    ],
    "198": [
        ("Benjamin Harris", "PATIENT"),
        ("72 years old", "AGE")
    ],
    "199": [
        ("Redwood City General Hospital", "HOSP")
    ],
    "200": [
        ("567 Oak Lane", "LOC"),
        ("Springfield", "LOC"),
        ("last week", "DATE")
    ],
    "201": [
        ("23 Corporate Blvd", "LOC"),
        ("Chicago", "LOC")
    ]
}


# Process the file
process_texts_from_file(input_file, output_file, labeled_data_map)


getSentenseList(input_file)
